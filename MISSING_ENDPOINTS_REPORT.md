# Syllaby API - Missing Endpoints Report

## Summary
- **Total Laravel routes**: 212
- **Total Postman endpoints**: 141  
- **Missing in Postman**: 133 endpoints
- **Potentially different parameter naming**: 62 endpoints

---

## Critical Missing Endpoints by Category

### 1. **Assets** (2 missing)
```
DELETE  assets/{asset}
PUT     assets/{asset}/bookmark/toggle
```

### 2. **Characters** (6 missing)
```
DELETE  characters/{character}
GET     characters/{character}
POST    characters/{character}/image
POST    characters/{character}/preview  
POST    characters/{character}/train
PUT     characters/{character}
```

### 3. **Clones** (6 missing)
```
DELETE  clones/{clonable}
GET     clones
GET     clones/{clonable}
PATCH   clones/{clonable}/voices
POST    clones/avatars
POST    clones/voices
```

### 4. **Events** (4 missing)
```
DELETE  events/{event}
GET     events/tracker-reports
PATCH   events/{event}
PUT     events/{event}/completes
```

### 5. **Folders** (3 missing)
```
PUT     folders/resources/{destination}/move
PUT     folders/{folder}
PUT     folders/{folder}/bookmark
```

### 6. **Generators** (1 missing)
```
GET     generators/options
```

### 7. **Media** (2 missing)
```
GET     media/{uuid}/download
POST    media/download
```

### 8. **Metadata** (7 missing)
```
GET     metadata/social-providers
GET     metadata/youtube/categories
POST    metadata/generate/context
POST    metadata/generate/description
POST    metadata/generate/tags
POST    metadata/generate/title
POST    metadata/tiktok/creator-info
```

### 9. **Presets** (2 missing)
```
DELETE  presets/faceless/{preset}
PATCH   presets/faceless/{preset}
```

### 10. **Previews** (3 missing)
```
GET     previews/audios
GET     previews/{video}
POST    previews/render
```

### 11. **Publications** (9 missing)
```
DELETE  publications/{publication}
DELETE  publications/{publication}/thumbnail
GET     publications/limits
GET     publications/{publication}
GET     publications/{publication}/channels/{channel}
PATCH   publications/{publication}
POST    publications/{publication}/thumbnail
PUT     publications/{publication}
PUT     publications/{publication}/thumbnails/attach
```

### 12. **Real Clones** (9 missing)
```
DELETE  real-clones/avatars/{avatar}
DELETE  real-clones/{clone}
GET     real-clones/{clone}
GET     real-clones/{clone}/status
PATCH   real-clones/{clone}
POST    real-clones/{clone}/generate
POST    real-clones/{clone}/retries
POST    real-clones/{clone}/scrape
PUT     real-clones/{clone}/scripts
```

### 13. **Root** (1 missing)
```
GET     / (Welcome endpoint)
```

### 14. **Schedulers** (10 missing)
```
DELETE  schedulers/{scheduler}/events
GET     schedulers/{scheduler}
GET     schedulers/{scheduler}/occurrences
PATCH   schedulers/occurrences/{occurrence}
PATCH   schedulers/{scheduler}
POST    schedulers/csv-parser
POST    schedulers/{scheduler}/occurrences
POST    schedulers/{scheduler}/run
PUT     schedulers/occurrences/{occurrence}/scripts
PUT     schedulers/{scheduler}/toggle
```

### 15. **Stock Media** (5 missing)
```
GET     stock-media/audios
GET     stock-media/images/collections/{collection}
GET     stock-media/images/search
GET     stock-media/videos/collections/{collection}
GET     stock-media/videos/search
```

### 16. **Subscriptions** (18 missing)
```
DELETE  subscriptions/cancel
DELETE  subscriptions/storage
GET     subscriptions/details
GET     subscriptions/plans
GET     subscriptions/plans/retention
GET     subscriptions/products/{product}
GET     subscriptions/storage/plans
PATCH   subscriptions/swap-plan
POST    subscriptions/checkout
POST    subscriptions/coupons/redeem
POST    subscriptions/customer-portal
POST    subscriptions/end-trial
POST    subscriptions/extend-trial
POST    subscriptions/google-play/checkout-completed
POST    subscriptions/payment-intent
POST    subscriptions/proration
POST    subscriptions/purchases
POST    subscriptions/resume
POST    subscriptions/subscribe
PUT     subscriptions/cancel-downgrade
PUT     subscriptions/storage
```

### 17. **Tags** (1 missing)
```
GET     tags/{tag}
```

### 18. **Templates** (1 missing)
```
GET     templates/{template}
```

### 19. **Thumbnails** (3 missing)
```
DELETE  thumbnails/{thumbnail}
GET     thumbnails
POST    thumbnails
```

### 20. **Topics** (1 missing)
```
PUT     topics/{topic}/bookmark
```

### 21. **Track Events** (1 missing)
```
POST    track-events
```

### 22. **User Feedback** (1 missing)
```
POST    user-feedback
```

### 23. **Videos** (33 missing - largest category)
```
DELETE  videos/{video}
DELETE  videos/{video}/assets/{asset}
GET     videos/faceless/{faceless}
GET     videos/faceless/{faceless}/assets
GET     videos/faceless/{faceless}/assets/{asset}
GET     videos/faceless/{faceless}/media/animation
GET     videos/footage/{footage}/timeline
GET     videos/{uuid}/render
GET     videos/{video}
GET     videos/{video}/assets
GET     videos/{video}/status
PATCH   videos/faceless/{faceless}
PATCH   videos/faceless/{faceless}/assets
PATCH   videos/footage/{footage}
PATCH   videos/{video}
POST    videos/faceless/{faceless}/convert
POST    videos/faceless/{faceless}/export
POST    videos/faceless/{faceless}/media/animation
POST    videos/faceless/{faceless}/media/generate
POST    videos/faceless/{faceless}/media/transload
POST    videos/faceless/{faceless}/media/upload
POST    videos/faceless/{faceless}/render
POST    videos/faceless/{faceless}/retry
POST    videos/faceless/{faceless}/scrape
POST    videos/faceless/{faceless}/scrape/images
POST    videos/faceless/{faceless}/transcriptions
POST    videos/faceless/{faceless}/transcriptions/upload
POST    videos/footage
POST    videos/footage/{footage}/render
POST    videos/{video}/assets
POST    videos/{video}/assets/transload
PUT     videos/faceless/{faceless}/scripts
PUT     videos/footage/{footage}/preference
PUT     videos/footage/{footage}/timeline
```

---

## Priority Implementation Recommendations

### **HIGH PRIORITY** (Core functionality missing)
1. **Subscriptions** (18 endpoints) - Payment and billing functionality
2. **Videos** (33 endpoints) - Core video creation features  
3. **Publications** (9 endpoints) - Content publishing functionality
4. **Real Clones** (9 endpoints) - AI avatar features
5. **Schedulers** (10 endpoints) - Content scheduling

### **MEDIUM PRIORITY** (Important features)
6. **Metadata** (7 endpoints) - Content metadata generation
7. **Characters** (6 endpoints) - Character management
8. **Clones** (6 endpoints) - Voice/avatar cloning
9. **Stock Media** (5 endpoints) - Media library access

### **LOW PRIORITY** (Nice to have)
10. **Events** (4 endpoints) - Event tracking
11. **Thumbnails** (3 endpoints) - Thumbnail management  
12. **Previews** (3 endpoints) - Content previews
13. **Folders** (3 endpoints) - Organization features
14. **Media** (2 endpoints) - Media downloads
15. **Assets**, **Presets**, and other smaller categories

---

## Parameter Naming Inconsistencies

Many endpoints exist in Postman but use different parameter naming:
- Laravel: `{asset}` vs Postman: `{asset_id}`
- Laravel: `{video}` vs Postman: `{video_id}`
- Laravel: `{character}` vs Postman: `{character_id}`

These should be standardized for consistency.

---

## Next Steps

1. **Start with HIGH PRIORITY categories** - Focus on Subscriptions and Videos first
2. **Create endpoint groups** - Organize similar endpoints into folders  
3. **Standardize parameter naming** - Use consistent naming conventions
4. **Add proper documentation** - Include descriptions and examples
5. **Test all endpoints** - Ensure they work with the actual API

Total estimated work: **133 new endpoints** to be added to the Postman collection.