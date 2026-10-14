# gta-imports-web

The informational product-showcase website of **GTA IMPORTS CHILE SpA** — www.gta-imports.cl.
Static HTML, served by GitHub Pages from `docs/`. No prices, no cart, no forms (ruling 2026-10-13).

## Change something
| What | Where |
|---|---|
| Product text, specs, photos list, families, old-URL redirects | `build/catalog.py` |
| Page layouts, home/FAQ/policies text, contact data, tracking tags | `build/build_site.py` |
| Look & feel | `build/site.css` |

```bash
python3 build/prepare_images.py   # only when a photo list changed (reads GTA BRAND/PRODUCT PHOTOS, read-only)
python3 build/build_site.py       # rebuilds docs/ and checks every internal link
git add -A && git commit -m "…" && git push   # live in ~1 minute
```

## Hosting & DNS
- GitHub Pages: branch `main`, folder `/docs`, custom domain `www.gta-imports.cl`, HTTPS enforced.
- GoDaddy DNS: `www` CNAME → `gta-imports-chile.github.io.` · apex `gta-imports.cl` keeps GoDaddy forwarding → www ·
  MX/SPF (email) untouched · TXT `_github-pages-challenge-GTA-IMPORTS-CHILE` = domain verification (optional).
- Tracking copied verbatim from the old Odoo site: GA4 `G-TBT2MG4KZP`, GTM `GTM-N36ZQXMX`, Search Console meta.
