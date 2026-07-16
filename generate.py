#!/usr/bin/env python3
"""Generate Case Studies portfolio HTML pages from structured content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES_DIR = ROOT / "cases"

BRANDS = {
    "robinhood": {
        "label": "Robinhood",
        "product": "Prediction Markets",
    },
    "fanduel": {
        "label": "FanDuel",
        "product": "Sportsbook & CPE",
    },
    "nfl": {
        "label": "NFL",
        "product": "Fantasy & Digital Media",
    },
}

CASES = [
    {
        "slug": "ftux-retention",
        "num": "01",
        "brand": "robinhood",
        "title": "FTUX Optimization & Strategic Retention",
        "short": "Behavioral segmentation and MaxDiff research that recovered $17M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Behavioral segmentation, quantitative survey methodology, and multi-million dollar revenue retention.",
        "stats": [
            ("$17M", "Retained monthly revenue"),
            ("~900K", "Users retained monthly"),
            ("60%+", "Drop in post-rejection churn"),
            ("18%", "Trade volume increase, top-tier customers"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The Event Contracts and Prediction Markets division at Robinhood was experiencing noticeable drop-offs in the first-time user flow—particularly right after signup and first-trade friction. Recruiting users who had already churned, or failed to complete a first trade, is notoriously difficult to study qualitatively.</p>""",
            ),
            (
                "Task",
                """<p>Isolate the exact friction points causing the drop-offs, understand the needs of disparate user archetypes within the same funnel, and implement structural changes to stabilize retention.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Behavioral segmentation</strong> — Uncovered two distinct mental models in the funnel: newly acquired sports bettors with zero brokerage or crypto experience, and existing Robinhood users exploring prediction markets as sophisticated traders.</li>
<li><strong>MaxDiff survey</strong> — Designed and deployed a Maximum Differential (MaxDiff) quantitative survey to systematically rank and isolate each segment’s unique informational needs.</li>
<li><strong>Experimental validation</strong> — Partnered with data science on a controlled experiment with isolated control groups; variant users received tailored onboarding, personalized recommendations, and custom watchlists aligned to their MaxDiff preferences.</li>
<li><strong>Friction remediation</strong> — Pinpointed the exact barriers causing drop-off after a first-trade rejection and built a targeted, personalized messaging strategy to guide users through failure states.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Retained ~$17M in monthly revenue and ~900K users monthly. Post-rejection churn dropped by over 60%. Trade volume among top-tier customers rose 18%, with retention lifts of 12% for the brokerage/crypto segment and 4% for sports-first users.</p>""",
            ),
        ],
    },
    {
        "slug": "live-prototyping",
        "num": "02",
        "brand": "robinhood",
        "title": "Live Prototype Interventions & UX Architecture",
        "short": "AI-orchestrated prototyping that collapsed a weeks-long design loop into a single interview.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Bypassing slow design-to-engineering loops via generative AI and real-time usability testing.",
        "stats": [
            ("10%", "Reduction in corporate overhead"),
            ("10 → 1", "Stakeholders typically required"),
            ("Same day", "Concept → usability → handoff"),
            ("0", "Production code required to validate"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Traditional feature validation required extensive alignment across growth, product, design, and marketing—stretching feature iterations out over weeks. Validating features that didn’t exist yet needed high-fidelity assets faster than standard research methods could produce them.</p>""",
            ),
            (
                "Task",
                """<p>Short-circuit the design iteration cycle by introducing real-time, interactive prototyping into the active research phase—testing concepts before a single line of production code was written.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>AI-orchestrated design flow</strong> — Used Claude and custom autonomous AI agents to interact directly with existing Figma design systems.</li>
<li><strong>Real-time synthesis</strong> — Identified user mental models and behavioral barriers at the start of a customer interview, then used the AI orchestration layer to generate and update high-fidelity, interactive prototypes mid-interview based on live feedback.</li>
<li><strong>Instant usability testing</strong> — Presented the freshly generated design variants back to the same participant by the middle and end of the same session—testing concepts that hadn’t existed an hour earlier.</li>
<li><strong>Direct engineering handoff</strong> — Packaged the successful, validated design components into engineering-ready specifications.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Where feature validation once required ~10 stakeholders across growth, product, and marketing, one researcher delivered fully validated, engineering-ready prototypes live within the interview—contributing to a 10% reduction in corporate overhead post-implementation.</p>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "brand": "robinhood",
        "title": "Research Ops Automation Lifecycle",
        "short": "An autonomous AI workflow that quadrupled concurrent research capacity.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Scaling research throughput, workflow automation, and compressing time-to-insight.",
        "stats": [
            ("4×", "Concurrent research capacity"),
            ("30 → 14", "Days typical cycle time"),
            ("End-to-end", "Compliance → multi-format reporting"),
            ("AI agents", "Autonomous study lifecycle"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The end-to-end process of executing a single research project at Robinhood was highly fragmented—compliance approvals, custom research plans, stakeholder feedback, manual database queries for user lists (4–5 days alone), data collection, analysis, and building decks and executive summaries. A standard project cycle consumed up to a full calendar month.</p>""",
            ),
            (
                "Task",
                """<p>Streamline the operational architecture, remove administrative lag, and multiply the volume of concurrent studies without compromising statistical or qualitative rigor.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>End-to-end automation</strong> — Built an autonomous AI workflow using Claude to orchestrate every step of the research lifecycle.</li>
<li><strong>Workflow compression</strong> — Automated compliance-check routing, dynamically generated standardized research plans for stakeholder review, and streamlined data pipelines for real-time list generation.</li>
<li><strong>Synthesis &amp; reporting</strong> — Programmed AI nodes to ingest raw survey and interview outputs and instantly draft dual-delivery assets: a concise one-page executive summary for leadership and a deep-dive, multi-slide deck for product teams.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Compressed a traditional 30-day project cycle to two weeks after full automation, and quadrupled concurrent capacity so four studies could run without pipeline blockages.</p>""",
            ),
        ],
    },
    {
        "slug": "acquisition-offers",
        "num": "04",
        "brand": "fanduel",
        "title": "Acquisition Offers & First-Bet Activation",
        "short": "A 1×3 RCT that lifted first-bet conversion 10 points—and proved the $5 offer beat $50 on ROI and loyalty.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2024",
        "summary": "A multi-factor evaluation of acquisition tactics: High-Accessibility vs High-Stakes promotions vs control, solving the Ease of Use paradox behind onboarding drop-off.",
        "stats": [
            ("+10 pts", "Absolute conversion lift vs control"),
            ("20% → 30%", "Activation-to-first-bet goal"),
            ("4×", "Lower payout cost for $5 offer vs $50"),
            ("N=1,050", "Randomized controlled trial"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Activation-to-first-bet was the #1 leading indicator for long-term retention and LTV. Onboarding conversion sat below target—and a 15% trust deficit looked like a technical problem. Surveys flipped that story: drop-offs rated Ease of Use the same as converters. The real barrier was conceptual confusion around promotional offers.</p>""",
            ),
            (
                "Task",
                """<p>Lead a cross-functional CPE strike team to raise first-bet conversion from 20% to 30%, and learn which incentive structure drives conversion without eroding loyalty—especially ahead of state launches where first impressions win market share.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>1×3 randomized controlled trial</strong> — New visitors assigned to High-Accessibility (Bet $5, Get $50), High-Stakes (Bet $50, Get $200), or control (no promo); n=350 per group (N=1,050).</li>
<li><strong>Immediate + longitudinal measurement</strong> — Alchemer surveys after first bet (Perceived Generosity, Loyalty, Ease of Use); Amplitude-triggered repeats at 30/60/90 days; Qualtrics via Braze for drop-off reasons.</li>
<li><strong>Statistical program</strong> — Chi-square and pairwise Z-tests (Bonferroni) for conversion; t-tests for Ease of Use; multiple regression for 90-day engagement; mixed-design ANOVA for loyalty decay.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Both offers delivered a significant 10-point absolute lift over control, with no difference between $5 and $50 offers (p=0.56)—making the High-Accessibility offer the ROI winner at ~4× lower payout cost. Ease of Use did not differ between drop-offs and converters; conceptual confusion around “Win to Get” rules did. A first win predicted 90-day engagement ~4× more than bonus size, while high-stakes loyalty crashed by Day 60.</p>
<p class="callout">Standardize Bet $5 / Get $50, redesign promo messaging for clarity, and prioritize features that create an early “First Win.”</p>""",
            ),
        ],
    },
    {
        "slug": "onboarding-deposit",
        "num": "05",
        "brand": "fanduel",
        "title": "Behavioral Onboarding & Deposit Optimization",
        "short": "Trust-first KYC and wallet UX that converted 150K+ stagnant users and unlocked $12M in incremental handle.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2025",
        "summary": "Onboarding UX, fintech compliance (KYC), and first-time deposit growth—diagnosing whether drop-off was motivation or a trust barrier.",
        "stats": [
            ("$12M", "Incremental handle in Q1 2025"),
            ("150K+", "Stagnant users converted"),
            ("65%", "New sign-ups blocked at wallet setup"),
            ("30%", "Fewer support tickets"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Users completed registration but abandoned before setting up banking or making a First-Time Deposit (FTD). Amplitude mapped the moment of exit: registration was seamless, yet the Wallet/Banking Setup screen was a barrier for 65% of new sign-ups.</p>""",
            ),
            (
                "Task",
                """<p>Determine whether the registration-to-deposit gap was a motivation problem or a specific trust barrier during financial setup—and close the Drop-off Delta between account creation and financial commitment.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Triangulated mixed methods</strong> — Combined Amplitude funnel mapping, in-depth interviews, moderated usability, and a MaxDiff survey to isolate where and why users stalled.</li>
<li><strong>Trust diagnosis</strong> — Interviews showed users were comfortable sharing basic identity info, but hit a hard wall at routing numbers and SSNs—with profound confusion around ACH payments and why that sensitivity was required on a sports platform.</li>
<li><strong>Progressive disclosure</strong> — Partnered with content designers to re-sequence: low-stakes data (phone, email) first to build momentum before sensitive wallet fields.</li>
<li><strong>Contextual framing</strong> — Introduced micro-explanations of why federal regulations required specific banking data, humanizing the compliance wall and clarifying ACH security.</li>
<li><strong>Validation</strong> — 15 moderated sessions observed hesitation at the routing-number field; a MaxDiff survey with 5,000 users identified which phrasing maximized confidence in sharing sensitive financial details.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Re-sequenced flow and optimized messaging lifted successful wallet setups and deposits. Converted 150,000+ stagnant users, generating an estimated $12M in incremental handle in Q1 2025, and cut support tickets by 30% by explaining why sensitive information was mandatory.</p>
<p class="callout">Established the Trust-First Onboarding Playbook as the company standard.</p>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "06",
        "brand": "fanduel",
        "title": "Continuous CX Measurement & Cross-Sell Growth",
        "short": "A real-time Hyper-Focused Lens that doubled cross-sell acquisition in 90 days.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2024–2025",
        "summary": "Enterprise UX and growth-driven research: a continuous CX measurement framework applied to a stalled cross-sell conversion funnel.",
        "stats": [
            ("$500M", "Projected LTV impact"),
            ("2×", "Cross-sell acquisitions within 90 days"),
            ("14%", "Lift in Monthly Active Users"),
            ("$5M+", "Incremental monthly revenue"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Lagging brand trackers could not keep pace with product health. Cross-sell conversion between product lines had stagnated at roughly 10% for the year—without a clear read on where, or why, customers were dropping off.</p>""",
            ),
            (
                "Task",
                """<p>Architect a real-time Continuous CX Measurement Framework—a “Hyper-Focused Lens” across Ease of Use, Functional Reliability, and User Satisfaction—then apply it to the cross-sell bottleneck to prove research could function as a growth engine, not a cost center.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Three-pronged methodology</strong> — Monthly in-app Pulse Checks (1% sampling), longitudinal quantitative benchmarking, and large-scale competitive usability testing (n=4,000).</li>
<li><strong>Technical integration</strong> — Partnered with engineering on event-based triggers (deposit_success, login_success) to capture sentiment at the Peak-End moment, reducing recall bias.</li>
<li><strong>Cross-functional alignment</strong> — Built a unified dashboard mapping UX metrics (UMUX-Lite / SEQ) directly to product KPIs and business OKRs.</li>
<li><strong>Cross-sell deep dive</strong> — Funnel analysis isolated drop-off at Payment Linking; 120 structured interviews (including 20 unmoderated) surfaced trust hurdles around data sharing; A/B usability testing with 30,000 users validated the optimal path; Amplitude telemetry enabled rapid iteration of messaging and UI.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Doubled annual cross-sell acquisitions within 90 days, with a 14% MAU lift, $5M+ incremental monthly revenue, and a projected $500M LTV impact. Support-per-user metrics fell enough to drive estimated seven-figure annual customer-operations savings.</p>
<p class="callout">Formally adopted as the Standardized Research Playbook for future product onboarding and promotional launches.</p>""",
            ),
        ],
    },
]


def header(active=None, prefix="", brand=None):
    brand_class = f' class="brand-{brand}"' if brand else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{"Sam Weinberger — Case Studies" if not active else f"{active} — Sam Weinberger"}</title>
  <meta name="description" content="Samuel Weinberger — applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. Bridging human behavior, analytics, and interactive design." />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
</head>
<body{brand_class}>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{prefix}index.html">Sam Weinberger</a>
      <nav class="nav" aria-label="Primary">
        <a href="{prefix}index.html#work">Work</a>
        <a href="{prefix}index.html#about">About</a>
        <a href="mailto:samuelcweinberger@gmail.com">Contact</a>
      </nav>
    </div>
  </header>
"""


def product_badge(brand_key, prefix=""):
    meta = BRANDS[brand_key]
    mark = ""
    if brand_key == "fanduel":
        mark = f'<img class="product-mark" src="{prefix}media/brands/fanduel-mark.png" alt="" width="22" height="22" />'
    elif brand_key == "robinhood":
        mark = '<span class="product-mark product-mark-rh" aria-hidden="true"></span>'
    elif brand_key == "nfl":
        mark = '<span class="product-mark product-mark-nfl" aria-hidden="true"></span>'
    return f'<span class="product-badge product-{brand_key}">{mark}<span class="product-name">{meta["label"]}</span></span>'


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
        badge = product_badge(c["brand"])
        rows.append(
            f"""    <a class="case-row case-{c['brand']} reveal" href="cases/{c['slug']}.html">
      <div class="case-num">{c['num']}</div>
      <div>
        {badge}
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
      <div class="hero-media" aria-hidden="true">
        <video autoplay muted loop playsinline poster="media/hero.jpg">
          <source src="media/hero.mp4" type="video/mp4" />
        </video>
      </div>
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
          <p>Case studies branded by product: Robinhood prediction markets and FanDuel sportsbook / CPE research.</p>
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
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market—including a quarterly product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
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
    badge = product_badge(case["brand"], prefix="../")
    html = (
        header(active=case["title"], prefix="../", brand=case["brand"])
        + f"""
  <main>
    <section class="case-hero">
      <div class="wrap">
        <div class="crumb"><a href="../index.html">Case studies</a> / {case['num']}</div>
        {badge}
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
