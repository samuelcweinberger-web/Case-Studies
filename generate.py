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
        "slug": "educational-module",
        "num": "01",
        "brand": "robinhood",
        "title": "High-Velocity Usability Testing of a Prediction Market Educational Module",
        "short": "Compressed a 3–4 week research cycle into under 48 hours—validating an educational module for event contracts ahead of the World Cup.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "One week before launch, I usability-tested a complex educational module for trading event contracts using only static images. I chose Listen Labs for adaptive AI moderation and multi-segment sourcing, delivered large-sample qualitative validation in under 48 hours, and drove design changes that lifted trade conversion among module completers.",
        "video": {
            "src": "educational-module.mp4",
            "caption": "Walkthrough of the Listen Labs study setup—recruitment, AI-moderated sessions on static stimuli, and synthesis workflow.",
        },
        "stats": [
            ("<48 hrs", "Research cycle (from 3–4 weeks)"),
            ("100", "Participants tested"),
            ("40%", "Completed the module"),
            ("15%", "Higher trade rate vs non-completers"),
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
<li><strong>Launch Metrics (World Cup)</strong> — Over 1 billion World Cup trades were executed across 1.5 million users. 40% of those users completed the educational module. Module completers traded event contracts at rates 15% higher than non-completers.</li>
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
        "short": "Recovered 85% of rejected first-time traders—generating $17M in monthly revenue and ~900K net new customers.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "I identified a first-trade rejection funnel where 1 in 5 trades failed and 90% of those users churned to competitors. Through qualitative interviews, MaxDiff segmentation, and targeted messaging, I recovered rejected traders at scale and quantified how early outcomes reshape long-term LTV.",
        "phone": {
            "src": "onboarding-retention-phone.png",
            "alt": "Robinhood Prediction markets screen showing featured and newly listed event contracts",
            "caption": "Prediction markets experience—featuring high-probability contracts used to guide first-time traders toward clearer, lower-risk first trades.",
        },
        "stats": [
            ("85%", "Rejected traders recovered"),
            ("$17M", "Additional monthly revenue"),
            ("~900K", "Net new customers"),
            ("15%", "Higher volume — power traders"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The Event Contracts and Prediction Markets division at Robinhood was experiencing noticeable drop-offs in the first-time user flow—specifically right after signup and first-trade friction. Recruiting users who have already churned or failed to complete a first trade is notoriously difficult to study qualitatively.</p>
<p>Specifically, I identified the single biggest barrier in the funnel: 1 out of every 5 first-time trades—representing roughly 450,000 customers each month—was being rejected due to peer-to-peer matching mechanics on the backend exchange. 90% of those users abandoned the platform entirely and defected to a competitor.</p>""",
            ),
            (
                "Task",
                """<p>Isolate the exact friction points causing these drop-offs, understand the needs of disparate user archetypes within the same funnel, and implement structural changes to stabilize retention and recover rejected traders.</p>""",
            ),
            (
                "Approach",
                """<ul>
<li><strong>Targeted Qual Recruitment &amp; Competitor Insights</strong> — I successfully recruited and conducted 1-on-1 interviews with users who abandoned the platform after a first-trade rejection. I discovered that many of them had defected directly to our primary competitors because they interpreted the backend rejection as a platform failure.</li>
<li><strong>Behavioral Segmentation</strong> — I uncovered two distinct mental models in the funnel: newly acquired sports bettors with zero brokerage/crypto experience, and existing Robinhood users exploring prediction markets as sophisticated traders.</li>
<li><strong>MaxDiff Survey</strong> — I designed and deployed a Maximum Differential (MaxDiff) quantitative survey to systematically rank and isolate each segment’s unique informational needs.</li>
<li><strong>Friction Remediation &amp; UI/UX Messaging</strong> — I recommended and designed targeted messaging and navigational changes to explain the backend rejection in plain language and guide users immediately back into the first-trade flow.</li>
<li><strong>Longitudinal Methodology &amp; LTV Mapping</strong> — To understand the long-term impact of early user experiences (first impressions), I initiated and designed a 3-month longitudinal tracking study evaluating the behavioral patterns of users based on their initial trading outcomes (winning vs. losing their very first contract).</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Recovery &amp; Revenue Impact</strong> — My messaging and navigational recommendations successfully recovered 85% of the rejected first-time traders who would have otherwise churned, directly generating $17M in additional monthly revenue and ~900K net new customers.</li>
<li><strong>Discovery of “Power Traders”</strong> — Through matched-sample testing against demographics like age, I proved that customers who overcame a first-trade rejection via the new messaging went on to trade at 15% higher volumes than those whose very first trade succeeded. Overcoming the initial barrier triggered highly active “power trader” behavior.</li>
<li><strong>Infrastructure Advocacy</strong> — Despite the recovery rate, I used these insights to initiate major cross-functional efforts to systematically reduce backend rejected trades, proving to engineering that a friction-free initial experience is vital for long-term customer health.</li>
<li><strong>LTV Quantification &amp; Loss Impact</strong> — Through my 3-month longitudinal study, I identified that losing a first trade reduces a customer’s Lifetime Value (LTV) by 20% to 25%.</li>
<li><strong>Strategic Onboarding &amp; Responsible Trading</strong> — Based on the LTV loss data, I recommended tailoring specific types of event contracts and highlighting details for first-time customers to direct them toward high-probability, lower-risk trades for their first transaction. This research successfully launched an ongoing, company-wide initiative focused on promoting responsible trading (e.g., preventing brand-new customers from immediately placing low-likelihood, “long-shot” trades).</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "brand": "robinhood",
        "title": "Engineering an AI-Agentic UX Research Pipeline (ResearchOps Automation)",
        "short": "Built an autonomous Claude + MCP research pipeline that cut cycle time from 30 to 14 days and scaled output up to 16 studies per month.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "I designed and engineered an autonomous AI research pipeline—using Claude, Model Context Protocol (MCP), and custom database APIs—to remove administrative bottlenecks, compress a 30-day cycle to 14 days, and multiply concurrent study capacity without sacrificing rigor.",
        "stats": [
            ("30 → 14", "Days per project cycle"),
            ("4×", "Concurrent study capacity"),
            ("10–16×", "Monthly throughput multiplier"),
            ("<1 hr", "Study setup (from weeks)"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The end-to-end process of executing a single research project at Robinhood was highly fragmented and bottlenecked by manual administrative steps. Drafting custom research plans, routing compliance approvals, manually setting up tools, and chasing stakeholders for alignment consumed valuable cycles. Most critically, waiting for data science to query and provision target user lists took 4 to 5 days alone.</p>
<p>Between these operational delays, asset compilation, and manual analysis, a standard project cycle consumed up to a full calendar month (30 days), capping the team’s ability to support rapid product cycles.</p>""",
            ),
            (
                "Task",
                """<p>Streamline the operational architecture, eliminate administrative lag, and multiply the volume of concurrent studies without compromising qualitative or quantitative rigor.</p>""",
            ),
            (
                "Approach",
                """<p>To eliminate these bottlenecks, I acted as both researcher and UX engineer—designing and building an autonomous AI workflow using Claude, Model Context Protocol (MCP), and custom database APIs to orchestrate the entire research lifecycle:</p>
<ul>
<li><strong>Instant Research Plan Generation</strong> — I built an AI agent that takes raw notes from stakeholder kickoff meetings and instantly structures them into a standardized research plan template. Based on preset instructions, the agent automatically selects the optimal methodology, drafts tailored survey questions or interview guides, and formats them for stakeholder feedback within 1 to 2 hours of the kickoff.</li>
<li><strong>Automated Study Provisioning</strong> — The pipeline automatically translates approved plans into programmatic study assets—instantly generating logic-ready Qualtrics surveys, Great Question screeners, budget allocations, and compliance tracking tickets via custom MCP integrations.</li>
<li><strong>Autonomous User List Generation</strong> — I partnered with the data science team to build a custom database skill for my AI assistant. The moment a user group is defined in the research plan, Claude autonomously queries the database and pulls the validated user list within minutes—completely bypassing the standard 1-week data science backlog.</li>
<li><strong>Stimuli &amp; Prototype Synthesis</strong> — To eliminate design dependencies, I trained an agent to locate existing design assets, organize screens into logical user flows, and compile prototypes tailored to the research questions. If testing an entirely new concept, the agent utilizes custom design-system templates to autonomously generate the required visual assets.</li>
<li><strong>Real-Time Synthesis &amp; Dual-Delivery Reporting</strong> — Once a study is launched, I leverage MCP SQL integrations to query and synthesize incoming participant data in real time. I programmed AI nodes to ingest raw survey and interview outputs and instantly draft dual-delivery assets: a concise one-page executive summary for leadership and a deep-dive, multi-slide deck for product teams.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<ul>
<li><strong>Timeline Compression</strong> — I successfully compressed a traditional 30-day project cycle down to 14 days after full automation, with the initial study-setup phase dropping from weeks to less than 1 hour.</li>
<li><strong>Quadrupled Concurrent Capacity</strong> — This automated workflow allowed me to run up to 4 studies simultaneously without pipeline blockages or cognitive fatigue.</li>
<li><strong>10x to 16x Throughput Multiplier</strong> — By running 4 concurrent studies in a single week, I scaled my personal output from completing 1 to 2 studies per month to executing up to 16 projects per month.</li>
<li><strong>Operational Autonomy</strong> — By building these custom MCP integrations, I successfully eliminated dependencies on data science for list generation, PMs/designers for stimuli creation, and manual administrative overhead, turning qualitative research into a high-velocity, engineering-grade resource.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "scaled-benchmarking",
        "num": "04",
        "brand": "fanduel",
        "title": "Scaled Product Benchmarking, Regulatory Strategy, and Core Experience Growth",
        "short": "Built FanDuel’s cross-product benchmarking engine—surveying 4M+ customers, lifting RG compliance 78%→92%, and scaling research from 2 to 32.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2025",
        "summary": "I designed and scaled a standardized benchmarking program across FanDuel’s fragmented product ecosystem—unifying measurement, engineering event-triggered telemetry, and partnering with regulators on Responsible Gaming standards—while growing research capacity and proving that every 5% RG compliance gain protects thousands of customers and families from real-world harm.",
        "stats": [
            ("78%→92%", "RG compliance in 2 years"),
            ("4M+", "Customers surveyed"),
            ("$220M", "Attributable revenue"),
            ("2→32", "UX researchers globally"),
        ],
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
                """<p>When I joined FanDuel, the company’s product ecosystem was highly fragmented across five individual apps. The development teams spanned the globe—from Los Angeles (TVG and Racing) to Atlanta and New York (Fantasy and Sportsbook) and the UK (FanDuel Casino). Product managers and designers had no baseline framework to identify, measure, or track the outcomes of their product decisions.</p>
<p>With only one other researcher on the team, we had to establish a baseline UX methodology to understand, retain, and grow a user base of 1.1 million active users across all four major verticals.</p>""",
            ),
            (
                "Task",
                """<p>Design and scale a standardized benchmarking program across all FanDuel products and their main competitors to track how design decisions impact user experience, while scaling the research team to meet the demands of rapid global expansion.</p>""",
            ),
            (
                "Approach",
                """<p>To build a unified, data-driven understanding of our customer experience, I took a multi-phased, highly cross-functional approach:</p>
<ul>
<li><strong>Standardized Journey Benchmarking</strong> — Because features differed wildly across Sportsbook, Racing, Casino, and Fantasy, I standardized a continuous tracking methodology across the core journeys common to all users: Onboarding, Promotional Engagement, Depositing/Withdrawing Funds, Bet Selection/Placement, In-Play (Live) Betting, and Outcome Tracking.</li>
<li><strong>Custom Event-Triggered Telemetry</strong> — To maintain methodological consistency across quarterly reports, I navigated a shifting tech stack of various survey and analytics tools. I eventually architected and engineered custom, event-triggered in-app surveys and behavioral trackers. This allowed me to capture real-time user sentiments the exact moment a high-friction action occurred, providing immediate qualitative context to raw behavioral data.</li>
<li><strong>Responsible Gaming (RG) &amp; Regulatory Standards</strong> — I prioritized the development of robust Responsible Gaming features. I worked directly with state gaming regulators to establish the first industry-wide standard for assessing a customer’s ability to bet responsibly. Recognizing that at-risk individuals would simply defect to other apps, I partnered with competitors (including DraftKings) to build a collaborative industry framework that prevents self-excluded or high-risk users from opening accounts across competing platforms.</li>
<li><strong>Anti-Fraud &amp; Compliance Collaboration</strong> — I supported efforts of Gaming Regulators and Federal Agents, collaborating directly with backend engineers to build real-time event triggers to identify suspicious account behavior, successfully preventing money laundering and fraud.</li>
<li><strong>Founding the Core Products Team</strong> — Based on the success of my quarterly benchmarking reports, I established and led the Core Products and Experiences team—a cross-functional unit consisting of UX/market researchers, data scientists, engineers, and legal/compliance stakeholders.</li>
<li><strong>Scaling Research Operations</strong> — I personally grew and mentored a direct team of 8, while scaling the broader UX Research organization from 2 to 32 researchers globally.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>Over my four-year tenure running this benchmarking program, I surveyed over 4 million customers, establishing myself as the definitive subject matter expert on the FanDuel user experience.</p>
<p><strong>Responsible Gaming &amp; Human Impact (Key Achievement)</strong></p>
<ul>
<li><strong>Double-Digit Compliance Gain</strong> — Driven directly by my design recommendations and strategic frameworks, we improved overall Responsible Gaming compliance from 78% to 92% in just two years.</li>
<li><strong>Direct Harm Mitigation</strong> — I conducted a groundbreaking study proving that every 5% increase in RG compliance directly prevents significant bodily and financial harm to 6,000 to 7,000 customers, and indirectly protects roughly 55,000 individuals (including spouses, children, and family members) from the cascading effects of problem gambling.</li>
</ul>
<p><strong>Growth, Revenue &amp; Operational Scale</strong></p>
<ul>
<li><strong>Massive User Growth</strong> — Scaled the active user base from 1.1 million to over 30 million users.</li>
<li><strong>Direct Revenue Generation</strong> — Generated $220M in attributable revenue by optimizing promotional engagement and messaging through large-scale A/B testing.</li>
<li><strong>High-Value Cross-Selling</strong> — Guided the UX strategy to cross-sell over 14 million users from Fantasy and Casino into the Sportsbook platform, unlocking an estimated $500M in Lifetime Value (LTV).</li>
<li><strong>Engagement &amp; Retention</strong> — Drove a 30% increase in Monthly Active Users (MAU) while maintaining a consistent market lead over key competitors.</li>
<li><strong>Support Cost Reduction</strong> — Reduced customer support contact rates and operational costs by $1.2 million by redesigning high-friction financial journeys (including integrating seamless ACH wallet systems).</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "acquisition-offers",
        "num": "05",
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
        "slug": "wallet-deposit",
        "num": "06",
        "brand": "fanduel",
        "title": "Wallet Deposit Optimization",
        "short": "Converted 150K+ stagnant sign-ups by redesigning wallet setup—generating $8M in Q1 handle and cutting support tickets 30%.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2025",
        "summary": "I used Amplitude to identify a 65% drop-off at Wallet/Banking Setup after seamless registration. Through interviews, moderated usability, and a 5,000-respondent MaxDiff, I rebuilt the flow with progressive disclosure and compliance framing—converting stagnant accounts into depositing players.",
        "stats": [
            ("150K+", "Stagnant users converted"),
            ("$8M", "Handle generated in Q1"),
            ("−30%", "Onboarding support tickets"),
            ("65%", "Pre-fix drop-off at wallet setup"),
        ],
        "sections": [
            (
                "Situation",
                """<p>At the top of our registration funnel, we faced a severe operational bottleneck: hundreds of thousands of users completed the initial sign-up process but abandoned the platform completely before linking a bank account or making their First-Time Deposit (FTD).</p>
<p>I utilized Amplitude to map this registration-to-deposit gap and discovered that while the initial registration steps were completely seamless, the Wallet/Banking Setup screen was a hard barrier for 65% of all new sign-ups.</p>""",
            ),
            (
                "Task",
                """<p>Determine whether this drop-off was driven by a lack of user motivation or specific trust barriers during financial onboarding, and systematically redesign the flow to convert stagnant accounts into active, depositing players.</p>""",
            ),
            (
                "Approach",
                """<p>To identify and dismantle this high-friction wall, I designed and led a triangulated, mixed-methods research strategy:</p>
<ul>
<li><strong>In-Depth Interviews (Evaluating the “Why”)</strong> — I conducted 1-on-1 interviews with churning users. The research revealed a profound mental model disconnect: while users were comfortable sharing standard identity info, they hit a hard wall when asked for routing numbers and Social Security Numbers (SSNs). They expressed deep confusion around ACH payments and simply did not understand why a sports platform required this level of sensitive financial data.</li>
<li><strong>Moderated Usability Sessions</strong> — I ran 15 moderated sessions to physically observe the exact micro-moments of hesitation, cognitive load, and friction when users encountered the routing number field.</li>
<li><strong>MaxDiff Survey Scaling</strong> — To validate my qualitative findings at scale, I designed and deployed a MaxDiff survey to 5,000 target users to systematically test and rank which visual framing and terminology maximized user confidence when sharing sensitive financial details.</li>
<li><strong>Progressive Disclosure &amp; Re-Sequencing</strong> — Partnering with content and product designers, I restructured the onboarding flow. I re-sequenced the experience to ask for low-stakes, high-momentum data (like email and phone number) first. By delaying the sensitive banking requests, we allowed users to build a sense of investment in their account setup first.</li>
<li><strong>Contextual Framing &amp; Humanizing Compliance</strong> — I designed contextual micro-copy explaining why federal compliance regulations mandate this specific banking data, effectively humanizing the regulatory KYC (Know Your Customer) wall while clearly articulating the safety and encryption of ACH transfers.</li>
</ul>""",
            ),
            (
                "Outcome",
                """<p>By translating behavioral psychology and clear compliance framing into the UI, I turned our highest-friction funnel drop-off into a high-converting growth engine:</p>
<ul>
<li><strong>Stagnant User Conversion</strong> — Successfully converted over 150,000 stagnant users who had previously abandoned the funnel.</li>
<li><strong>Significant Financial Impact</strong> — Generated an estimated $8M in handle (the sum of every single bet placed, regardless of whether those bets win or lose) in Q1 alone as a direct result of the optimized wallet setup flow.</li>
<li><strong>Operational Efficiency</strong> — Reduced onboarding-related customer support tickets by 30% by preemptively answering compliance and security questions within the UI.</li>
<li><strong>Institutional Legacy</strong> — I established this “Trust-First Onboarding Playbook” as the permanent design and research standard across all corporate onboarding and wallet initiatives.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "responsible-gaming",
        "num": "07",
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
        "num": "08",
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
        "title": "High-Velocity Usability Testing of a Prediction Market Educational Module",
        "brand": "robinhood",
        "logos": [("robinhood.png", "Robinhood")],
        "body": "One week before World Cup launch, I used Listen Labs’ adaptive AI moderation to usability-test a complex event-contracts educational module with 100 participants—compressing a 3–4 week cycle into under 48 hours. Module completers traded at rates 15% higher than non-completers.",
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

    stats_html = ""
    if case["stats"]:
        stats = "\n".join(
            f"""          <div class="impact-card">
            <div class="impact-label">{l}</div>
            <div class="impact-value">{v}</div>
          </div>"""
            for v, l in case["stats"]
        )
        stats_html = f"""
      <div class="impact-row">
{stats}
      </div>"""

    media_html = ""
    if case.get("video") or case.get("phone"):
        caption = ""
        screen_inner = ""
        if case.get("video"):
            v = case["video"]
            caption = v.get("caption", "")
            screen_inner = f"""<video controls playsinline preload="metadata">
              <source src="../media/{v['src']}" type="video/mp4" />
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
        charts_html = f"""
      <section class="chart-gallery reveal">
        <h2>Benchmarking artifacts</h2>
        <div class="chart-grid">
{chr(10).join(items)}
        </div>
      </section>"""

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
    badge = product_badge(case["brand"], prefix="../")
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
{charts_html}
      <div class="case-board-body">
        <section class="exec-summary">
          <h2>Executive summary</h2>
          <p>{case['summary']}</p>
        </section>
        <div class="star-grid">
{chr(10).join(star_cells)}
        </div>
      </div>
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
    write_notable_page()
    write_about_page()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote home + section pages + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
