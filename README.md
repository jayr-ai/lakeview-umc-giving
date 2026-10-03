# Lakeview UMC - Ministry Partner Page

A fast, static site inviting people, companies, churches, and institutions
to become financial Ministry Partners of Lakeview United Methodist Church
(@RockforJesus). Plain HTML/CSS/JS - no build step, no framework, no
backend. A homepage plus 9 ministry detail pages (one per ministry card),
so specific amounts live on the detail pages rather than the first thing a
visitor sees.

**Live at:** https://give.thelakeviewumc.com/
**Repo:** https://github.com/jayr-ai/lakeview-umc-giving

## Preview locally

No build step is required. Any static file server works, for example:

```bash
cd lakeview-umc-giving
python3 -m http.server 8080
```

Then open `http://localhost:8080` in a browser. Opening `index.html`
directly by double-clicking also works for a quick look, though a local
server more closely matches how GitHub Pages serves the real site.

## How GitHub Pages deployment works for this repo

This follows the same pattern as the church's main site,
`thelakeviewumc.com`. Already done for this repo - notes kept here for
reference or if this ever needs to be redeployed elsewhere.

1. Push this folder's contents to a GitHub repository. (Done: `jayr-ai/lakeview-umc-giving`.)
2. In that repo's **Settings -> Pages**, set the source to deploy from the
   `main` branch, root (`/`) folder. (Done.)
3. The `CNAME` file already in this repo's root (containing
   `give.thelakeviewumc.com`) tells GitHub Pages which custom domain to
   serve the site on - keep that file as-is.
4. Once DNS (below) is pointed correctly and GitHub Pages shows the custom
   domain as verified, enable **Enforce HTTPS** in the same Pages settings
   screen.

## DNS record needed

DNS is already pointed and propagated. For reference, the record added was:

- **Type:** CNAME
- **Host/Name:** `give`
- **Value/Target:** `jayr-ai.github.io`
- **TTL:** default/automatic

This points `give.thelakeviewumc.com` at GitHub Pages, matching the pattern
already used for the main site.

## Ministry detail pages

Each ministry card on the homepage links to its own page, so the
homepage grid can stay warm and amount-free while the real cost lives
where it belongs - after enough context has been given:

| Ministry | Live page |
|---|---|
| Youth Connect | `/youthconnect/` |
| Kids Connect | `/kidsconnect/` |
| Kids Sunday School | `/kidssundayschool/` |
| MYAF Connect | `/myafconnect/` |
| Pick Up Ministry | `/pickupministry/` |
| Sunday Celebration | `/sundaycelebration/` |
| Encounter Retreat | `/encounterretreat/` |
| Leaders & Volunteers Night | `/leadersnight/` |
| LANDASIN Graduation | `/landasingraduation/` |

Each page has a hero banner, an "About" paragraph, a short highlights
list, a "What your partnership provides" cost callout, a 2-photo gallery,
and a "Become a Ministry Partner" button back to the homepage's giving
section.

**These 9 pages are generated, not hand-written.** They all come from one
shared template in [`tools_generate_ministry_pages.py`](./tools_generate_ministry_pages.py),
driven by a `MINISTRIES` data list at the top of that file (title,
tagline, about paragraph, highlights, cost line, image filenames). To
change a ministry page's copy:

1. Edit that ministry's entry in the `MINISTRIES` list in
   `tools_generate_ministry_pages.py`.
2. Re-run `python3 tools_generate_ministry_pages.py` - this overwrites
   all 9 `<slug>/index.html` files from the template.
3. Commit and push the regenerated files.

Editing a generated `<slug>/index.html` file directly works too for a
one-off tweak, but it will be overwritten the next time the generator
script runs.

## Where to drop in real photos

See [`PHOTOS.md`](./PHOTOS.md) for the full manifest - every image slot,
its exact file path, and the recommended photo shape. Short version: name
your photo exactly like the placeholder it replaces (e.g. `hero.jpg`) and
drop it into `/assets/images/`, overwriting the placeholder.

The real church logo goes at `/assets/logo.svg`, replacing the placeholder
text wordmark currently there.

## Where to add the real PayMongo links

Open [`js/main.js`](./js/main.js) and find the `PAYMONGO_LINKS` object near
the top of the file:

```js
var PAYMONGO_LINKS = {
  onetime: "https://pm.link/PAYMONGO_LINK_ONETIME",
  monthly: "https://pm.link/PAYMONGO_LINK_MONTHLY",
  lovegift: "https://pm.link/PAYMONGO_LINK_LOVEGIFT"
};
```

Replace each placeholder URL with the real PayMongo-hosted Payment Link
created in the PayMongo dashboard for that giving type. That's the only
place these need to change - the three buttons in the "Ways to Partner"
section pick up the new links automatically.

### Important decision needed: single-use Payment Links

PayMongo's dashboard-generated **Payment Links** are typically **single-use
per link** (reusable for repeat page views is not guaranteed the way a
generic "pay us" page needs). Before launch, confirm with PayMongo support
or your PayMongo dashboard whether a single Payment Link can safely be
reused by many different donors over time, or whether it needs to be
regenerated periodically.

**If a reusable link is not available**, the fallback path (not yet built -
build this only if needed) is a minimal **Cloudflare Worker** (serverless,
no full backend required) that calls PayMongo's **Checkout Sessions API**
server-side on each visit, generating a fresh checkout session per donor
while keeping the PayMongo secret key safe (never exposed in this static
site's client-side code). This keeps the site static and fast while solving
the single-use-link problem. Ask for this to be built once the single-use
question is confirmed.

## GCash / Bank Transfer fallback details

In `index.html`, search for `[FILL IN]` inside the "Prefer to give directly
via GCash or bank transfer?" expandable section and replace with the real
GCash name/number and bank account name/number/bank name.

## Final headline choice

The hero headline currently live is:

> "You're Invited to Become a Ministry Partner"

Two alternates were considered and can be swapped in instead by editing the
`<h1>` inside the `.hero-content` block in `index.html`:

- "We'd Love to Invite You Into What God Is Doing Here"
- "An Invitation: Partner With Us in Raising Disciples"

## Placeholders still needing real content before launch

- [ ] Real PayMongo links for all 3 giving types (`js/main.js`)
- [ ] Confirm PayMongo Payment Link reusability (see decision above)
- [ ] Real church logo at `/assets/logo.svg`
- [ ] All real photos per `PHOTOS.md`
- [ ] 3 real testimonials + names (search `index.html` for `[PLACEHOLDER TESTIMONY]` and `[PLACEHOLDER NAME]`)
- [ ] GCash name/number + bank transfer details (search `index.html` for `[FILL IN]`)
- [ ] Final hero headline pick (see above - current default already works)
- [ ] Tax-deductibility FAQ answer, once SEC/BIR non-profit status is confirmed (search `index.html` for the tax-deductible FAQ item)
- [ ] Jayvee's (Discipleship Head) contact info, for the FAQ "who can I talk to" answer and the footer

## Project structure

```
lakeview-umc-giving/
  index.html                        the homepage
  youthconnect/index.html           ministry detail page (generated, see below)
  kidsconnect/index.html            ...and 7 more ministry detail pages,
  kidssundayschool/index.html       one folder per ministry, same pattern
  myafconnect/index.html
  pickupministry/index.html
  sundaycelebration/index.html
  encounterretreat/index.html
  leadersnight/index.html
  landasingraduation/index.html
  css/styles.css                    all styling, shared by every page
  js/main.js                        PayMongo link config + nav/reveal/toggle behavior
  assets/logo.svg                   church logo (placeholder wordmark for now)
  assets/images/                    all photo placeholders (see PHOTOS.md)
  tools_generate_placeholders.py    script that generated the placeholder images (not deployed; safe to ignore/delete)
  tools_generate_ministry_pages.py  script that generates the 9 detail pages (see "Ministry detail pages" above)
  CNAME                             GitHub Pages custom domain config
  PHOTOS.md                         full photo manifest
  README.md                         this file
```

## Editing copy without breaking layout

All visible text lives directly in `index.html` as plain readable sentences
inside tags like `<h2>`, `<p>`, and `<li>`. To edit copy:

1. Open `index.html` in any text editor.
2. Find the sentence you want to change (use your editor's search/Find).
3. Type over the text between the tags, leaving the tags themselves
   (`<p>` ... `</p>`, etc.) untouched.
4. Save and refresh the browser to see the change.

Do not remove or reorder the opening/closing tag pairs, and do not delete
the `class="..."` or `id="..."` attributes on any element - those are what
the CSS and JS use to find and style things.

## Self-review checklist (completed before handoff)

- [x] Page load speed: single CSS file, single JS file, no external
      frameworks loaded, images lazy-loaded below the fold, hero image
      preloaded with `fetchpriority="high"`.
- [x] Mobile layout at 375px width: single-column stacking, nav collapses
      to a toggle menu, tables scroll horizontally instead of breaking
      layout.
- [x] Color contrast: navy (#0E2E57) on white/cream and white text on navy
      both meet WCAG AA for body text; gold accents are used for large
      text/accents, not small low-contrast body copy.
- [x] No em dashes or en dashes anywhere in the copy - plain hyphens only.
