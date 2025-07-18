# Syllaby Postman Collection

This repository contains the Postman collection and environments for the Syllaby API.

## Repository Structure

```
├── syllaby-api-collection.json      # Main API collection
├── syllaby-local-environment.json   # Local development (Valet)
├── syllaby-development-environment.json  # Dev server
├── syllaby-staging-environment.json     # Staging server
├── syllaby-production-environment.json  # Production server
├── sync-to-postman.sh              # Script to sync with Postman
├── package.json                    # NPM dependencies for Postman CLI
└── README.md                       # This file
```

## Environment URLs

- **Local**: http://syllaby.test
- **Development**: https://dev-api.syllaby.dev
- **Staging**: https://stg-api.syllaby.dev
- **Production**: https://api.syllaby.io

## Quick Start

### 1. Import to Postman

1. Clone this repository
2. Open Postman
3. Import the collection: `syllaby-api-collection.json`
4. Import your environment file (e.g., `syllaby-local-environment.json`)
5. Select the environment from the dropdown

### 2. Using Postman CLI (Recommended)

```bash
# Install dependencies
npm install

# Login to Postman (first time only)
npm run postman:login

# Push collection to Postman cloud
npm run push:collection

# Push all environments
npm run push:environments

# Pull latest from Postman cloud
npm run pull:collection
```

## Workflow

### Making Changes

1. Make changes in Postman UI
2. Export the collection/environment
3. Replace the files in this repo
4. Commit and push:

```bash
git add .
git commit -m "Update: [describe your changes]"
git push
```

### Syncing Changes

After pulling latest changes from Git:

```bash
# Push all changes to Postman cloud
npm run sync:all
```

## API Collection Structure

- **Authentication**
  - Login
  - Register
  - Logout
  
- **User Management**
  - Get Profile
  - Update Profile
  - Credit History
  
- **Videos - Faceless**
  - Create/Read/Update/Delete
  - Render & Export
  - Assets Management
  - Media Operations
  - Transcriptions
  - Web Scraping
  - Configuration Options

## Environment Variables

| Variable | Description |
|----------|-------------|
| `base_url` | API base URL |
| `api_version` | API version (v1) |
| `auth_token` | Authentication token (auto-saved) |
| `user_email` | Test user email |
| `user_password` | Test user password |
| `faceless_id` | Current faceless video ID |
| `asset_id` | Current asset ID |

## Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Team Setup

1. Team members clone this repo
2. Install Postman CLI: `npm install -g @postman/cli`
3. Import the collection and environment
4. Pull latest changes regularly: `git pull && npm run sync:all`

## Automation

This repository includes GitHub Actions for:
- Validating collection syntax
- Running API tests with Newman
- Syncing with Postman cloud on push

## Security

- Never commit sensitive data in environment files
- Use Postman's environment variables for secrets
- Keep production credentials in Postman cloud only

## License

Private repository - Syllaby internal use only