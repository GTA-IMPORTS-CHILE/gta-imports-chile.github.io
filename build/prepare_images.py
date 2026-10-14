"""Copy + resize the website's photos from the GTA BRAND tree (read-only) into docs/assets/img/.

Sources are listed per product in catalog.py (PHOTOS). Re-run after changing a photo list:
    python3 company/website/build/prepare_images.py
Output: <slug>/<n>.jpg (max 1400 px, white background, q82) + <slug>/<n>-s.jpg (max 640 px thumb).
"""
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent.parent
sys.path.insert(0, str(WORKSPACE / "ingest"))
sys.path.insert(0, str(HERE))
from paths import GTA_BRAND  # noqa: E402
from catalog import PHOTOS, SITE_PHOTOS  # noqa: E402

PHOTO_ROOTS = {"brand": GTA_BRAND / "PRODUCT PHOTOS", "logo": GTA_BRAND / "LOGO",
               "ws": WORKSPACE, "static": HERE / "assets_static"}
OUT = HERE.parent / "docs" / "assets" / "img"


def src_path(ref):
    root, rel = ref.split(":", 1)
    return PHOTO_ROOTS[root] / rel


def flatten(im):
    im.draft("RGB", (2800, 2800))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def write(im, dest, size):
    im = im.copy()
    im.thumbnail((size, size), Image.LANCZOS)
    im.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    return im.size


def main():
    missing, n = [], 0
    jobs = [(slug, refs) for slug, refs in PHOTOS.items()] + [("site", [r for _, r in SITE_PHOTOS])]
    for slug, refs in jobs:
        d = OUT / slug
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.jpg"):
            old.unlink()
        for i, ref in enumerate(refs, 1):
            p = src_path(ref)
            if not p.is_file():
                missing.append(ref)
                continue
            im = flatten(Image.open(p))
            write(im, d / f"{i}.jpg", 1400)
            write(im, d / f"{i}-s.jpg", 640)
            n += 1
    print(f"wrote {n} photos (+ thumbs) into {OUT}")
    if missing:
        print("MISSING SOURCES (not written):", *missing, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
