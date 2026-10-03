"""
One-off script to generate on-brand placeholder JPGs for every photo slot
listed in PHOTOS.md. Not part of the deployed site - safe to delete once
real photos are dropped in. Run with: python3 tools_generate_placeholders.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

NAVY = (14, 46, 87)       # #0E2E57 - matches thelakeviewumc.com --lake-900
NAVY_DEEP = (8, 28, 54)   # darker navy for gradient end
GOLD = (216, 163, 64)     # #D8A340 - matches thelakeviewumc.com --gold

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "images")

# (filename, width, height, label)
SLOTS = [
    ("hero.jpg", 1600, 900, "Photo coming soon"),
    ("youth-connect.jpg", 1200, 900, "Youth Connect"),
    ("kids-connect.jpg", 1200, 900, "Kids Connect"),
    ("kids-sunday-school.jpg", 1200, 900, "Kids Sunday School"),
    ("myaf-connect.jpg", 1200, 900, "MYAF Connect"),
    ("pickup-ministry.jpg", 1200, 900, "Pick Up Ministry"),
    ("sunday-celebration.jpg", 1200, 900, "Sunday Celebration"),
    ("encounter-retreat.jpg", 1200, 900, "Encounter Retreat"),
    ("leaders-night.jpg", 1200, 900, "Leaders & Volunteers Night"),
    ("landasin-graduation.jpg", 1200, 900, "LANDASIN Graduation"),
    ("story-1.jpg", 800, 800, "Story Coming Soon"),
    ("story-2.jpg", 800, 800, "Story Coming Soon"),
    ("story-3.jpg", 800, 800, "Story Coming Soon"),
    # second gallery photo for each ministry detail page
    ("youth-connect-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("kids-connect-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("kids-sunday-school-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("myaf-connect-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("pickup-ministry-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("sunday-celebration-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("encounter-retreat-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("leaders-night-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("landasin-graduation-2.jpg", 1200, 900, "More Photos Coming Soon"),
    ("og-image.jpg", 1200, 630, "Lakeview UMC - Ministry Partners"),
]

def load_font(size):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def make_placeholder(path, w, h, label):
    img = Image.new("RGB", (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Diagonal-ish vertical gradient navy -> deeper navy
    for y in range(h):
        t = y / h
        r = int(NAVY[0] * (1 - t) + NAVY_DEEP[0] * t)
        g = int(NAVY[1] * (1 - t) + NAVY_DEEP[1] * t)
        b = int(NAVY[2] * (1 - t) + NAVY_DEEP[2] * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Thin gold rule frame
    margin = int(min(w, h) * 0.04)
    draw.rectangle(
        [margin, margin, w - margin, h - margin],
        outline=GOLD,
        width=max(2, int(min(w, h) * 0.004)),
    )

    # Small gold cross-and-flame-ish mark (simple cross) above label
    cross_size = int(min(w, h) * 0.09)
    cx, cy = w // 2, int(h * 0.42)
    bar = max(3, int(cross_size * 0.16))
    draw.rectangle([cx - bar // 2, cy - cross_size // 2, cx + bar // 2, cy + cross_size // 2], fill=GOLD)
    draw.rectangle([cx - cross_size // 2, cy - bar // 2, cx + cross_size // 2, cy + bar // 2], fill=GOLD)

    # Label text, centered
    font_size = max(18, int(min(w, h) * 0.055))
    font = load_font(font_size)
    text = label
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx, ty = (w - tw) / 2, h * 0.58
    draw.text((tx, ty), text, font=font, fill=(237, 230, 216))

    sub_font = load_font(max(14, int(font_size * 0.5)))
    sub = "Lakeview UMC"
    bbox2 = draw.textbbox((0, 0), sub, font=sub_font)
    sw = bbox2[2] - bbox2[0]
    draw.text(((w - sw) / 2, ty + th + 14), sub, font=sub_font, fill=GOLD)

    img.save(path, "JPEG", quality=72, optimize=True)
    print(f"wrote {path} ({os.path.getsize(path)} bytes)")

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, w, h, label in SLOTS:
        make_placeholder(os.path.join(OUT_DIR, name), w, h, label)
