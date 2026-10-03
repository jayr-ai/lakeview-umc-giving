"""
One-off script that generates the 9 ministry detail pages (one per
ministry card on the homepage) as static HTML files. Not run automatically
by the site - re-run this only when the shared template or the ministry
data below changes. Safe to delete once pages are hand-edited directly.

Run with: python3 tools_generate_ministry_pages.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

MINISTRIES = [
    {
        "slug": "youthconnect",
        "title": "Youth Connect",
        "tagline": "A monthly table set for every teen who walks in.",
        "image": "youth-connect",
        "image_alt": "Youth Connect monthly outreach gathering",
        "about": "Every month, Youth Connect brings together 100 to 120 teens and volunteers for an evangelistic outreach night reaching barangay youth. It lands on the 4th Saturday of the month, and every single time, it ends the same way: with the gospel shared plainly, and an altar call.",
        "highlights": [
            "Happens every 4th Saturday of the month, reaching barangay youth",
            "Draws 100 to 120 teens and volunteers each time",
            "Always ends with the gospel shared, and an altar call",
        ],
        "cost_amount": "₱4,000 a month",
        "cost_annual": "₱48,000 a year",
        "cost_detail": "covers food for every teen who walks through the door - a full table, every time, for every teen.",
    },
    {
        "slug": "kidsconnect",
        "title": "Kids Connect",
        "tagline": "A monthly gathering built just for kids.",
        "image": "kids-connect",
        "image_alt": "Kids Connect monthly gathering",
        "about": "Kids Connect is a monthly gathering for 60 to 100 kids, built around one simple goal: helping kids learn who Jesus is, in a space made just for them.",
        "highlights": [
            "Gathers 60 to 100 kids every month",
            "Built entirely around helping kids learn who Jesus is",
            "Part of our weekly rhythm across the Kids ministry stream",
        ],
        "cost_amount": "₱3,000 a month",
        "cost_annual": "₱36,000 a year",
        "cost_detail": "keeps this gathering running for every child who comes, every month of the year.",
    },
    {
        "slug": "kidssundayschool",
        "title": "Kids Sunday School",
        "tagline": "Every single Sunday, for our youngest learners.",
        "image": "kids-sunday-school",
        "image_alt": "Kids Sunday School weekly program",
        "about": "Kids Sunday School runs every single Sunday during worship, so our youngest learners always have a place built for them - no child ever ages out of belonging here.",
        "highlights": [
            "Runs every single Sunday, without exception",
            "Built specifically for our youngest learners",
            "Happens alongside the main worship service",
        ],
        "cost_amount": "₱1,000 a week",
        "cost_annual": "₱52,000 a year",
        "cost_detail": "keeps this program running for our youngest learners, every Sunday of the year.",
    },
    {
        "slug": "myafconnect",
        "title": "MYAF Connect",
        "tagline": "A quarterly space for young adults navigating it all.",
        "image": "myaf-connect",
        "image_alt": "MYAF Connect young adult gathering",
        "about": "MYAF Connect gathers 30 to 50 young adults and volunteers each quarter - a space built for those in their 20s and 30s navigating work, relationships, and a faith that's becoming their own.",
        "highlights": [
            "Gathers 30 to 50 young adults plus volunteers, four times a year",
            "Built for the questions that come with this season of life",
            "Part of our weekly Young Adult ministry stream",
        ],
        "cost_amount": "₱3,000 a quarter",
        "cost_annual": "₱12,000 a year",
        "cost_detail": "keeps this space open for young adults, four times a year.",
    },
    {
        "slug": "pickupministry",
        "title": "Pick Up Ministry",
        "tagline": "So transportation is never the reason someone misses church.",
        "image": "pickup-ministry",
        "image_alt": "Pick Up Ministry vehicle bringing people to church",
        "about": "Every week, our Pick Up Ministry physically picks up people who want to come to church but have no way to get here. It exists for one reason: so a lack of transportation is never what keeps someone from showing up.",
        "highlights": [
            "Runs every single week",
            "Exists so transportation is never the reason someone misses church",
            "Covers real gasoline cost for every ride, every week",
        ],
        "cost_amount": "₱2,000 a week in gasoline",
        "cost_annual": "₱104,000 a year",
        "cost_detail": "keeps every ride running, every week of the year.",
    },
    {
        "slug": "sundaycelebration",
        "title": "Sunday Celebration",
        "tagline": "Lunch fellowship - so no one rushes home hungry.",
        "image": "sunday-celebration",
        "image_alt": "Sunday lunch fellowship after service",
        "about": "After service, Sunday Celebration keeps the table open for lunch fellowship - so no one has to rush home hungry. It's a tight, carefully managed weekly budget that stretches to feed the whole church family, then carries straight into the afternoon's Discipleship Groups.",
        "highlights": [
            "Happens every Sunday, right after service",
            "Feeds the whole church family on a carefully managed weekly budget",
            "Leads straight into the afternoon's Discipleship Groups",
        ],
        "cost_amount": "₱3,000 a week",
        "cost_annual": "₱156,000 a year",
        "cost_detail": "keeps the table open, every single Sunday.",
    },
    {
        "slug": "encounterretreat",
        "title": "Encounter Retreat",
        "tagline": "A weekend that marks a milestone in someone's walk with Jesus.",
        "image": "encounter-retreat",
        "image_alt": "Encounter Retreat weekend",
        "about": "Twice a year, the Encounter Retreat brings disciples through a life-marking weekend that marks one of the defining milestones on the journey: salvation, water baptism, the Encounter Retreat, baptism of the Holy Spirit, becoming an apprentice leader, and eventually commissioning into ministry.",
        "highlights": [
            "Held twice a year, every year",
            "Marks one of the key milestones in a disciple's journey",
            "A full weekend experience, not a single session",
        ],
        "cost_amount": "₱50,000 per retreat, twice a year",
        "cost_annual": "₱100,000 a year",
        "cost_detail": "makes this milestone weekend possible for every disciple who's ready for it.",
    },
    {
        "slug": "leadersnight",
        "title": "Leaders & Volunteers Appreciation Night",
        "tagline": "One night a year, for the people who give the rest of theirs.",
        "image": "leaders-night",
        "image_alt": "Leaders and Volunteers Appreciation Night",
        "about": "Once a year, we set aside a night to honor our unpaid volunteer leaders - the people who give their weeknights and weekends to disciple others, on top of their own jobs and families.",
        "highlights": [
            "Happens once a year",
            "Honors leaders who serve entirely as volunteers",
            "A small thank-you for people who give far more than they're asked",
        ],
        "cost_amount": "₱10,000 a year",
        "cost_annual": "₱10,000 a year",
        "cost_detail": "is set aside for one night that honors the people who give the rest of their year to everyone else.",
    },
    {
        "slug": "landasingraduation",
        "title": "LANDASIN Graduation",
        "tagline": "A celebration for every disciple ready to lead others.",
        "image": "landasin-graduation",
        "image_alt": "LANDASIN Graduation celebration",
        "about": "LANDASIN is our discipleship curriculum - three levels (TUKLAS: new life and salvation, SIBOL: becoming like Christ, GANAP: equipped to lead), 36 lessons over about 8 to 9 months. Once a year, we celebrate every disciple who completes the full journey and is ready to lead others through it.",
        "highlights": [
            "Happens once a year, for every disciple who finishes the journey",
            "LANDASIN is 36 lessons across 3 levels, over about 8 to 9 months",
            "Marks a disciple's readiness to lead others through DGroups",
        ],
        "cost_amount": "₱10,000 a year",
        "cost_annual": "₱10,000 a year",
        "cost_detail": "is set aside for a celebration that marks the finish of an 8 to 9 month journey.",
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Lakeview United Methodist Church</title>
<meta name="description" content="{tagline} See how your partnership with Lakeview United Methodist Church's {title} makes it possible.">
<link rel="canonical" href="https://give.thelakeviewumc.com/{slug}/">

<meta property="og:type" content="website">
<meta property="og:title" content="{title} | Lakeview United Methodist Church">
<meta property="og:description" content="{tagline}">
<meta property="og:image" content="https://give.thelakeviewumc.com/assets/images/{image}.jpg">
<meta property="og:url" content="https://give.thelakeviewumc.com/{slug}/">
<meta property="og:site_name" content="Lakeview United Methodist Church">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | Lakeview United Methodist Church">
<meta name="twitter:description" content="{tagline}">
<meta name="twitter:image" content="https://give.thelakeviewumc.com/assets/images/{image}.jpg">

<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>

<a class="skip-link" href="#main">Skip to main content</a>

<header class="site-header" id="top">
  <div class="wrap header-inner">
    <a class="brand" href="/">
      <img src="/assets/logo.svg" alt="Lakeview United Methodist Church" width="160" height="32">
    </a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="primary-nav" id="primaryNav">
      <a href="/#ministries">Ministries</a>
      <a href="/#budget">The Full Picture</a>
      <a href="/#partner">Ways to Partner</a>
      <a href="/#faq">FAQ</a>
      <a class="nav-cta" href="/#partner">Become a Partner</a>
    </nav>
  </div>
</header>

<main id="main">

  <section class="hero hero-short">
    <div class="hero-media">
      <img src="/assets/images/{image}.jpg" alt="{image_alt}" width="1200" height="900" fetchpriority="high">
    </div>
    <div class="hero-scrim"></div>
    <div class="wrap hero-content reveal">
      <a href="/#ministries" class="back-link">&larr; Back to all ministries</a>
      <h1>{title}</h1>
      <p class="lede">{tagline}</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow reveal">
      <p>{about}</p>

      <ul class="detail-highlights">
{highlights_html}
      </ul>

      <div class="cost-callout">
        <h2>What your partnership provides</h2>
        <p><strong>{cost_amount}</strong> - <strong>{cost_annual}</strong> - {cost_detail}</p>
      </div>

      <div class="detail-gallery">
        <img src="/assets/images/{image}.jpg" alt="{image_alt}" width="1200" height="900" loading="lazy">
        <img src="/assets/images/{image}-2.jpg" alt="More photos of {title} coming soon" width="1200" height="900" loading="lazy">
      </div>

      <div class="detail-cta">
        <a class="btn btn-gold btn-large" href="/#partner">Become a Ministry Partner</a>
      </div>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-brand">
      <img src="/assets/logo.svg" alt="Lakeview United Methodist Church" width="160" height="32">
      <p>@RockforJesus</p>
    </div>
    <div class="footer-info">
      <p>[PLACEHOLDER ADDRESS]</p>
      <p>[PLACEHOLDER CONTACT - phone / email]</p>
      <p><a href="https://thelakeviewumc.com">thelakeviewumc.com</a></p>
    </div>
  </div>
</footer>

<script src="/js/main.js" defer></script>
</body>
</html>
"""


def build_page(data):
    highlights_html = "\n".join(
        '        <li>{}</li>'.format(h) for h in data["highlights"]
    )
    return TEMPLATE.format(highlights_html=highlights_html, **data)


if __name__ == "__main__":
    for m in MINISTRIES:
        out_dir = os.path.join(ROOT, m["slug"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(build_page(m))
        print("wrote", out_path)
