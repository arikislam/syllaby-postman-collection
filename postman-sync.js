#!/usr/bin/env node

/**
 * Postman Sync Script
 * Syncs local collection and environments to Postman cloud using API
 * 
 * Usage: 
 *   POSTMAN_API_KEY=your-key node postman-sync.js
 *   or
 *   node postman-sync.js your-api-key
 */

const fs = require('fs');
const https = require('https');
const path = require('path');

// Load .env file if it exists
if (fs.existsSync('.env')) {
  const envContent = fs.readFileSync('.env', 'utf8');
  envContent.split('\n').forEach(line => {
    const [key, value] = line.split('=');
    if (key && value && key.trim() === 'POSTMAN_API_KEY') {
      process.env.POSTMAN_API_KEY = value.trim();
    }
  });
}

// Get API key from environment or command line
const API_KEY = process.env.POSTMAN_API_KEY || process.argv[2];

if (!API_KEY) {
  console.error('❌ No API key provided!');
  console.error('\nUsage:');
  console.error('  POSTMAN_API_KEY=your-key npm run sync');
  console.error('  or');
  console.error('  node postman-sync.js your-api-key');
  console.error('\nGet your API key from: https://web.postman.co/settings/me/api-keys');
  process.exit(1);
}

// Configuration
const config = {
  collection: {
    file: 'syllaby-api-collection.json',
    name: 'Syllaby API Collection'
  },
  environments: [
    { file: 'syllaby-local-environment.json', name: 'Syllaby Local Development' },
    { file: 'syllaby-development-environment.json', name: 'Syllaby Development' },
    { file: 'syllaby-staging-environment.json', name: 'Syllaby Staging' },
    { file: 'syllaby-production-environment.json', name: 'Syllaby Production' }
  ]
};

// Helper function to make API requests
function makeRequest(options, data) {
  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', (chunk) => body += chunk);
      res.on('end', () => {
        try {
          const response = JSON.parse(body);
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve(response);
          } else {
            reject(new Error(`API Error: ${res.statusCode} - ${response.error?.message || body}`));
          }
        } catch (e) {
          reject(new Error(`Parse Error: ${e.message}`));
        }
      });
    });

    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

// Get all collections and environments
async function getExistingItems() {
  console.log('📋 Fetching existing items from Postman...');
  
  const options = {
    hostname: 'api.postman.com',
    headers: {
      'X-Api-Key': API_KEY
    }
  };

  try {
    const [collections, environments] = await Promise.all([
      makeRequest({ ...options, path: '/collections', method: 'GET' }),
      makeRequest({ ...options, path: '/environments', method: 'GET' })
    ]);

    return {
      collections: collections.collections || [],
      environments: environments.environments || []
    };
  } catch (error) {
    console.error('❌ Failed to fetch existing items:', error.message);
    return { collections: [], environments: [] };
  }
}

// Update or create collection
async function syncCollection(existing) {
  console.log('\n📤 Syncing collection...');
  
  try {
    const collectionData = JSON.parse(fs.readFileSync(config.collection.file, 'utf8'));
    
    // Check if collection exists
    const existingCollection = existing.collections.find(c => c.name === config.collection.name);
    
    const options = {
      hostname: 'api.postman.com',
      method: existingCollection ? 'PUT' : 'POST',
      headers: {
        'X-Api-Key': API_KEY,
        'Content-Type': 'application/json'
      }
    };

    if (existingCollection) {
      options.path = `/collections/${existingCollection.uid}`;
      console.log(`   Updating existing collection: ${existingCollection.uid}`);
    } else {
      options.path = '/collections';
      console.log('   Creating new collection');
    }

    const payload = JSON.stringify({
      collection: {
        ...collectionData,
        info: {
          ...collectionData.info,
          name: config.collection.name
        }
      }
    });

    await makeRequest(options, payload);
    console.log(`   ✅ Collection synced: ${config.collection.name}`);
  } catch (error) {
    console.error(`   ❌ Failed to sync collection: ${error.message}`);
  }
}

// Update or create environments
async function syncEnvironments(existing) {
  console.log('\n📤 Syncing environments...');
  
  for (const env of config.environments) {
    try {
      const envData = JSON.parse(fs.readFileSync(env.file, 'utf8'));
      
      // Check if environment exists
      const existingEnv = existing.environments.find(e => e.name === env.name);
      
      const options = {
        hostname: 'api.postman.com',
        method: existingEnv ? 'PUT' : 'POST',
        headers: {
          'X-Api-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      };

      if (existingEnv) {
        options.path = `/environments/${existingEnv.uid}`;
        console.log(`   Updating ${env.name}: ${existingEnv.uid}`);
      } else {
        options.path = '/environments';
        console.log(`   Creating ${env.name}`);
      }

      const payload = JSON.stringify({
        environment: {
          name: env.name,
          values: envData.values
        }
      });

      await makeRequest(options, payload);
      console.log(`   ✅ ${env.name}`);
    } catch (error) {
      console.error(`   ❌ Failed to sync ${env.name}: ${error.message}`);
    }
  }
}

// Main sync function
async function sync() {
  console.log('🚀 Syllaby Postman Sync');
  console.log('=======================');
  
  try {
    // Validate files exist
    const files = [config.collection.file, ...config.environments.map(e => e.file)];
    for (const file of files) {
      if (!fs.existsSync(file)) {
        throw new Error(`File not found: ${file}`);
      }
    }

    // Get existing items
    const existing = await getExistingItems();
    
    // Sync collection and environments
    await syncCollection(existing);
    await syncEnvironments(existing);
    
    console.log('\n✅ Sync complete!');
    console.log('\n📌 Next steps:');
    console.log('   1. Open Postman');
    console.log('   2. Your collection and environments should be updated');
    console.log('   3. Select the appropriate environment from the dropdown');
    
  } catch (error) {
    console.error('\n❌ Sync failed:', error.message);
    process.exit(1);
  }
}

// Run sync
sync();