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

CASES = [
    {
        "slug": "educational-module",
        "num": "01",
        "brand": "robinhood",
        "title": "High-Velocity Usability Testing of a Prediction Market Educational Module",
        "short": "Compressed a multi-week research cycle into under 48 hours—validating an educational module for event contracts ahead of the World Cup.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "One week before launch, I usability-tested a complex educational module for trading event contracts using only static images. I chose Listen Labs for adaptive AI moderation and multi-segment sourcing, delivered large-sample qualitative validation in under 48 hours, and drove design changes that boosted trade conversion among module completers.",
        "video": {
            "src": "educational-module.mp4",
            "caption": "Walkthrough of the Listen Labs study setup—recruitment, AI-moderated sessions on static stimuli, and synthesis workflow.",
        },
        "stats": [
            ("Under 48 hrs", "End-to-end research cycle time", "efficiency"),
            ("40%", "Event-contract traders who completed the module", "conversion"),
            ("15% increase", "Trade rate vs. users who skipped the module", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<p>One week before launch, a new educational module designed to educate new customers about trading event contracts needed to be tested. The module consisted of complex concepts that typically require a human explanation. Stakeholders needed a large sample size to validate it before the start of the World Cup. The target audience included both net-new customers and existing brokerage/crypto users.</p>
<p>Testing had to be done using static images instead of an interactive prototype, with less than a week to complete the study.</p>""",
            ),
            (
                "Task",
                """<p>Usability test the efficacy of the module to understand how to tailor content to motivate different types of users. KPIs included:</p>
<ul>
<li>Length of time it takes.</li>
<li>How effective it is at educating customers.</li>
<li>Whether it prepares them to trade event contracts.</li>
</ul>""",
            ),
            (
                "Approach",
                """<p>To solve the constraint of having only static images under a one-week deadline, I selected Listen Labs. I chose this platform specifically for its ability to scale qualitative depth through automated, adaptive AI moderation and rapid, multi-segment participant sourcing.</p>
<p>I executed the study through the following steps:</p>
<ul>
<li><strong>Targeted Recruitment</strong> — I recruited 50 existing customers internally and leveraged the platform’s integrated panel sourcing to instantly recruit 50 potential customers from a third-party panel.</li>
<li><strong>Custom AI Training</strong> — I actively trained the automated AI interviewers to master and explain the complex trading concepts, allowing them to act as the virtual “human-in-the-loop” required to guide users through the material.</li>
<li><strong>Stimuli Testing &amp; Adaptive Moderation</strong> — I uploaded the static images into the platform. Instead of using a rigid, static script, the AI interviewers walked all 100 participants through the images simultaneously, dynamically pivoting with custom follow-up questions based on each participant’s individual responses to test comprehension.</li>
<li><strong>Enterprise LLM Synthesis</strong> — I utilized our enterprise LLM to automatically analyze and cluster the qualitative feedback, mapping usability barriers and comprehension metrics within 24 hours.</li>
<li><strong>Design Collaboration</strong> — I worked directly with product designers, using these synthesized findings to rapidly adjust visual elements and tailor examples before the module was shipped.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Operational Efficiency</strong> — I compressed a 3-to-4 week manual research cycle into less than 48 hours.</li>
<li><strong>Stakeholder Validation</strong> — I provided the large-sample qualitative validation required to greenlight the launch on schedule.</li>
<li><strong>Prototype Savings</strong> — I successfully evaluated conceptual comprehension using only static images, bypassing interactive prototype development.</li>
<li><strong>Design Optimization</strong> — I answered key research questions and provided design-specific recommendations on tailoring examples and highlighting key elements to increase completion and subsequent engagement.</li>
<li><strong>Launch Metrics (World Cup)</strong> — Over 1 billion World Cup trades were executed across 1.5 million users. 40% of those users completed the educational module. Module completers traded event contracts at a 15% increase vs. users who did not complete the module.</li>
<li><strong>Experimental Proof (Tailoring vs. Non-Tailored)</strong> — I ran a subsequent experiment to evaluate the module’s performance on existing brokerage and crypto traders trying event contracts for the first time. The tailored modules (based on my recommendations) significantly outperformed non-tailored modules in both initial trade conversion and total trade volume.</li>
<li><strong>Strategic Product Direction</strong> — The performance of the tailored modules proved the value of personalization to product managers and leadership. I then led the follow-up research on how to personalize the user experience to increase engagement and satisfaction in prediction markets.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "onboarding-retention",
        "num": "02",
        "brand": "robinhood",
        "title": "Onboarding Optimization & Strategic Retention in Prediction Markets",
        "short": "Used survival analysis and loss-aversion messaging to cut post-rejection drop-off—retaining ~900K users/month and ~$17M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "I used survival analysis to pinpoint when post-first-trade-rejection drop-off occurred, then built a personalized, loss-aversion-framed messaging strategy that cut that drop-off by over 60%. Parallel Growth &amp; Acquisition research—behavioral archetypes via KMeans on product telemetry, validated in controlled A/B/n experiments—drove engagement/retention lifts and higher trade volume among top-tier customers.",
        "phone": {
            "src": "onboarding-retention-phone.png",
            "alt": "Robinhood Prediction markets screen showing featured and newly listed event contracts",
            "caption": "Prediction markets experience—featuring high-probability contracts used to guide first-time traders toward clearer, lower-risk first trades.",
        },
        "stats": [
            ("60%+ reduction", "Post-first-trade-rejection drop-off", "conversion"),
            ("$17M", "Monthly revenue retained from recovered traders", "revenue"),
            ("~900K", "Users retained per month", "scale"),
            ("18% increase", "Trade volume among top-tier customers", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The Event Contracts and Prediction Markets division at Robinhood was experiencing noticeable drop-offs in the first-time user flow—specifically right after signup and first-trade friction. Recruiting users who have already churned or failed to complete a first trade is notoriously difficult to study qualitatively.</p>
<p>Specifically, I identified the single biggest barrier in the funnel: 1 out of every 5 first-time trades—representing roughly 450,000 customers each month—was being rejected due to peer-to-peer matching mechanics on the backend exchange. 90% of those users abandoned the platform entirely and defected to a competitor.</p>""",
            ),
            (
                "Task",
                """<p>Pinpoint exactly when post-first-trade-rejection drop-off occurred, understand needs across behavioral archetypes in the same funnel, and ship messaging and product changes that stabilize retention—while also informing Growth &amp; Acquisition UI and engagement strategy for Prediction Markets.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Survival analysis</strong> — Modeled time-to-churn after first-trade rejection to isolate the precise window where drop-off concentrated, so interventions could fire when loss aversion and abandonment risk peaked.</li>
<li><strong>Targeted Qual Recruitment &amp; Competitor Insights</strong> — Recruited and conducted 1-on-1 interviews with users who abandoned after a first-trade rejection. Many had defected to primary competitors because they interpreted the backend rejection as a platform failure.</li>
<li><strong>Behavioral Segmentation &amp; KMeans</strong> — Segmented behavioral archetypes from product telemetry (including newly acquired sports bettors vs. existing Robinhood traders exploring prediction markets), then validated patterns with controlled A/B/n experiments for Growth &amp; Acquisition.</li>
<li><strong>MaxDiff Survey</strong> — Designed and deployed a Maximum Differential (MaxDiff) quantitative survey to systematically rank and isolate each segment’s unique informational needs.</li>
<li><strong>Loss-aversion-framed messaging</strong> — Built personalized messaging and navigational changes that explained the backend rejection in plain language, reframed the moment with loss-aversion principles, and guided users immediately back into the first-trade flow.</li>
<li><strong>Longitudinal Methodology &amp; LTV Mapping</strong> — Designed a 3-month longitudinal tracking study evaluating behavioral patterns based on initial trading outcomes (winning vs. losing the first contract).</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Retention strategy</strong> — The personalized, loss-aversion-framed messaging strategy cut post-first-trade-rejection drop-off by over 60%, retaining ~900K users per month (~$17M in monthly revenue).</li>
<li><strong>Growth &amp; Acquisition lifts</strong> — Formative and evaluative research on UI design and user needs—archetypes via KMeans on telemetry, validated in A/B/n experiments—drove 4–12% engagement/retention lifts and an 18% increase in trade volume among top-tier customers.</li>
<li><strong>Infrastructure Advocacy</strong> — Used these insights to initiate cross-functional efforts to systematically reduce backend rejected trades, proving to engineering that a friction-free initial experience is vital for long-term customer health.</li>
<li><strong>LTV Quantification &amp; Loss Impact</strong> — Through the 3-month longitudinal study, losing a first trade decreased a customer’s Lifetime Value (LTV) by 20% to 25%.</li>
<li><strong>Strategic Onboarding &amp; Responsible Trading</strong> — Based on the LTV loss data, recommended tailoring event contracts and highlighting details for first-time customers toward high-probability, lower-risk first trades—launching an ongoing initiative focused on responsible trading (e.g., preventing brand-new customers from immediately placing low-likelihood, “long-shot” trades).</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "brand": "robinhood",
        "title": "Engineering an AI-Agentic UX Research Pipeline (ResearchOps Automation)",
        "short": "Built autonomous Claude + Figma agents that compressed a 30-day research cycle to 1 week or less and quadrupled concurrent study capacity.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "I built autonomous AI agents—Claude plus Figma design systems—to produce engineering-ready prototypes live, mid-interview, and to manage end-to-end study lifecycles. The pipeline compressed a 30-day research cycle to 1 week or less and quadrupled concurrent study capacity without sacrificing rigor.",
        "stats": [
            ("1 week or less", "Typical research project cycle (from 30 days)", "efficiency"),
            ("4× increase", "Concurrent study capacity", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The end-to-end process of executing a single research project at Robinhood was highly fragmented and bottlenecked by manual administrative steps. Drafting custom research plans, routing compliance approvals, manually setting up tools, and chasing stakeholders for alignment consumed valuable cycles. Most critically, waiting for data science to query and provision target user lists took 4 to 5 days alone.</p>
<p>Between these operational delays, asset compilation, and manual analysis, a standard project cycle consumed up to a full calendar month (30 days), capping the team’s ability to support rapid product cycles.</p>""",
            ),
            (
                "Task",
                """<p>Streamline the operational architecture, eliminate administrative lag, and multiply concurrent study capacity—including live prototype production mid-interview—without compromising qualitative or quantitative rigor.</p>""",
            ),
            (
                "Approach",
                """<p>To eliminate these bottlenecks, I acted as both researcher and UX engineer—building autonomous AI agents with Claude, Figma design systems, Model Context Protocol (MCP), and custom database APIs to orchestrate the entire research lifecycle:</p>
<ul>
<li><strong>Instant Research Plan Generation</strong> — An AI agent takes raw notes from stakeholder kickoff meetings and structures them into a standardized research plan template. Based on preset instructions, the agent selects the optimal methodology, drafts tailored survey questions or interview guides, and formats them for stakeholder feedback within 1 to 2 hours of the kickoff.</li>
<li><strong>Automated Study Provisioning</strong> — The pipeline translates approved plans into programmatic study assets—generating logic-ready Qualtrics surveys, Great Question screeners, budget allocations, and compliance tracking tickets via custom MCP integrations.</li>
<li><strong>Autonomous User List Generation</strong> — Partnered with data science to build a custom database skill. The moment a user group is defined in the research plan, Claude queries the database and pulls the validated user list within minutes—bypassing the standard 1-week data science backlog.</li>
<li><strong>Live mid-interview prototypes (Claude + Figma)</strong> — Agents use Figma design-system templates to produce engineering-ready prototypes live during interviews—locating existing assets, organizing screens into flows, or generating new visual stimuli on the spot so concepts can be tested in-session.</li>
<li><strong>Real-Time Synthesis &amp; Dual-Delivery Reporting</strong> — MCP SQL integrations query and synthesize incoming participant data in real time. AI nodes ingest raw survey and interview outputs and draft dual-delivery assets: a concise one-page executive summary for leadership and a deep-dive deck for product teams.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Timeline Compression</strong> — Compressed a traditional 30-day research cycle to 1 week or less after full automation, with initial study-setup dropping from weeks to less than 1 hour.</li>
<li><strong>Quadrupled Concurrent Capacity</strong> — The automated workflow quadrupled concurrent study capacity—running up to four studies simultaneously without pipeline blockages.</li>
<li><strong>Operational Autonomy</strong> — Custom MCP and Figma integrations eliminated dependencies on data science for list generation and on PMs/designers for stimuli creation mid-cycle, turning qualitative research into a high-velocity, engineering-grade resource.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "scaled-benchmarking",
        "num": "04",
        "brand": "fanduel",
        "title": "Scaled Product Benchmarking, Responsible Gaming &amp; Research Operations",
        "short": "Scaled UX research into a 32-person division, built AI research pipelines that cut turnaround 75%, and grew Responsible Gaming into a regulator-approved Sentiment Scale.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2021–2025",
        "summary": "Benchmarking was my foundation at FanDuel: a continuous measurement system across fragmented products that improved core product health and spawned most of my later portfolio. Open-ended Voice of Customer feedback surfaced at-risk behaviors, which I connected to Legal/Compliance data and grew into a proprietary Responsible Gaming Sentiment Scale—psychometrically validated and regulator-approved for predictive user-protection models. Research operations and AI-enabled pipelines scaled the org into a 32-person division delivering 200+ studies annually while cutting research turnaround time 75%.",
        "stats": [
            ("Increased to 32", "UX researchers in the division (from 2)", "scale"),
            ("200+", "Studies delivered annually", "scale"),
            ("75% reduction", "Research turnaround time (AI-enabled pipelines)", "efficiency"),
            ("1.5M → 20M+", "Users across multi-state rollouts", "scale"),
        ],
        "gallery_title": "Benchmarking artifacts",
        "charts": [
            {
                "src": "benchmarking/q2-2023-metrics-dashboard.jpg",
                "alt": "Q2 2023 product benchmarking metrics dashboard with SUPR-Q, Ease of Use, RG, and Loyalty scores",
                "caption": "Q2 2023 scorecard—SUPR-Q, Ease of Use, Responsible Gaming, and Loyalty tracked quarter-over-quarter.",
            },
            {
                "src": "benchmarking/q2-2023-exec-summary.jpg",
                "alt": "Q2 2023 all-product executive summary from FanDuel product benchmarking",
                "caption": "Executive synthesis across Sportsbook, TVG, Casino, DFS, and Racing.",
            },
            {
                "src": "benchmarking/q2-2023-all-products-a.jpg",
                "alt": "Q2 2023 all-products benchmarking results charts",
                "caption": "Cross-product results view used in quarterly leadership reviews.",
            },
            {
                "src": "benchmarking/q1-2022-rg-scores.jpg",
                "alt": "Responsible Gaming score comparison across FanDuel products and competitors",
                "caption": "Responsible Gaming scores across FanDuel products and competitors—foundation for regulatory strategy.",
            },
            {
                "src": "benchmarking/q1-2022-supr-q-trend.jpg",
                "alt": "SUPR-Q trend chart across FanDuel products from Q4 2021 to Q1 2022",
                "caption": "SUPR-Q trends across verticals—baseline tracking that made design outcomes comparable.",
            },
            {
                "src": "benchmarking/q1-2022-competitor-supr.jpg",
                "alt": "Competitor SUPR-Q comparison chart for FanDuel vs DraftKings and others",
                "caption": "Competitive SUPR-Q benchmarking against DraftKings, BetMGM, TwinSpires, and others.",
            },
        ],
        "sections": [
            (
                "Situation",
                """<p>When I joined FanDuel, the product ecosystem was fragmented across five apps and global teams—TVG/Racing in Los Angeles, Fantasy and Sportsbook in Atlanta and New York, Casino in the UK. Product managers and designers had no shared baseline to measure how design decisions affected experience. With only one other researcher on the team, we needed a durable UX measurement system as the company prepared multi-state expansion.</p>""",
            ),
            (
                "Task",
                """<p>Design and scale standardized benchmarking across FanDuel products and primary competitors; grow research capacity for rapid expansion; and—when Voice of Customer and compliance data demanded it—build Responsible Gaming measurement that could satisfy product, Legal/Compliance, and state regulators as the company entered new markets.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Standardized journey benchmarking</strong> — Continuous tracking across journeys common to Sportsbook, Racing, Casino, and Fantasy: Onboarding, Promotional Engagement, Depositing/Withdrawing, Bet Selection/Placement, In-Play Betting, and Outcome Tracking.</li>
<li><strong>Event-triggered telemetry &amp; automation</strong> — Architected in-app surveys and behavioral trackers so sentiment fired at high-friction moments. Over time, journey surveys fed automatically into stakeholder dashboards (Alchemer + triggers)—I remained owner of the instruments, data, and reporting layer.</li>
<li><strong>Responsible Gaming Sentiment Scale</strong> — Open-ended feedback repeatedly surfaced at-risk behaviors. I developed and psychometrically validated a proprietary Responsible Gaming Sentiment Scale, linked it to Legal/Compliance behavioral signals, and grew the work into regulator collaboration as FanDuel went live in new states—including partnership patterns so high-risk / self-excluded users could not simply hop platforms.</li>
<li><strong>Multi-state message testing</strong> — Led message testing across multi-state rollouts as the user base scaled from 1.5M to 20M+, using RG measurement to support predictive user-protection models.</li>
<li><strong>Research operations &amp; AI pipelines (~10% of the work)</strong> — Ops was inherent to benchmarking and commissioned projects: connecting siloed stakeholder tools, libraries for data/findings, templates and guides, and AI-enabled research pipelines. As impact and budget grew, hiring and tool-procurement work scaled UX research into a 32-person division delivering 200+ studies annually.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Org &amp; ops leverage</strong> — Scaled UX Research into a 32-person division delivering 200+ studies annually; AI-enabled research pipelines cut turnaround time 75% while I retained ownership of the benchmarking stack.</li>
<li><strong>Multi-state growth</strong> — Message testing and measurement supported rollouts that grew users from 1.5M to 20M+.</li>
<li><strong>Responsible Gaming</strong> — The proprietary RG Sentiment Scale earned regulatory approval for predictive user-protection models and became a core compliance and product-safety input across jurisdictions.</li>
<li><strong>Portfolio effect</strong> — Roughly 60% of my FanDuel projects were inspired by benchmarking findings; the system also made it possible to execute large requested deep dives without abandoning core product health tracking.</li>
</ul>
<p class="callout">Acquisition-offer economics, wallet/first-deposit conversion, and multi-product cross-sell outcomes are covered in separate FanDuel cases so impact figures stay exclusive and non-overlapping.</p>""",
            ),
        ],
    },
    {
        "slug": "acquisition-offers",
        "num": "05",
        "brand": "fanduel",
        "title": "Acquisition Offers &amp; First-Bet Activation",
        "short": "A requested deep dive on acquisition offers that boosted first-bet conversion and showed the lower-stakes offer won on ROI and loyalty.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2024",
        "summary": "Leadership brought this as a deep dive on acquisition tactics. With journey benchmarking largely automated (in-app surveys → dashboard; I remained owner of Alchemer, triggers, and reporting), I focused solely on a 1×3 RCT comparing High-Accessibility vs High-Stakes offers vs control—and resolved the Ease of Use paradox behind first-bet drop-off.",
        "stats": [
            ("10% increase", "First-bet conversion vs. control", "conversion"),
            ("4× reduction", "Payout cost of the $5 offer vs. the $50 offer", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Activation-to-first-bet was the #1 leading indicator for long-term retention and LTV. Onboarding conversion sat below target—and a 15% trust deficit looked like a technical problem. Surveys flipped that story: drop-offs rated Ease of Use the same as converters. The real barrier was conceptual confusion around promotional offers.</p>
<p>This work was brought to me as a dedicated deep dive. By then, much of the core journey benchmarking was automated—data flowed into stakeholder dashboards—so I could concentrate on this program while still owning the underlying survey instruments, triggers, and reporting.</p>""",
            ),
            (
                "Task",
                """<p>Lead a cross-functional CPE strike team to increase first-bet conversion from 20% to 30%, and learn which incentive structure drives conversion without eroding loyalty—especially ahead of state launches where first impressions win market share.</p>""",
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
                """<p>Both offers delivered about a 10% increase in first-bet conversion versus control, with no difference between the $5 and $50 offers (p=0.56)—making the High-Accessibility offer the ROI winner at roughly a 4× reduction in payout cost. Ease of Use did not differ between drop-offs and converters; conceptual confusion around “Win to Get” rules did. A first win predicted 90-day engagement ~4× more than bonus size, while high-stakes loyalty decreased sharply by Day 60.</p>
<p class="callout">Standardize Bet $5 / Get $50, redesign promo messaging for clarity, and prioritize features that create an early “First Win.”</p>""",
            ),
        ],
    },
    {
        "slug": "wallet-deposit",
        "num": "06",
        "brand": "fanduel",
        "title": "Wallet Deposit Optimization",
        "short": "Diagnosed 65% wallet-setup drop-off and redesigned KYC with progressive disclosure and trust framing—converting 150K+ users and ~$8M in Q1 handle.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "Following the benchmarking program, I initiated this work when analyses showed onboarding challenges were tied to banking setup and first deposit. Triangulated mixed-methods research (Amplitude funnel analysis, 15 moderated sessions, a 5,000-respondent MaxDiff survey) rebuilt the KYC flow with progressive disclosure and trust framing—converting 150,000+ stagnant users, generating ~$8M in incremental handle in Q1 2025, and cutting onboarding support tickets 30%.",
        "stats": [
            ("150K+", "Previously abandoned sign-ups who completed wallet setup", "scale"),
            ("$8M", "Incremental betting handle in Q1 2025", "revenue"),
            ("30% reduction", "Onboarding customer-support tickets", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Hundreds of thousands of users completed initial sign-up but abandoned before linking a bank account or making a First-Time Deposit (FTD). Amplitude showed a hard wall at Wallet/Banking Setup for 65% of new sign-ups—even when earlier registration steps felt seamless.</p>
<p>I initiated this project after journey work showed onboarding pain concentrated in banking/FTD. Analyses also showed that customers who onboarded and deposited successfully in the same visit placed more bets and engaged more deeply—the customers we most needed to keep and make successful.</p>""",
            ),
            (
                "Task",
                """<p>Determine whether drop-off was lack of motivation or trust barriers in financial onboarding—and redesign the KYC flow so stagnant accounts become depositing, engaged players. Explicitly connect onboarding, acquisition, and first-time deposit as one continuous experience.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Triangulated mixed methods</strong> — Amplitude funnel analysis, 15 moderated sessions, and a 5,000-respondent MaxDiff survey to diagnose trust and comprehension barriers at wallet/banking setup.</li>
<li><strong>In-depth interviews</strong> — Churning users hit a mental-model wall at routing numbers and SSNs; ACH felt opaque, and they did not understand why a sports platform needed that level of financial data.</li>
<li><strong>Progressive disclosure &amp; re-sequencing</strong> — Low-stakes data first (email, phone); delay banking until users had momentum.</li>
<li><strong>Trust framing for KYC</strong> — Micro-copy explaining why compliance requires banking data, and how ACH transfers are protected—humanizing the ask without softening regulatory requirements.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Stagnant user conversion</strong> — 150,000+ previously abandoned accounts converted.</li>
<li><strong>Handle</strong> — Generated ~$8M in incremental handle in Q1 2025 from the optimized wallet setup flow.</li>
<li><strong>Customer support</strong> — About a 30% reduction in onboarding-related customer-support tickets by answering compliance and security questions in-product.</li>
<li><strong>Playbook</strong> — “Trust-First Onboarding” adopted as the standard for corporate onboarding and wallet initiatives.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "07",
        "brand": "fanduel",
        "title": "Cross-Sell Growth Across FanDuel Products",
        "short": "Architected continuous CX measurement to diagnose a cross-sell plateau—doubling acquisition in 90 days and unlocking $500M projected LTV.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "Marketing brought this project because of my cross-product customer knowledge. Cross-sell conversion had stalled near 10%. I architected a continuous CX measurement framework—in-app pulse checks, competitive usability testing with 4,000 users, and behavioral event tracking via custom telemetry hooks—diagnosed drop-off (especially payment linking / trust), and shipped a path that doubled cross-sell acquisitions within 90 days, lifted MAU 14%, and generated $5M+ in incremental monthly revenue (~$500M projected LTV). Outcome figures here are exclusive to this case.",
        "stats": [
            ("2× increase", "Cross-sell acquisitions within 90 days", "conversion"),
            ("$500M", "Projected lifetime value from the cross-sell program", "revenue"),
            ("$5M+", "Incremental monthly revenue from cross-sell", "revenue"),
            ("14% increase", "Monthly active users", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Cross-sell conversion between FanDuel product lines had stagnated at roughly 10% for the year, without a clear read on where or why customers dropped off. Marketing requested this work based on my knowledge of the full customer base—including who already used multiple products and who did not.</p>
<p>This was not a benchmarking workstream; it was a commissioned growth problem that leveraged that customer fluency.</p>""",
            ),
            (
                "Task",
                """<p>Diagnose the cross-sell conversion plateau with continuous CX measurement, then ship interventions that unlock multi-product acquisition without eroding trust—especially at payment linking.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Continuous CX measurement framework</strong> — In-app pulse checks, competitive usability testing with 4,000 users, and behavioral event tracking via custom telemetry hooks to locate drop-off and compare FanDuel’s multi-product journey against competitors.</li>
<li><strong>Mixed-methods diagnosis</strong> — Funnel and event analysis paired with moderated sessions focused on payment linking and trust barriers between product lines.</li>
<li><strong>Intervention design</strong> — Redesigned cross-sell entry points and trust framing so customers understood why financial credentials were needed again—and what they gained by linking products.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Acquisition</strong> — Doubled cross-sell acquisitions within 90 days.</li>
<li><strong>Engagement &amp; revenue</strong> — Lifted MAU 14% and generated $5M+ in incremental monthly revenue (~$500M projected LTV).</li>
<li><strong>Measurement system</strong> — Left Marketing and Product with an ongoing CX pulse + telemetry layer so cross-sell health could be tracked continuously—not only in one-off deep dives.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "fantasy-d2c-ideation",
        "num": "08",
        "brand": "nfl",
        "title": "Fantasy D2C Ideation — Tools Package Monetization",
        "short": "Proved the NFL could monetize Fantasy directly without disrupting free gameplay—via a mid-season Tools Package.",
        "context": "NFL · Fantasy Sports",
        "year": "2020",
        "summary": "Prove the NFL could monetize the Fantasy user base directly—without disrupting core free gameplay—by identifying tools season-long players would pay for, then shipping a mid-season Tools Package with a five-person product team.",
        "stats": [
            ("$600K", "Direct-to-consumer revenue in the first week", "revenue"),
            ("$920K", "Direct-to-consumer revenue by season end", "revenue"),
            ("1.4M (45%)", "Active Fantasy users who bought the Tools Package", "scale"),
        ],
        "gallery_title": "Fantasy+ tools in product",
        "charts": [
            {
                "src": "fantasy/lineup-view.jpg",
                "alt": "NFL Fantasy Lineup View modal showing starter upgrade recommendations",
                "caption": "Lineup View — upgrade starters with projected-point comparisons.",
            },
            {
                "src": "fantasy/personalized-lists.jpg",
                "alt": "Personalized player lists with roster boost percentages",
                "caption": "Personalized player lists tailored to your roster.",
            },
            {
                "src": "fantasy/backups.jpg",
                "alt": "Backups feature card for setting automatic fantasy backups",
                "caption": "Backups — avoid last-minute inactives.",
            },
            {
                "src": "fantasy/optimize-team.jpg",
                "alt": "Team page with green Optimize CTA over the matchup card",
                "caption": "Optimize CTA integrated into the existing Team page.",
            },
            {
                "src": "fantasy/optimize-modal.jpg",
                "alt": "Optimize Lineup modal with Castrol Edge sponsorship and Optimize button",
                "caption": "Optimize Lineup — in-app window, not a paid ad placement.",
            },
            {
                "src": "fantasy/fantasy-plus-upsell.jpg",
                "alt": "Fantasy+ upsell card on the Players tab for waiver tools",
                "caption": "Fantasy+ upsell on Players — next-level waiver tools for your team.",
            },
        ],
        "sections": [
            (
                "Situation",
                """<p>The Fantasy app had always been a free product—treated as a flywheel to get people into the main NFL app, where revenue came through existing channels. Advanced analytic exploration of new features suggested it might be feasible to monetize the high engagement and unmet needs of Fantasy users directly, without breaking the free core experience.</p>""",
            ),
            (
                "Task",
                """<p>Prove the NFL could monetize the Fantasy user base directly without disrupting core free gameplay. Guardrails set up front: no unfair competitive advantage; core fantasy gameplay stays intact; avoid content the team doesn’t control; don’t charge for what competitors give away free; prioritize ideas likely to drive repeat purchases.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Design Thinking cycle</strong> — Ran the group through Empathize → Define → Ideate → Prototype → Test with structured ideation sessions.</li>
<li><strong>Large-scale customer survey</strong> — Identified the top 6 features that would encourage engagement among a large subset of casual and highly active Fantasy users who want to do better.</li>
<li><strong>Competitive analysis</strong> — Mapped pay-to-play features competitors offered, gaps in those offerings, and shortcomings relative to what Fantasy users need to win. Needs for daily fantasy vs. season-long differed—opening space to serve season-long users in public and private leagues.</li>
<li><strong>Tool goals</strong> — Tools for casual players that increase odds of winning without extra work; tools that solve common mistakes for all players; tools that save time; tools that use proprietary data (NGS, NFL Pro); features using proprietary content (highlights, games); features centered on identity/experience and league (history, communication, trophies).</li>
<li><strong>Tools Package</strong> — Monthly in-app purchase giving access to all tools across all of a user’s teams.</li>
<li><strong>Build &amp; launch</strong> — Worked with engineering alongside 2 product managers and 2 designers (team of 5) to concept-test tools, ship a mid-season beta in the first weeks of the NFL season, and run 10+ A/B tests on CTA placement, copy, timing, and upsell design—in-app windows only, no advertisements. Tool features were built into existing product pages without changing the UI for purchasers vs. non-purchasers.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Week-one DTC</strong> — Launched mid-season and drove $600K in DTC revenue after 1 week, converting 1.4 million active users (45% of all customers).</li>
<li><strong>Season close</strong> — By season end, an additional 24% of active users completed in-app purchases, resulting in $920K in annual revenue from these tools.</li>
<li><strong>Product integration</strong> — Fantasy+ tools (Lineup View, personalized lists, Backups, Optimize, waiver tools) shipped inside existing Fantasy surfaces without fragmenting the free experience.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "09",
        "brand": "nfl",
        "title": "NFL+ Direct-to-Consumer Packaging Research",
        "short": "Evaluated alternate NFL+ packaging configurations to inform Direct-to-Consumer pricing and bundling for the league’s first mobile subscription offering.",
        "context": "NFL · Digital Media &amp; NFL+",
        "year": "2020",
        "summary": "Evaluated five alternate NFL+ subscription packaging configurations to inform Direct-to-Consumer pricing and bundling strategy, using a combined qualitative Design Studio and quantitative national survey approach analyzed with TURF-style reach/preference analysis and a Maximum Differential (MaxDiff)-adapted motivation measure.",
        "stats": [
            ("1.1M", "NFL+ sign-ups after the 2022 launch", "scale"),
            ("~2.7M", "NFL+ subscribers heading into the 2024 season", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The NFL was preparing its first Direct-to-Consumer subscription bundle for the mobile app—NFL+—and needed empirical guidance on how to structure, price, and bundle features against existing products like Club+, League Pass, Club Pass, and Mobile RedZone. Product and media strategy required a data-driven blueprint before the league’s first mobile subscription offering shipped.</p>""",
            ),
            (
                "Task",
                """<p>Evaluate five alternate NFL+ subscription packaging configurations to inform D2C pricing and bundling strategy—and explain preference differences across fan segments with a Motivation to Consume Content measure adapted from academic literature.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Pilot survey evaluation</strong> — Conducted semi-structured interviews with 3 fans to pressure-test survey comprehension before fielding.</li>
<li><strong>Design Studios</strong> — Two in-person sessions with 24 NFL fans. Participants sorted NFL+, Club+, League Pass, Club Pass, and Mobile RedZone into MoSCoW (Must / Should / Could / Won’t) categories, then rank-ordered Packages A–E before and after pricing was revealed.</li>
<li><strong>National quantitative survey</strong> — Fielded to 2,208 NFL fans, measuring competitor-platform usage and quantitative interest in each proposed feature.</li>
<li><strong>Motivation to Consume Content (MCC)</strong> — Adapted a novel MCC measure from an academic literature review (Affect, Cognition, Environment dimensions) and used its maximum-differential component to explain preference differences between packages.</li>
<li><strong>Analysis</strong> — Univariate and multivariate statistics in SPSS to evaluate reach, rank, preference, and appeal for each package across fan segments, including TURF-style reach/preference analysis.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>First NFL+ D2C offering</strong> — Recommendations supported the final product of the first NFL+ Direct-to-Consumer offering available—the first time a subscription bundle (mobile app) was offered by the NFL.</li>
<li><strong>Launch scale</strong> — About 1.1 million sign-ups after the product launched in 2022. While I wasn’t at the NFL during that time, total subscribers increased 29% year-over-year, with NFL+ and NFL Sunday Ticket together reaching close to 6 million subscribers (those two are often reported as a combined figure).</li>
<li><strong>Later footprint</strong> — An earlier standalone NFL+ figure put it at about 2.7 million subscribers heading into the 2024 season.</li>
</ul>
<p class="callout">Designed and moderated the full program—from pilot through Design Studios, national survey, MCC / MaxDiff, and SPSS analysis—and partnered with NFL Media and Product Strategy on packaging recommendations.</p>""",
            ),
        ],
    },
    {
        "slug": "intel-trueview",
        "num": "10",
        "brand": "nfl",
        "badge_label": "NFL Labs",
        "title": "Intel TrueView Design Studio",
        "short": "Tested Intel’s interactive replay prototype with fans to learn whether—and how—the NFL should use it in Game Pass highlights.",
        "context": "NFL Labs · Partner research with Intel",
        "year": "2019",
        "summary": "Intel built TrueView: a replay tool that lets you rotate the camera around a play instead of watching from one fixed angle. NFL Labs needed a clear read on fan appetite before investing further. I ran design studios where fans tried the working prototype, then delivered recommendations for how (and whether) to use it in Game Pass–style highlight experiences.",
        "stats": [],
        "gallery_after_body": True,
        "gallery_title": "What fans tested",
        "charts": [],
        "sections": [
            (
                "Situation",
                """<p>Intel’s TrueView prototype let fans change the camera angle on recorded NFL plays. The league needed to know if fans actually wanted that—and what it would take to make it useful in products like Game Pass highlights—before committing more partnership effort.</p>""",
            ),
            (
                "Task",
                """<p>Put the working prototype in front of fans, learn how they used it, and turn that into clear product recommendations for NFL Labs and Intel.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Design studios</strong> — Fans tried the live TrueView prototype and talked through what felt useful, confusing, or unnecessary.</li>
<li><strong>Usage feedback</strong> — Focused on when perspective control helped (e.g., understanding a play) vs. when a normal highlight was enough.</li>
<li><strong>Recommendations</strong> — Translated session findings into guidance for Game Pass / condensed-replay use cases Intel and Labs could act on.</li>
</ul>
<figure class="prototype-video">
  <video controls playsinline preload="metadata" poster="../media/nfl-intel/trueview-prototype-poster.jpg">
    <source src="../media/nfl-intel/trueview-prototype.mp4" type="video/mp4" />
  </video>
  <figcaption>TrueView prototype clip used in studio sessions.</figcaption>
</figure>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Clear partner brief</strong> — Delivered an appetite read plus concrete recommendations for interactive-replay use in highlight products.</li>
<li><strong>Decision support</strong> — Gave Labs and Intel a shared research basis for next partnership steps, instead of guessing from demos alone.</li>
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
    mark = ""
    if brand_key == "fanduel":
        mark = f'<img class="product-mark product-mark-fd-img" src="{prefix}media/brands/fanduel-icon.png" alt="" width="22" height="22" />'
    elif brand_key == "robinhood":
        mark = f'<img class="product-mark product-mark-rh-img" src="{prefix}media/brands/robinhood-icon.png" alt="" width="22" height="22" />'
    elif brand_key == "nfl":
        mark = f'<img class="product-mark product-mark-nfl-img" src="{prefix}media/brands/nfl-fantasy-icon.png" alt="" width="22" height="22" />'
    elif brand_key == "ipsos":
        mark = f'<img class="product-mark product-mark-ipsos-img" src="{prefix}media/brands/ipsos.png" alt="" width="22" height="22" />'
    elif brand_key == "cgu":
        mark = f'<img class="product-mark product-mark-cgu-img" src="{prefix}media/brands/cgu.png" alt="" width="22" height="22" />'
    elif brand_key == "burkmont":
        mark = '<span class="product-mark product-mark-burkmont" aria-hidden="true"></span>'
    return f'<span class="product-badge product-{brand_key}">{mark}<span class="product-name">{label}</span></span>'


ABOUT_COPY = """
          <p>I’m an applied cognitive and social psychologist turned UX Engineer and Quantitative UX Researcher. I specialize in bridging the gap between human behavior, advanced data analytics, and interactive design. My academic background—including graduate research focused on human motivation, persuasion, and systemic behavior change—serves as the foundation for how I approach product strategy.</p>
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market—including a quarterly product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
          <p>Today, I operate as a highly technical hybrid. By integrating generative AI and automated workflows into my practice, I’ve expanded my reach across product, design, engineering, and data science. Whether I am orchestrating end-to-end research operations, deploying automated quantitative surveys, or rapidly generating interactive, engineering-ready prototypes mid-interview, I focus on one thing: translating complex human behavior into massive product momentum.</p>
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
          <a href="case-studies.html" title="Merck study (case study forthcoming)"><img src="media/brands/merck.png" alt="Merck" /></a>
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
          <p>In-depth work across Robinhood, FanDuel, and NFL digital media—Fantasy tools, NFL+ packaging, and Intel TrueView.</p>
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

    stats_html = ""
    if case["stats"]:
        normalized = [normalize_stat(s) for s in case["stats"]]
        hero = " impact-row--hero" if len(normalized) <= 2 else ""
        stats = "\n".join(
            f"""          <div class="impact-card impact-card--{k}">
            <p class="impact-metric">
              <span class="impact-label">{l}</span><span class="impact-sep">: </span><span class="impact-value impact-value--{k}">{v}</span>
            </p>
          </div>"""
            for v, l, k in normalized
        )
        stats_html = f"""
      <div class="impact-row{hero}">
{stats}
      </div>"""

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

    star_cells = []
    for title, body in case["sections"]:
        star_cells.append(
            f"""        <section class="star-card">
          <h2>{title}</h2>
          <div class="star-body">{body}</div>
        </section>"""
        )

    prev_link = (
        f'<a href="{prev_c["slug"]}.html">← Previous Case Study</a>'
        if prev_c
        else "<span></span>"
    )
    next_link = (
        f'<a href="{next_c["slug"]}.html">Next Case Study →</a>'
        if next_c
        else "<span></span>"
    )
    badge = product_badge(
        case["brand"], prefix="../", label_override=case.get("badge_label")
    )

    html = (
        header(active=case["title"], prefix="../", brand=case["brand"], nav_active="cases")
        + f"""
  <main class="case-board">
    <div class="wrap case-board-inner">
      <header class="case-board-head">
        <div class="case-board-meta">
          <div class="crumb"><a href="../case-studies.html">Case studies</a> / {case['num']}</div>
          {badge}
          <h1>{case['title']}</h1>
        </div>
        <div class="case-board-side">
          <div class="case-meta-block">{case['context']}</div>
          <div class="case-meta-block">{case['year']}</div>
        </div>
      </header>
{stats_html}
{media_html}
{charts_before}
      <div class="case-board-body">
        <section class="exec-summary">
          <h2>Executive summary</h2>
          <p>{case['summary']}</p>
        </section>
        <div class="star-grid">
{chr(10).join(star_cells)}
        </div>
      </div>
{charts_after}
      <div class="pager">
        {prev_link}
        {next_link}
      </div>
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
