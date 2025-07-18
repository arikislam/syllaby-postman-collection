#!/bin/bash

# Syllaby Postman Collection Sync Script
# This script syncs the local collection and environments to Postman cloud

echo "🚀 Syllaby Postman Collection Sync"
echo "=================================="

# Check if Postman CLI is installed
if ! command -v postman &> /dev/null; then
    echo "❌ Postman CLI not found. Installing..."
    npm install -g @postman/cli
fi

# Check if logged in to Postman
echo "📝 Checking Postman login status..."
if ! postman whoami &> /dev/null; then
    echo "❌ Not logged in to Postman"
    echo "Please run: npm run postman:login"
    exit 1
fi

echo "✅ Logged in to Postman"
echo ""

# Push collection
echo "📤 Pushing collection..."
if postman collection push syllaby-api-collection.json --name "Syllaby API Collection"; then
    echo "✅ Collection pushed successfully"
else
    echo "❌ Failed to push collection"
    exit 1
fi

echo ""

# Push environments
echo "📤 Pushing environments..."

environments=(
    "syllaby-local-environment.json:Syllaby Local Development"
    "syllaby-development-environment.json:Syllaby Development"
    "syllaby-staging-environment.json:Syllaby Staging"
    "syllaby-production-environment.json:Syllaby Production"
)

for env in "${environments[@]}"; do
    IFS=':' read -r filename envname <<< "$env"
    echo "   Pushing $envname..."
    if postman environment push "$filename" --name "$envname"; then
        echo "   ✅ $envname pushed"
    else
        echo "   ❌ Failed to push $envname"
    fi
done

echo ""
echo "✅ Sync complete!"
echo ""
echo "📌 Next steps:"
echo "   1. Open Postman"
echo "   2. Your collection and environments should be updated"
echo "   3. Select the appropriate environment from the dropdown"
echo ""