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

CASES = [
    {
        "slug": "first-trade-conversion",
        "num": "01",
        "brand": "robinhood",
        "title": "Cracking First-Trade Conversion Before Tip-Off",
        "short": "A five-day sprint that traced first-trade drop-off to findability, not disinterest—recommendations lifted first-trade conversion to a record 88%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "5 business days",
        "methods": "AI-moderated interviews (Listen Labs) · Large-scale survey · Third-party panel · Funnel analysis · LLM + Claude/Python synthesis",
        "summary": "With a one-week build window before the NCAA tournament and World Cup, I ran a five-day study proving first-trade drop-off was a findability problem—recommendations helped lift first-trade conversion to a record 88%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Robinhood opened event-contract trading to its 27M+ customers.</li>
<li>~950K approved brokerage and crypto users—“non-converters”—had funded accounts but never placed a first trade, and no one could explain why.</li>
<li>Leadership was split ahead of the NCAA tournament and FIFA World Cup: build for both, build only for the World Cup, or skip both.</li>
<li>Some stakeholders were wary that a fee-cheaper competitor made the investment feel like wasted spend.</li>
<li>A recent re-org left the design team with roughly a one-week build window—the call couldn’t wait.</li>
</ul>"""),
            ("Task", """<ul>
<li>Started March 2nd, kicked off two days later with five business days to deliver.</li>
<li>Answer four questions: why approved users stall before a first trade; which levers re-engage non-converters; what design changes lift conversion; how strong appetite was for the two tent-pole events.</li>
<li>Output had to be decision-ready in time for designers to ship before tip-off.</li>
</ul>"""),
            ("Action", """<ul>
<li>Paired AI-moderated 1:1 interviews with a large-scale survey across internal and third-party panels.</li>
<li>Trained the AI moderator to teach event-contract concepts and adapt follow-ups to each participant in real time.</li>
<li>Recruited converters and non-converters from a 50K internal list, plus 50 external users from a 10K panel.</li>
<li>Had a complete sample answering all four questions within two hours of launch.</li>
<li>A prior funnel analysis had already revealed the pattern: non-converters weren’t disinterested—they returned repeatedly, navigated featured markets, searched, and left without opening an event.</li>
<li>Synthesized findings with our internal LLM alongside Claude and Python into a one-page executive summary per stakeholder—under 48 hours end to end.</li>
</ul>"""),
            ("Result", """<ul>
<li>The barrier was findability, not disinterest, and it broke in two places: the category row gave no signal that more markets existed off-screen, and search dead-ended because tournament contracts hadn’t been built.</li>
<li>Recommended three changes: rank Featured by popularity (page views, trades, notional volume) instead of alphabetically; offset the category carousel so the next category peeks into view; build tournament assets so search by team, sport, or event returns real markets.</li>
<li>Appetite ran high among both traders and non-traders, and net-new activation intent was strong—so the team built for the tournaments.</li>
<li>~630K additional brokerage and crypto users registered in the days before tip-off.</li>
<li>First-trade conversion spiked to a record 88%.</li>
<li>~480K prior non-converters (63%) placed a first trade—at zero re-engagement cost.</li>
<li>~220M college-basketball event contracts traded (~$400M notional); 1.3M users traded them.</li>
</ul>"""),
        ],
    },
    {
        "slug": "cold-start-personalization",
        "num": "02",
        "brand": "robinhood",
        "title": "The Cold-Start Problem: A Deep Dive Into a Personalization Experiment",
        "short": "Re-examined a celebrated personalization A/B test, proved it couldn’t cold-start new users, and reframed the roadmap—cutting one-and-done churn from 54% to 37%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Multi-week deep dive",
        "methods": "Behavioral segmentation · AI-moderated interviews · Factorial ANOVA (arm × segment) · Matched-sample analysis · Prototyping (Cursor · GitHub · Figma · Python)",
        "summary": "A personalization algorithm looked like a win (+4% in its A/B test) but trade volume had plateaued. My re-analysis showed it couldn’t cold-start new users, and the fixes I recommended cut one-and-done churn from 54% to 37%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Data Science built and launched a personalization algorithm; its A/B test showed the experimental group trading ~4% more than control (p<.001).</li>
<li>The result impressed leadership, who let the algorithm run.</li>
<li>Weeks later, executives hit a puzzle: event-contract trade volume had plateaued despite meaningful MAU growth.</li>
<li>No one could explain the disconnect—they asked me to find the “why.”</li>
</ul>"""),
            ("Task", """<ul>
<li>Map what actually drives and suppresses trade volume, and diagnose the plateau.</li>
<li>Preliminary analysis surfaced the risk immediately: ~70% of the base traded sports contracts only.</li>
<li>Higher-value multi-category traders—who trade significantly more—were shrinking fast.</li>
<li>That set up a seasonal cliff: once college basketball and the NBA season ended, volume had nowhere to go.</li>
</ul>"""),
            ("Action", """<ul>
<li>Working from a defined research plan, ran behavioral segmentation and interviewed the top 2% of four groups: sports-only traders, multi-category traders, former-multi-category traders who had retreated, and net-new “cold-start” users the algorithm had no history for.</li>
<li>In-app, users showed me the mechanism directly: the algorithm kept re-surfacing the same events and buried inventory they’d have loved.</li>
<li>One high-value trader had defected to a competitor for WNBA contracts that Robinhood actually offered but hid so deep in the UI he assumed they didn’t exist.</li>
<li>Went back to Data Science for the raw experiment data and found the aggregate +4% couldn’t support “personalization works”: the treatment window overlapped the NBA Finals (a major confound), the test was heavily overpowered, and the lift was carried by users with existing trading history.</li>
<li>A planned cold-start contrast (factorial ANOVA, arm × segment) told the opposite story—for net-new users, control outperformed the personalized experience by 24%.</li>
</ul>"""),
            ("Result", """<ul>
<li>Core finding: personalization alone can’t cold-start. With no history to draw on, the algorithm funneled new users into the same popular-sports events, starving discovery and manufacturing the seasonal cliff.</li>
<li>Recommended pairing personalization with explicit customization—users select categories during onboarding and toggle them on or off as interests change, a need ~90% of interviewees raised unprompted.</li>
<li>Recommended a Watch List giving traders a cross-category home to return to.</li>
<li>Prototyped both (Cursor, GitHub, Figma, Python); the Watch List shipped in a variant form.</li>
<li>One-and-done churn among crossover first-traders fell from 54% to 37% in one month.</li>
<li>The improvement held even as the cohort grew by ~300K new signups; churned users overwhelmingly had not adopted the Watch List (~3% had).</li>
<li>Onboarding customization step recommended and pending product adoption.</li>
</ul>"""),
        ],
    },
    {
        "slug": "diversify-single-category",
        "num": "03",
        "brand": "robinhood",
        "title": "From Coin Toss to Informed Call: Getting Single-Category Traders to Diversify",
        "short": "Showed diversification was blocked by confidence, not risk—new decision tools (limit order, Tool Tip) made trying a new category feel informed and lifted multi-category traders 11%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "Follow-on deep dive",
        "methods": "In-depth interviews · Scenario-based probing · Behavioral segmentation · Concept testing · Competitive analysis · Prototyping (Figma)",
        "summary": "Single-category traders wouldn’t diversify because unfamiliar categories felt like a coin toss. New decision tools—a limit order and a chart Tool Tip—made trying a new category feel informed and lifted multi-category traders 11%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Previous research indicated ~70% of users traded a single prediction-market category, overwhelmingly sports.</li>
<li>The company wanted them to expand into other categories—the trading-app version of “diversify your portfolio.”</li>
<li>Initial research surfaced the two usual suspects as the most-reported barriers: risk-aversion and lack of knowledge.</li>
<li>These were the same reasons the org reflexively met with education modules and risk-free promotions.</li>
</ul>"""),
            ("Task", """<ul>
<li>Understand the real difference between sports-only and multi-category traders—what motivates expansion versus avoidance—rather than accept the surface explanation.</li>
<li>If risk-aversion and knowledge gaps weren’t the true blockers, the company was spending on the wrong fixes.</li>
<li>Find what would genuinely move single-category traders into new domains.</li>
</ul>"""),
            ("Action", """<ul>
<li>Interviewed both sports-only and multi-category traders; found “risk-averse” and “don’t know enough” were proxies for confidence—users didn’t believe they could win.</li>
<li>The binary win/lose nature of event contracts made unfamiliar categories feel like a coin toss, too much like gambling—and a core part of these users’ identity was informed decision-making, distancing themselves from the “gambler” stereotype.</li>
<li>Walking participants through scenarios in low-knowledge categories revealed that several tools and pieces of information they’d need already existed in the app but were undiscovered.</li>
<li>Hypothesized that of the 70% “sports-only,” only ~10% are truly sports-only, while ~60% would explore if they could find something that sparked their interest.</li>
</ul>"""),
            ("Result", """<ul>
<li>The barrier was that trading a new category felt like a bet, not an informed decision—and the tools to change that were either hidden or missing.</li>
<li>The platform had no limit order—the definitional tool of a controlled trade; on my recommendation it was built into the order form, reaching ~24% of total trade volume within two weeks.</li>
<li>On the fast, binary BTC 15-minute contract, pricing history lived inside the chart but wasn’t surfaced; recommended surfacing it and turning “Source: BRTI” into a tappable link so skeptical traders could verify provenance themselves.</li>
<li>Concept-tested Tool Tip—a one-time feature prompting users to hold and scrub the chart to inspect price at any moment; it drew a night-and-day shift in willingness, shipped, and lifted multi-category traders 11%.</li>
<li>Together, these changes did what education modules and promotions never could: made trying a new category feel less like a bet and more like an informed decision. Further recommendations are on the Q4 roadmap in build/test.</li>
</ul>"""),
        ],
    },
    {
        "slug": "first-trade-recovery",
        "num": "04",
        "brand": "robinhood",
        "title": "Turning a Dead End Into a Second Chance",
        "short": "An unfixable backend error was churning 1 in 5 first-time traders—a recovery message alone won back 6 in 10, recovering ~$12M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Interview → data diagnosis → shipped fix",
        "methods": "In-depth interviews · Python/SQL prevalence analysis · Churn analysis · Message design with content partners",
        "summary": "A backend failure the company couldn’t fix was silently churning 1 in 5 first-time traders. Redesigning the moment around the error—with no engineering fix or spend—won back 6 of every 10 at-risk users and ~$12M in monthly revenue.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>A backend error the company could not control, prevent, or fix was interrupting first-time customers mid-attempt on their very first trade.</li>
<li>The failure produced a blank screen with no recovery path—no explanation, no retry, no way forward; users’ only option was to exit the app entirely.</li>
<li>It hit 1 in every 5 first-time users and had been happening since prediction markets launched; almost all affected users churned completely and experienced it as a platform failure that destroyed trust.</li>
<li>That constraint defined the problem: the error couldn’t be eliminated, so the only available lever was the experience surrounding it.</li>
</ul>"""),
            ("Task", """<ul>
<li>The problem surfaced in an interview—a participant described hitting the dead end firsthand.</li>
<li>Establish how widespread it actually was, since no one in the company had quantified it.</li>
<li>Because the error couldn’t be fixed at the source, find what would keep affected users from abandoning entirely despite it still happening—recovering a segment being lost silently, at scale, every month.</li>
</ul>"""),
            ("Action", """<ul>
<li>Used Python and SQL to diagnose prevalence across the first-trade funnel, confirming it affected 1 in 5 first-time users and was a major driver of onboarding abandonment and 7–8 figure monthly revenue loss.</li>
<li>Identified a rare and valuable population: the ~10% of affected users who returned and tried again despite the failure.</li>
<li>Interviewed that group specifically—asking what would have prevented everyone else from dropping off for good.</li>
<li>Their answer was consistent and specific: a brief explanation of what happened, plus a CTA that kept them inside the app and returned them to the event they’d been trying to trade.</li>
<li>Worked with content partners to design that messaging: a plain-language explanation of the failure and a recovery path straight back into the trade funnel.</li>
</ul>"""),
            ("Result", """<ul>
<li>Identified first-time-user friction outside company control that was driving 7–8 figure monthly losses from user abandonment.</li>
<li>Recommended a simple messaging strategy—a plain-language explanation plus a CTA back to the event they’d been trading.</li>
<li>Reduced drop-off significantly: abandonment after a failed first-trade attempt fell from roughly 9 in 10 to 3 in 10, recovering 6 of every 10 at-risk users.</li>
<li>Recovered ~$12M in monthly revenue—roughly 70% of future monthly losses.</li>
<li>The underlying error was never fixed—it still occurs. The recovery came entirely from redesigning the moment around it, with no incentives, no engineering fix, and no spend.</li>
</ul>"""),
        ],
    },
    {
        "slug": "registration-dropoff",
        "num": "05",
        "brand": "fanduel",
        "title": "Studying the Users You Can’t Recruit: Fixing Registration Drop-Off",
        "short": "Studied an unrecruitable, churned population through a simulated signup—reordering when SSN and banking are asked lifted registration completion from ~50% to ~65%.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2025",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (simulation → A/B → production)",
        "methods": "Simulated-app experiment · Step-by-step intention measurement · Third-party panel recruitment · A/B testing · Behavioral theory (foot-in-the-door)",
        "summary": "More than half of prospective FanDuel customers abandoned registration on every state launch, and they couldn’t be recruited. A simulated-app study localized the drop and a reordered flow lifted completion from ~50% to ~65% in production.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Every time FanDuel launched in a new state, more than half of prospective customers failed to complete the registration funnel.</li>
<li>The people who abandoned were the ones the business most needed to understand—but because they never finished signing up, they couldn’t be recruited for any study.</li>
<li>Users who did complete registration couldn’t explain the drop-off either; they hadn’t experienced it as a blocker.</li>
<li>This was a top priority because benchmarking had flagged registration and login as the two highest-leverage steps in the entire experience.</li>
<li>The company was scaling fast, growing from ~1.5M users when I began to 20M+ by the time I left.</li>
</ul>"""),
            ("Task", """<ul>
<li>Understand friction in a funnel I couldn’t observe directly, with a population I couldn’t recruit.</li>
<li>Ethical and compliance constraints meant no real people could attempt a real signup.</li>
<li>Find what was driving abandonment and prove a fix that would raise completion on future launches.</li>
</ul>"""),
            ("Action", """<ul>
<li>Had engineers build a simulated onboarding flow mirroring our real registration steps, framed as an e-commerce app.</li>
<li>Recruited a screened third-party panel across three interest levels (strong, medium, minimal).</li>
<li>Participants moved through the flow one step at a time, giving qualitative feedback and rating behavioral intention to continue after each step—localizing the drop to exactly two steps: providing Social Security details and banking information.</li>
<li>Key insight: our live funnel asked for SSN first and banking last—participants described deep distrust at handing over an SSN before they’d even seen the product, judging fraud and identity-theft risk not worth it for an unfamiliar sportsbook.</li>
<li>Hypothesized that the order of requests was itself driving abandonment (foot-in-the-door: small, easily accepted requests first increase the likelihood of a larger request later) and tested it with an A/B experiment (two homogeneous samples, N=500) comparing SSN-first against SSN-later.</li>
</ul>"""),
            ("Result", """<ul>
<li>Asking for email, name, and address before SSN and banking nearly doubled completion in simulation—from 30% to 58% (N=500 per arm).</li>
<li>The reordered flow shipped to production and held up on real launches, lifting completion from ~50% to ~65%.</li>
<li>Became the reordered standard applied to every subsequent state rollout.</li>
<li>Method breakthrough: studied an unrecruitable, churned population via a simulated-app proxy—ethically and compliance-safe.</li>
<li>Registration and login were a top investment area as FanDuel scaled from ~1.5M to 20M+ users during this period.</li>
</ul>"""),
        ],
    },
    {
        "slug": "benchmarking-decision-engine",
        "num": "06",
        "brand": "fanduel",
        "title": "Benchmarking as a Decision Engine: Measuring Experience Across a Fragmented Portfolio",
        "short": "Built the cross-product benchmarking system the org ran on—surfacing Same Game Parlays, collapsing reporting from quarterly to daily, and growing research into a 32-person team.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2025",
        "role": "UX Researcher (system owner)",
        "timeline": "Ongoing program",
        "methods": "Journey benchmarking · Event-triggered in-app surveys · Behavioral telemetry · Competitive benchmarking · Stakeholder dashboards",
        "summary": "FanDuel’s products were siloed with no shared baseline. I built continuous cross-product benchmarking that became the strategic document the org ran on—surfacing Same Game Parlays and growing research into a 32-person team.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>FanDuel’s products were siloed, and no research ran across them.</li>
<li>Designers and product managers shipped changes with no shared baseline and no feedback loop—no way to know whether a change had helped or hurt the experience.</li>
<li>No way to compare one product’s health against another, or against the competition.</li>
<li>The organization was, in effect, flying blind.</li>
</ul>"""),
            ("Task", """<ul>
<li>Build a standardized, ongoing way to measure user experience across every product.</li>
<li>Give teams visibility into the effect of their design decisions.</li>
<li>Give leadership a basis for prioritizing where to invest scarce design and research capacity across the portfolio.</li>
</ul>"""),
            ("Action", """<ul>
<li>Built continuous journey benchmarking across the journeys every vertical shares—onboarding, promotional engagement, deposits and withdrawals, bet selection and placement, in-play, and outcome tracking.</li>
<li>Instrumented with event-triggered in-app surveys and behavioral tracking that fired at high-friction moments and fed stakeholder dashboards.</li>
<li>Retained ownership of the instruments, data, and reporting layer.</li>
<li>Designed it to measure on three levels at once: each product’s improvement over time, products compared against one another, and every product benchmarked consistently against its main competitors.</li>
</ul>"""),
            ("Result", """<ul>
<li>The system became the strategic document the product organization ran on.</li>
<li>Led to Same Game Parlays—FanDuel’s most valuable feature—by exposing the opportunity gap (users rating FanDuel vs. rivals like DraftKings on the same dimensions) and validating the concept through development.</li>
<li>Pinpointed Onboarding and Login as the highest-leverage journey step—carrying both conversion cost and jurisdictional compliance risk (state-based registration, location controls, users logged out mid-bet-placement).</li>
<li>Connected specific pain points to customer-support costs, translating UX friction into the dollar language leadership acts on.</li>
<li>Fused sentiment with behavior in one pipeline and collapsed reporting from quarterly to daily, enabling a continuous build-measure loop; unified a fractured product suite into one comparable ecosystem and strengthened cross-sell.</li>
<li>Grew research into a 32-person team by creating org-wide demand that outstripped capacity, and defined the standardized journeys that became the foundation for Core Products & Experiences—the team I now lead.</li>
<li>Seeded the Responsible Gaming program (dedicated RG metric, tools, and risk-factor identification—developed in a separate case).</li>
</ul>"""),
        ],
    },
    {
        "slug": "ach-adoption",
        "num": "07",
        "brand": "fanduel",
        "title": "ACH Adoption: Turning a Payments Risk Into a Trust Problem Worth Solving",
        "short": "Diagnosed ACH avoidance as a trust misperception, not mechanics—message reframing nearly doubled ACH adoption from under 20% to ~32% and drained a football-Sunday fraud exploit.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2025",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (research → A/B → production)",
        "methods": "In-depth interviews · A/B message testing · Behavioral + sentiment pairing · Cross-functional work with content design",
        "summary": "Customers avoided ACH—the safer deposit method—because bank numbers felt least secure. Reframing the message (not adding incentives) nearly doubled ACH adoption from <20% to ~32%, draining a costly debit-float exploit.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Customers frequently deposited via debit card on Sundays during football, when banks were closed and their other pending transactions hadn’t posted—so accounts looked funded when they weren’t.</li>
<li>Bets settled the next day as those transactions cleared, sometimes leaving the bank unable to transfer funds; if the customer had lost, they were left with a negative balance many never repaid.</li>
<li>This cost the company directly and incentivized fraud, with bad actors opening new accounts under others’ information to keep exploiting the gap.</li>
<li>ACH deposits—tied to a verifiable bank balance—would close it, but adoption sat below 20%.</li>
</ul>"""),
            ("Task", """<ul>
<li>Understand why customers avoided ACH despite it being the safer, more stable deposit method.</li>
<li>Find a way to move adoption up without adding friction.</li>
<li>Shrink the negative-balance and fraud exposure the debit-float created.</li>
</ul>"""),
            ("Action", """<ul>
<li>Ran interviews to understand the avoidance and paired that qualitative signal with behavioral data.</li>
<li>Surfaced a counterintuitive root cause: customers perceived entering bank routing and account numbers as the least secure way to pay—riskier, in their minds, than the debit card they were used to.</li>
<li>Since the barrier was perception rather than mechanics, partnered with the content design team (copywriters) to explore message framing and tone conveying how ACH is actually safer and more secure.</li>
<li>A/B tested the variations to find what genuinely moved behavior.</li>
</ul>"""),
            ("Result", """<ul>
<li>ACH adoption rose from <20% to ~32%—nearly doubled—by correcting the security misperception rather than adding incentives or friction.</li>
<li>Because ACH ties to a verifiable balance, the shift directly drained the football-Sunday debit exploit.</li>
<li>Reduced unrecoverable negative balances and the fraudulent account creation it had motivated.</li>
<li>Root cause was a perception problem—bank numbers felt least secure—not a mechanical or incentive one.</li>
<li>A cross-functional win with content design: message framing + tone, validated by A/B testing paired with interview sentiment.</li>
</ul>"""),
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
        "headline_kpis": [
            ("Sign-ups at Launch", "1.1M"),
            ("Subscribers by 2024", "2.7M"),
        ],
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
        "video": {
            "src": "nfl-intel/trueview-prototype.mp4",
            "poster": "intel-trueview-poster.png",
            "caption": "Intel TrueView prototype — rotate-the-camera replay.",
        },
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
    {
        "slug": "insulin-pen-usability",
        "num": "12",
        "brand": "ipsos",
        "title": "Insulin Pen Usability: Turning Device Research Into Commercial Evidence",
        "short": "Authored and ran a multi-country comparative usability study of a biosimilar insulin pen—reshaping device training and cutting device-use errors 27%.",
        "context": "Ipsos Healthcare · Medical Devices & Diabetes Research",
        "year": "2015–2017",
        "role": "UX Research Analyst (protocol author, moderator, analyst)",
        "timeline": "Multi-country study",
        "methods": "Comparative usability testing · Simulated-injection task protocol · In-person moderation · Cognitive debriefing · Video capture · Follow-up interviews",
        "summary": "A pharma company needed defensible evidence of where its biosimilar insulin pen stood against market leaders. My multi-country comparative usability study reshaped the device training protocol and was associated with a 27% reduction in device-use errors.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>A global pharmaceutical company was co-developing a biosimilar insulin glargine and pen injector.</li>
<li>It needed to know how its device compared to established market leaders on the factors that determine adherence: handling, dose setting, dose reading, injection force, and confidence.</li>
<li>Insulin pens improve adherence over vial-and-syringe methods, but vary widely in usability.</li>
<li>In a market with entrenched competitor devices, the company needed defensible evidence of where its pen stood before building launch messaging or making a market-access case.</li>
</ul>"""),
            ("Task", """<ul>
<li>Produce evidence credible to three audiences at once: patients and educators who would use the device, commercial teams who needed launch messaging, and regulatory and payer stakeholders who required rigor.</li>
<li>Design and run the study that generated it.</li>
<li>Turn subjective device preference into structured, comparable data across patients and certified diabetes educators.</li>
</ul>"""),
            ("Action", """<ul>
<li>Authored the research protocol and built the study materials.</li>
<li>Moderated in-person usability sessions with patients and nurses recruited from a local clinic; participants performed simulated injections with each device in randomized order.</li>
<li>Captured performance data (task completion, whether injections were performed correctly, time on task) alongside structured preference ratings across handling, dose selection, dose reading, injection force, and confidence.</li>
<li>Filmed the sessions and conducted follow-up interviews to capture the reasoning behind participants’ ratings, then analyzed the combined behavioral and attitudinal data.</li>
</ul>"""),
            ("Result", """<ul>
<li>Central contribution: showed that how the device is taught mattered as much as the device itself.</li>
<li>Findings reshaped how the device education protocol is presented to educators and patients—a change associated with a 27% reduction in device-use errors and meaningful improvement in training time.</li>
<li>Session footage and follow-up interviews became commercial assets in their own right—the raw material for field materials used by pharmaceutical representatives and diabetes educators.</li>
<li>Produced comparative evidence across patients and certified diabetes educators to support launch messaging and market access.</li>
<li>Owned the study end to end: protocol, materials, moderation, filming, follow-up interviews, and analysis.</li>
</ul>"""),
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

    video_rail_html = ""
    if case.get("video"):
        v = case["video"]
        vtype = v.get("type", "video/mp4")
        poster = v.get("poster")
        poster_attr = f' poster="../media/{poster}"' if poster else ""
        caption = v.get("caption", "")
        caption_html = (
            f'<figcaption class="video-loop-caption">{caption}</figcaption>'
            if caption
            else ""
        )
        video_rail_html = f"""      <aside class="case-media-rail">
        <figure class="video-loop reveal">
          <div class="video-loop-frame">
            <video class="video-loop-el" autoplay loop muted playsinline preload="metadata"{poster_attr}>
              <source src="../media/{v['src']}" type="{vtype}" />
              Your browser does not support the video tag.
            </video>
            <button type="button" class="video-loop-cta" data-video-cta aria-label="Restart video and expand to full screen">
              <span class="video-loop-cta-icon" aria-hidden="true">&#10227;</span>
              <span>Restart &amp; expand</span>
            </button>
          </div>
          {caption_html}
        </figure>
      </aside>"""

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
            f"""        <section class="case-section reveal">
          <div class="case-section-label">
            <h2>{title}</h2>
          </div>
          <div class="case-section-body">{body}</div>
        </section>"""
        )
    flow_html = f"""      <div class="case-flow">
{chr(10).join(section_blocks)}
      </div>"""
    if video_rail_html:
        body_main = f"""      <div class="case-layout">
{flow_html}
{video_rail_html}
      </div>"""
    else:
        body_main = flow_html

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
    brief_rows = []
    for key, label in (("role", "Role"), ("timeline", "Timeline"), ("methods", "Methods")):
        if case.get(key):
            brief_rows.append((label, case[key]))
    brief_html = ""
    if brief_rows:
        items = "\n".join(
            f"""          <div class="brief-item">
            <dt>{label}</dt>
            <dd>{value}</dd>
          </div>"""
            for label, value in brief_rows
        )
        brief_html = f"""
        <dl class="case-brief">
{items}
        </dl>"""

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
        {brief_html}
      </div>
    </header>
    <div class="wrap case-body">
{charts_before}
{body_main}
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
