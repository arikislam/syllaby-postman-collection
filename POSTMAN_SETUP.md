# Postman Setup Guide for Syllaby API

## Quick Start - Automatic Sync (NEW!)

### 1. Get Your Postman API Key
1. Go to: https://web.postman.co/settings/me/api-keys
2. Click "Generate API Key"
3. Copy the key

### 2. Run the Sync Script

```bash
# Method 1: One-time sync
POSTMAN_API_KEY=your-key-here npm run sync

# Method 2: Save key in .env file
echo "POSTMAN_API_KEY=your-key-here" > .env
npm run sync

# Method 3: Pass as argument
node postman-sync.js your-key-here
```

The script will:
- ✅ Check if collection/environments exist in your Postman account
- ✅ Update existing items or create new ones
- ✅ Sync everything in one command
- ✅ Show progress and results

## Quick Start - Manual Import

### 1. Import to Postman Desktop App

1. Open Postman Desktop App
2. Click the **Import** button
3. Drag and drop all JSON files from this folder:
   - `syllaby-api-collection.json`
   - `syllaby-local-environment.json`
   - `syllaby-development-environment.json`
   - `syllaby-staging-environment.json`
   - `syllaby-production-environment.json`

### 2. Select Environment

1. Click the environment dropdown (top right)
2. Select the appropriate environment:
   - **Local Development** - for http://syllaby.test
   - **Development** - for https://dev-api.syllaby.dev
   - **Staging** - for https://stg-api.syllaby.dev
   - **Production** - for https://api.syllaby.io

### 3. Start Testing

1. Run **Login** request first to get auth token
2. The token is automatically saved to environment
3. All other requests will use this token

## Running Tests with Newman

Newman is the command-line collection runner for Postman.

### Install Newman

```bash
# Install dependencies
cd /Users/smariqislam/Sites/syllaby/storage/data/ariq
npm install
```

### Run Tests

```bash
# Test with local environment
npm run test:local

# Test with dev environment
npm run test:dev

# Test with staging environment
npm run test:staging

# Test all environments
npm run test:all

# Generate HTML report
npm run report
```

### Validate JSON Files

```bash
# Check all JSON files are valid
npm run validate
```

## Team Collaboration Workflow

### Option 1: Via Git (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/arikislam/syllaby-postman-collection.git
   cd syllaby-postman-collection
   ```

2. **Import to Postman**
   - Open Postman
   - Import all JSON files

3. **Stay synchronized**
   ```bash
   # Pull latest changes
   git pull
   
   # Re-import updated files to Postman
   ```

### Option 2: Via Postman Team Workspace

1. **Create Team Workspace**
   - In Postman: Workspaces → Create Workspace → Team
   
2. **Import Collection**
   - Import the collection and environments
   
3. **Share with Team**
   - Invite team members to workspace
   - Changes sync automatically

### Option 3: Via Collection Links

1. **Share Collection**
   - In Postman: Collection → Share → Get public link
   
2. **Team Import**
   - Team members: Import → Link → Paste URL

## Making Changes

### When you update in Postman:

1. Export the updated collection/environment
2. Save to this folder (overwrite existing)
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update: [description]"
   git push
   ```

### When pulling updates from Git:

1. Pull latest changes
   ```bash
   git pull
   ```

2. Re-import to Postman:
   - Delete old version in Postman
   - Import updated files

## Using Postman API for Automation

While Postman CLI is not available via npm, you can use the Postman API:

### 1. Get API Key

Go to: https://web.postman.co/settings/me/api-keys

### 2. Upload Collection via API

```bash
# Example using curl
curl --location --request POST 'https://api.postman.com/collections' \
--header 'X-API-Key: YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-binary '@syllaby-api-collection.json'
```

### 3. Upload Environment via API

```bash
curl --location --request POST 'https://api.postman.com/environments' \
--header 'X-API-Key: YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-binary '@syllaby-local-environment.json'
```

## GitHub Actions Integration

The repository includes GitHub Actions that:
1. Validate JSON syntax on every push
2. Run basic Newman tests
3. Generate test reports

To enable full integration:
1. Go to repository Settings → Secrets → Actions
2. Add `POSTMAN_API_KEY` secret

## Troubleshooting

### Collection not updating?
- Make sure you're in the right workspace
- Delete and re-import the collection
- Check JSON validity: `npm run validate`

### Tests failing?
- Verify environment variables are set
- Check auth token is valid
- Ensure server is running (for local)

### Newman errors?
```bash
# Install globally if needed
npm install -g newman

# Check version
newman --version
```

## Best Practices

1. **Never commit sensitive data**
   - Keep passwords in Postman environment only
   - Use environment variables for all secrets

2. **Use descriptive commits**
   ```bash
   git commit -m "Add: User profile update endpoint"
   git commit -m "Fix: Authentication token header"
   ```

3. **Test before pushing**
   ```bash
   npm run validate
   npm run test:local
   ```

4. **Document changes**
   - Update README for new endpoints
   - Add request descriptions in Postman

## Quick Reference

| Command | Description |
|---------|-------------|
| `npm install` | Install Newman and dependencies |
| `npm run test:local` | Run tests with local env |
| `npm run test:dev` | Run tests with dev env |
| `npm run test:all` | Run tests on all environments |
| `npm run validate` | Validate JSON syntax |
| `npm run report` | Generate HTML test report |

## Support

- Postman Documentation: https://learning.postman.com/
- Newman Documentation: https://github.com/postmanlabs/newman
- API Documentation: [Add your API docs link here]