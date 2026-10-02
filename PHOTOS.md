# Photo Manifest - Lakeview UMC Ministry Partner Page

Every image slot the page uses, with its exact file path. Placeholder
images (navy/gold gradient panels with a label) are already in place at
every path below so the page never shows a broken image icon. Drop in the
real photo using the **exact same filename** and the new photo replaces
the placeholder automatically - no code changes needed.

| Path | Used for | Recommended shape |
|---|---|---|
| `/assets/images/hero.jpg` | Hero banner | Wide landscape (e.g. 1600x900 or wider), the congregation or a worship moment |
| `/assets/images/youth-connect.jpg` | Youth Connect ministry card | Landscape, 4:3 |
| `/assets/images/kids-connect.jpg` | Kids Connect ministry card | Landscape, 4:3 |
| `/assets/images/kids-sunday-school.jpg` | Kids Sunday School ministry card | Landscape, 4:3 |
| `/assets/images/myaf-connect.jpg` | MYAF Connect (Young Adults) ministry card | Landscape, 4:3 |
| `/assets/images/pickup-ministry.jpg` | Pick Up Ministry ministry card | Landscape, 4:3 |
| `/assets/images/sunday-celebration.jpg` | Sunday Celebration / Lunch Fellowship ministry card | Landscape, 4:3 |
| `/assets/images/encounter-retreat.jpg` | Encounter Retreat ministry card | Landscape, 4:3 |
| `/assets/images/leaders-night.jpg` | Leaders and Volunteers Appreciation Night ministry card | Landscape, 4:3 |
| `/assets/images/landasin-graduation.jpg` | LANDASIN Graduation ministry card | Landscape, 4:3 |
| `/assets/images/story-1.jpg` | Testimonial 1 photo | Square, 1:1 |
| `/assets/images/story-2.jpg` | Testimonial 2 photo | Square, 1:1 |
| `/assets/images/story-3.jpg` | Testimonial 3 photo | Square, 1:1 |
| `/assets/logo.svg` | Header logo + footer logo | Church cross-and-flame mark + "Lakeview UMC" wordmark, SVG preferred |
| `/assets/images/og-image.jpg` | Social share preview (Facebook/Messenger/Twitter link previews) | Landscape, 1200x630 exactly |

## How to replace a placeholder

1. Resize/export your real photo close to the recommended shape above (exact pixel size isn't critical - the page crops to fit).
2. Compress it (keep JPGs under ~300KB each so the page stays fast - [tinypng.com](https://tinypng.com) or any photo editor's "export for web" works).
3. Name it **exactly** as shown in the table (same filename, same `.jpg`/`.svg` extension).
4. Drop it into the matching folder, overwriting the placeholder file.
5. Also update `story-1.jpg` / `story-2.jpg` / `story-3.jpg`'s matching testimony text and name directly in `index.html` (search for `[PLACEHOLDER TESTIMONY]` and `[PLACEHOLDER NAME]`).

## Regenerating placeholders

If you ever need to regenerate the placeholder images (for example, to preview a layout before real photos are ready), run:

```
python3 tools_generate_placeholders.py
```

This script requires Pillow (`pip3 install Pillow`) and is not part of the deployed site - safe to delete once all real photos are in place.
