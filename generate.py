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
        "label": "NFL Fantasy",
        "product": "Fantasy & Digital Media",
    },
}

CASES = [
    {
        "slug": "onboarding-retention",
        "num": "01",
        "brand": "robinhood",
        "title": "Onboarding Optimization & Strategic Retention",
        "short": "Behavioral segmentation and MaxDiff research that recovered $17M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "Behavioral segmentation, quantitative survey methodology, and multi-million dollar revenue retention.",
        "stats": [
            ("Generated $17M", "in monthly revenue"),
            ("~900K", "Acquired customers"),
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
                """<p>Generated ~$17M in monthly revenue and ~900K acquired customers. Post-rejection churn dropped by over 60%. Trade volume among top-tier customers rose 18%, with retention lifts of 12% for the brokerage/crypto segment and 4% for sports-first users.</p>""",
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
        "title": "Optimizing the Onboarding Experience",
        "short": "Mixed-methods onboarding and deposit research that lifted deposit success 22% and cut related support tickets 18%.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2025",
        "summary": "Reduce friction in onboarding and first-time deposits by diagnosing usability barriers, trust gaps, and language confusion in wallet setup.",
        "stats": [
            ("+22%", "Successful deposits"),
            ("−18%", "Onboarding/wallet support tickets"),
            ("83%", "Ease of Use (+4% QoQ)"),
            ("150K+", "Stagnant users converted"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Users completed registration but abandoned before setting up banking or making a First-Time Deposit. Amplitude showed registration was seamless, yet wallet/banking setup blocked a large share of new sign-ups. SUPR-Q and Ease of Use needed to move while promotions like “Kick of Destiny” raised excitement (+8%) but also added confusion.</p>""",
            ),
            (
                "Task",
                """<p>Identify pain points in sign-up, wallet setup, and trust barriers—then improve completion rates and lower support contact volume without sacrificing compliance requirements.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Mixed methods</strong> — Behavioral analytics, remote moderated usability, competitive benchmarking, and triangulation across deposit-flow metrics, app logs, and qualitative sessions.</li>
<li><strong>Language &amp; trust diagnosis</strong> — Users struggled differentiating “funding” vs “depositing”; missing verification reassurance cues lowered first-time trust; early-stage overload hindered completion.</li>
<li><strong>Progressive disclosure</strong> — Re-sequenced low-stakes data before sensitive wallet fields; partnered with content design on micro-explanations for why banking data was required.</li>
<li><strong>Validation at scale</strong> — Moderated sessions observed hesitation at sensitive fields; MaxDiff messaging tests identified phrasing that maximized confidence sharing financial details.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Deposit success rose 22%; onboarding/wallet support tickets fell 18%. Ease of Use reached 83% (+4% QoQ, +3% YoY) with Responsible Gaming at 86%. Trust and clarity around verification unlocked conversion of 150K+ stagnant users and an estimated $12M incremental handle in Q1 2025.</p>
<p class="callout">Established the Trust-First Onboarding Playbook—progressive disclosure, verification transparency, and guided deposit recovery—as the company standard.</p>""",
            ),
        ],
    },
    {
        "slug": "responsible-gaming",
        "num": "06",
        "brand": "fanduel",
        "title": "Building Responsible Gaming Metrics",
        "short": "A regulator-validated Responsible Gaming Index deployed across 23M+ accounts—bridging behavioral science, compliance, and trust.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2023",
        "summary": "Design and validate measurable indicators of responsible gaming behavior that meet regulatory standards and promote user trust across digital platforms.",
        "stats": [
            ("23M+", "Accounts covered"),
            ("Approved", "Regulator-validated RG Index"),
            ("−17%", "Risky session length via messaging"),
            ("Core KPI", "RGI adopted by product teams"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Product teams needed more than lagging brand trackers and spend thresholds to protect players. Responsible gaming tools existed, but content and measurement lacked a foundational, regulator-ready framework that connected behavioral science to product KPIs.</p>""",
            ),
            (
                "Task",
                """<p>Design and validate a quantifiable Responsible Gaming Index (RGI)—and baseline RG messaging—so compliance, product, and design could monitor risk, improve tool uptake, and meet regulatory standards across platforms.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Behavioral science + modeling</strong> — Literature review, expert interviews, and longitudinal analysis of player engagement trends to define measurable RG indicators.</li>
<li><strong>Risk signal discovery</strong> — Temporal play patterns (session spikes and chaining) predicted at-risk behavior more accurately than spending thresholds alone.</li>
<li><strong>Messaging baseline</strong> — Moderated prototype interviews on RG copy, motivation, placement, and competitor patterns; recommendations drove a subsequent ~30% lift in tool usage.</li>
<li><strong>Cross-functional approval</strong> — Partnered UXR, analytics, and compliance to accelerate regulatory validation and institutionalize the metric.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>The Responsible Gaming Index was approved by regulators and deployed across 23M+ active user accounts as a core product KPI. Real-time messaging raised self-awareness and reduced risky session length by 17%. The model later influenced player-safety protocols across multiple jurisdictions.</p>
<p class="callout">Framework bridges behavioral science, compliance, and user trust—turning responsible play into measurable product infrastructure.</p>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "07",
        "brand": "fanduel",
        "title": "Continuous CX Measurement & Cross-Sell Growth",
        "short": "A real-time Hyper-Focused Lens that doubled cross-sell acquisition in 90 days.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2025",
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
    {
        "slug": "product-benchmarking",
        "num": "08",
        "brand": "fanduel",
        "title": "Product Benchmarking Program",
        "short": "A quarterly UX scorecard across Ease of Use, Loyalty, and Responsible Gaming that became a core 2023 OKR input.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2022",
        "summary": "Replace anecdotal UX reporting with a standardized, executive-ready benchmark across products—and tie improvements to loyalty, retention, and safe play.",
        "stats": [
            ("+4 pts", "Ease of Use improvement"),
            ("+3 pts", "Responsible Gaming score"),
            ("−30%", "Support tickets"),
            ("7%", "Active-user lift with +10 Ease"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Product teams operated in silos without a unified UX scorecard. Leadership needed comparable, metric-based evidence to guide investment—and Responsible Gaming goals required proof that design supported safe play. Anecdotal reporting could not keep pace.</p>""",
            ),
            (
                "Task",
                """<p>Design and run a quarterly Product Benchmarking Program measuring Ease of Use, Loyalty (Net Intention Score), and Responsible Gaming sentiment—giving executives a single view of UX health across verticals.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Metric framework</strong> — Standardized Ease of Use, Loyalty (NIS), and RG sentiment so products could be compared over time and against strategic goals.</li>
<li><strong>Cross-functional alignment</strong> — Brought Product, Design, and Compliance onto shared success measures instead of team-local narratives.</li>
<li><strong>Executive synthesis</strong> — Translated quarterly waves into actionable priorities: wallet clarity, promotion redesign, and bet-tracking reliability.</li>
<li><strong>Behavioral linkage</strong> — Connected comprehension of results to higher responsible play and retention—not just satisfaction scores in isolation.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Q4 delivered measurable movement: Ease of Use +4 pts, Responsible Gaming +3 pts, and ~30% fewer support tickets. A 10-point Ease lift correlated with a 7% rise in active users. Benchmarking became a core input to 2023 OKRs and executive KPI reviews—shifting UX from qualitative feedback into business intelligence.</p>
<p class="callout">Designed the framework, led execution and synthesis, and influenced roadmaps with data-backed insights across four verticals.</p>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "09",
        "brand": "nfl",
        "title": "NFL Direct-to-Consumer Packaging Research",
        "short": "Design studios and multivariate analysis that showed how price disclosure reshapes package preference—and informed early NFL+ packaging.",
        "context": "NFL · Fantasy Sports & Digital Media",
        "year": "2020",
        "summary": "Determine which D2C package structures maximize appeal, and which motivational drivers shape subscription decisions as the league expanded beyond traditional distribution partners.",
        "stats": [
            ("p&lt;.001", "Package C ranked #1 after pricing"),
            ("50%", "Shifted from à-la-carte once priced"),
            ("60%+", "Purchase intent from loyalty/cognition"),
            ("5", "Package architectures tested (A–E)"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The NFL needed empirical guidance for Direct-to-Consumer packaging as it prepared to expand streaming and subscriptions beyond traditional partners. Product and marketing required a data-driven blueprint for how to structure and price NFL+ and add-ons.</p>""",
            ),
            (
                "Task",
                """<p>Identify which combinations of price, features, and structure maximize appeal—and link Motivation to Consume Content drivers to purchase intent across fan segments.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Design studios</strong> — Fans interacted with five prototype subscription configurations (Packages A–E) and ranked them before and after price disclosure.</li>
<li><strong>National survey panel</strong> — Measured reach, preference, and feature awareness with standardized Motivation to Consume Content scales.</li>
<li><strong>Multivariate modeling</strong> — SPSS univariate and multivariate models linked demographics, motivational clusters, and package preference.</li>
<li><strong>Feature motivation</strong> — Condensed Game Replays led broad appeal; Live Game Audio served loyal connectors; RedZone Mobile underperformed for socially motivated fans.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Before price, à-la-carte (Package D) led; after pricing, <strong>tiered Package C</strong> ranked first (p&lt;.001), with ~50% of fans shifting toward A/C. Vicarious achievement and game-strategy thinking explained over 60% of purchase-intent variance. Findings informed early NFL+ packaging—live local audio, condensed replays, team content—and validated flexibility over exclusivity for modern streaming fans.</p>
<p class="callout">Designed and moderated the full program—from recruitment through statistical models—and partnered with NFL Media and Product Strategy on packaging recommendations.</p>""",
            ),
        ],
    },
]


def header(active=None, prefix="", brand=None, nav_active=None):
    brand_class = f' class="brand-{brand}"' if brand else ""
    title = "Sam Weinberger — Case Studies" if not active else f"{active} — Sam Weinberger"

    def nav_link(href, label, key):
        cls = ' class="is-active"' if nav_active == key else ""
        return f'<a href="{prefix}{href}"{cls}>{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="Samuel Weinberger — applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. Bridging human behavior, analytics, and interactive design." />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
</head>
<body{brand_class}>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{prefix}index.html">Sam Weinberger</a>
      <nav class="nav" aria-label="Primary">
        {nav_link("case-studies.html", "Case studies", "cases")}
        {nav_link("notable.html", "Notable projects", "notable")}
        {nav_link("about.html", "About me", "about")}
        <a href="mailto:samuelcweinberger@gmail.com">Contact</a>
      </nav>
    </div>
  </header>
"""


def product_badge(brand_key, prefix=""):
    meta = BRANDS[brand_key]
    mark = ""
    if brand_key == "fanduel":
        mark = f'<img class="product-mark product-mark-fd-img" src="{prefix}media/brands/fanduel-icon.png" alt="" width="22" height="22" />'
    elif brand_key == "robinhood":
        mark = f'<img class="product-mark product-mark-rh-img" src="{prefix}media/brands/robinhood-icon.png" alt="" width="22" height="22" />'
    elif brand_key == "nfl":
        mark = f'<img class="product-mark product-mark-nfl-img" src="{prefix}media/brands/nfl-fantasy-icon.png" alt="" width="22" height="22" />'
    return f'<span class="product-badge product-{brand_key}">{mark}<span class="product-name">{meta["label"]}</span></span>'


NOTABLE = [
    {
        "org": "Robinhood",
        "title": "Onboarding Optimization & Strategic Retention",
        "brand": "robinhood",
        "logos": [("robinhood.png", "Robinhood")],
        "body": "Segmented users via MaxDiff (sports-first bettors vs. brokerage/crypto traders) and shipped personalized onboarding through a controlled experiment — 4–12% engagement/retention lift, 60%+ reduction in post-rejection drop-off, and $17M in retained monthly revenue.",
    },
    {
        "org": "FanDuel",
        "title": "Cross-Sell Acquisition & Revenue Growth",
        "brand": "fanduel",
        "logos": [("fanduel-icon.png", "FanDuel")],
        "body": "Directed the research strategy linking behavioral signals to cross-sell opportunities while scaling a 32-person research org to support it — doubled cross-sell acquisition, adding $8–10M in monthly recurring revenue (>$500M LTV).",
    },
    {
        "org": "NFL",
        "title": "Verizon 5G SuperStadium Fan Experience",
        "brand": "nfl",
        "logos": [
            ("5g-superstadium.png", "NFL 5G SuperStadium"),
            ("verizon-5g.png", "Verizon 5G"),
        ],
        "body": "Partnered with Verizon to test immersive AR overlays for in-stadium fan engagement across next-generation hardware — 25% engagement lift and 18% higher retention across the NFL Fantasy App and 5G/AR experiences.",
    },
    {
        "org": "Claremont Graduate University",
        "title": "Behavioral Messaging for Diabetes Management",
        "brand": "cgu",
        "logos": [("cgu.png", "Claremont Graduate University")],
        "body": "As Research Associate, designed and evaluated an SMS-based behavioral intervention for chronic disease patients, grounded in cognitive and social psychology theory — 30% reduction in hospitalizations among enrolled participants.",
    },
    {
        "org": "Ipsos Healthcare",
        "title": "Multi-Country Insulin Pen Validation Study",
        "brand": "ipsos",
        "logos": [("ipsos.png", "Ipsos"), ("merck.png", "Merck")],
        "body": "FDA comparative insulin injector pen study across the US, UK, and Canada ahead of FDA submission — 27% fewer device-use errors, 40% faster training.",
    },
]


ABOUT_COPY = """
          <p>I’m an applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. I specialize in bridging the gap between human behavior, advanced data analytics, and interactive design. My academic background—including graduate research focused on human motivation, persuasion, and systemic behavior change—serves as the foundation for how I approach product strategy.</p>
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market—including a quarterly product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
          <p>Today, I operate as a highly technical hybrid. By integrating generative AI and automated workflows into my practice, I’ve expanded my reach across product, design, engineering, and data science. Whether I am orchestrating end-to-end research operations, deploying automated quantitative surveys, or rapidly generating interactive, engineering-ready prototypes mid-interview, I focus on one thing: translating complex human behavior into massive product momentum.</p>
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


def build_case_blocks(case_href_prefix="cases/"):
    company_order = [
        ("robinhood", "Robinhood"),
        ("fanduel", "FanDuel"),
        ("nfl", "NFL"),
    ]
    case_blocks = []
    for brand_key, brand_label in company_order:
        brand_cases = [c for c in CASES if c["brand"] == brand_key]
        rows = []
        for c in brand_cases:
            badge = product_badge(c["brand"])
            rows.append(
                f"""    <a class="case-row case-{c['brand']} reveal" href="{case_href_prefix}{c['slug']}.html">
      <div class="case-num">{c['num']}</div>
      <div>
        {badge}
        <h3>{c['title']}</h3>
        <p>{c['short']}</p>
      </div>
      <div class="case-meta">{c['year']}</div>
    </a>"""
            )
        if brand_key == "nfl":
            rows.append(
                """    <a class="case-row case-nfl reveal" href="#trueview">
      <div class="case-num">10</div>
      <div>
        <span class="product-badge product-nfl"><img class="product-mark product-mark-nfl-img" src="media/brands/nfl-fantasy-icon.png" alt="" width="22" height="22" /><span class="product-name">NFL · TrueView</span></span>
        <h3>NFL Design Studio — Usability Testing and Generative Ideation with Fans</h3>
        <p>A design-studio program exploring volumetric TrueView capture for condensed, interactive NFL game replays.</p>
      </div>
      <div class="case-meta">2020</div>
    </a>"""
            )
        if not rows:
            continue
        case_blocks.append(
            f"""        <div class="company-group company-{brand_key} reveal" id="cases-{brand_key}">
          <h3 class="company-heading">{brand_label}</h3>
          <div class="case-list">
{chr(10).join(rows)}
          </div>
        </div>"""
        )
    return case_blocks


def build_notable_blocks():
    notable_order = [
        ("robinhood", "Robinhood"),
        ("fanduel", "FanDuel"),
        ("nfl", "NFL"),
        ("cgu", "Claremont Graduate University"),
        ("ipsos", "Ipsos Healthcare"),
    ]
    notable_blocks = []
    for brand_key, brand_label in notable_order:
        projects = [p for p in NOTABLE if p["brand"] == brand_key]
        if not projects:
            continue
        rows = []
        for p in projects:
            if brand_key in {"robinhood", "fanduel", "nfl"}:
                logo_href = f"case-studies.html#cases-{brand_key}"
            else:
                logo_href = f"#project-{brand_key}"
            logos = "".join(
                f'<a class="notable-logo-link" href="{logo_href}"><img src="media/brands/{src}" alt="{alt}" /></a>'
                for src, alt in p["logos"]
            )
            rows.append(
                f"""        <article class="notable-row notable-{brand_key} reveal" id="project-{brand_key}">
          <div class="notable-logos">{logos}</div>
          <div>
            <h3><span class="notable-org">{p['org']}</span> — {p['title']}</h3>
            <p>{p['body']}</p>
          </div>
        </article>"""
            )
        notable_blocks.append(
            f"""        <div class="company-group company-{brand_key} reveal" id="notable-{brand_key}">
          <h3 class="company-heading">{brand_label}</h3>
          <div class="notable-list">
{chr(10).join(rows)}
          </div>
        </div>"""
        )
    return notable_blocks


def write_home():
    html = (
        header(nav_active="home")
        + """
  <main>
    <section class="hero hero-page">
      <div class="hero-media" aria-hidden="true"></div>
      <div class="hero-atmosphere" aria-hidden="true"></div>
      <div class="wrap hero-copy">
        <div class="hero-kicker">AI-Driven Insights</div>
        <h1 class="hero-brand">Sam<br />Weinberger</h1>
        <p class="hero-role">Applied Cognitive and Social psychologist</p>
        <p class="hero-lede">9+ years of mixed-methods research across fintech, sports media, and healthcare—connecting usability, field research, and AI-augmented workflows to product and revenue outcomes.</p>
        <div class="brand-strip" aria-label="Brands worked with">
          <a href="case-studies.html#cases-robinhood" title="Robinhood case studies"><img src="media/brands/robinhood.png" alt="Robinhood" /></a>
          <a href="case-studies.html#cases-fanduel" title="FanDuel case studies"><img src="media/brands/fanduel.png" alt="FanDuel" /></a>
          <a href="case-studies.html#cases-nfl" title="NFL case studies"><img src="media/brands/nfl.png" alt="NFL" /></a>
          <a href="notable.html#notable-nfl" title="NFL · Verizon 5G SuperStadium"><img src="media/brands/verizon-5g.png" alt="Verizon 5G" /></a>
          <a href="notable.html#notable-ipsos" title="Ipsos Healthcare projects"><img src="media/brands/ipsos.png" alt="Ipsos" /></a>
          <a href="notable.html#notable-ipsos" title="Ipsos Healthcare · Merck study"><img src="media/brands/merck.png" alt="Merck" /></a>
          <a href="notable.html#notable-cgu" title="Claremont Graduate University projects"><img src="media/brands/cgu.png" alt="Claremont Graduate University" /></a>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="case-studies.html">View case studies</a>
          <a class="btn btn-ghost" href="notable.html">Notable projects</a>
          <a class="btn btn-ghost" href="about.html">About me</a>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "index.html").write_text(html)


def write_case_studies_page():
    case_blocks = build_case_blocks()
    html = (
        header(active="Case studies", nav_active="cases")
        + f"""
  <main>
    <section class="section page-section" id="case-studies">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Case studies</h2>
          <p>In-depth work across Robinhood prediction markets, FanDuel sportsbook / CPE, and NFL digital media—including an Intel TrueView studio reel.</p>
        </div>
{chr(10).join(case_blocks)}

        <div class="trueview-section" id="trueview">
          <div class="section-head reveal">
            <div class="product-badge product-nfl">
              <img class="product-mark product-mark-nfl-img" src="media/brands/nfl-fantasy-icon.png" alt="" width="22" height="22" />
              <span class="product-name">NFL · TrueView</span>
            </div>
            <h2>NFL Design Studio — Usability Testing and Generative Ideation with Fans</h2>
            <p>A 2020 design-studio program exploring how volumetric TrueView capture could power condensed, interactive game replays—personalizing NFL D2C content for fans who already know the score but still want the story.</p>
          </div>

          <div class="trueview-player reveal">
            <video controls playsinline preload="metadata" poster="media/hero.jpg">
              <source src="media/hero.mp4" type="video/mp4" />
              Your browser does not support the video tag.
            </video>
            <p class="trueview-caption">Studio reel from the TrueView concept exploration—volumetric capture, multi-angle replay, and next-generation fan viewing.</p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "case-studies.html").write_text(html)


def write_notable_page():
    notable_blocks = build_notable_blocks()
    html = (
        header(active="Notable projects", nav_active="notable")
        + f"""
  <main>
    <section class="section page-section notable-section" id="notable">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Notable projects</h2>
          <p>Highlight outcomes across fintech, sports media, healthcare devices, and academic research.</p>
        </div>
{chr(10).join(notable_blocks)}
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "notable.html").write_text(html)


def write_about_page():
    html = (
        header(active="About me", nav_active="about")
        + f"""
  <main>
    <section class="section page-section" id="about">
      <div class="wrap about-grid">
        <div class="reveal">
          <div class="section-head">
            <h2>About me</h2>
          </div>
{ABOUT_COPY}
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
    (ROOT / "about.html").write_text(html)


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
        header(active=case["title"], prefix="../", brand=case["brand"], nav_active="cases")
        + f"""
  <main>
    <section class="case-hero">
      <div class="wrap">
        <div class="crumb"><a href="../case-studies.html">Case studies</a> / {case['num']}</div>
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
    write_home()
    write_case_studies_page()
    write_notable_page()
    write_about_page()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote home + section pages + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
