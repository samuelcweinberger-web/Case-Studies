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
        "label": "NFL Fantasy App & NFL+",
        "product": "Fantasy & Digital Media",
    },
    "burkmont": {
        "label": "Burkmont Analytics",
        "product": "Team Chemistry · Phoenix Suns",
    },
    "ipsos": {
        "label": "Ipsos Healthcare",
        "product": "Medical Device Research",
    },
    "cgu": {
        "label": "Claremont Colleges",
        "product": "Grant-Supported Research",
    },
}

CASES = [{
        "slug": "educational-module",
        "num": "01",
        "brand": "robinhood",
        "title": "Validating a Prediction-Markets Education Module in 48 Hours",
        "short": "Validated a complex education module in under 48 hours with AI-moderated sessions—lifting trade rates 15% among completers.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "One week before the World Cup, I validated an event-contracts education module with 100 AI-moderated sessions on static images—and shipped design changes that lifted trade rates 15% among completers.",
        "insight": "You don’t need a working prototype to test comprehension—you need an interviewer that can adapt to every answer.",
        "stats": [
            ("Under 48 hrs", "End-to-end research cycle time", "efficiency"),
            ("40%", "Event-contract traders who completed the module", "conversion"),
            ("15% increase", "Trade rate vs. users who skipped the module", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>A new education module had to teach event-contract concepts that usually need a human explanation.</li>
<li>Launch was one week out, timed to the World Cup, with only static images to test—no interactive prototype.</li>
<li>Stakeholders needed large-sample validation across net-new and existing brokerage/crypto users.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Validate whether the module actually teaches the concepts and prepares people to trade.</li>
<li>Learn how to tailor content for different user types before launch.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran 100 adaptive AI-moderated sessions in Listen Labs (50 existing + 50 potential customers) on static stimuli.</li>
<li>Trained interviewers on trading concepts so they could probe real comprehension with custom follow-ups.</li>
<li>Synthesized findings in 24 hours and worked with designers to ship tailored examples the same week.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Compressed a 3–4 week research cycle to under 48 hours and greenlit launch on schedule.</li>
<li>40% of World Cup traders completed the module; completers traded at a 15% higher rate.</li>
<li>Tailored modules later outperformed non-tailored versions on first-trade conversion and volume.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "onboarding-retention",
        "num": "02",
        "brand": "robinhood",
        "title": "Turning First-Trade Rejection Into Retention",
        "short": "Cut post-rejection drop-off 60%+ with survival analysis and loss-aversion messaging—retaining ~900K users and ~$17M monthly.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "One in five first trades was rejected and 90% of those users left. Survival analysis plus loss-aversion messaging cut that drop-off 60%+—retaining ~900K users and ~$17M monthly.",
        "insight": "The most dangerous moment in the funnel wasn’t signup—it was the silence right after a first trade failed.",
        "stats": [
            ("60%+ reduction", "Post-first-trade-rejection drop-off", "conversion"),
            ("$17M", "Monthly revenue retained from recovered traders", "revenue"),
            ("~900K", "Users retained per month", "scale"),
            ("18% increase", "Trade volume among top-tier customers", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>1 in 5 first-time trades (~450K/month) was rejected by backend matching mechanics.</li>
<li>Users read rejection as a platform failure; 90% abandoned—often to competitors.</li>
<li>Churned first-time traders were hard to recruit for research.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Pinpoint when post-rejection drop-off happened and why different mental models churned.</li>
<li>Ship messaging and product changes that stabilize retention for Growth &amp; Acquisition.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Used survival analysis to isolate the peak churn window after rejection.</li>
<li>Segmented users (KMeans + MaxDiff) and interviewed churned traders who had defected.</li>
<li>Shipped personalized, loss-aversion-framed messaging that explained the rejection and routed users back into the first-trade flow.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Cut post-first-trade-rejection drop-off by over 60% (~900K users/month; ~$17M monthly revenue).</li>
<li>Drove 4–12% engagement/retention lifts and an 18% trade-volume increase among top-tier customers.</li>
<li>Showed a first-trade loss decreases LTV 20–25%, launching a responsible-trading first-trade initiative.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "brand": "robinhood",
        "title": "Building an AI-Agentic Research Pipeline",
        "short": "Built Claude + Figma agents that cut research cycles from 30 days to 1 week or less and quadrupled concurrent capacity.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "A standard research project took 30 days of admin lag. I built Claude + MCP + Figma agents that run the lifecycle end to end—cutting cycles to 1 week or less and quadrupling concurrent capacity.",
        "insight": "Research velocity is an infrastructure problem. Rigor was never the bottleneck—administration was.",
        "stats": [
            ("1 week or less", "Typical research project cycle (from 30 days)", "efficiency"),
            ("4× increase", "Concurrent study capacity", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>A typical research project took up to 30 days—mostly plans, approvals, tool setup, and stakeholder chasing.</li>
<li>User-list pulls from data science alone took 4–5 days.</li>
<li>Admin lag—not rigor—capped how many studies the team could run.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Remove administrative lag from the research lifecycle.</li>
<li>Multiply concurrent study capacity—including live prototypes mid-interview—without losing rigor.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Built autonomous agents on Claude, MCP, Figma design systems, and custom database APIs.</li>
<li>Automated plans, Qualtrics/Great Question provisioning, and user-list queries in minutes.</li>
<li>Generated engineering-ready prototypes live mid-interview and dual-delivery reports in real time.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Compressed a 30-day cycle to 1 week or less (setup under an hour).</li>
<li>Quadrupled concurrent study capacity (up to four studies at once).</li>
<li>Removed dependencies on data science for lists and on design for mid-cycle stimuli.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "scaled-benchmarking",
        "num": "04",
        "brand": "fanduel",
        "title": "Benchmarking, Responsible Gaming &amp; Research at Scale",
        "short": "Scaled UX research 2→32 and built regulator-approved RG measurement—while cutting research turnaround 75%.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2021–2025",
        "summary": "Built continuous cross-product benchmarking, scaled UX research 2→32 people (200+ studies/year), and delivered a regulator-approved Responsible Gaming Sentiment Scale—cutting research turnaround 75%.",
        "insight": "Measure every product the same way and the roadmap starts finding you—roughly 60% of my FanDuel projects began as benchmarking findings.",
        "stats": [
            ("2 → 32", "UX researchers in the division", "scale"),
            ("200+", "Studies delivered annually", "scale"),
            ("75% reduction", "Research turnaround time (AI-enabled pipelines)", "efficiency"),
            ("1.5M → 20M+", "Users across multi-state rollouts", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>FanDuel’s products were fragmented across five apps and regions with no shared UX baseline.</li>
<li>The research team was two people heading into multi-state expansion.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Stand up standardized benchmarking across products and competitors.</li>
<li>Scale research capacity and build Responsible Gaming measurement fit for Legal/Compliance and regulators.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Built continuous journey benchmarking with event-triggered surveys feeding stakeholder dashboards.</li>
<li>Developed and psychometrically validated a proprietary RG Sentiment Scale tied to compliance signals.</li>
<li>Scaled ops and AI research pipelines as hiring grew the org.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Grew UX Research from 2 to a 32-person division delivering 200+ studies/year; cut turnaround 75%.</li>
<li>Supported multi-state growth from 1.5M to 20M+ users.</li>
<li>RG Sentiment Scale earned regulatory approval for predictive user-protection models.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "acquisition-offers",
        "num": "05",
        "brand": "fanduel",
        "title": "Acquisition Offers &amp; First-Bet Activation",
        "short": "RCT showed the $5 offer matched the $50 offer on conversion at 4× lower cost—clarity beat generosity.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2024",
        "summary": "A 1,050-person RCT showed Bet $5 / Get $50 matched the $50 offer on conversion (~10% over control) at 4× lower payout cost—clarity beat generosity.",
        "insight": "Generosity didn’t drive conversion—clarity did. An early win predicted 90-day engagement four times better than bonus size.",
        "stats": [
            ("10% increase", "First-bet conversion vs. control", "conversion"),
            ("4× reduction", "Payout cost of the $5 offer vs. the $50 offer", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>First-bet activation was the top leading indicator of retention and LTV, and conversion sat below target.</li>
<li>A trust deficit looked technical—until surveys showed drop-offs rated Ease of Use the same as converters.</li>
<li>The real barrier was confusion about how promotional offers worked.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Lift first-bet conversion from 20% toward 30% ahead of state launches.</li>
<li>Learn which incentive structure converts without eroding loyalty.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran a 1×3 RCT (Bet $5 / Get $50 vs. Bet $50 / Get $200 vs. control; N=1,050).</li>
<li>Measured conversion, generosity, loyalty, and ease immediately and at 30/60/90 days.</li>
<li>Analyzed conversion and loyalty decay with chi-square, Z-tests, regression, and mixed ANOVA.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Both offers lifted first-bet conversion ~10% vs. control—with no difference between $5 and $50 (p=0.56).</li>
<li>High-Accessibility won on ROI at ~4× lower payout cost; “Win to Get” confusion—not ease—drove drop-off.</li>
<li>Recommended standardizing Bet $5 / Get $50 and prioritizing an early “First Win.”</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "wallet-deposit",
        "num": "06",
        "brand": "fanduel",
        "title": "Trust-First Wallet &amp; Deposit Onboarding",
        "short": "Fixed 65% wallet drop-off with trust-framed KYC—converting 150K+ users and ~$8M in Q1 handle.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "65% of new sign-ups abandoned at wallet/banking. Trust-framed KYC and progressive disclosure converted 150K+ accounts, drove ~$8M Q1 handle, and cut onboarding tickets 30% ($1–$1.5M saved annually).",
        "insight": "Users weren’t unmotivated—they were being asked for a routing number before anyone explained why.",
        "stats": [
            ("150K+", "Previously abandoned sign-ups who completed wallet setup", "scale"),
            ("$8M", "Incremental betting handle in Q1 2025", "revenue"),
            ("30% reduction", "Onboarding support tickets ($1–$1.5M saved annually)", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>65% of new sign-ups hit a hard wall at wallet/banking setup and abandoned before first deposit.</li>
<li>Users who deposited in the same visit became the highest-engagement players—and we were losing them.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Determine whether drop-off was motivation or trust.</li>
<li>Redesign KYC so stagnant accounts become depositing, engaged players.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Triangulated Amplitude funnels, 15 moderated sessions, and a 5,000-respondent MaxDiff.</li>
<li>Found a mental-model wall at routing numbers/SSNs—users didn’t understand why a sports app needed bank data.</li>
<li>Re-sequenced the flow (progressive disclosure) and added trust-framed KYC micro-copy.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Converted 150,000+ previously abandoned accounts.</li>
<li>Generated ~$8M in incremental Q1 2025 handle.</li>
<li>Cut onboarding support tickets ~30% ($1–$1.5M saved annually); “Trust-First Onboarding” became the corporate standard.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "07",
        "brand": "fanduel",
        "title": "Doubling Cross-Sell Across FanDuel Products",
        "short": "Diagnosed a cross-sell plateau at payment linking—doubling acquisitions in 90 days and adding $5M+ monthly revenue.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "Cross-sell sat near 10% for a year. Continuous CX measurement found the choke point at payment linking—doubling acquisitions in 90 days, lifting MAU 14%, and adding $5M+ monthly revenue.",
        "insight": "The barrier to a second product wasn’t interest—it was being asked for financial credentials all over again.",
        "stats": [
            ("2× increase", "Cross-sell acquisitions within 90 days", "conversion"),
            ("$300M", "Projected lifetime value from the cross-sell program", "revenue"),
            ("$5M+", "Incremental monthly revenue from cross-sell", "revenue"),
            ("14% increase", "Monthly active users", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>Cross-sell conversion between FanDuel products had stagnated near 10% for a year.</li>
<li>Marketing commissioned the work based on my cross-product customer knowledge.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Diagnose the plateau with continuous CX measurement.</li>
<li>Ship interventions that unlock multi-product acquisition without eroding trust at payment linking.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Built a CX layer: in-app pulse checks, competitive usability with 4,000 users, and custom telemetry hooks.</li>
<li>Paired funnel analysis with moderated sessions on payment linking and data-sharing trust.</li>
<li>Redesigned cross-sell entry points and trust framing around linking products.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Doubled cross-sell acquisitions within 90 days.</li>
<li>Lifted MAU 14% with $5M+ incremental monthly revenue (~$300M projected LTV).</li>
<li>Left Marketing/Product with an ongoing CX pulse + telemetry system.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "fantasy-d2c-ideation",
        "num": "08",
        "brand": "nfl",
        "title": "NFL Fantasy Mobile App",
        "subtitle": "Monetizing Fantasy Football — The Tools Package",
        "short": "Developed and shipped features available via in-app purchase—converting 45% of users and generating $920K.",
        "headline_kpis": [
            ("Subscriptions Purchased", "45% of users"),
            ("Total Revenue", "$920K"),
        ],
        "context": "NFL · Fantasy Sports",
        "year": "2020",
        "summary": "Developed and shipped Fantasy features available via in-app purchase—converting 45% of active users and generating $920K in direct-to-consumer revenue.",
        "insight": "Fans would pay to win their league—as long as paying never changed the game itself.",
        "stats": [
            ("$600K", "Direct-to-consumer revenue in the first week", "revenue"),
            ("$920K", "Direct-to-consumer revenue by season end", "revenue"),
            ("1.4M (45%)", "Active Fantasy users who bought the Tools Package", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>Fantasy was a free flywheel into the NFL app; revenue lived elsewhere.</li>
<li>High engagement and unmet needs suggested users might pay—if monetization never broke free core play.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Prove direct Fantasy monetization inside hard guardrails (no pay-to-win, core game intact, no charging for competitor freebies).</li>
<li>Prioritize tools likely to drive repeat purchases.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran a design-thinking cycle plus a large survey to find the top tools season-long players would pay for.</li>
<li>Mapped competitor gaps and NFL-only advantages (NGS, Pro content, league identity).</li>
<li>Shipped a mid-season Tools Package with a five-person team and 10+ A/B tests on in-app upsells.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>$600K DTC in week one; 1.4M buyers (45% of active users).</li>
<li>$920K by season end as more users purchased.</li>
<li>Tools shipped inside existing Fantasy surfaces without fragmenting the free experience.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "09",
        "brand": "nfl",
        "title": "Pricing &amp; Packaging: D2C Subscription for NFL+",
        "short": "Formative research on the NFL’s first direct-to-consumer mobile subscription.",
        "context": "NFL · Digital Media &amp; NFL+",
        "year": "2020",
        "summary": "Formative research on the NFL’s first direct-to-consumer mobile subscription—NFL+, launched in 2022 to ~1.1M sign-ups.",
        "insight": "Features alone didn’t explain what fans would pay for—motivation to consume content explained why segments chose differently.",
        "stats": [
            ("1.1M", "NFL+ sign-ups after the 2022 launch", "scale"),
            ("~2.7M", "NFL+ subscribers heading into the 2024 season", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>The NFL was preparing NFL+—its first D2C mobile subscription—against Club+, League Pass, Club Pass, and Mobile RedZone.</li>
<li>Product and media strategy needed empirical packaging and pricing guidance before launch.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Evaluate five alternate NFL+ packaging configurations.</li>
<li>Explain preference differences across fan segments with a motivation-to-consume measure.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran Design Studios (24 fans) with MoSCoW sorting and package ranking before/after price reveal.</li>
<li>Fielded a 2,208-fan national survey on features and competitor usage.</li>
<li>Analyzed reach/preference (TURF-style) and MaxDiff motivation dimensions in SPSS.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Recommendations supported the first NFL+ mobile subscription offering.</li>
<li>~1.1M sign-ups after the 2022 launch; later footprint ~2.7M heading into 2024.</li>
<li>Partnered with NFL Media and Product Strategy on the packaging blueprint.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "intel-trueview",
        "num": "10",
        "brand": "nfl",
        "badge_label": "NFL Labs",
        "title": "Intel TrueView 360° Prototype",
        "short": "Tested Intel’s TrueView replay prototype with fans and recommended how to integrate it into the NFL app and monetize it.",
        "context": "NFL Labs · Partner research with Intel",
        "year": "2019",
        "summary": "Ran design studios on Intel’s TrueView rotate-the-camera replay prototype and delivered recommendations for how to integrate it into the NFL app and monetize it.",
        "insight": "Perspective control earned its place when fans wanted to understand a play—not as a default for every highlight.",
        "stats": [],
        "sections": [
            (
                "Situation",
                """<ul>
<li>Intel’s TrueView prototype let fans rotate the camera around a recorded play.</li>
<li>NFL Labs needed a clear appetite read before investing further in partner integration.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Put the working prototype in front of fans and learn how they used it.</li>
<li>Turn findings into product recommendations for Labs and Intel.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran design studios where fans tried the live TrueView prototype.</li>
<li>Captured when perspective control helped vs. when a normal highlight was enough.</li>
<li>Translated findings into Game Pass / condensed-replay recommendations.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Delivered an appetite read plus concrete interactive-replay recommendations.</li>
<li>Gave Labs and Intel a shared research basis for next partnership steps.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "verizon-superstadium",
        "num": "11",
        "brand": "nfl",
        "badge_label": "NFL Labs",
        "title": "Verizon 5G SuperStadium — In-Stadium Fan Experience",
        "short": "Partnered with Verizon 5G to test the SuperStadium experience—an in-stadium-only, next-generation experience for live NFL games that later morphed into the VIP Fan Experience.",
        "context": "NFL Labs · Verizon 5G partnership",
        "year": "2019–2021",
        "summary": "NFL Labs partnered with Verizon 5G to explore next-generation ways to deepen in-stadium fan engagement. I directed usability and field research on the SuperStadium experience—an in-stadium-only concept pairing cognitive task analysis with field observation during live events—that later morphed into the VIP Fan Experience.",
        "insight": "In-stadium fans didn’t want a second screen—they wanted the stadium itself to become the interface.",
        "stats": [
            ("25% increase", "Engagement lift from Fantasy App &amp; 5G/AR research", "conversion"),
            ("18% increase", "Retention from Fantasy App &amp; 5G/AR research", "conversion"),
            ("59.6%", "Super Bowl LX attendees connected to SuperStadium", "conversion"),
            ("$1B+", "NFL–Verizon technology partnership", "revenue"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>NFL Labs wanted next-generation ways to deepen live and in-stadium fan engagement with partner technology.</li>
<li>Verizon 5G opened the door to real-time AR overlays and multi-angle viewing inside the stadium.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Direct usability and field research on Verizon-powered 5G/AR/VR fan experiences for in-stadium use.</li>
<li>Turn findings into a concrete product direction Labs could formalize with Verizon.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran cognitive task analysis and in-stadium field research during live events to capture real fan behavior.</li>
<li>Ran prototype and usability evaluation on immersive AR hardware with Verizon’s innovation team.</li>
<li>Shaped the product direction: multi-angle live/replay views, Next Gen Stats AR overlays, and in-stadium navigation over 5G Ultra Wideband.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Fantasy App and 5G/AR research achieved a 25% engagement lift and 18% higher retention.</li>
<li>Helped seed SuperStadium—now embedded in the official NFL app and central to a $1B+ NFL–Verizon partnership.</li>
<li>At Super Bowl LX, 59.6% of attendees were actively connected to the SuperStadium experience.</li>
</ul>""",
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
        {nav_link("skills.html", "Skills", "skills")}
        {nav_link("about.html", "About me", "about")}
        <a href="mailto:samuelcweinberger@gmail.com">Contact</a>
      </nav>
    </div>
  </header>
"""


def normalize_stat(item):
    """Return (value, label, kpi_type). kpi_type drives consistent accent colors."""
    if len(item) == 3:
        return item[0], item[1], item[2]
    return item[0], item[1], "default"


def product_badge(brand_key, prefix="", label_override=None):
    meta = BRANDS[brand_key]
    label = label_override or meta["label"]
    return f'<span class="product-badge product-{brand_key}"><span class="product-name">{label}</span></span>'


ABOUT_COPY = """
          <p>I’m an applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. I specialize in bridging the gap between human behavior, advanced data analytics, and interactive design. My academic background—including graduate research focused on human motivation, persuasion, and systemic behavior change—serves as the foundation for how I approach product strategy.</p>
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market—including a quarterly product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
          <p>“UX Engineer” describes a modern hybrid role—and the engineering isn’t backend software. What I engineer is the research operation itself: automated pipelines that field studies in days instead of weeks, telemetry and dashboards that tie what users say to what they actually do, and interactive prototypes built mid-interview so ideas get tested the moment they surface. That infrastructure connects research to analytics, design, and product management, so insights arrive fast enough—and connected enough—to shape product strategy. Working across all four disciplines is what lets me tie every research effort directly to a business objective.</p>
          <p>By integrating generative AI and automated workflows into my practice, I’ve expanded my reach across product, design, and data science. Whether I am orchestrating end-to-end research operations, deploying automated quantitative surveys, or rapidly generating interactive, engineering-ready prototypes mid-interview, I focus on one thing: translating complex human behavior into massive product momentum.</p>
"""

SKILLS = [
    {
        "title": "Advanced Quantitative UX &amp; Causal Inference",
        "items": [
            (
                "End-to-End A/B/n &amp; Multivariate Testing",
                "Designing, code-implementing, and statistically evaluating complex multi-variant live mobile app experiments.",
            ),
            (
                "Quasi-Experimental Designs",
                "Applying methodologies like Propensity Score Matching or Regression Discontinuity in Python/SPSS when random assignment is unethical or technically impossible.",
            ),
            (
                "Survival Analysis &amp; Churn Modeling",
                "Tracking time-to-event metrics in SPSS/Python to discover precisely when drop-off occurs.",
            ),
            (
                "Predictive Behavioral Segmentation",
                "Running cluster analysis (K-Means/Hierarchical) on product telemetry SQL data to group users by behavioral archetypes (e.g., “Casual Bettors” vs. “Hardcore Stat Trackers”).",
            ),
        ],
    },
    {
        "title": "Psychometrics &amp; Behavioral Psychology Frameworks",
        "items": [
            (
                "Custom Scale Development &amp; Validation",
                "Designing and validating proprietary psychometric scales in SPSS to measure specialized phenomena.",
            ),
            (
                "Cognitive Task Analysis (CTA)",
                "Mapping the high-velocity cognitive and decision-making processes of users during live events.",
            ),
            (
                "Behavioral Economics Testing",
                "Implementing and measuring micro-interventions grounded in cognitive biases (like loss aversion or the framing effect) to boost user engagement.",
            ),
            (
                "Implicit Association Testing (IAT)",
                "Programmatically building tests in Python to capture subconscious emotional biases toward sports teams or app branding.",
            ),
        ],
    },
    {
        "title": "Sports-Specific &amp; In-the-Wild Methodologies",
        "items": [
            (
                "Biometric &amp; Psychophysiological Tracking",
                "Integrating mobile app testing with wearable telemetry data (heart rate variability, galvanic skin response) using Python to measure user stress during live sporting events.",
            ),
            (
                "Digital Diary Studies for Sports Seasons",
                "Structuring longitudinal studies to evaluate fluctuating fan sentiment and feature adoption across a season.",
            ),
        ],
    },
    {
        "title": "Engineered Research Infrastructure &amp; Tooling",
        "items": [
            (
                "Custom Research Telemetry Hooks",
                "Embedding custom event trackers directly into the mobile app’s repository, bypassing reliance on product managers.",
            ),
            (
                "Automated Data Pipelines &amp; Dashboards",
                "Creating Python scripts and SQL queries that automatically clean, aggregate, and visualize user study metrics in real time.",
            ),
            (
                "Synthetic User Testing Simulation",
                "Building behavioral simulation scripts in Python to model potential user traffic pathways and identify technical bottlenecks or design flaws before launch.",
            ),
        ],
    },
]

RESEARCH_TOOLS = sorted(
    {
        "Amplitude",
        "Claude Code",
        "Coda",
        "Confluence",
        "Contentful",
        "Cursor",
        "Displayr",
        "FigJam",
        "Figma",
        "Glean",
        "GitHub",
        "Great Question",
        "Jira",
        "Listen",
        "Lucid",
        "Major Oak",
        "Miro",
        "Notion",
        "Python",
        "Qualtrics",
        "Quantilope",
        "Quantum Metric",
        "R",
        "RedOak",
        "Roder RDE",
        "Salesforce",
        "SAS",
        "Slack",
        "SPSS",
        "SQL",
        "StatSig",
        "UserTesting",
    },
    key=str.casefold,
)


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
        ("burkmont", "Burkmont Analytics · Phoenix Suns"),
        ("ipsos", "Ipsos Healthcare"),
        ("cgu", "Claremont Colleges"),
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
          <a href="case-studies.html" title="Ipsos Healthcare (case study forthcoming)"><img src="media/brands/ipsos.png" alt="Ipsos" /></a>
          <a href="case-studies.html" title="Claremont Colleges (case study forthcoming)"><img src="media/brands/cgu.png" alt="Claremont Graduate University" /></a>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="case-studies.html">View case studies</a>
          <a class="btn btn-ghost" href="skills.html">Skills</a>
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
          <p>Ten studies across Robinhood, FanDuel, and the NFL—each tied to a shipped product decision and a measured outcome.</p>
        </div>
{chr(10).join(case_blocks)}
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "case-studies.html").write_text(html)


def write_skills_page():
    groups = []
    for group in SKILLS:
        items = "\n".join(
            f"""          <li>
            <strong>{name}</strong>
            <span>{desc}</span>
          </li>"""
            for name, desc in group["items"]
        )
        groups.append(
            f"""        <section class="skills-group reveal">
          <h3>{group['title']}</h3>
          <ul class="skills-list">
{items}
          </ul>
        </section>"""
        )
    tools = "\n".join(
        f'          <li class="tool-pill">{tool}</li>' for tool in RESEARCH_TOOLS
    )
    html = (
        header(active="Skills", nav_active="skills")
        + f"""
  <main>
    <section class="section page-section" id="skills">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Skills</h2>
          <p>Quantitative UX, psychometrics, sports/in-the-wild methods, and engineered research infrastructure.</p>
        </div>
        <div class="skills-grid">
{chr(10).join(groups)}
        </div>

        <div class="section-head reveal tools-head" id="research-tools">
          <h2>Research tools</h2>
          <p>Platforms and languages I use across survey, analytics, experimentation, collaboration, and analysis.</p>
        </div>
        <ul class="tools-cloud reveal">
{tools}
        </ul>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "skills.html").write_text(html)


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

    kpi_html = ""
    if case["stats"]:
        normalized = [normalize_stat(s) for s in case["stats"]]
        cells = "\n".join(
            f"""        <div class="kpi kpi--{k}">
          <p class="kpi-value kpi-value--{k}">{v}</p>
          <p class="kpi-label">{l}</p>
        </div>"""
            for v, l, k in normalized
        )
        kpi_html = f"""
      <section class="kpi-band reveal" aria-label="Key outcomes">
{cells}
      </section>"""

    media_html = ""
    if case.get("video") or case.get("phone"):
        caption = ""
        screen_inner = ""
        if case.get("video"):
            v = case["video"]
            caption = v.get("caption", "")
            vtype = v.get("type", "video/mp4")
            poster = v.get("poster")
            poster_attr = f' poster="../media/{poster}"' if poster else ""
            screen_inner = f"""<video controls playsinline preload="metadata"{poster_attr}>
              <source src="../media/{v['src']}" type="{vtype}" />
              Your browser does not support the video tag.
            </video>"""
        else:
            p = case["phone"]
            caption = p.get("caption", "")
            alt = p.get("alt", "")
            screen_inner = f'<img src="../media/{p["src"]}" alt="{alt}" />'
        caption_html = (
            f'<p class="case-video-caption">{caption}</p>' if caption else ""
        )
        media_html = f"""
      <div class="case-video reveal">
        <div class="phone-frame">
          <div class="phone-notch" aria-hidden="true"></div>
          <div class="phone-screen">
            {screen_inner}
          </div>
        </div>
        {caption_html}
      </div>"""

    charts_html = ""
    if case.get("charts"):
        items = []
        for c in case["charts"]:
            cap = c.get("caption", "")
            cap_html = f'<figcaption>{cap}</figcaption>' if cap else ""
            items.append(
                f"""        <figure class="chart-card">
          <img src="../media/{c['src']}" alt="{c.get('alt', '')}" loading="lazy" />
          {cap_html}
        </figure>"""
            )
        gallery_title = case.get("gallery_title", "Artifacts")
        charts_html = f"""
      <section class="chart-gallery reveal">
        <h2>{gallery_title}</h2>
        <div class="chart-grid">
{chr(10).join(items)}
        </div>
      </section>"""

    charts_before = "" if case.get("gallery_after_body") else charts_html
    charts_after = charts_html if case.get("gallery_after_body") else ""

    section_blocks = []
    total = len(case["sections"])
    for i, (title, body) in enumerate(case["sections"]):
        section_blocks.append(
            f"""      <section class="case-section reveal">
        <div class="case-section-label">
          <h2>{title}</h2>
        </div>
        <div class="case-section-body">{body}</div>
      </section>"""
        )

    prev_link = (
        f"""<a class="pager-link pager-prev" href="{prev_c['slug']}.html">
          <span class="pager-kicker">← Previous</span>
          <span class="pager-title">{prev_c['title']}</span>
        </a>"""
        if prev_c
        else "<span></span>"
    )
    next_link = (
        f"""<a class="pager-link pager-next" href="{next_c['slug']}.html">
          <span class="pager-kicker">Next →</span>
          <span class="pager-title">{next_c['title']}</span>
        </a>"""
        if next_c
        else "<span></span>"
    )
    badge = product_badge(
        case["brand"], prefix="../", label_override=case.get("badge_label")
    )
    subtitle_html = (
        f'<p class="case-subtitle">{case["subtitle"]}</p>' if case.get("subtitle") else ""
    )
    hero_desc_html = (
        f'<p class="case-dek">{case["short"]}</p>' if case.get("subtitle") else ""
    )
    headline_html = ""
    if case.get("headline_kpis"):
        items = "\n".join(
            f"""          <div class="headline-metric">
            <span class="headline-metric-label">{label}</span>
            <span class="headline-metric-value">{value}</span>
          </div>"""
            for label, value in case["headline_kpis"]
        )
        headline_html = f"""
        <div class="case-headline" aria-label="Headline results">
{items}
        </div>"""

    html = (
        header(active=case["title"], prefix="../", brand=case["brand"], nav_active="cases")
        + f"""
  <main class="case-page">
    <header class="case-hero">
      <div class="wrap">
        <div class="crumb"><a href="../case-studies.html">Case studies</a> <span aria-hidden="true">/</span> {case['num']}</div>
        {badge}
        <h1>{case['title']}</h1>
        {subtitle_html}
        {hero_desc_html}
        {headline_html}
        <div class="case-meta-line">
          <span>{case['context']}</span>
          <span class="case-meta-dot" aria-hidden="true">·</span>
          <span>{case['year']}</span>
        </div>
      </div>
    </header>
    <div class="wrap case-body">
{media_html}
{charts_before}
      <div class="case-flow">
{chr(10).join(section_blocks)}
      </div>
{charts_after}
      <nav class="pager" aria-label="Case study pagination">
        {prev_link}
        {next_link}
      </nav>
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
    write_skills_page()
    write_about_page()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote home + section pages + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
