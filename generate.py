#!/usr/bin/env python3
"""Generate Case Studies portfolio HTML pages from structured content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES_DIR = ROOT / "cases"

CASES = [
    {
        "slug": "ftux-retention",
        "num": "01",
        "title": "FTUX Optimization & Strategic Retention",
        "short": "Behavioral segmentation and MaxDiff research that recovered $17M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Two mental models lived in the same first-trade funnel. Segment-specific onboarding and failure-state messaging turned drop-off into retained revenue.",
        "stats": [
            ("$17M", "Retained monthly revenue"),
            ("~900K", "Users retained monthly"),
            ("60%+", "Drop in post-rejection drop-off"),
            ("18%", "Trade volume lift, top-tier customers"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The Event Contracts and Prediction Markets division was losing users in the first-time experience—especially right after signup and first-trade friction. People who had already churned or never completed a first trade were hard to study with traditional qualitative recruiting alone.</p>""",
            ),
            (
                "Task",
                """<p>Isolate the exact friction points, understand the needs of different archetypes inside the same funnel, and ship structural changes that stabilized retention without flattening the product for either group.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Behavioral segmentation</strong> — Uncovered two mental models: newly acquired sports bettors with little brokerage/crypto experience, and existing Robinhood users treating prediction markets like sophisticated trading.</li>
<li><strong>MaxDiff survey</strong> — Ranked each segment’s unique informational needs with Maximum Differential scaling.</li>
<li><strong>Experimental validation</strong> — Partnered with data science on controlled tests; variants received tailored onboarding, personalized recommendations, and custom watchlists aligned to MaxDiff preferences.</li>
<li><strong>Friction remediation</strong> — Mapped barriers after first-trade rejection and built personalized messaging through failure states.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>A personalized messaging strategy after first-trade rejection cut drop-off by over 60%, retaining ~900K users/month (~$17M monthly revenue). MaxDiff-informed experiments drove 4–12% engagement/retention lifts and an 18% increase in trade volume among top-tier customers.</p>
<p class="callout">Research did not just describe the funnel — it rewired onboarding around how sports-first bettors and brokerage/crypto traders actually think.</p>""",
            ),
        ],
    },
    {
        "slug": "live-prototyping",
        "num": "02",
        "title": "Live Prototype Interventions & UX Architecture",
        "short": "AI-orchestrated prototyping that collapsed a weeks-long design loop into a single interview.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Concepts were generated and stress-tested inside live interviews—before production engineering ever started.",
        "stats": [
            ("10%", "Reduction in corporate overhead"),
            ("1", "Researcher delivering validated prototypes"),
            ("Same day", "Concept → usability → handoff"),
            ("0", "Production code required to validate"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Feature validation typically required alignment across growth, product, design, and marketing, stretching iteration cycles across weeks. Teams needed high-fidelity assets faster than standard research workflows could produce them.</p>""",
            ),
            (
                "Task",
                """<p>Short-circuit the design loop by bringing interactive prototyping into the active research session—testing concepts before a single line of production code was written.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>AI-orchestrated design flow</strong> — Used Claude and custom agents against existing Figma systems.</li>
<li><strong>Real-time synthesis</strong> — Spotted mental models and barriers early in an interview, then generated/updated interactive prototypes mid-session from live feedback.</li>
<li><strong>Instant usability testing</strong> — Put fresh variants back in front of the same participant within the same hour.</li>
<li><strong>Engineering handoff</strong> — Packaged validated components as engineering-ready specs.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Delivered engineering-ready designs mid-interview and bypassed traditional multi-cycle design reviews. A volume of cross-functional insight work that would typically require up to 10 stakeholders contributed to a ~10% reduction in corporate overhead after implementation.</p>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "title": "Research Ops Automation Lifecycle",
        "short": "An autonomous AI workflow that quadrupled concurrent research capacity.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "A month-long research cycle became a two-week system—without sacrificing rigor.",
        "stats": [
            ("4×", "Concurrent research capacity"),
            ("30 → 14", "Days typical cycle time"),
            ("End-to-end", "Compliance → multi-format reporting"),
            ("AI agents", "Autonomous study lifecycle"),
        ],
        "sections": [
            (
                "Situation",
                """<p>A single research project was fragmented across compliance approvals, custom plans, stakeholder review, multi-day user-list queries, collection, analysis, and executive packaging. A standard cycle could consume a full calendar month.</p>""",
            ),
            (
                "Task",
                """<p>Streamline the operational architecture, remove administrative lag, and multiply concurrent studies without compromising statistical or qualitative rigor.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>End-to-end automation</strong> — Architected autonomous AI agents to manage study lifecycles from compliance approval through user-list generation and multi-format reporting.</li>
<li><strong>Workflow compression</strong> — Removed administrative lag that previously stretched a standard project across a full calendar month.</li>
<li><strong>Concurrent capacity</strong> — Designed the system so multiple studies could run without pipeline blockages.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Compressed a 30-day research cycle to two weeks and quadrupled concurrent capacity to four active studies—without sacrificing methodological rigor.</p>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "04",
        "title": "Cross-Sell Acquisition & Research Org Scale",
        "short": "Doubled cross-sell acquisition while scaling UX Research into a 32-person division.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2024–2025",
        "summary": "As Lead UX Researcher, I linked behavioral signals to cross-sell growth while building the research organization that could sustain it—AI-enabled pipelines included.",
        "stats": [
            (">$500M", "Projected LTV impact"),
            ("2×", "Cross-sell acquisition"),
            ("$8–10M", "Added monthly recurring revenue"),
            ("32", "Researchers in scaled org"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Cross-sell conversion had room to grow, and the research function needed to scale with the ambition of FanDuel’s core products—delivering reliable insight at the pace of Product, Marketing, and Engineering.</p>""",
            ),
            (
                "Task",
                """<p>Direct research strategy that tied behavioral signals to cross-sell opportunities, while scaling UX Research into an organization capable of 200+ studies a year—and accelerating insight-to-launch with AI-enabled pipelines.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Research leadership</strong> — Scaled UX Research into a 32-person division; mentored researchers and designers; partnered across Product and Marketing.</li>
<li><strong>Growth diagnosis</strong> — Connected continuous CX measurement and behavioral signals to stalled cross-sell funnels.</li>
<li><strong>AI-enabled pipelines</strong> — Directed research systems that cut turnaround time by ~75%, accelerating insight-to-launch cycles.</li>
<li><strong>Experimentation</strong> — Validated interventions with large-scale testing and product analytics so recommendations shipped with evidence.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Cross-sell acquisition doubled, adding $8–10M in monthly recurring revenue (&gt;$500M LTV). The scaled org supported 14% MAU growth and a durable research operating model for core products.</p>
<p class="callout">Research operated as a growth engine and a leadership practice—not a reporting function.</p>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "05",
        "title": "NFL Direct-to-Consumer Packaging Research",
        "short": "Design studios and a national panel that revealed how price reshapes package preference.",
        "context": "NFL · Fantasy Sports & NFL+",
        "year": "2018–2021",
        "summary": "Five D2C packaging architectures were evaluated with studio fans and validated against a 2,208-fan national survey—showing à-la-carte appeal before price, and tiered preference after.",
        "stats": [
            ("24", "Studio participants across 2 design studios"),
            ("2,208", "National survey respondents"),
            ("5", "Package architectures tested (A–E)"),
            ("p&lt;.001", "Package C ranked #1 after pricing"),
        ],
        "sections": [
            (
                "Situation",
                """<p>NFL Digital Media needed evidence for how to structure Direct-to-Consumer offerings spanning NFL+, Clubs+, Club Pass, League Pass, and RedZone Mobile—before committing to a packaging architecture fans would actually buy.</p>""",
            ),
            (
                "Task",
                """<p>Determine which package arrangements fans were most motivated to consume, measure reach and appeal by segment, and explain preferences through Motivation to Consume Content (MCC) drivers drawn from fan-behavior literature.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Pilot interviews</strong> — Stress-tested survey comprehension with 3 fans; refined instruments and studio protocol.</li>
<li><strong>Design studios (n=24)</strong> — Fans built MOSCOW media packages, then ranked Packages A–E before and after pricing.</li>
<li><strong>National survey (n=2,208)</strong> — Quantified feature interest and competitor platform usage at scale.</li>
<li><strong>Multivariate analysis</strong> — Linked package preference to motives: excitement/drama, loyalty, social interaction, performance tracking, escape, aesthetics, vicarious achievement, and football IQ.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Before price, Package D (à-la-carte) led; after price, <strong>Package C (tiered)</strong> ranked first (79% top-two), with a large shift away from single-platform options. Package D still scored highest on perceived flexibility/value, while C balanced cognitive and affective motives—critical input for packaging strategy.</p>
<p class="callout">“Must have” demand concentrated on League Pass (42%) and NFL+ (29%); RedZone Mobile trailed as a won't-have for many social/family-driven fans.</p>""",
            ),
        ],
    },
    {
        "slug": "product-benchmarking",
        "num": "06",
        "title": "Competitive Product Benchmarking System",
        "short": "A quarterly usability & loyalty scorecard across FanDuel products and key competitors.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2022",
        "summary": "SUPR-Q, journey Ease of Use, loyalty intentions, and Responsible Gaming scores—weighted to revenue/platform mix—became a living product scorecard.",
        "stats": [
            ("2,881", "Customers in the Q2 wave"),
            ("13,637", "Surveyed since 2021 across quarters"),
            ("75%", "Industry standard for SUPR-Q / Ease"),
            ("85%", "FanDuel RG score standard"),
        ],
        "sections": [
            (
                "Situation",
                """<p>FanDuel needed a repeatable way to track whether digital products were improving in the wild—against both internal baselines and competitors like DraftKings, BetMGM, and TwinSpires—not just against one-off usability tests.</p>""",
            ),
            (
                "Task",
                """<p>Run a quarterly benchmarking program that surfaces strengths, weaknesses, and actionable design insights across Sportsbook, Casino, Fantasy, TVG, and related experiences—including financial-transaction ease and Responsible Gaming.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Metric stack</strong> — SUPR-Q usability, journey Ease of Use, Net Intentions loyalty, and Responsible Gaming Likert scores.</li>
<li><strong>Competitive scorecards</strong> — Side-by-side cards vs. primary rivals per product line.</li>
<li><strong>Weighted scoring</strong> — Platform split and revenue weights so underrepresented cohorts did not distort product-level decisions.</li>
<li><strong>2022 expansions</strong> — Deeper live-dealer analysis, deposit/withdrawal ease, and verbatim loyalty drivers.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Q2 showed Ease of Use above industry standard across FanDuel products, with SUPR-Q gains nearly everywhere except TVG (Kentucky Derby friction). Loyalty lagged as the shared improvement theme—especially around discovery, variety, and promo-driven engagement—giving product teams a clear, comparable roadmap each quarter.</p>""",
            ),
        ],
    },
    {
        "slug": "team-chemistry",
        "num": "07",
        "title": "Team Chemistry Measurement Program",
        "short": "A season-long sports psychology program to measure and shape team cohesion.",
        "context": "Burkmont Analytics · PHX Proposal",
        "year": "2016–2017",
        "summary": "A three-mission engagement—Recon, Unite, Conquer—turned team chemistry from anecdote into a weekly measurement and intervention system.",
        "stats": [
            ("3", "Mission phases across the season"),
            ("Weekly", "Game-linked chemistry measures"),
            ("30+ yrs", "Research basis in sports & orgs"),
            ("Time-series", "Design for in-season change"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Elite talent and traditional analytics explain only part of on-court performance. Burkmont Analytics proposed treating team chemistry—the tendency of a group to remain united toward instrumental goals—as a measurable performance lever.</p>""",
            ),
            (
                "Task",
                """<p>Design a full-season program for a professional basketball organization: assess culture, intervene deliberately, and monitor chemistry with the same seriousness as physical performance data.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Mission 1 — Recon</strong> — Literature review, culture definition, baseline surveys/observations, staff debrief (Jun–Jul 2016).</li>
<li><strong>Mission 2 — Unite</strong> — Preseason activity, 2–3 in-season sessions, weekly game measures, midseason reporting (Aug 2016–Feb 2017).</li>
<li><strong>Mission 3 — Conquer</strong> — Continued monitoring, additional sessions, and a comprehensive end-of-season report (Feb–Apr 2017).</li>
</ul>
<p>Methods blended sports psychology, social psychology, and advanced measurement—weekly reporting kept coaching staff close to the signal.</p>""",
            ),
            (
                "Outcome",
                """<p>The proposal established a concrete operating model: chemistry as an analytic input alongside talent, with deliverables that moved from baseline identity work to season-long regulation. It framed performance enhancement as a measurable behavioral systems problem—not a motivational poster.</p>""",
            ),
        ],
    },
    {
        "slug": "smartphone-esm",
        "num": "08",
        "title": "Smartphone-Enabled Experience Sampling",
        "short": "Bringing ESM into the field with PACO to study engagement, stress, and burnout in daily life.",
        "context": "Claremont Graduate University · WSH 2013",
        "year": "2013",
        "summary": "A methods contribution: using Android smartphones and Google’s PACO platform to run robust Experience Sampling in occupational health research.",
        "stats": [
            ("ESM", "In-the-moment self-report method"),
            ("PACO", "Scalable smartphone signaling platform"),
            ("2", "Field studies at CGU exemplified"),
            ("Offline", "Capable data collection on-device"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Classic ESM relied on booklets, pagers, watches, or early PDAs. Researchers studying daily engagement, stress, and burnout needed scalable signaling and data entry that matched how people actually lived and worked.</p>""",
            ),
            (
                "Task",
                """<p>Introduce smartphone-enabled ESM—specifically PACO (Personal Analytic Companion)—as a secure, scalable way to run occupational health ESM and intervention designs.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Platform</strong> — PACO surveys authored in-browser; Android clients could run offline; response types included Likert, text, lists, GPS, and photo.</li>
<li><strong>Schedules</strong> — Daily, weekly, monthly, random ESM, and self-report triggers.</li>
<li><strong>Field examples</strong> — Flow Experience study (50 students; devices provided; 6 random vs 1 daily signal) and Study of Experience class project (59 participants on own devices; 8 random signals × 5 days).</li>
<li><strong>Methods honesty</strong> — Documented device heterogeneity, signaling UX, remote participant management, and emerging custom feedback/intervention hooks.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Presented at the 10th International Conference on Occupational Stress and Health (Los Angeles), the work positioned smartphone ESM as a practical research infrastructure—bridging academic method and real-world deployment constraints.</p>
<p class="callout">This methods foundation threads through later industry work: measurement in context, event-tied capture, and research instruments that survive contact with real users.</p>""",
            ),
        ],
    },
]


def header(active=None, prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{"Sam Weinberger — Case Studies" if not active else f"{active} — Sam Weinberger"}</title>
  <meta name="description" content="Samuel Weinberger — applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. Bridging human behavior, analytics, and interactive design." />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{prefix}index.html">Sam Weinberger</a>
      <nav class="nav" aria-label="Primary">
        <a href="{prefix}index.html#work">Work</a>
        <a href="{prefix}index.html#about">About</a>
        <a href="{prefix}index.html#life">Life</a>
        <a href="mailto:samuelcweinberger@gmail.com">Contact</a>
      </nav>
    </div>
  </header>
"""


def footer(prefix=""):
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div>© {__import__('datetime').datetime.now().year} Sam Weinberger</div>
      <div><a href="mailto:samuelcweinberger@gmail.com">samuelcweinberger@gmail.com</a></div>
    </div>
  </footer>
  <script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def write_index():
    rows = []
    for c in CASES:
        rows.append(
            f"""    <a class="case-row reveal" href="cases/{c['slug']}.html">
      <div class="case-num">{c['num']}</div>
      <div>
        <h3>{c['title']}</h3>
        <p>{c['short']}</p>
      </div>
      <div class="case-meta">{c['year']}</div>
    </a>"""
        )
    html = (
        header()
        + f"""
  <main>
    <section class="hero">
      <div class="hero-media" role="img" aria-label="Research work in progress"></div>
      <div class="hero-atmosphere" aria-hidden="true"></div>
      <div class="wrap hero-copy">
        <div class="hero-kicker">AI-Driven Insights</div>
        <h1 class="hero-brand">Sam<br />Weinberger<em>.</em></h1>
        <p class="hero-role">Applied Cognitive and Social psychologist</p>
        <p class="hero-lede">9+ years of mixed-methods research across fintech, sports media, and healthcare—connecting usability, field research, and AI-augmented workflows to product and revenue outcomes.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#work">View case studies</a>
          <a class="btn btn-ghost" href="mailto:samuelcweinberger@gmail.com">Email Sam</a>
        </div>
      </div>
    </section>

    <section class="section" id="work">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Selected work</h2>
          <p>Case studies from Robinhood prediction markets, FanDuel sportsbook research, NFL digital products, and academic methods work.</p>
        </div>
        <div class="case-list">
{chr(10).join(rows)}
        </div>
      </div>
    </section>

    <section class="section" id="about">
      <div class="wrap about-grid">
        <div class="reveal">
          <div class="section-head">
            <h2>About</h2>
          </div>
          <p>I’m an applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. I specialize in bridging the gap between human behavior, advanced data analytics, and interactive design. My academic background—including graduate research focused on human motivation, persuasion, and systemic behavior change—serves as the foundation for how I approach product strategy.</p>
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
          <p>Today, I operate as a highly technical hybrid. By integrating generative AI and automated workflows into my practice, I’ve expanded my reach across product, design, engineering, and data science. Whether I am orchestrating end-to-end research operations, deploying automated quantitative surveys, or rapidly generating interactive, engineering-ready prototypes mid-interview, I focus on one thing: translating complex human behavior into massive product momentum.</p>
        </div>
        <div class="reveal">
          <div class="pill-row">
            <span class="pill">Cognitive &amp; social psychology</span>
            <span class="pill">UX Engineering</span>
            <span class="pill">Quantitative UX research</span>
            <span class="pill">Human behavior</span>
            <span class="pill">Data analytics</span>
            <span class="pill">Interactive design</span>
            <span class="pill">Generative AI</span>
            <span class="pill">Research ops</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="life">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Life outside the lab</h2>
          <p>Devoted father, aviation enthusiast, poet, and former NCAA Division I athlete.</p>
        </div>

        <div class="life-intro reveal">
          <p>Away from products and experiments, I’m focused on raising my son, building and flying RC jets, writing poetry, and staying competitive as a former athlete. Those pursuits keep me grounded in curiosity, discipline, and care—the same instincts that shape how I do research.</p>
          <p class="life-athletics">I competed as a fullback for <a href="https://gostanford.com/sports/football/roster/player/sam-weinberger" target="_blank" rel="noopener noreferrer">Stanford Football</a> and later pitched for <a href="https://usctrojans.com/sports/baseball/roster/sam-weinberger/354" target="_blank" rel="noopener noreferrer">USC Baseball</a>.</p>
        </div>

        <div class="life-themes reveal">
          <div>
            <h3>Devoted father</h3>
            <p>Weekends look like school drop-offs, fishing trips, and hands-on projects together—showing up is the constant.</p>
          </div>
          <div>
            <h3>Aviation enthusiast</h3>
            <p>RC jets, airfields, and the craft of getting machines flight-ready—engineering for the joy of it.</p>
          </div>
          <div>
            <h3>Poet</h3>
            <p>Writing is how I process motivation, meaning, and the quieter patterns in everyday life.</p>
          </div>
          <div>
            <h3>Former athlete</h3>
            <p>From Division I football and baseball to the golf course today—competition taught focus under pressure.</p>
          </div>
        </div>

        <div class="life-gallery reveal">
          <figure class="life-shot life-shot-tall">
            <img src="media/life/father-son.jpg" alt="Sam with his son outside school" loading="lazy" />
            <figcaption>Fatherhood first</figcaption>
          </figure>
          <figure class="life-shot">
            <img src="media/life/aviation-sabre.jpg" alt="Son with a U.S. Air Force RC Sabre jet" loading="lazy" />
            <figcaption>Aviation, shared</figcaption>
          </figure>
          <figure class="life-shot">
            <img src="media/life/aviation-mig.jpg" alt="Son giving a thumbs up beside an RC MiG jet" loading="lazy" />
            <figcaption>Flight day</figcaption>
          </figure>
          <figure class="life-shot life-shot-tall">
            <img src="media/life/fishing.jpg" alt="Son holding a fish he caught" loading="lazy" />
            <figcaption>On the water</figcaption>
          </figure>
          <figure class="life-shot">
            <img src="media/life/golf.jpg" alt="Sam teeing off on a golf course" loading="lazy" />
            <figcaption>Still competing</figcaption>
          </figure>
          <figure class="life-shot life-shot-tall">
            <img src="media/life/boat.jpg" alt="Sam smiling at the helm of a boat" loading="lazy" />
            <figcaption>I enjoy steering the ship</figcaption>
          </figure>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "index.html").write_text(html)


def write_case(case, index):
    prev_c = CASES[index - 1] if index > 0 else None
    next_c = CASES[index + 1] if index < len(CASES) - 1 else None
    stats = "\n".join(
        f'      <div class="stat"><strong>{v}</strong><span>{l}</span></div>'
        for v, l in case["stats"]
    )
    sections = "\n".join(
        f'      <section class="reveal">\n        <h2>{title}</h2>\n        {body}\n      </section>'
        for title, body in case["sections"]
    )
    prev_link = (
        f'<a href="{prev_c["slug"]}.html">← {prev_c["num"]} {prev_c["title"]}</a>'
        if prev_c
        else "<span></span>"
    )
    next_link = (
        f'<a href="{next_c["slug"]}.html">{next_c["num"]} {next_c["title"]} →</a>'
        if next_c
        else "<span></span>"
    )
    html = (
        header(active=case["title"], prefix="../")
        + f"""
  <main>
    <section class="case-hero">
      <div class="wrap">
        <div class="crumb"><a href="../index.html">Case studies</a> / {case['num']}</div>
        <div class="eyebrow">{case['context']} · {case['year']}</div>
        <h1>{case['title']}</h1>
        <p class="summary">{case['summary']}</p>
        <div class="stat-band">
{stats}
        </div>
      </div>
    </section>
    <div class="wrap prose">
{sections}
    </div>
    <div class="wrap pager">
      {prev_link}
      {next_link}
    </div>
  </main>
"""
        + footer(prefix="../")
    )
    (CASES_DIR / f"{case['slug']}.html").write_text(html)


def main():
    CASES_DIR.mkdir(parents=True, exist_ok=True)
    write_index()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote index + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
