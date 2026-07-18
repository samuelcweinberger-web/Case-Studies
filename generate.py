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
        "title": "Validating a Prediction-Markets Education Module in 48 Hours",
        "short": "One week before the World Cup, I usability-tested a complex education module with 100 participants using adaptive AI moderation—compressing a month of research into two days.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "A complex education module for event contracts had to be validated one week before the World Cup—with only static images to test. I ran adaptive AI-moderated sessions with 100 participants, synthesized findings within 24 hours, and shipped design changes that lifted trade rates 15% among module completers.",
        "insight": "You don’t need a working prototype to test comprehension—you need an interviewer that can adapt to every answer.",
        "stats": [
            ("Under 48 hrs", "End-to-end research cycle time", "efficiency"),
            ("40%", "Event-contract traders who completed the module", "conversion"),
            ("15% increase", "Trade rate vs. users who skipped the module", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The education module had one job: teach brand-new customers how event contracts work—concepts that usually need a human to explain them. Launch was a week away, timed to the start of the World Cup, and stakeholders wanted large-sample validation before greenlighting.</p>
<p>Two constraints made that hard. The audience spanned both net-new customers and existing brokerage/crypto users, and there was no interactive prototype to test—only static images.</p>""",
            ),
            (
                "Task",
                """<p>Validate the module’s efficacy before launch and learn how to tailor its content to motivate different types of users. The study had to answer three questions:</p>
<ul>
<li>How long does the module take?</li>
<li>How well does it actually teach the concepts?</li>
<li>Does it leave people prepared to trade event contracts?</li>
</ul>""",
            ),
            (
                "Action",
                """<p>Static images and a one-week deadline ruled out traditional moderation. I chose Listen Labs for its adaptive AI interviewers and rapid multi-segment sourcing, then ran the study in five moves:</p>
<ul>
<li><strong>Two-segment recruitment</strong> — 50 existing customers recruited internally, 50 potential customers sourced instantly from the platform’s integrated third-party panel.</li>
<li><strong>Training the AI moderator</strong> — I trained the automated interviewers to master and explain the trading concepts themselves, so they could act as the “human in the loop” the material normally requires.</li>
<li><strong>Adaptive sessions on static stimuli</strong> — All 100 participants moved through the images simultaneously. Instead of a rigid script, the interviewers pivoted with custom follow-ups based on each person’s answers to probe real comprehension.</li>
<li><strong>24-hour synthesis</strong> — Our enterprise LLM clustered the qualitative feedback into usability barriers and comprehension metrics within a day.</li>
<li><strong>Same-week design changes</strong> — I worked directly with product designers to tailor examples and highlight key elements before the module shipped.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Cycle time</strong> — A 3-to-4-week manual research cycle compressed to under 48 hours, delivering the large-sample validation that greenlit the launch on schedule—no interactive prototype required.</li>
<li><strong>World Cup launch</strong> — Over 1 billion trades executed across 1.5 million users. 40% of those users completed the module, and completers traded event contracts at a 15% higher rate than users who skipped it.</li>
<li><strong>Personalization proof</strong> — A follow-up experiment with existing brokerage and crypto traders showed the tailored modules (built on my recommendations) significantly outperformed non-tailored versions on both first-trade conversion and total trade volume.</li>
<li><strong>What it changed</strong> — The tailoring results proved the value of personalization to product leadership, and I went on to lead the follow-up research on personalizing the prediction-markets experience.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "onboarding-retention",
        "num": "02",
        "brand": "robinhood",
        "title": "Turning First-Trade Rejection Into Retention",
        "short": "Survival analysis pinpointed when rejected first-time traders churned; loss-aversion messaging cut that drop-off 60%+—retaining ~900K users and ~$17M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "One in five first-time trades was rejected by backend matching mechanics, and 90% of those users left—many straight to competitors. I modeled exactly when they churned, rebuilt the moment with personalized loss-aversion-framed messaging, and cut post-rejection drop-off by more than 60%—about 900K users and $17M in revenue retained every month.",
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
                """<p>Robinhood’s prediction-markets funnel was leaking right after signup. The single biggest barrier: 1 in every 5 first-time trades—roughly 450,000 customers a month—was rejected by peer-to-peer matching mechanics on the backend exchange. Users read the rejection as a platform failure. 90% abandoned entirely, many defecting straight to competitors.</p>
<p>Studying them was its own problem: people who churn after one failed trade are notoriously difficult to recruit for research.</p>""",
            ),
            (
                "Task",
                """<p>Pinpoint exactly when post-rejection drop-off happened, understand the different mental models moving through the same funnel, and ship messaging and product changes that stabilized retention—while feeding Growth &amp; Acquisition strategy for prediction markets.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Survival analysis</strong> — Modeled time-to-churn after first-trade rejection to isolate the window where abandonment risk peaked—so interventions could fire at exactly the right moment.</li>
<li><strong>Interviews with the churned</strong> — Recruited and interviewed users who had abandoned after a rejection. They blamed the platform, not the market mechanics—and many had already moved to a competitor.</li>
<li><strong>Behavioral segmentation</strong> — KMeans clustering on product telemetry separated newly acquired sports bettors from experienced Robinhood traders exploring prediction markets, with archetypes validated through controlled A/B/n experiments.</li>
<li><strong>MaxDiff survey</strong> — Systematically ranked each segment’s informational needs so messaging could be tailored rather than averaged.</li>
<li><strong>Loss-aversion-framed messaging</strong> — Personalized messaging and navigation that explained the rejection in plain language, reframed the moment using loss-aversion principles, and routed users immediately back into the first-trade flow.</li>
<li><strong>Longitudinal LTV study</strong> — A 3-month tracking study following behavior based on whether users won or lost their very first contract.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Retention</strong> — The personalized messaging strategy cut post-first-trade-rejection drop-off by over 60%, retaining ~900K users per month—about $17M in monthly revenue.</li>
<li><strong>Growth &amp; Acquisition lifts</strong> — Archetype-driven UI research, validated in A/B/n experiments, drove 4–12% engagement and retention lifts and an 18% increase in trade volume among top-tier customers.</li>
<li><strong>LTV quantification</strong> — The longitudinal study showed that losing a first trade decreases a customer’s lifetime value by 20–25%.</li>
<li><strong>Responsible trading</strong> — That LTV finding launched an ongoing initiative steering first-time customers toward high-probability, lower-risk first trades—and away from immediate “long-shot” bets.</li>
<li><strong>Infrastructure advocacy</strong> — The insights kicked off cross-functional engineering work to reduce backend rejections at the source, not just recover from them.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "research-ops",
        "num": "03",
        "brand": "robinhood",
        "title": "Building an AI-Agentic Research Pipeline",
        "short": "Claude + Figma agents that draft plans, provision studies, pull user lists, and prototype live mid-interview—compressing a 30-day cycle to a week or less.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "summary": "A standard research project took 30 days, most of it lost to administration—plans, approvals, tool setup, and a 4-to-5-day wait for user lists. I built autonomous agents on Claude, MCP, and Figma design systems that run the lifecycle end to end, cutting the cycle to a week or less and quadrupling concurrent study capacity without sacrificing rigor.",
        "insight": "Research velocity is an infrastructure problem. Rigor was never the bottleneck—administration was.",
        "stats": [
            ("1 week or less", "Typical research project cycle (from 30 days)", "efficiency"),
            ("4× increase", "Concurrent study capacity", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Executing a single research project at Robinhood took up to 30 calendar days—and most of that time wasn’t research. Drafting custom plans, routing compliance approvals, configuring tools, and chasing stakeholder alignment consumed the cycle. Waiting on data science to query and provision target user lists took 4 to 5 days by itself.</p>
<p>The cap on the team’s throughput wasn’t rigor. It was administration.</p>""",
            ),
            (
                "Task",
                """<p>Rebuild the operational architecture so administrative lag disappears and concurrent study capacity multiplies—including producing prototypes live, mid-interview—without compromising qualitative or quantitative rigor.</p>""",
            ),
            (
                "Action",
                """<p>I acted as both researcher and UX engineer, building autonomous agents on Claude, Model Context Protocol (MCP), Figma design systems, and custom database APIs to run the research lifecycle end to end:</p>
<ul>
<li><strong>Research plans in hours, not days</strong> — An agent turns raw kickoff-meeting notes into a standardized research plan: it selects the optimal methodology, drafts tailored survey questions or interview guides, and formats everything for stakeholder feedback within 1–2 hours of the meeting.</li>
<li><strong>Automated study provisioning</strong> — Approved plans become programmatic assets automatically: logic-ready Qualtrics surveys, Great Question screeners, budget allocations, and compliance tracking tickets via custom MCP integrations.</li>
<li><strong>User lists in minutes</strong> — A custom database skill built with data science lets Claude query and pull a validated user list the moment a group is defined in the plan—bypassing the standard week-long backlog.</li>
<li><strong>Live prototypes mid-interview</strong> — Agents use Figma design-system templates to assemble engineering-ready prototypes during sessions: pulling existing assets into flows, or generating new stimuli on the spot so a concept can be tested the moment it comes up.</li>
<li><strong>Real-time synthesis, dual delivery</strong> — MCP SQL integrations synthesize participant data as it lands, and AI nodes draft both deliverables at once: a one-page executive summary for leadership and a deep-dive deck for product teams.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Timeline compression</strong> — A traditional 30-day cycle now runs in 1 week or less, with study setup dropping from weeks to under an hour.</li>
<li><strong>Quadrupled capacity</strong> — Up to four studies run simultaneously without pipeline blockages or cognitive fatigue.</li>
<li><strong>Operational autonomy</strong> — No more waiting on data science for lists or on PMs and designers for stimuli. Qualitative research became a high-velocity, engineering-grade resource.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "scaled-benchmarking",
        "num": "04",
        "brand": "fanduel",
        "title": "Benchmarking, Responsible Gaming &amp; Research at Scale",
        "short": "Built FanDuel’s cross-product measurement engine, scaled UX research from 2 to a 32-person division, and grew Responsible Gaming into a regulator-approved sentiment scale.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2021–2025",
        "summary": "Four years of foundation-building: a continuous benchmarking system across five fragmented products, a research org that grew from 2 to a 32-person division delivering 200+ studies a year, and a psychometrically validated Responsible Gaming Sentiment Scale that regulators approved for predictive user protection. AI-enabled pipelines cut research turnaround 75% along the way.",
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
                """<p>FanDuel’s ecosystem was fragmented across five apps and as many time zones—TVG/Racing in Los Angeles, Fantasy and Sportsbook in Atlanta and New York, Casino in the UK. Product managers and designers had no shared baseline for how design decisions affected experience.</p>
<p>The research team was two people. The company was preparing multi-state expansion.</p>""",
            ),
            (
                "Task",
                """<p>Design and scale standardized benchmarking across FanDuel products and primary competitors; grow research capacity for rapid expansion; and—when Voice of Customer and compliance data demanded it—build Responsible Gaming measurement rigorous enough for product, Legal/Compliance, and state regulators.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Standardized journey benchmarking</strong> — Continuous tracking across the journeys every vertical shares: Onboarding, Promotional Engagement, Depositing/Withdrawing, Bet Selection/Placement, In-Play Betting, and Outcome Tracking.</li>
<li><strong>Event-triggered telemetry</strong> — In-app surveys and behavioral trackers fired at high-friction moments. Over time, journey surveys fed stakeholder dashboards automatically (Alchemer + triggers), with me remaining owner of the instruments, data, and reporting layer.</li>
<li><strong>Responsible Gaming Sentiment Scale</strong> — Open-ended feedback kept surfacing at-risk behaviors. I developed and psychometrically validated a proprietary RG Sentiment Scale, linked it to the behavioral signals Legal/Compliance was monitoring, and grew the work into regulator collaboration as new states went live—including partnership patterns with competitors so high-risk and self-excluded users couldn’t simply hop platforms.</li>
<li><strong>Multi-state message testing</strong> — Led message testing across rollouts as the user base scaled from 1.5M to 20M+, with RG measurement supporting predictive user-protection models.</li>
<li><strong>Research ops &amp; AI pipelines</strong> — Connected siloed stakeholder tools, built libraries for data and findings, and stood up AI-enabled research pipelines. As impact and budget grew, hiring and tool procurement scaled UX research into a 32-person division delivering 200+ studies annually.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Org &amp; ops leverage</strong> — UX Research scaled from 2 to a 32-person division delivering 200+ studies annually, while AI-enabled pipelines cut turnaround time 75%—and I retained ownership of the benchmarking stack.</li>
<li><strong>Multi-state growth</strong> — Message testing and measurement supported rollouts that grew the user base from 1.5M to 20M+.</li>
<li><strong>Responsible Gaming</strong> — The proprietary RG Sentiment Scale earned regulatory approval for predictive user-protection models and became a core compliance and product-safety input across jurisdictions.</li>
<li><strong>Portfolio effect</strong> — Roughly 60% of my FanDuel projects were inspired by benchmarking findings, and the system let me take on large deep dives without abandoning core product-health tracking.</li>
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
        "short": "A 1×3 randomized trial showed the $5 offer converted as well as the $50 offer—the same 10% lift at a quarter of the payout cost.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2024",
        "summary": "Leadership asked which acquisition offer actually earns its payout. A 1,050-person randomized controlled trial answered: Bet $5 / Get $50 converted identically to Bet $50 / Get $200—both about 10% over control—at a 4× lower payout cost. The real conversion barrier was never ease of use; it was confusion about how the offers worked.",
        "insight": "Generosity didn’t drive conversion—clarity did. An early win predicted 90-day engagement four times better than bonus size.",
        "stats": [
            ("10% increase", "First-bet conversion vs. control", "conversion"),
            ("4× reduction", "Payout cost of the $5 offer vs. the $50 offer", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Activation-to-first-bet was the #1 leading indicator of long-term retention and LTV, and onboarding conversion sat below target. A 15% trust deficit looked like a technical problem—until surveys flipped the story: drop-offs rated Ease of Use exactly the same as converters. The real barrier was conceptual confusion around promotional offers.</p>
<p>Leadership brought the question to me as a dedicated deep dive. By then, core journey benchmarking ran automated into stakeholder dashboards, so I could focus here while still owning the underlying instruments, triggers, and reporting.</p>""",
            ),
            (
                "Task",
                """<p>Lead a cross-functional CPE strike team chartered to lift first-bet conversion from 20% to 30%—and determine which incentive structure converts without eroding loyalty, ahead of state launches where first impressions decide market share.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>1×3 randomized controlled trial</strong> — New visitors assigned to High-Accessibility (Bet $5, Get $50), High-Stakes (Bet $50, Get $200), or control (no promo); n=350 per group (N=1,050).</li>
<li><strong>Immediate + longitudinal measurement</strong> — Alchemer surveys after the first bet (Perceived Generosity, Loyalty, Ease of Use); Amplitude-triggered repeats at 30/60/90 days; Qualtrics via Braze for drop-off reasons.</li>
<li><strong>Statistical program</strong> — Chi-square and pairwise Z-tests (Bonferroni) for conversion; t-tests for Ease of Use; multiple regression for 90-day engagement; mixed-design ANOVA for loyalty decay.</li>
</ul>""",
            ),
            (
                "Result",
                """<p>Both offers lifted first-bet conversion about 10% over control—with no difference between the $5 and $50 offers (p=0.56). That made High-Accessibility the ROI winner at roughly a 4× reduction in payout cost. Ease of Use didn’t separate drop-offs from converters; confusion around “Win to Get” rules did. And a first win predicted 90-day engagement ~4× more strongly than bonus size, while High-Stakes loyalty decayed sharply by Day 60.</p>
<p class="callout">The recommendation: standardize Bet $5 / Get $50, redesign promo messaging for clarity, and prioritize features that create an early “First Win.”</p>""",
            ),
        ],
    },
    {
        "slug": "wallet-deposit",
        "num": "06",
        "brand": "fanduel",
        "title": "Trust-First Wallet &amp; Deposit Onboarding",
        "short": "65% of new sign-ups stalled at banking setup. Progressive disclosure and trust-framed KYC converted 150K+ abandoned accounts and ~$8M in Q1 handle.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "Amplitude showed a hard wall: 65% of new sign-ups abandoned at wallet and banking setup. Interviews, moderated sessions, and a 5,000-respondent MaxDiff revealed a trust problem, not a motivation problem. Re-sequencing the flow and explaining the compliance ask converted 150,000+ stagnant accounts, drove ~$8M in Q1 handle, and cut onboarding support tickets 30%.",
        "insight": "Users weren’t unmotivated—they were being asked for a routing number before anyone explained why.",
        "stats": [
            ("150K+", "Previously abandoned sign-ups who completed wallet setup", "scale"),
            ("$8M", "Incremental betting handle in Q1 2025", "revenue"),
            ("30% reduction", "Onboarding customer-support tickets", "efficiency"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Hundreds of thousands of users finished sign-up, then vanished before linking a bank account or making a first-time deposit. Amplitude showed a hard wall at Wallet/Banking Setup for 65% of new sign-ups—even when every earlier registration step felt seamless.</p>
<p>I initiated this project after journey work localized onboarding pain to banking and first deposit. The same analyses showed that customers who deposit in their first visit go on to bet and engage the most—exactly the customers we were losing.</p>""",
            ),
            (
                "Task",
                """<p>Determine whether the drop-off was a motivation problem or a trust problem—then redesign the KYC flow so stagnant accounts become depositing, engaged players, treating onboarding, acquisition, and first deposit as one continuous experience.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Triangulated mixed methods</strong> — Amplitude funnel analysis, 15 moderated usability sessions, and a 5,000-respondent MaxDiff survey isolated where—and why—trust broke down.</li>
<li><strong>The mental-model wall</strong> — Interviews showed churning users hit a wall at routing numbers and SSNs. ACH felt opaque, and nobody understood why a sports platform needed bank-grade financial data.</li>
<li><strong>Progressive disclosure &amp; re-sequencing</strong> — Low-stakes information first (email, phone); banking delayed until users had momentum in the product.</li>
<li><strong>Trust-framed KYC</strong> — Micro-copy explaining why compliance requires banking data and how ACH transfers are protected—humanizing the ask without softening the regulatory requirements.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Stagnant-user conversion</strong> — 150,000+ previously abandoned accounts completed wallet setup and converted.</li>
<li><strong>Handle</strong> — The optimized flow generated ~$8M in incremental betting handle in Q1 2025.</li>
<li><strong>Support load</strong> — Onboarding-related support tickets fell about 30% because compliance and security questions were answered in-product.</li>
<li><strong>Playbook</strong> — “Trust-First Onboarding” was adopted as the standard for corporate onboarding and wallet initiatives.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "cx-measurement",
        "num": "07",
        "brand": "fanduel",
        "title": "Doubling Cross-Sell Across FanDuel Products",
        "short": "Continuous CX measurement diagnosed a 10% cross-sell plateau—interventions doubled acquisitions in 90 days and unlocked ~$500M in projected LTV.",
        "context": "FanDuel · Core Products &amp; Experiences",
        "year": "2025",
        "summary": "Cross-sell between FanDuel products had been stuck near 10% all year. I built a continuous CX measurement layer—in-app pulse checks, competitive usability testing with 4,000 users, and custom telemetry hooks—found the choke point at payment linking, and shipped redesigned entry points that doubled cross-sell acquisitions in 90 days, lifted MAU 14%, and added $5M+ in monthly revenue. Outcome figures here are exclusive to this case.",
        "insight": "The barrier to a second product wasn’t interest—it was being asked for financial credentials all over again.",
        "stats": [
            ("2× increase", "Cross-sell acquisitions within 90 days", "conversion"),
            ("$500M", "Projected lifetime value from the cross-sell program", "revenue"),
            ("$5M+", "Incremental monthly revenue from cross-sell", "revenue"),
            ("14% increase", "Monthly active users", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Cross-sell conversion between FanDuel product lines had stagnated near 10% for a year, with no clear read on where—or why—customers dropped off. Marketing commissioned the work because I knew the full customer base: who already used multiple products, who didn’t, and how the two groups differed.</p>
<p>This wasn’t a benchmarking workstream; it was a growth problem that leveraged that customer fluency.</p>""",
            ),
            (
                "Task",
                """<p>Diagnose the cross-sell plateau with continuous CX measurement, then ship interventions that unlock multi-product acquisition without eroding trust—especially at payment linking.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Continuous CX measurement</strong> — In-app pulse checks, competitive usability testing with 4,000 users, and behavioral event tracking via custom telemetry hooks located the drop-off and compared FanDuel’s multi-product journey against competitors.</li>
<li><strong>Mixed-methods diagnosis</strong> — Funnel and event analysis paired with moderated sessions zeroed in on payment linking and the trust barriers around sharing data between product lines.</li>
<li><strong>Intervention design</strong> — Redesigned cross-sell entry points and trust framing so customers understood why financial credentials were needed again—and what linking products got them.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Acquisition</strong> — Cross-sell acquisitions doubled within 90 days.</li>
<li><strong>Engagement &amp; revenue</strong> — MAU rose 14%, with $5M+ in incremental monthly revenue and ~$500M in projected lifetime value from the program.</li>
<li><strong>A lasting measurement system</strong> — Marketing and Product kept an ongoing CX pulse + telemetry layer, so cross-sell health is tracked continuously—not only in one-off deep dives.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "fantasy-d2c-ideation",
        "num": "08",
        "brand": "nfl",
        "title": "Monetizing NFL Fantasy — The Tools Package",
        "short": "Identified the tools season-long players would pay for, then shipped a mid-season package that converted 45% of active users—$600K in week one.",
        "context": "NFL · Fantasy Sports",
        "year": "2020",
        "summary": "Fantasy had always been a free flywheel into the NFL app. With a five-person team, I ran a full design-thinking cycle to find the tools season-long players would actually pay for—then shipped a mid-season Tools Package that converted 1.4M users (45%) in week one for $600K, closing the season at $920K, without touching the free core game.",
        "insight": "Fans would pay to win their league—as long as paying never changed the game itself.",
        "stats": [
            ("$600K", "Direct-to-consumer revenue in the first week", "revenue"),
            ("$920K", "Direct-to-consumer revenue by season end", "revenue"),
            ("1.4M (45%)", "Active Fantasy users who bought the Tools Package", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<p>Fantasy had always been free—a flywheel into the main NFL app, where revenue flowed through existing channels. But engagement was high, needs were unmet, and analytic exploration suggested Fantasy users might pay for the right tools—if monetization never broke the free core experience.</p>""",
            ),
            (
                "Task",
                """<p>Prove the NFL could monetize the Fantasy user base directly, inside hard guardrails set up front: no unfair competitive advantage, core gameplay stays intact, avoid content the team doesn’t control, never charge for what competitors give away free, and prioritize ideas likely to drive repeat purchases.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Design-thinking cycle</strong> — Ran the group through Empathize → Define → Ideate → Prototype → Test with structured ideation sessions.</li>
<li><strong>Large-scale survey</strong> — Surfaced the top 6 features that would deepen engagement among casual and highly active players who want to do better.</li>
<li><strong>Competitive analysis</strong> — Mapped competitors’ pay-to-play features and their gaps. Daily-fantasy and season-long needs diverged—opening space to serve season-long players in public and private leagues.</li>
<li><strong>Tool principles</strong> — Help casual players win without extra work, fix common mistakes, save time, and use what only the NFL has: proprietary data (NGS, NFL Pro), proprietary content (highlights, games), and league identity (history, communication, trophies).</li>
<li><strong>The Tools Package</strong> — A monthly in-app purchase unlocking every tool across all of a user’s teams.</li>
<li><strong>Build &amp; launch</strong> — With 2 product managers and 2 designers (a team of five), concept-tested the tools, shipped a mid-season beta in the first weeks of the NFL season, and ran 10+ A/B tests on CTA placement, copy, timing, and upsell design—in-app windows only, no ads, and no UI differences between purchasers and non-purchasers.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>Week one</strong> — The mid-season launch drove $600K in direct-to-consumer revenue in the first week, converting 1.4 million active users—45% of all customers.</li>
<li><strong>Season close</strong> — An additional 24% of active users purchased by season end, bringing the tools to $920K in annual revenue.</li>
<li><strong>Product integration</strong> — Fantasy+ tools (Lineup View, personalized lists, Backups, Optimize, waiver tools) shipped inside existing Fantasy surfaces without fragmenting the free experience.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "09",
        "brand": "nfl",
        "title": "Pricing &amp; Packaging NFL+",
        "short": "Design studios plus a 2,208-fan national survey shaped the league’s first mobile subscription—NFL+ launched in 2022 to 1.1M sign-ups.",
        "context": "NFL · Digital Media &amp; NFL+",
        "year": "2020",
        "summary": "Before the NFL’s first mobile subscription could ship, the league needed to know which of five packaging configurations fans would actually pay for. I combined in-person design studios, a 2,208-fan national survey, TURF-style reach analysis, and a motivation measure adapted from academic literature into the packaging recommendations behind NFL+—which launched in 2022 to about 1.1M sign-ups.",
        "insight": "Features alone didn’t explain what fans would pay for—motivation to consume content explained why segments chose differently.",
        "stats": [
            ("1.1M", "NFL+ sign-ups after the 2022 launch", "scale"),
            ("~2.7M", "NFL+ subscribers heading into the 2024 season", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<p>The NFL was preparing NFL+—its first direct-to-consumer subscription inside the mobile app—and needed empirical guidance on how to structure, price, and bundle it against existing products like Club+, League Pass, Club Pass, and Mobile RedZone. Product and media strategy wanted a data-driven blueprint before the league’s first mobile subscription shipped.</p>""",
            ),
            (
                "Task",
                """<p>Evaluate five alternate NFL+ packaging configurations to inform D2C pricing and bundling strategy—and explain why preferences differed across fan segments using a Motivation to Consume Content measure adapted from academic literature.</p>""",
            ),
            (
                "Action",
                """<ul>
<li><strong>Pilot evaluation</strong> — Semi-structured interviews with 3 fans pressure-tested survey comprehension before fielding.</li>
<li><strong>Design Studios</strong> — Two in-person sessions with 24 NFL fans, who sorted NFL+, Club+, League Pass, Club Pass, and Mobile RedZone into MoSCoW (Must / Should / Could / Won’t) categories, then rank-ordered Packages A–E before and after pricing was revealed.</li>
<li><strong>National survey</strong> — Fielded to 2,208 NFL fans, measuring competitor-platform usage and quantitative interest in each proposed feature.</li>
<li><strong>Motivation to Consume Content (MCC)</strong> — Adapted a novel MCC measure from an academic literature review (Affect, Cognition, Environment dimensions) and used its maximum-differential component to explain preference differences between packages.</li>
<li><strong>Analysis</strong> — Univariate and multivariate statistics in SPSS evaluated reach, rank, preference, and appeal for each package across fan segments, including TURF-style reach/preference analysis.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li><strong>The first NFL+ offering</strong> — The recommendations supported the final shape of the first NFL+ direct-to-consumer product—the first subscription bundle the NFL ever offered in its mobile app.</li>
<li><strong>Launch scale</strong> — About 1.1 million sign-ups followed the 2022 launch. Though I had moved on by then, total subscribers grew 29% year-over-year, with NFL+ and NFL Sunday Ticket together reaching close to 6 million subscribers (the two are often reported as a combined figure).</li>
<li><strong>Later footprint</strong> — A standalone figure put NFL+ at about 2.7 million subscribers heading into the 2024 season.</li>
</ul>
<p class="callout">I designed and moderated the full program—pilot, Design Studios, national survey, MCC / MaxDiff, and SPSS analysis—and partnered with NFL Media and Product Strategy on the packaging recommendations.</p>""",
            ),
        ],
    },
    {
        "slug": "intel-trueview",
        "num": "10",
        "brand": "nfl",
        "badge_label": "NFL Labs",
        "title": "Intel TrueView Design Studio",
        "short": "Put Intel’s rotate-the-camera replay prototype in front of fans to learn whether—and where—it belonged in Game Pass highlights.",
        "context": "NFL Labs · Partner research with Intel",
        "year": "2019",
        "summary": "Intel built TrueView: a replay tool that lets you rotate the camera around a play instead of watching from one fixed angle. NFL Labs needed a clear read on fan appetite before investing further. I ran design studios where fans tried the working prototype, then delivered recommendations for how—and whether—to use it in Game Pass–style highlight experiences.",
        "insight": "Perspective control earned its place when fans wanted to understand a play—not as a default for every highlight.",
        "stats": [],
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
                "Action",
                """<ul>
<li><strong>Design studios</strong> — Fans tried the live TrueView prototype and talked through what felt useful, confusing, or unnecessary.</li>
<li><strong>Usage feedback</strong> — Focused on when perspective control helped (e.g., understanding a play) vs. when a normal highlight was enough.</li>
<li><strong>Recommendations</strong> — Translated session findings into guidance for Game Pass / condensed-replay use cases Intel and Labs could act on.</li>
</ul>""",
            ),
            (
                "Result",
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
    return f'<span class="product-badge product-{brand_key}"><span class="product-name">{label}</span></span>'


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
        if case.get("insight") and i == total - 1:
            section_blocks.append(
                f"""      <aside class="case-insight reveal">
        <p>“{case['insight']}”</p>
      </aside>"""
            )
        section_blocks.append(
            f"""      <section class="case-section reveal">
        <div class="case-section-label">
          <span class="case-section-num">{i + 1:02d}</span>
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

    html = (
        header(active=case["title"], prefix="../", brand=case["brand"], nav_active="cases")
        + f"""
  <main class="case-page">
    <header class="case-hero">
      <div class="wrap">
        <div class="crumb"><a href="../case-studies.html">Case studies</a> <span aria-hidden="true">/</span> {case['num']}</div>
        {badge}
        <h1>{case['title']}</h1>
        <p class="case-dek">{case['summary']}</p>
        <div class="case-meta-line">
          <span>{case['context']}</span>
          <span class="case-meta-dot" aria-hidden="true">·</span>
          <span>{case['year']}</span>
        </div>
      </div>
    </header>
    <div class="wrap case-body">
{kpi_html}
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
