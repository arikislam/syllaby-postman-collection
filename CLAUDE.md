# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains the Postman API collection and testing suite for the Syllaby platform. It serves as the central source of truth for API documentation, testing, and integration workflows.

## Key Commands

```bash
# Validate JSON syntax
npm run validate

# Run tests for specific environments
npm run test:local      # Test against http://syllaby.test
npm run test:dev        # Test against https://dev-api.syllaby.dev
npm run test:staging    # Test against https://stg-api.syllaby.dev
npm run test:prod       # Test against https://api.syllaby.io (with --bail)

# Run all non-production tests
npm run test:all

# Generate HTML test report
npm run report

# Sync with Postman cloud (requires POSTMAN_API_KEY)
npm run sync
```

## Repository Structure

```
syllaby-api-collection.json          # Main Postman collection with all API endpoints
syllaby-local-environment.json       # Environment for local development
syllaby-development-environment.json # Environment for dev server
syllaby-staging-environment.json     # Environment for staging
syllaby-production-environment.json  # Environment for production
postman-sync.js                     # Script for syncing with Postman cloud
sync-to-postman.sh                  # Shell script with sync instructions
```

## Working with the Collection

### Making Updates
1. Import the collection in Postman desktop app
2. Make changes and test locally
3. Export the collection (v2.1 format)
4. Replace `syllaby-api-collection.json` with exported file
5. Run `npm run validate` to ensure JSON validity
6. Commit changes and create PR

### Testing Changes
Always test changes across environments before committing:
```bash
npm run test:local
npm run test:dev
npm run test:staging
```

## Environment Variables

Each environment file contains:
- `baseUrl`: API endpoint URL
- `apiKey`: Authentication token
- `userId`: Test user ID
- `characterId`: Test character ID
- `videoId`: Test video ID
- Additional test data IDs

## API Collection Organization

The collection is organized by domain:
- **Auth**: Authentication endpoints
- **User Management**: User CRUD operations
- **Videos**: Video creation and management
- **Characters**: AI character operations
- **Ideas**: Content ideation endpoints
- **Publications**: Social media publishing
- **Billing**: Subscription and payment endpoints

Each request includes:
- Pre-request scripts for setup
- Tests for response validation
- Example responses for documentation

## Important Conventions

### Request Naming
- Use descriptive names: `[Domain] - [Action]`
- Example: `Videos - Create Faceless Video`

### Variable Usage
- Use environment variables for all URLs and IDs
- Example: `{{baseUrl}}/api/v1/videos`
- Store generated IDs in collection variables for chaining requests

### Test Organization
- Each request should have basic status code tests
- Critical endpoints should validate response structure
- Use collection variables to pass data between requests

## Common Workflows

### Adding a New Endpoint
1. Create request in appropriate folder
2. Add pre-request script if needed
3. Add response tests
4. Include example response
5. Test across all environments
6. Update documentation if needed

### Debugging Failed Tests
```bash
# Run with verbose output
newman run syllaby-api-collection.json -e syllaby-local-environment.json --verbose

# Run specific folder only
newman run syllaby-api-collection.json -e syllaby-local-environment.json --folder "Videos"

# Export variables for debugging
newman run syllaby-api-collection.json -e syllaby-local-environment.json --export-environment debug-env.json
```

### Updating Environment Variables
1. Edit the appropriate environment JSON file
2. Ensure sensitive values are not committed
3. Update all environment files consistently
4. Document new variables in team communication

## Integration with Main Codebase

This collection mirrors the API routes defined in the main Laravel application:
- Routes defined in `routes/api-v1.php`
- Controllers in `app/Syllaby/[Domain]/Controllers/`
- Authentication via Laravel Sanctum tokens

When API changes are made in the main codebase:
1. Update the corresponding Postman request
2. Update tests to match new response format
3. Add new example responses
4. Test across all environments

## Automation and CI/CD

The collection can be integrated into CI/CD pipelines:
```bash
# In GitHub Actions or similar
npm install
npm run test:staging
```

For production monitoring:
```bash
# Run with custom reporter
newman run syllaby-api-collection.json -e syllaby-production-environment.json -r cli,json --reporter-json-export results.json
```

## Troubleshooting

### Common Issues
- **401 Errors**: Check API key in environment file
- **404 Errors**: Verify baseUrl matches environment
- **JSON Parse Errors**: Run `npm run validate`
- **Sync Failures**: Ensure POSTMAN_API_KEY is set

### Debug Commands
```bash
# Check Newman version
npx newman --version

# Validate collection structure
node -e "console.log(JSON.parse(require('fs').readFileSync('syllaby-api-collection.json', 'utf8')).info)"

# Test single request
newman run syllaby-api-collection.json -e syllaby-local-environment.json --folder "Auth" -n 1
```

## Best Practices

1. **Never commit sensitive data**: API keys, passwords, or production data
2. **Test before syncing**: Run local tests before pushing to Postman cloud
3. **Document complex requests**: Add descriptions for non-obvious parameters
4. **Maintain consistency**: Follow existing patterns for new requests
5. **Use version control**: All changes should go through PR review
6. **Keep environments in sync**: Update all environment files when adding new variables