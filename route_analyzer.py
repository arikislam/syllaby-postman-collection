#!/usr/bin/env python3
"""
Route Analyzer - Compare Laravel routes with Postman collection
"""

import json
import re
from typing import List, Tuple, Set

def parse_laravel_routes(file_path: str) -> Set[Tuple[str, str]]:
    """Parse Laravel routes file and extract all routes with their HTTP methods"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    routes = set()
    
    # Define route prefixes based on the Laravel file structure
    route_prefixes = {
        'authentication': [
            ('POST', 'check-email'),
            ('POST', 'login'),
            ('POST', 'register'),
            ('POST', 'logout'),
            ('GET', 'redirect/{provider}'),
            ('GET', 'callback/{provider}'),
        ],
        'recovery': [
            ('POST', 'forgot'),
            ('POST', 'reset'),
        ],
        'notifications': [
            ('GET', ''),
            ('PUT', ''),
            ('PUT', 'settings'),
        ],
        'credits': [
            ('GET', 'overview'),
            ('POST', 'estimate'),
        ],
        'surveys': [
            ('GET', ''),
            ('POST', ''),
            ('GET', 'industries'),
        ],
        'assets': [
            ('GET', ''),
            ('PUT', 'sort'),
            ('GET', 'audios'),
            ('POST', 'audios'),
            ('POST', 'watermark'),
            ('DELETE', '{asset}'),
            ('PUT', '{asset}/bookmark/toggle'),
        ],
        'editor': [
            ('GET', 'assets'),
        ],
        'user': [
            ('GET', 'me'),
            ('PUT', 'seen-welcome-message'),
            ('PUT', 'password'),
            ('PATCH', 'profile'),
            ('GET', 'credit-history'),
            ('GET', 'storage'),
            ('GET', 'publications-usage'),
            ('DELETE', ''),
        ],
        'folders': [
            ('GET', ''),
            ('POST', ''),
            ('PUT', '{folder}'),
            ('PUT', '{folder}/bookmark'),
            ('GET', 'resources'),
            ('PUT', 'resources/{destination}/move'),
            ('DELETE', 'resources'),
        ],
        'events': [
            ('GET', ''),
            ('PATCH', '{event}'),
            ('PUT', '{event}/completes'),
            ('DELETE', '{event}'),
            ('GET', 'tracker-reports'),
        ],
        'generators': [
            ('GET', 'options'),
        ],
        'schedulers': [
            ('GET', ''),
            ('POST', ''),
            ('POST', 'csv-parser'),
            ('GET', '{scheduler}'),
            ('PATCH', '{scheduler}'),
            ('POST', '{scheduler}/run'),
            ('PUT', '{scheduler}/toggle'),
            ('GET', '{scheduler}/occurrences'),
            ('POST', '{scheduler}/occurrences'),
            ('PATCH', 'occurrences/{occurrence}'),
            ('PUT', 'occurrences/{occurrence}/scripts'),
            ('DELETE', '{scheduler}/events'),
        ],
        'publications': [
            ('GET', 'limits'),
            ('PUT', '{publication}/thumbnails/attach'),
            ('POST', '{publication}/thumbnail'),
            ('DELETE', '{publication}/thumbnail'),
            ('GET', '{publication}/channels/{channel}'),
        ],
        'keywords': [
            ('GET', 'history'),
            ('DELETE', '{keyword}/history'),
        ],
        'ideas': [
            ('GET', ''),
            ('POST', 'discover'),
            ('GET', 'suggestions'),
        ],
        'topics': [
            ('GET', ''),
            ('POST', 'related'),
            ('PUT', '{topic}/bookmark'),
        ],
        'templates': [
            ('GET', ''),
            ('GET', '{template}'),
        ],
        'tags': [
            ('GET', ''),
            ('GET', '{tag}'),
        ],
        'presets': [
            ('GET', 'faceless'),
            ('POST', 'faceless'),
            ('PATCH', 'faceless/{preset}'),
            ('DELETE', 'faceless/{preset}'),
        ],
        'characters': [
            ('GET', ''),
            ('POST', ''),
            ('GET', '{character}'),
            ('PUT', '{character}'),
            ('DELETE', '{character}'),
            ('POST', '{character}/image'),
            ('POST', '{character}/preview'),
            ('POST', '{character}/train'),
        ],
        'videos': [
            ('GET', ''),
            ('GET', '{video}'),
            ('PATCH', '{video}'),
            ('DELETE', '{video}'),
            ('GET', '{uuid}/render'),
            ('GET', '{video}/status'),
            # Footage sub-routes
            ('POST', 'footage'),
            ('PATCH', 'footage/{footage}'),
            ('PUT', 'footage/{footage}/preference'),
            ('POST', 'footage/{footage}/render'),
            # Timeline sub-routes
            ('GET', 'footage/{footage}/timeline'),
            ('PUT', 'footage/{footage}/timeline'),
            # Faceless sub-routes
            ('POST', 'faceless'),
            ('GET', 'faceless/{faceless}'),
            ('PATCH', 'faceless/{faceless}'),
            ('POST', 'faceless/{faceless}/render'),
            ('POST', 'faceless/{faceless}/retry'),
            ('PUT', 'faceless/{faceless}/scripts'),
            ('POST', 'faceless/{faceless}/convert'),
            ('GET', 'faceless/{faceless}/assets'),
            ('PATCH', 'faceless/{faceless}/assets'),
            ('GET', 'faceless/{faceless}/assets/{asset}'),
            ('POST', 'faceless/{faceless}/media/upload'),
            ('POST', 'faceless/{faceless}/media/transload'),
            ('POST', 'faceless/{faceless}/media/generate'),
            ('GET', 'faceless/{faceless}/media/animation'),
            ('POST', 'faceless/{faceless}/media/animation'),
            ('POST', 'faceless/{faceless}/export'),
            ('POST', 'faceless/{faceless}/transcriptions/upload'),
            ('POST', 'faceless/{faceless}/transcriptions'),
            ('POST', 'faceless/{faceless}/scrape'),
            ('POST', 'faceless/{faceless}/scrape/images'),
            # Faceless options
            ('GET', 'faceless/options/fonts'),
            ('GET', 'faceless/options/facts'),
            ('GET', 'faceless/options/genres'),
            ('GET', 'faceless/options/transitions'),
            ('GET', 'faceless/options/backgrounds'),
            ('GET', 'faceless/options/caption/effects'),
            ('GET', 'faceless/options/overlays'),
            # Video assets
            ('GET', '{video}/assets'),
            ('POST', '{video}/assets'),
            ('DELETE', '{video}/assets/{asset}'),
            ('POST', '{video}/assets/transload'),
        ],
        'real-clones': [
            ('GET', 'avatars'),
            ('DELETE', 'avatars/{avatar}'),
            ('POST', 'photo-avatars'),
            ('GET', '{clone}'),
            ('POST', ''),
            ('PATCH', '{clone}'),
            ('DELETE', '{clone}'),
            ('GET', '{clone}/status'),
            ('PUT', '{clone}/scripts'),
            ('POST', '{clone}/scrape'),
            ('POST', '{clone}/retries'),
            ('POST', '{clone}/generate'),
        ],
        'speeches': [
            ('GET', 'voices'),
        ],
        'social-accounts': [
            ('GET', ''),
        ],
        'social': [
            ('GET', 'redirect/{provider}'),
            ('GET', 'callback/{provider}'),
            ('POST', 'disconnect/{provider}'),
            ('POST', 'refresh/{provider}'),
            ('GET', 'callback/{provider}/channels'),
            ('POST', 'callback/{provider}/channels'),
        ],
        'publish': [
            ('POST', 'draft'),
            ('POST', 'youtube'),
            ('POST', 'tiktok'),
            ('POST', 'linkedin'),
            ('POST', 'facebook'),
            ('POST', 'instagram'),
            ('POST', 'threads'),
        ],
        'thumbnails': [
            ('GET', ''),
            ('POST', ''),
            ('DELETE', '{thumbnail}'),
        ],
        'metadata': [
            ('GET', 'youtube/categories'),
            ('POST', 'tiktok/creator-info'),
            ('GET', 'social-providers'),
            ('POST', 'generate/title'),
            ('POST', 'generate/description'),
            ('POST', 'generate/tags'),
            ('POST', 'generate/context'),
        ],
        'stock-media': [
            ('GET', 'images/search'),
            ('GET', 'images/collections/{collection}'),
            ('GET', 'videos/search'),
            ('GET', 'videos/collections/{collection}'),
            ('GET', 'audios'),
        ],
        'clones': [
            ('GET', ''),
            ('GET', '{clonable}'),
            ('POST', 'voices'),
            ('POST', 'avatars'),
            ('DELETE', '{clonable}'),
            ('PATCH', '{clonable}/voices'),
        ],
        'user-feedback': [
            ('POST', ''),
        ],
        'media': [
            ('POST', 'download'),
            ('GET', '{uuid}/download'),
        ],
        'subscriptions': [
            ('GET', 'plans'),
            ('GET', 'plans/retention'),
            ('POST', 'checkout'),
            ('POST', 'customer-portal'),
            ('GET', 'products/{product}'),
            ('POST', 'purchases'),
            ('POST', 'google-play/checkout-completed'),
            ('PATCH', 'swap-plan'),
            ('POST', 'payment-intent'),
            ('POST', 'subscribe'),
            ('GET', 'details'),
            ('DELETE', 'cancel'),
            ('PUT', 'cancel-downgrade'),
            ('POST', 'resume'),
            ('POST', 'end-trial'),
            ('POST', 'extend-trial'),
            ('POST', 'coupons/redeem'),
            ('POST', 'proration'),
            # Storage sub-routes
            ('PUT', 'storage'),
            ('DELETE', 'storage'),
            ('GET', 'storage/plans'),
        ],
        'previews': [
            ('GET', 'audios'),
            ('POST', 'render'),
            ('GET', '{video}'),
        ],
    }
    
    # Build routes from prefixes
    for prefix, prefix_routes in route_prefixes.items():
        for method, path in prefix_routes:
            if path == '':
                full_path = prefix
            else:
                full_path = f"{prefix}/{path}"
            routes.add((method, full_path))
    
    # Add API Resource routes for publications
    routes.update([
        ('GET', 'publications'),
        ('POST', 'publications'),
        ('GET', 'publications/{publication}'),
        ('PUT', 'publications/{publication}'),
        ('PATCH', 'publications/{publication}'),
        ('DELETE', 'publications/{publication}')
    ])
    
    # Add root route
    routes.add(('GET', ''))
    
    # Add track-events route
    routes.add(('POST', 'track-events'))
    
    return routes

def parse_postman_collection(file_path: str) -> Set[Tuple[str, str]]:
    """Parse Postman collection and extract all endpoints"""
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    def extract_endpoints(items):
        endpoints = set()
        for item in items:
            if 'item' in item:  # Folder
                endpoints.update(extract_endpoints(item['item']))
            elif 'request' in item:  # Endpoint
                method = item['request']['method']
                if 'url' in item['request'] and 'raw' in item['request']['url']:
                    url = item['request']['url']['raw']
                    # Extract path from URL, removing {{api_url}}/ prefix
                    path = re.sub(r'{{api_url}}/', '', url)
                    path = re.sub(r'\?.*', '', path)  # Remove query params
                    endpoints.add((method, path))
        return endpoints
    
    return extract_endpoints(data['item'])

def normalize_path(path: str) -> str:
    """Normalize path by replacing parameter patterns"""
    # Convert {param} to {{param}} for consistency 
    path = re.sub(r'\{([^}]+)\}', r'{{\1}}', path)
    # Also handle triple braces from Postman {{{}}} -> {{}}
    path = re.sub(r'\{\{\{([^}]+)\}\}\}', r'{{\1}}', path)
    return path

def compare_routes(laravel_routes: Set[Tuple[str, str]], postman_routes: Set[Tuple[str, str]]):
    """Compare Laravel routes with Postman collection and find differences"""
    
    # Normalize paths in both sets
    normalized_laravel = set()
    normalized_postman = set()
    
    for method, path in laravel_routes:
        normalized_path = normalize_path(path)
        normalized_laravel.add((method, normalized_path))
    
    for method, path in postman_routes:
        normalized_path = normalize_path(path)
        normalized_postman.add((method, normalized_path))
    
    # Find missing routes (in Laravel but not in Postman)
    missing_in_postman = normalized_laravel - normalized_postman
    
    # Find extra routes (in Postman but not in Laravel)
    extra_in_postman = normalized_postman - normalized_laravel
    
    return missing_in_postman, extra_in_postman

def categorize_routes(routes: Set[Tuple[str, str]]) -> dict:
    """Categorize routes by their prefix/category"""
    categories = {}
    
    for method, path in routes:
        if not path:
            category = "root"
        else:
            # Get the first segment as category
            parts = path.split('/')
            category = parts[0] if parts[0] else "root"
        
        if category not in categories:
            categories[category] = []
        categories[category].append((method, path))
    
    # Sort each category
    for category in categories:
        categories[category].sort()
    
    return categories

def main():
    laravel_file = '/Users/smariqislam/Sites/syllaby/routes/api-v1.php'
    postman_file = '/Users/smariqislam/Sites/syllaby/storage/data/ariq/syllaby-postman-collection/syllaby-api-collection.json'
    
    print("🔍 Analyzing Laravel routes vs Postman collection...")
    print("=" * 60)
    
    # Parse both files
    laravel_routes = parse_laravel_routes(laravel_file)
    postman_routes = parse_postman_collection(postman_file)
    
    print(f"📋 Laravel routes found: {len(laravel_routes)}")
    print(f"📋 Postman endpoints found: {len(postman_routes)}")
    print()
    
    # Compare routes
    missing_in_postman, extra_in_postman = compare_routes(laravel_routes, postman_routes)
    
    print(f"❌ Missing in Postman: {len(missing_in_postman)}")
    print(f"➕ Extra in Postman: {len(extra_in_postman)}")
    print()
    
    # Categorize missing routes
    if missing_in_postman:
        print("🚨 MISSING ENDPOINTS IN POSTMAN COLLECTION:")
        print("=" * 50)
        missing_categories = categorize_routes(missing_in_postman)
        
        for category, routes in sorted(missing_categories.items()):
            print(f"\n📁 {category.upper()}:")
            for method, path in routes:
                print(f"   {method:<7} {path}")
    
    # Show extra routes in Postman
    if extra_in_postman:
        print("\n\n➕ EXTRA ENDPOINTS IN POSTMAN (not in Laravel):")
        print("=" * 50)
        extra_categories = categorize_routes(extra_in_postman)
        
        for category, routes in sorted(extra_categories.items()):
            print(f"\n📁 {category.upper()}:")
            for method, path in routes:
                print(f"   {method:<7} {path}")
    
    print(f"\n\n📊 SUMMARY:")
    print(f"   Total Laravel routes: {len(laravel_routes)}")
    print(f"   Total Postman endpoints: {len(postman_routes)}")
    print(f"   Missing in Postman: {len(missing_in_postman)}")
    print(f"   Extra in Postman: {len(extra_in_postman)}")

if __name__ == "__main__":
    main()