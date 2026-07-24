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
        "images": [
            {
                "src": "01-non-converters/featured-before-change.png",
                "alt": "Prediction markets home before the change",
                "caption": "Before: the Featured card and category row sit flush to the edge — no signal more exists off-screen.",
            },
            {
                "src": "01-non-converters/featured-after-change.png",
                "alt": "Prediction markets home after the change",
                "caption": "After: offsetting the frame lets the next card peek in, cueing a sideways swipe.",
            },
            {
                "src": "01-non-converters/featured-non-sports-carousel.png",
                "alt": "New non-sports carousel above Newly Listed",
                "caption": "After: a dedicated non-sports carousel (Politics, Crypto, Technology, Commodities) added above Newly Listed.",
            },
        ],
        "title": "Why Approved Traders Never Placed Their First Trade",
        "short": "Approved traders kept signing up for prediction markets but never placed a first trade—matched interviews traced it to findability on the home page, and five low-effort design changes brought ~480K stalled customers back to a first trade.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "~1 week (vs. typical 3–4 weeks)",
        "methods": "AI-moderated interviews (Listen Labs) · Matched converter/non-converter design · Funnel analysis · Claude/Python/SQL deep dive",
        "summary": "A large group of approved customers went through every step to trade event contracts, then never placed a first trade. A one-week matched study showed the barrier was findability on the home page—and five low-effort changes brought roughly 480K stalled customers back to a first trade.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Robinhood opened event-contract trading to its 27M+ customers, but crossover from traditional traders (stocks, futures, crypto) was low — only a small share moved into event contracts.</li>
<li>A large group of existing customers went through the steps to get approved to trade event contracts, then never placed a first trade.</li>
<li>These “non-converters” stayed active on Robinhood otherwise — still trading and investing as before, just not in prediction markets — so disinterest didn’t explain it.</li>
<li>They accounted for more than half of all registered prediction-market users.</li>
<li>The question: what drove them in, and what drove them out before a first trade?</li>
</ul>"""),
            ("Task", """<ul>
<li>Kicked off within two days of the request; typical turnaround for this study type was 3–4 weeks.</li>
<li>Answer where users dropped off (home page, event-details page, or order form), why approved users stall before a first trade, and what low-effort design changes would lift first-trade conversion.</li>
<li>Determine whether barriers differed by trader type (stocks, futures, crypto).</li>
<li>Determine whether non-converters returned to the prediction-market section only to leave again without trading.</li>
<li>Output had to be design-specific recommendations that were minimal effort and low cost.</li>
</ul>"""),
            ("Action", """<ul>
<li>Ran AI-moderated interviews via Listen Labs with two matched groups of similar background: 25 converters (placed a first trade) and 25 non-converters (had not).</li>
<li>Trained the AI moderator to adapt follow-ups to each participant in real time.</li>
<li>Recruited both groups from a 50K internal list — all active futures, crypto, and stock traders.</li>
<li>Paired the qualitative signal with funnel analysis and a Claude/Python/SQL deep dive into engagement behavior.</li>
</ul>"""),
            ("Result", """<p>The two groups arrived at the app for different reasons, and the design only worked for one of them:</p>
<ul>
<li>Converters came in looking for a specific event. They already knew what they wanted, so they used the search bar to find it and place a trade.</li>
<li>Non-converters came in to browse. They were looking for something to catch their interest but never found it, so they left. Most never used search, because they didn’t know what to type.</li>
<li>Non-converters gave up on the home page. They didn’t know the row of category buttons at the top held more categories, and they didn’t realize the Featured and Newly Listed rows could be swiped sideways to reveal more events. So they never saw the markets that might have interested them.</li>
<li>Interest was split fairly evenly in both groups: a little over half leaned toward sports, and the rest toward commodities, elections, and politics. The home page needed to speak to both, instead of using an alphabetical order that highlighted neither.</li>
</ul>
<p>Recommended five low-effort, low-cost design changes:</p>
<ul>
<li>Offset the top category bar so hidden category pills peek into view, cueing that more categories exist.</li>
<li>Offset the frame on the Featured and Newly Listed rows so the next card is partly visible, signaling the rows are swipeable.</li>
<li>Add a non-sports carousel above Newly Listed — dedicated space for commodities, elections, and politics.</li>
<li>Add a sports-focused section below Newly Listed for the slightly-larger sports-first half.</li>
<li>Rank every row by a popularity-and-recency system — weighting page views first, surfacing the most current high-interest events earliest, and diverting soon-but-less-viewed events to the Live section.</li>
</ul>
<p><strong>What happened after the changes shipped.</strong> The changes recovered a large share of the stalled customers and improved two separate measures the business tracked. Each is described below in plain terms.</p>
<ul>
<li><strong>Half the stalled group finally traded.</strong> Of the roughly 900,000 approved customers who had never traded, about 480,000 placed their first trade.</li>
<li><strong>More people traded in the same sitting they signed up — up from 57% to about 66%.</strong> The company wanted customers to place their first trade in the same session they got approved, without leaving the app and coming back. (This measure counts only people who finish in one sitting, which usually takes a few minutes; it excludes new customers who need a manual review first.) This mattered because customers who trade in that first sitting go on to trade about 15% more than those who don’t.</li>
<li><strong>Nearly everyone who traded within a day did so quickly — 88%.</strong> A second measure looked at customers who placed a first trade within 24 hours of being approved; that figure reached 88%. The 24-hour mark mattered because separate research showed that customers who trade within a day stay more engaged over time than those who take longer.</li>
</ul>"""),
        ],
    },
    {
        "slug": "first-trade-recovery",
        "num": "02",
        "brand": "robinhood",
        "title": "Turning a Dead End Into a Second Chance",
        "short": "A backend failure the company couldn’t fix was silently churning 1 in 5 first-time traders. Redesigning the moment around the error—a plain-language message and a path back to the trade—won back 6 of every 10 at-risk users and ~$12M in monthly revenue.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Interview → data diagnosis → shipped fix",
        "methods": "In-depth interviews · Python/SQL prevalence analysis · Churn analysis · Message design with content partners",
        "summary": "A backend failure the company couldn’t control was silently churning 1 in 5 first-time traders. Redesigning the moment around the error—with no engineering fix or spend—kept 6 of every 10 at-risk users and recovered about $12M in monthly revenue.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>A backend error the company could not control, prevent, or fix was interrupting first-time customers mid-attempt on their very first trade.</li>
<li>The failure produced a blank screen with no recovery path — no explanation, no retry, no way forward.</li>
<li>Users’ only option was to exit the app entirely.</li>
<li>It hit 1 in every 5 first-time users, and it had been happening since prediction markets launched.</li>
<li>Almost all affected users churned completely and never came back.</li>
<li>Users experienced it as a platform failure, and it destroyed their trust.</li>
<li>That constraint defined the problem: the error couldn’t be eliminated, so the only available lever was the experience surrounding it.</li>
</ul>"""),
            ("Task", """<ul>
<li>The problem surfaced in an interview — a participant described hitting the dead end firsthand.</li>
<li>Establish how widespread it actually was, since no one in the company had quantified it.</li>
<li>Because the error couldn’t be fixed at the source, find what would keep affected users from abandoning entirely despite it still happening.</li>
<li>Recover a customer segment that was being lost silently, at scale, every month.</li>
</ul>"""),
            ("Action", """<ul>
<li>Used Python and SQL to diagnose prevalence across the first-trade funnel, confirming it affected 1 in 5 first-time users and was a major driver of onboarding abandonment and 7–8 figure monthly revenue loss.</li>
<li>Identified a rare and valuable population: the ~10% of affected users who returned and tried again despite the failure.</li>
<li>Interviewed that group specifically — asking what would have prevented everyone else from dropping off for good.</li>
<li>Their answer was consistent and specific: a brief explanation of what happened, plus a CTA that kept them inside the app and returned them to the event they’d been trying to trade.</li>
<li>Worked with content partners to design that messaging: a plain-language explanation of the failure and a recovery path straight back into the trade funnel.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>The problem was a failure the company couldn’t fix, and it was costing millions a month.</strong> New customers were hitting a technical error the company had no control over, and most of them left for good. The lost business ran into the tens of millions of dollars a month.</li>
<li><strong>The fix was a simple message, not an engineering change.</strong> I recommended showing customers a short, plain explanation of what went wrong, plus a button that took them straight back to the event they’d been trying to trade — instead of leaving them stuck on a blank screen with no way forward.</li>
<li><strong>Far fewer people gave up.</strong> Before, about 9 out of 10 customers who hit the error abandoned the app. After the change, that dropped to about 3 out of 10 — meaning 6 of every 10 customers who would have been lost were kept.</li>
<li>This recovered about $12 million in revenue a month, roughly 70% of what the company had been on track to lose.</li>
<li>The underlying error was never fixed — it still happens. The entire recovery came from redesigning what customers see when it happens, with no financial incentives, no engineering fix, and no added spend.</li>
</ul>"""),
        ],
    },
    {
        "slug": "diversify-single-category",
        "num": "03",
        "brand": "robinhood",
        "images": [
            {
                "src": "03-category-expansion/order-form-before-change.png",
                "alt": "Order form before the change",
                "caption": "Before: one lever — a dollar amount, buy at the market price or not at all.",
            },
            {
                "src": "03-category-expansion/order-type-menu.png",
                "alt": "New order-type menu",
                "caption": "The new order-type menu introducing the Limit order — set your own price, good for the day.",
            },
            {
                "src": "03-category-expansion/order-form-after-change.png",
                "alt": "Order form after the change",
                "caption": "After: full limit-order controls — set price, quantity, and expiry, with cost and payout shown before you commit.",
            },
        ],
        "video": {
            "src": "03-category-expansion/btc-scrub.mp4",
            "poster": "03-category-expansion/btc-scrub-poster.jpg",
            "mode": "click",
            "cta": "Click to watch video",
            "caption": "Scrubbing the Bitcoin chart to inspect the price at any moment, sourced from CF Benchmarks’ BRTI.",
        },
        "title": "From Coin Toss to Informed Call: Getting Single-Category Traders to Diversify",
        "short": "About 70% of users traded a single category, mostly sports. The real blocker wasn’t risk or knowledge but confidence—new decision tools (a limit order and a chart Tool Tip) made trying a new category feel informed and lifted multi-category trading 11%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "Follow-on deep dive",
        "methods": "In-depth interviews · Behavioral segmentation · Scenario-based probing · Usability testing · Concept testing · Competitive analysis · Prototyping (Figma)",
        "summary": "Single-category traders wouldn’t diversify because unfamiliar categories felt like a coin toss. Surfacing tools that were already in the app—a limit order and a chart Tool Tip—made trying a new category feel informed and lifted the share of multi-category traders 11%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Previous research showed about 70% of users traded a single prediction-market category, overwhelmingly sports.</li>
<li>The company wanted them to expand into other categories — the trading-app version of “diversify your portfolio.”</li>
<li>Initial research surfaced the two usual suspects as the most-reported barriers: risk-aversion and lack of knowledge.</li>
<li>These were the same reasons the org reflexively met with education modules and risk-free promotions.</li>
</ul>"""),
            ("Task", """<ul>
<li>Understand the real difference between sports-only and multi-category traders — what actually blocks expansion — rather than accept the surface explanation.</li>
<li>If risk-aversion and knowledge gaps weren’t the true blockers, the company was spending on the wrong fixes.</li>
<li>Find what would genuinely move single-category traders into new categories.</li>
</ul>"""),
            ("Action", """<ul>
<li>Interviewed both sports-only and multi-category traders, and paired that with behavioral segmentation of the single-category group.</li>
<li>Behavioral analysis split the sports-only population into two clear segments:
<ul>
<li>About 60% were exploring but never trading. They visited other categories’ event pages and looked around, but never placed a trade outside sports.</li>
<li>About 40% never explored at all. They came in, went straight to the sports event they wanted, traded, and left — staying within sports every time.</li>
</ul>
</li>
<li>For the exploring 60%, interviews showed “risk-averse” and “don’t know enough” were really about confidence — they didn’t believe they could win. The binary win/lose nature of event contracts made unfamiliar categories feel like a coin toss, too close to gambling — which mattered because these users saw themselves as informed decision-makers and wanted to distance themselves from the “gambler” stereotype.</li>
<li>Walking them through scenarios in unfamiliar categories revealed that the tools and information they’d need to feel confident already existed in the app but were hidden or undiscovered.</li>
<li>For the 40% who never explored, the issue was different: personalization kept recommending more of what they already traded (more sports), so it never exposed them to anything new — and their engagement narrowed and dropped off when their main sport’s season ended.</li>
<li>Identified a time-horizon barrier unique to sports-only traders: they like sports because an event starts and settles quickly, so their money isn’t tied up. A long-dated market (like “who wins the 2028 election”) locks up funds for months, which they actively avoid — so most non-sports categories felt like money-jail.</li>
<li>Ran usability testing on the 15-minute Bitcoin market to see whether a fast-settling non-sports event would satisfy that quick-turnaround need — it did.</li>
</ul>"""),
            ("Result", """<p>The real barrier for the exploring majority: trading a new category felt like a gamble, not an informed choice — and the tools that would make it feel informed were either hidden in the app or missing entirely. The recommendations below are ordered by how easily they could be acted on.</p>
<p><strong>Lowest-hanging fruit — tell people about tools that already existed.</strong> The fastest wins required no new capability, just surfacing what was buried:</p>
<ul>
<li><strong>Point users to the limit order.</strong> The limit order lets a trader set the price they’re willing to pay instead of taking whatever the market offers, but it was buried deep in the order form and few users ever reached it. After it was surfaced and added to the order form, limit orders made up about 24% of all trading volume within two weeks.</li>
<li><strong>Show where the price comes from, and how to see its history.</strong> On the 15-minute Bitcoin market, the price history was on the chart but wasn’t presented as decision support, and the source wasn’t clearly credited. I recommended making the pricing history easier to find and turning the “Source: BRTI” label into a tappable link to the independent benchmark, so skeptical traders could verify it themselves.</li>
<li><strong>For sports-only traders specifically — surface fast-settling non-sports events.</strong> Because these users avoid anything that ties up their money, I recommended surfacing quick-turnaround non-sports markets like the 15-minute Bitcoin event. Usability testing confirmed this satisfied their need for a fast start-to-finish window — giving them a non-sports on-ramp that didn’t feel like money-jail.</li>
<li><strong>Teach the chart-scrub.</strong> Testing the Bitcoin event surfaced the next problem: users didn’t know they could press and drag along the chart to see the price at any point in time. I concept-tested Tool Tip, a one-time prompt that shows them this is possible. In testing it clearly changed how willing people were to engage, and after it shipped, the share of people trading in more than one category rose 11%.</li>
</ul>
<ul>
<li>Further recommendations were added to the Q4 roadmap and are being built and tested now.</li>
<li>This study is what led to the deeper dive into personalization that followed. The 40% who never explored turned out to be a cold-start problem in miniature: whatever a user happens to trade first becomes the only kind of event the system shows them, which quietly locks in a single-category habit from day one. That finding is why the next study focused entirely on personalization — and why the customization features (letting users choose what they see, rather than having their first trade decide it) are being built for Q4.</li>
<li>Together, these changes did what education pop-ups and free-money promotions never managed to: they made trying a new category feel less like a gamble and more like an informed decision.</li>
</ul>
<p><strong>The three features, briefly:</strong></p>
<ul>
<li><strong>Limit order</strong> — added to the order form; lets a trader set their own price. Closed a gap competitors already had.</li>
<li><strong>Tool Tip</strong> — a one-time prompt showing users they can press and drag the chart to inspect the price at any moment. Appears once, then disappears. This was the change behind the 11% lift.</li>
<li><strong>“Source: BRTI” link</strong> — a tappable link on the Bitcoin market that lets users verify where the price comes from.</li>
</ul>"""),
        ],
    },
    {
        "slug": "cold-start-personalization",
        "num": "04",
        "brand": "robinhood",
        "title": "The Cold-Start Problem: A Deep Dive Into a Personalization Experiment",
        "short": "A personalization algorithm looked like a win (+4% in its A/B test) but trade volume had plateaued. Re-analysis showed it couldn’t cold-start new users; the fixes I recommended cut post-first-trade drop-off from 54% to 37%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Multi-week deep dive",
        "methods": "Behavioral segmentation · AI-moderated interviews · Factorial ANOVA (arm × segment) · Matched-sample analysis · Prototyping (Cursor · GitHub · Figma · Python)",
        "summary": "A personalization algorithm looked like a win (+4% in its A/B test), yet trade volume had plateaued. My re-analysis showed it couldn’t cold-start new users, and the fixes I recommended cut post-first-trade drop-off from 54% to 37%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Data Science built and launched a personalization algorithm; its A/B test showed the experimental group trading ~4% more than control (p&lt;.001).</li>
<li>The result impressed leadership, who let the algorithm run.</li>
<li>Weeks later, executives hit a puzzle: event-contract trade volume had plateaued despite meaningful MAU growth.</li>
<li>No one could explain the disconnect — they asked me to find the “why.”</li>
</ul>"""),
            ("Task", """<ul>
<li>Map what actually drives and suppresses trade volume, and diagnose the plateau.</li>
<li>Preliminary analysis surfaced the risk immediately: ~70% of the base traded sports contracts only.</li>
<li>Higher-value multi-category traders — who trade significantly more — were shrinking fast.</li>
<li>That set up a seasonal cliff: once college basketball and the NBA season ended, volume had nowhere to go.</li>
</ul>"""),
            ("Action", """<ul>
<li>Working from a defined research plan, ran behavioral segmentation and interviewed the top 2% of four groups: sports-only traders, multi-category traders, former-multi-category traders who had retreated, and net-new “cold-start” users the algorithm had no history for.</li>
<li>In-app, users showed me the mechanism directly: the algorithm kept re-surfacing the same events and buried inventory they’d have loved.</li>
<li>One high-value trader had defected to a competitor for WNBA contracts that Robinhood actually offered but hid so deep in the UI he assumed they didn’t exist.</li>
<li>Went back to Data Science for the raw experiment data and found the aggregate +4% couldn’t support “personalization works”: the treatment window overlapped the NBA Finals (a major confound), the test was heavily overpowered, and the lift was carried by users with existing trading history.</li>
<li>A planned cold-start contrast (factorial ANOVA, arm × segment) told the opposite story — for net-new users, control outperformed the personalized experience by 24%.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>The main finding: personalization can’t get a brand-new user started.</strong> With no past behavior to learn from, the algorithm kept showing new users the same popular sports events. That left them nothing new to discover, and it set up the seasonal drop-off — when sports seasons ended, these users had nowhere else to go.</li>
<li><strong>Recommendation 1 — let users choose their own categories.</strong> Rather than rely on the algorithm alone, let people pick the categories they care about when they sign up, and turn them on or off as their interests change. About 90% of the people interviewed asked for this without being prompted.</li>
<li><strong>Recommendation 2 — add a Watch List.</strong> Give traders one place to save events across categories and come back to, so they always have a reason to return.</li>
<li>I built working prototypes of both (using Cursor, GitHub, Figma, and Python). The Watch List design moved into beta testing.</li>
</ul>
<p><strong>What the A/B test showed</strong></p>
<ul>
<li><strong>The Watch List cut drop-off after a first trade.</strong> In the control group (no Watch List), 54% of users dropped off after placing a trade; with the Watch List, only 37% dropped off after their first trade.</li>
<li>The customization idea — letting users pick their own categories — was recommended and is being built, with those options planned for release in Q4.</li>
</ul>
<p class="callout">Note: The watchlist designs that shaped this work are in beta testing and not yet fully live in prediction markets, so any visuals reflect the existing investing-side watchlist that set the framework for the initial prediction-markets design.</p>"""),
        ],
    },
    {
        "slug": "registration-dropoff",
        "num": "05",
        "brand": "fanduel",
        "title": "Studying the Users You Can’t Recruit: Fixing Registration Drop-Off",
        "short": "More than half of prospective customers abandoned registration on every state launch, and they couldn’t be recruited. A simulated-app study localized the drop and a reordered flow lifted completion from ~50% to ~65% in production.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2023",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (simulation → A/B → production)",
        "methods": "Simulated-app experiment · Step-by-step intention measurement · Third-party panel recruitment · A/B testing · Behavioral theory (foot-in-the-door)",
        "summary": "More than half of prospective FanDuel customers abandoned registration on every state launch—and they couldn’t be recruited to study. A simulated-app experiment localized the drop, and reordering when SSN and banking are asked lifted completion from ~50% to ~65% in production.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Every time FanDuel launched in a new state, more than half of prospective customers failed to complete the registration funnel.</li>
<li>The people who abandoned were the ones the business most needed to understand — but because they never finished signing up, they couldn’t be recruited for any study.</li>
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
<li>Participants moved through the flow one step at a time, giving qualitative feedback and rating behavioral intention to continue after each step.</li>
<li>That localized the drop in intention to exactly two steps: providing Social Security details and banking information.</li>
<li>Key insight: our live funnel asked for SSN first and banking last — participants described deep distrust at handing over an SSN before they’d even seen the product, judging fraud and identity-theft risk not worth it for an unfamiliar sportsbook.</li>
<li>Hypothesized that the order of requests was itself driving abandonment, grounded in the foot-in-the-door principle (small, easily accepted requests first increase the likelihood of a larger request later).</li>
<li>Tested it with an A/B experiment (two homogeneous samples, N=500) comparing SSN-first against SSN-later.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>Changing the order of the questions nearly doubled sign-ups in testing.</strong> When the flow asked for email, name, and address first — and saved the Social Security number and banking details for later — completion rose from 30% to 58% in the simulation (500 people in each version).</li>
<li><strong>The same fix worked just as well with real customers.</strong> Once the reordered flow went live, completion climbed from about 50% to about 65%.</li>
<li><strong>It became the standard.</strong> Every new-state launch afterward used the reordered flow.</li>
<li><strong>The method itself was the breakthrough.</strong> It made it possible to study people who had quit and couldn’t be recruited — by watching new participants go through a stand-in version of the flow — without any ethical or compliance problems.</li>
<li>Registration and login stayed a top area of investment while FanDuel grew from about 1.5 million to more than 20 million registered users during this period.</li>
</ul>"""),
        ],
    },
    {
        "slug": "benchmarking-decision-engine",
        "num": "06",
        "brand": "fanduel",
        "title": "Benchmarking as a Decision Engine: Measuring Experience Across a Fragmented Portfolio",
        "short": "FanDuel’s products were siloed with no shared baseline. I built continuous cross-product benchmarking that became the reference point the org used to decide where to invest—surfacing Same Game Parlays and growing research into a 32-person team.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2023",
        "role": "UX Researcher (system owner)",
        "timeline": "Ongoing program",
        "methods": "Journey benchmarking · Event-triggered in-app surveys · Behavioral telemetry · Competitive benchmarking · Stakeholder dashboards",
        "summary": "FanDuel’s products were siloed with no shared baseline. I built continuous cross-product benchmarking that became the reference point the organization used to decide where to invest—surfacing Same Game Parlays and growing research into a 32-person team.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>FanDuel’s products were siloed, and no research ran across them.</li>
<li>Designers and product managers shipped changes with no shared baseline and no feedback loop.</li>
<li>No way to know whether a change had helped or hurt the experience.</li>
<li>No way to compare one product’s health against another, or against the competition.</li>
<li>The organization was, in effect, flying blind.</li>
</ul>"""),
            ("Task", """<ul>
<li>Build a standardized, ongoing way to measure user experience across every product.</li>
<li>Give teams visibility into the effect of their design decisions.</li>
<li>Give leadership a basis for prioritizing where to invest scarce design and research capacity across the portfolio.</li>
</ul>"""),
            ("Action", """<ul>
<li>Built continuous journey benchmarking across the journeys every vertical shares — onboarding, promotional engagement, deposits and withdrawals, bet selection and placement, in-play, and outcome tracking.</li>
<li>Instrumented with event-triggered in-app surveys and behavioral tracking that fired at high-friction moments and fed stakeholder dashboards.</li>
<li>Retained ownership of the instruments, data, and reporting layer.</li>
<li>Designed it to measure on three levels at once: each product’s improvement over time, products compared against one another, and every product benchmarked consistently against its main competitors.</li>
</ul>"""),
            ("Result", """<p>The system became the reference point the whole product organization used to decide where to invest.</p>
<p><strong>What it uncovered</strong></p>
<ul>
<li><strong>It led to Same Game Parlays, FanDuel’s most valuable feature.</strong> By having customers rate FanDuel against rivals like DraftKings on the same measures, the system exposed a gap in what FanDuel offered — and the research then helped shape and confirm the feature as it was built.</li>
<li><strong>It showed that onboarding and login were the most important place to improve.</strong> This step cost the company the most sign-ups and also carried the most legal risk — customers had to register state by state, location had to be verified, and some were getting logged out in the middle of placing a bet.</li>
<li>It tied specific frustrations to support costs, which put customer-experience problems in the dollar terms leadership responds to.</li>
</ul>
<p><strong>What it created</strong></p>
<ul>
<li><strong>One combined view of how customers felt and how they behaved.</strong> The system could show, for example, how people felt about a feature they weren’t actually using — and it moved reporting from once a quarter to every day, so teams could make a change and see the effect quickly.</li>
<li><strong>One shared way to compare every product.</strong> It turned a set of disconnected products into a single comparable picture, fed every team’s plans, and helped move customers between products.</li>
</ul>
<p><strong>What it grew into</strong></p>
<ul>
<li><strong>A 32-person research team.</strong> The system gave every product group a clear view of their gaps, which created more demand for research than the existing team could handle — and that demand is what justified growing it.</li>
<li><strong>A new cross-functional team, Core Products &amp; Experiences, which I now lead.</strong> The standardized customer journeys the system defined became that team’s foundation.</li>
<li>The starting point for the Responsible Gaming program — its dedicated measure, tools, and risk detection (covered in a separate case study).</li>
</ul>"""),
        ],
    },
    {
        "slug": "ach-adoption",
        "num": "07",
        "brand": "fanduel",
        "title": "ACH Adoption: Turning a Payments Risk Into a Trust Problem Worth Solving",
        "short": "Customers avoided ACH—the safer deposit method—because bank numbers felt least secure. Reframing the message (not adding incentives) roughly doubled ACH adoption from under 20% to ~32%, draining a costly football-Sunday debit exploit.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2024–2026",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (research → A/B → production)",
        "methods": "In-depth interviews · A/B message testing · Behavioral + sentiment pairing · Cross-functional work with content design",
        "summary": "Customers avoided ACH—the safer deposit method—because entering bank numbers felt least secure. Reframing the message rather than adding incentives roughly doubled ACH adoption from under 20% to about 32%, draining a costly football-Sunday debit exploit.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Customers frequently deposited via debit card on Sundays during football, when banks were closed.</li>
<li>Their other pending transactions hadn’t posted yet — so accounts looked funded when they weren’t.</li>
<li>Bets settled the next day as those transactions cleared, sometimes leaving the bank unable to transfer funds.</li>
<li>If the customer had lost, they were left with a negative balance many never repaid.</li>
<li>This cost the company directly and incentivized fraud, with bad actors opening new accounts under others’ information to keep exploiting the gap.</li>
<li>ACH deposits — tied to a verifiable bank balance — would close it, but adoption sat below 20%.</li>
</ul>"""),
            ("Task", """<ul>
<li>Understand why customers avoided ACH despite it being the safer, more stable deposit method.</li>
<li>Find a way to move adoption up without adding friction.</li>
<li>Shrink the negative-balance and fraud exposure the debit-float created.</li>
</ul>"""),
            ("Action", """<ul>
<li>Ran interviews to understand the avoidance and paired that qualitative signal with behavioral data.</li>
<li>Surfaced a counterintuitive root cause: customers perceived entering bank routing and account numbers as the least secure way to pay — riskier, in their minds, than the debit card they were used to.</li>
<li>Since the barrier was perception rather than mechanics, partnered with the content design team (copywriters) to explore message framing and tone conveying how ACH is actually safer and more secure.</li>
<li>A/B tested the variations to find what genuinely moved behavior.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>Roughly twice as many customers started using bank transfers.</strong> Adoption of ACH (paying directly from a bank account) rose from under 20% to about 32%.</li>
<li><strong>The fix was to correct a false impression, not to add rewards or extra steps.</strong> Customers had believed that typing in bank account and routing numbers was the least safe way to pay — less safe than the debit card they were used to, which is the opposite of the truth. Better wording, developed with the content design team and tested head-to-head, changed that belief.</li>
<li><strong>This directly shrank the Sunday-football problem.</strong> Because a bank transfer is tied to money the customer actually has, moving people onto it removed much of the gap that let bets get placed against funds that weren’t really there.</li>
<li>It reduced two costly outcomes: customers left owing money they never paid back, and the fraud that came with it — people opening new accounts under other identities to keep exploiting the gap.</li>
</ul>"""),
        ],
    },
    {
        "slug": "fantasy-d2c-ideation",
        "num": "08",
        "brand": "nfl",
        "title": "NFL Fantasy Mobile App",
        "subtitle": "Monetizing Fantasy Football — The Tools Package",
        "short": "Developed and shipped Fantasy features available via in-app purchase—$600K in the first week, $920K in total revenue in 2020, bought by 1.4M users (45% of active users).",
        "brand_card": {
            "logo": "nfl/nfl-fantasy-logo.png",
            "logo_alt": "NFL Fantasy logo",
            "tagline": "In-App Tools Package",
        },
        "media_gallery": [
            {
                "src": "fantasy/tools-package.png",
                "alt": "The Tools Package inside the Fantasy app",
                "caption": "The Tools Package, shipped inside the Fantasy app — waiver tools, most-added players, and upgrade prompts.",
            },
            {
                "row": [
                    {"src": "fantasy/lineup-view.png", "alt": "The all-new Lineup View"},
                    {"src": "fantasy/player-lists.png", "alt": "Personalized player lists"},
                    {"src": "fantasy/backups.png", "alt": "Set your backups to avoid last-minute inactives"},
                ],
                "caption": "Feature set: the all-new Lineup View, personalized player lists, and backups to avoid last-minute inactives.",
            },
        ],
        "headline_kpis": [
            ("Total Revenue (2020)", "$920K"),
            ("Active Users Who Bought", "1.4M (45%)"),
        ],
        "context": "NFL · NFL Fantasy App · Fantasy Sports",
        "year": "2019–2021",
        "role": "UX Researcher (study lead) · 5-person cross-functional team (2 designers, 1 researcher, 1 PM, 1 engineer)",
        "methods": "In-depth interviews · Large-scale survey · MaxDiff · Design-thinking · Static-concept testing · A/B testing",
        "summary": "Developed and shipped Fantasy features sold via in-app purchase—$600K in direct-to-consumer sales in the first week, $920K in total revenue in 2020, bought by 1.4M users (45% of active users), and later folded into NFL+.",
        "insight": "Fans would pay to win their league—as long as paying never changed the game itself.",
        "stats": [
            ("$600K", "Direct-to-consumer sales in the first week", "revenue"),
            ("$920K", "Total revenue in 2020", "revenue"),
            ("1.4M (45%)", "Active Fantasy users who bought the Tools Package", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>Fantasy Football was a free feature that pulled fans into the NFL app, but the app’s actual revenue came from elsewhere.</li>
<li>Engagement was high and players had needs the free game didn’t meet — a sign they might pay, as long as paying never interfered with the core game everyone came for.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Prove that Fantasy could make money directly, within strict guardrails: no pay-to-win, the core game left intact, and no charging for things competitors gave away free.</li>
<li>Focus on the tools most likely to earn repeat purchases, not one-time buys.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Started with interviews to understand what players actually needed, then validated it at scale with a large survey.</li>
<li>Used MaxDiff analysis to find which combinations of tools were most in demand and most likely to convert.</li>
<li>Designed and tested static versions of the features, upsells, and different call-to-action placements and messaging.</li>
<li>Landed on two ways to buy: the full bundle, or “à la carte” — one tool at a time. The tools included automatic lineup optimization, automatic injured-player replacement, and an auto-draft feature.</li>
<li>Ran A/B tests on the in-app upsells to tune what converted.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>The Tools Package sold immediately — $600K in direct-to-consumer sales in its first week.</li>
<li>It reached $920K in total revenue in 2020, bought by 1.4 million users (45% of active users).</li>
<li>It never broke the free game. The paid tools lived inside the existing Fantasy screens, so the free experience stayed whole.</li>
<li>It became part of NFL+. The Tools Package was later folded into the NFL+ subscription in 2022.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "nfl-d2c-packaging",
        "num": "09",
        "brand": "nfl",
        "title": "Pricing &amp; Packaging: The NFL+ Subscription",
        "short": "Formative research on the NFL’s first direct-to-consumer mobile subscription—NFL+, launched in 2022 to ~1.1M sign-ups and ~2.7M subscribers by 2024.",
        "brand_card": {
            "logo": "nfl/nflplus-logo.png",
            "logo_alt": "NFL+ logo",
            "tagline": "Direct-to-Consumer Subscription",
        },
        "headline_kpis": [
            ("Sign-ups at Launch", "1.1M"),
            ("Subscribers by 2024", "~2.7M"),
        ],
        "context": "NFL · Digital Media &amp; NFL+",
        "year": "2019–2021",
        "role": "UX Researcher (study lead)",
        "methods": "Design Studios · MoSCoW sorting · Package ranking · National survey (N=2,208) · TURF analysis · MaxDiff · SPSS",
        "summary": "Formative research on the NFL’s first direct-to-consumer mobile subscription—NFL+, launched in 2022 to about 1.1M sign-ups and grew to roughly 2.7M subscribers heading into 2024.",
        "insight": "Features alone didn’t explain what fans would pay for—a measure of what motivates fans to subscribe explained why segments chose differently.",
        "stats": [
            ("1.1M", "NFL+ sign-ups in 2022", "scale"),
            ("~2.7M", "NFL+ subscribers heading into 2024", "scale"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>The NFL was preparing NFL+, its first direct-to-consumer mobile subscription, in a field that already included Club+, League Pass, Club Pass, and Mobile RedZone.</li>
<li>Before launch, product and media strategy needed evidence — not instinct — for how to package and price it.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Evaluate five different ways NFL+ could be packaged.</li>
<li>Explain why different fan segments preferred different packages, using a measure of what actually motivates fans to subscribe.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran Design Studios with 24 fans, using MoSCoW sorting (Must / Should / Could / Won’t Have) and package ranking both before and after fans saw the prices.</li>
<li>Fielded a national survey of 2,208 fans on the features they wanted and the competitor services they already used.</li>
<li>Analyzed which features had the broadest appeal (a TURF-style reach analysis) and what most motivated subscription (MaxDiff), all in SPSS.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>The research shaped the NFL’s first-ever mobile subscription. The packaging and pricing recommendations became the basis for the initial NFL+ offering.</li>
<li>It launched to about 1.1 million sign-ups in 2022 and grew to roughly 2.7 million subscribers heading into 2024.</li>
<li>It was a cross-team effort. The packaging blueprint was built in partnership with NFL Media and Product Strategy.</li>
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
        "short": "Tested Intel’s TrueView rotate-the-camera replay prototype with fans and delivered recommendations for how to integrate it into the NFL app and Game Pass.",
        "context": "NFL Labs · Partner research with Intel",
        "year": "2019–2021",
        "role": "UX Researcher (study lead)",
        "methods": "Design studios · Live-prototype testing · Behavioral observation",
        "summary": "Ran design studios on Intel’s TrueView rotate-the-camera replay prototype and delivered a clear read on fan appetite plus concrete recommendations for how an interactive replay should work in Game Pass and condensed-replay experiences.",
        "insight": "Perspective control earned its place when fans wanted to understand a play—not as a default for every highlight.",
        "video": {
            "src": "nfl-intel/trueview-prototype.mp4",
            "poster": "intel-trueview-poster.png",
            "caption": "The Intel TrueView prototype — rotate the camera around a recorded play. (Click to watch.)",
        },
        "stats": [],
        "sections": [
            (
                "Situation",
                """<ul>
<li>Intel’s TrueView prototype let fans rotate the camera all the way around a recorded play.</li>
<li>Before investing further in the partnership, NFL Labs needed a clear read on whether fans actually wanted this.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Put the working prototype in front of real fans and learn how they used it.</li>
<li>Turn what we learned into concrete product recommendations for both NFL Labs and Intel.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran design studios where fans tried the live TrueView prototype hands-on.</li>
<li>Captured the moments when controlling the camera angle genuinely helped — and the moments when a normal highlight was all fans wanted.</li>
<li>Translated those findings into recommendations for Game Pass and condensed-replay experiences.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>Answered whether fans actually wanted the feature. The study delivered a clear read on fan appetite, plus specific recommendations for how an interactive replay should work.</li>
<li>Gave both partners a shared starting point. NFL Labs and Intel came away with a common research basis for deciding their next steps together.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "verizon-superstadium",
        "num": "11",
        "brand": "nfl",
        "badge_label": "NFL Labs",
        "title": "Verizon 5G SuperStadium: The In-Stadium Fan Experience",
        "short": "Led usability and in-stadium field research on Verizon 5G’s SuperStadium experience—now built into the official NFL app and central to a $1B+ NFL–Verizon partnership.",
        "context": "NFL Labs · Verizon 5G partnership",
        "year": "2019–2021",
        "role": "UX Researcher (study lead)",
        "methods": "Cognitive task analysis · In-stadium field research · Immersive-AR prototype &amp; usability evaluation",
        "summary": "NFL Labs partnered with Verizon 5G to explore next-generation in-stadium fan engagement. I led usability and field research—cognitive task analysis plus in-stadium field observation at SoFi Stadium during an LA Rams game—that helped seed SuperStadium, now built into the official NFL app.",
        "insight": "In-stadium fans didn’t want a second screen—they wanted the stadium itself to become the interface.",
        "video": {
            "src": "nfl-intel/superstadium-demo.mp4",
            "poster": "nfl-intel/superstadium-poster.jpg",
            "caption": "SuperStadium — multi-angle views and Next Gen Stats AR overlays from your seat. (Click to watch.)",
        },
        "stats": [
            ("$1B+", "NFL–Verizon technology partnership", "revenue"),
            ("59.6%", "Super Bowl LX attendees connected to SuperStadium", "conversion"),
        ],
        "sections": [
            (
                "Situation",
                """<ul>
<li>NFL Labs wanted next-generation ways to deepen how fans engage during live games, especially inside the stadium.</li>
<li>Verizon’s 5G network made new experiences possible: real-time AR overlays and multi-angle viewing from your seat.</li>
</ul>""",
            ),
            (
                "Task",
                """<ul>
<li>Lead usability and field research on the Verizon-powered 5G, AR, and VR fan experiences built for in-stadium use.</li>
<li>Turn the findings into a concrete product direction NFL Labs could formalize with Verizon.</li>
</ul>""",
            ),
            (
                "Action",
                """<ul>
<li>Ran cognitive task analysis and in-stadium field research during live events — capturing real fan behavior at SoFi Stadium during an LA Rams game.</li>
<li>Ran prototype and usability testing on immersive AR hardware alongside Verizon’s innovation team.</li>
<li>Shaped the product direction: multi-angle live and replay views, Next Gen Stats AR overlays, and in-stadium navigation running over 5G Ultra Wideband.</li>
</ul>""",
            ),
            (
                "Result",
                """<ul>
<li>The research helped seed SuperStadium, which is now built into the official NFL app and sits at the center of a $1 billion-plus partnership between the NFL and Verizon.</li>
<li>Fans used it at the sport’s biggest event. At Super Bowl LX, 59.6% of attendees were actively connected to the SuperStadium experience.</li>
</ul>""",
            ),
        ],
    },
    {
        "slug": "insulin-pen-usability",
        "num": "12",
        "brand": "ipsos",
        "title": "Insulin Pen Usability: Turning Device Research Into Commercial Evidence",
        "short": "A pharma company needed defensible evidence of where its biosimilar insulin pen stood against market leaders. My multi-country comparative usability study reshaped device training and was linked to a 27% reduction in device-use errors.",
        "context": "Ipsos Healthcare · Medical Devices & Diabetes Research",
        "year": "2015–2017",
        "role": "UX Research Analyst (protocol author, moderator, analyst)",
        "timeline": "Multi-country study",
        "methods": "Comparative usability testing · Simulated-injection task protocol · In-person moderation · Cognitive debriefing · Video capture · Follow-up interviews",
        "summary": "A pharma company needed defensible evidence of where its biosimilar insulin pen stood against market leaders. My multi-country comparative usability study reshaped the device training protocol and was linked to a 27% reduction in device-use errors.",
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
<li>Moderated in-person usability sessions with patients and nurses recruited from a local clinic.</li>
<li>Participants performed simulated injections with each device in randomized order.</li>
<li>Captured performance data (task completion, whether injections were performed correctly, time on task) alongside structured preference ratings across handling, dose selection, dose reading, injection force, and confidence.</li>
<li>Filmed the sessions and conducted follow-up interviews to capture the reasoning behind participants’ ratings.</li>
<li>Analyzed the combined behavioral and attitudinal data.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>The main insight: how the device is taught matters as much as the device itself.</strong> The way patients and educators were trained turned out to be just as important as the pen’s design.</li>
<li><strong>The research changed how the device is taught — and that change was linked to fewer mistakes.</strong> After the training approach for educators and patients was reshaped based on the findings, device-use errors were about 27% lower and training took less time. (The study is linked to these improvements; it isn’t claiming to be the sole cause.)</li>
<li><strong>The recordings became marketing material.</strong> The filmed sessions and follow-up interviews were used to build the training and sales materials that pharmaceutical representatives and diabetes educators used in the field.</li>
<li><strong>The study gave the company evidence it could compare.</strong> It produced side-by-side results across patients and certified diabetes educators, supporting both launch messaging and the case for getting the device covered and paid for.</li>
<li>I ran the whole study: writing the plan, building the materials, moderating the sessions, filming, conducting the follow-up interviews, and analyzing the data.</li>
</ul>"""),
        ],
    },
]


def header(active=None, prefix="", brand=None, nav_active=None, body_classes=None):
    classes = []
    if brand:
        classes.append(f"brand-{brand}")
    if body_classes:
        classes.extend(body_classes)
    brand_class = f' class="{" ".join(classes)}"' if classes else ""
    title = "Sam Weinberger" if not active else f"{active} — Sam Weinberger"

    def nav_link(href, label, key):
        cls = ' class="is-active"' if nav_active == key else ""
        return f'<a href="{prefix}{href}"{cls}>{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="Samuel Weinberger — applied cognitive and social psychologist turned UX Engineer and Design Researcher. Bridging human behavior, analytics, and interactive design." />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
</head>
<body{brand_class}>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{prefix}index.html">Sam Weinberger</a>
      <nav class="nav" aria-label="Primary">
        {nav_link("case-studies.html", "Case studies", "cases")}
        {nav_link("skills.html", "Skills", "skills")}
        {nav_link("research-tools.html", "Tech Stack", "research-tools")}
        {nav_link("about.html", "About me", "about")}
        {nav_link("resume.html", "Resume", "resume")}
        {nav_link("education.html", "Education", "education")}
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
          <p>I’m an applied cognitive and social psychologist turned UX Engineer and Design Researcher. I specialize in bridging the gap between human behavior, advanced data analytics, and interactive design. My academic background—including graduate research focused on human motivation, persuasion, and systemic behavior change—serves as the foundation for how I approach product strategy.</p>
          <p>After starting my career in human factors and FDA-regulated medical device research, I stepped into the digital product space. I spent my early UX career at the NFL optimizing the Fantasy mobile app, and later spent four years at FanDuel helping build and scale one of the most successful sportsbooks on the market—including a quarterly product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard. Most recently, I joined Robinhood to focus on first-time user experience, customer acquisition, and retention within the rapid-fire world of event contracts and prediction markets.</p>
          <p>“UX Engineer” describes a modern hybrid role—and the engineering isn’t backend software. What I engineer is the research operation itself: automated pipelines that field studies in days instead of weeks, telemetry and dashboards that tie what users say to what they actually do, and interactive prototypes built mid-interview so ideas get tested the moment they surface. That infrastructure connects research to analytics, design, and product management, so insights arrive fast enough—and connected enough—to shape product strategy. Working across all four disciplines is what lets me tie every research effort directly to a business objective.</p>
          <p>By integrating generative AI and automated workflows into my practice, I’ve expanded my reach across product, design, and data science. Whether I am orchestrating end-to-end research operations, deploying automated quantitative surveys, or rapidly generating interactive, engineering-ready prototypes mid-interview, I focus on one thing: translating complex human behavior into massive product momentum.</p>
"""

RESUME_TITLE = "User Experience Research Engineer | AI-Driven Insights"

RESUME_CONTACT = {
    "phone": "(310) 529-7223",
    "phone_href": "tel:+13105297223",
    "location": "Los Angeles, CA",
    "email": "samuelcweinberger@gmail.com",
    "linkedin_label": "linkedin.com/in/samuelcweinberger",
    "linkedin_href": "https://www.linkedin.com/in/samuelcweinberger",
}

RESUME_EDUCATION = [
    {
        "name": "Claremont Graduate University",
        "dates": "2016–2020",
        "details": "Ph.D. Candidate in Cognitive &amp; Social Psychology · Master of Arts in Psychology, GPA 3.45",
    },
    {
        "name": "University of Southern California",
        "dates": "2008–2010",
        "details": "B.A. in Public Policy &amp; Evaluation, GPA 3.65",
    },
    {
        "name": "Stanford University",
        "dates": "2006–2008",
        "details": "Communications &amp; Media Studies, GPA 3.88",
    },
]

RESUME_ATHLETICS = (
    "Athletics: NCAA Division 1 Football (Stanford) · NCAA Division 1 Baseball (USC) · "
    "Team USA, Track Cycling"
)

# Flat, reverse-chronological list mirroring the "PROFESSIONAL EXPERIENCE" section of the
# source resume exactly — one entry per job (no earlier/later tiering, no nested roles).
RESUME_EXPERIENCE = [
    {
        "company": "Robinhood",
        "brand": "robinhood",
        "context": "Prediction Markets Team",
        "title": "Quantitative UX Researcher",
        "dates": "Feb 2026 – July 2026",
        "bullets": [
            (
                "Growth &amp; Expansion",
                'Combined in-depth interviews and behavioral segmentation to identify key factors limiting prediction market engagement. Designed and tested multifaceted solutions that drove an <a href="cases/diversify-single-category.html">11% increase in engagement in new markets</a>, accounting for ~24% of total trade volume.',
            ),
            (
                "Retention Strategy",
                'Diagnosed first-time-user friction outside company control that was driving 7–8 figure monthly losses from user abandonment; recommended a simple messaging strategy that reduced drop-off significantly, <a href="cases/first-trade-recovery.html">recovering ~$12M in monthly revenue</a> (70% of projected monthly losses).',
            ),
            (
                "AI Research Automation",
                'Programmed AI agents supporting UX workflows that produce engineering-ready prototypes, accelerating average research cycles from ~20–30 days to one week or less, improving project capacity 4×, and maximizing high-velocity <a href="case-studies.html#cases-robinhood">A/B testing</a>.',
            ),
        ],
    },
    {
        "company": "FanDuel Group",
        "brand": "fanduel",
        "context": "Core Products &amp; Experiences Team",
        "title": "Lead UX Researcher",
        "dates": "Jan 2024 – Feb 2026",
        "bullets": [
            (
                "Responsible Gaming",
                "Built and psychometrically validated a proprietary Responsible Gaming Sentiment Scale and the risk-prevention tools for users, raising the share of users that meet regulatory standards from 78% to 92%.",
            ),
            (
                "Wallet Optimization",
                "Diagnosed a 65% drop-off at wallet/banking setup via triangulated mixed-methods research (Amplitude funnel analysis, moderated interviews, large scale survey) generating ~$8M boost in handle from first-time deposits.",
            ),
            (
                "ACH Adoption",
                'Identified barriers and developed targeted messaging that <a href="cases/ach-adoption.html">improved ACH adoption from 20% to 32%</a>, reducing account takeovers from 7–8% to under 4%.',
            ),
            (
                "Cross-sell Conversion",
                "Drove ~150K new Sportsbook customers that generated a 7-figure increase in monthly revenue from solutions recommended to improve promotional offers (i.e., Bet $5 and Get $200).",
            ),
            (
                "Team Scaling",
                "Scaled UX Research from 2 to 32 researchers, delivering 200+ studies annually while directing AI-enabled research pipelines that cut project turnaround time 75%.",
            ),
        ],
    },
    {
        "company": "FanDuel Group",
        "brand": "fanduel",
        "context": "Core Products &amp; Experiences Team",
        "title": "Senior UX Researcher",
        "dates": "March 2021 – Dec 2023",
        "bullets": [
            (
                "Onboarding &amp; Acquisition",
                "Identified onboarding friction and developed messaging strategies that cut support tickets by 30% and reduced annual costs by $1.2M, helping grow the user base from 1.5M to +20M.",
            ),
            (
                "Benchmarking &amp; Competitive Analysis",
                'Architected a <a href="cases/benchmarking-decision-engine.html">continuous and automated measurement framework</a> (in-app pulse checks, competitive usability testing, behavioral event tracking via custom telemetry hooks), directly feeding into product road maps and feature development for Casino, Fantasy, Racing, and Sportsbook products.',
            ),
        ],
    },
    {
        "company": "NFL",
        "brand": "nfl",
        "context": "Fantasy App and NFL+ Team",
        "title": "Senior UX Researcher",
        "dates": "Jan 2019 – April 2021",
        "bullets": [
            (
                "Fantasy+ Tools",
                'Led generative and formative research on a small cross-functional team to develop and test in-app features that shipped — <a href="cases/fantasy-d2c-ideation.html">converting 45% of users and generating $920K in revenue</a>.',
            ),
            (
                "NFL+ Pricing &amp; Packaging",
                'Evaluated the league\'s first direct-to-consumer mobile subscription and made recommendations that resulted in <a href="cases/nfl-d2c-packaging.html">+1M sign-ups after initial launch</a>.',
            ),
            (
                "Intel TrueView",
                'Delivered integration and monetization recommendations for the NFL app / Game Pass highlights, giving <a href="cases/intel-trueview.html">NFL Labs and Intel a shared research basis</a> for the next phase of the partnership.',
            ),
            (
                "Verizon 5G SuperStadium",
                'Directed usability and in-stadium field research connecting Intel technology and 5G Ultra Wideband, generating recommendations that <a href="cases/verizon-superstadium.html">supported the development of NFL\'s VIP Fan Experience</a>.',
            ),
        ],
    },
    {
        "company": "Claremont Graduate University",
        "brand": "cgu",
        "context": "",
        "title": "Grant Writer and Research Associate",
        "dates": "Jan 2017 – Sept 2019",
        "bullets": [
            (
                "Grant Funding &amp; Execution",
                "Awarded $200K in institutional grant funding to develop and evaluate mobile health (mHealth) artifacts and cross-platform applications focused on chronic disease tracking and preventative lifestyle behavior change.",
            ),
        ],
    },
    {
        "company": "Ipsos Healthcare",
        "brand": "ipsos",
        "context": "",
        "title": "User Experience Analyst",
        "dates": "May 2016 – September 2017",
        "bullets": [
            (
                "Medical Device Usability",
                'Authored the research protocol and ran end-to-end <a href="cases/insulin-pen-usability.html">comparative usability testing of a biosimilar insulin pen</a> with patients and clinic nurses — moderating simulated-injection sessions, filming, and analyzing behavioral and preference data.',
            ),
            (
                "Research-to-Commercial Impact",
                "Reshaped the device education protocol for diabetes educators and patients — a change associated with a 27% reduction in device-use errors and improved training time — and turned session footage into field materials used by pharmaceutical reps and educators.",
            ),
        ],
    },
]

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

TOOL_ICONS = {
    "Amplitude": "amplitude.png",
    "Claude Code": "claude-code.svg",
    "Coda": "coda.svg",
    "Confluence": "confluence.svg",
    "Contentful": "contentful.svg",
    "Cursor": "cursor.svg",
    "Displayr": "displayr.png",
    "FigJam": "figjam.svg",
    "Figma": "figma.svg",
    "GitHub": "github.svg",
    "Glean": "glean.png",
    "Great Question": "great-question.png",
    "Jira": "jira.svg",
    "Listen": "listen.png",
    "Lucid": "lucid.svg",
    "Miro": "miro.svg",
    "Notion": "notion.svg",
    "Python": "python.svg",
    "Qualtrics": "qualtrics.svg",
    "Quantilope": "quantilope.png",
    "Quantum Metric": "quantum-metric.png",
    "R": "r.svg",
    "Salesforce": "salesforce.svg",
    "SAS": "sas.svg",
    "Slack": "slack.svg",
    "SPSS": "spss.svg",
    "SQL": "sql.svg",
    "StatSig": "statsig.png",
    "UserTesting": "usertesting.png",
    # Major Oak, RedOak, and Coder RDE are internal/proprietary tools with
    # no public brand marks, so they intentionally have no icon entry here.
}

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
        "Coder RDE",
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
        ("ipsos", "Ipsos Healthcare"),
        ("burkmont", "Burkmont Analytics · Phoenix Suns"),
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
        <p class="hero-role">UX Engineer and Design Researcher</p>
        <p class="hero-lede">Applied Cognitive and Social Psychologist with 9+ years of mixed-methods research across fintech, sports media, and healthcare—connecting usability, field research, and AI-augmented workflows to product and revenue outcomes.</p>
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
          <p>Twelve studies across Robinhood, FanDuel, Ipsos Healthcare, and the NFL—each tied to a shipped product decision and a measured outcome.</p>
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
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "skills.html").write_text(html)


def write_research_tools_page():
    tiles = []
    for tool in RESEARCH_TOOLS:
        icon_file = TOOL_ICONS.get(tool)
        if icon_file:
            icon_html = (
                f'<span class="tool-icon-swatch">'
                f'<img src="media/tool-icons/{icon_file}" alt="{tool} logo" loading="lazy" />'
                f"</span>"
            )
        else:
            initial = tool[0]
            icon_html = f'<span class="tool-icon-fallback" aria-hidden="true">{initial}</span>'
        tiles.append(
            f"""          <li class="tool-icon-tile">
            {icon_html}
            <span class="tool-icon-name">{tool}</span>
          </li>"""
        )
    tools = "\n".join(tiles)
    html = (
        header(active="Tech Stack", nav_active="research-tools")
        + f"""
  <main>
    <section class="section page-section" id="research-tools">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Tech Stack</h2>
          <p>Platforms and languages I use across survey, analytics, experimentation, collaboration, and analysis.</p>
        </div>
        <ul class="tool-icon-grid reveal">
{tools}
        </ul>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "research-tools.html").write_text(html)


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


def write_resume_page():
    def bullets_html(bullets):
        items = "\n".join(
            f"""            <li>
              <strong>{label}</strong>
              <span>{desc}</span>
            </li>"""
            for label, desc in bullets
        )
        return f"""          <ul class="skills-list resume-bullets">
{items}
          </ul>"""

    contact_items = [
        f'<a href="{RESUME_CONTACT["phone_href"]}">{RESUME_CONTACT["phone"]}</a>',
        f'<span>{RESUME_CONTACT["location"]}</span>',
        f'<a href="mailto:{RESUME_CONTACT["email"]}">{RESUME_CONTACT["email"]}</a>',
        f'<a href="{RESUME_CONTACT["linkedin_href"]}" target="_blank" rel="noopener">{RESUME_CONTACT["linkedin_label"]}</a>',
    ]
    contact_html = f'<span class="case-meta-dot" aria-hidden="true">·</span>\n          '.join(
        contact_items
    )

    job_blocks = []
    for job in RESUME_EXPERIENCE:
        context_html = (
            f'<span class="resume-context">{job["context"]}</span>' if job.get("context") else ""
        )
        job_blocks.append(
            f"""        <section class="resume-job company-{job['brand']} reveal">
          <div class="resume-job-head">
            <h3 class="company-heading">{job['company']}</h3>
            {context_html}
          </div>
          <div class="resume-role">
            <div class="resume-role-head">
              <h4>{job['title']}</h4>
              <span class="resume-dates">{job['dates']}</span>
            </div>
{bullets_html(job['bullets'])}
          </div>
        </section>"""
        )

    html = (
        header(active="Resume", nav_active="resume")
        + f"""
  <main>
    <section class="section page-section resume-page" id="resume">
      <div class="wrap">
        <div class="resume-header reveal">
          <div>
            <h1 class="resume-name">Sam Weinberger</h1>
            <p class="resume-title">{RESUME_TITLE}</p>
            <p class="resume-contact">
          {contact_html}
            </p>
          </div>
          <div class="resume-actions">
            <a class="btn btn-ghost" href="education.html">View education</a>
            <a class="btn btn-ghost" href="skills.html">View skills</a>
            <a class="btn btn-ghost" href="mailto:{RESUME_CONTACT['email']}">Email me</a>
            <button type="button" class="btn btn-primary" data-print>Print / Save as PDF</button>
          </div>
        </div>

        <div class="section-head reveal">
          <h2>Professional experience</h2>
        </div>
        <div class="resume-jobs">
{chr(10).join(job_blocks)}
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "resume.html").write_text(html)


def write_education_page():
    education_rows = "\n".join(
        f"""          <li>
            <div class="resume-role-head">
              <h4>{edu['name']}</h4>
              <span class="resume-dates">{edu['dates']}</span>
            </div>
            <p>{edu['details']}</p>
          </li>"""
        for edu in RESUME_EDUCATION
    )
    html = (
        header(active="Education", nav_active="education")
        + f"""
  <main>
    <section class="section page-section resume-page" id="education">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Education</h2>
          <p>Graduate and undergraduate study in cognitive and social psychology, public policy, and communications—alongside a Division 1 and international athletics background.</p>
        </div>
        <ul class="resume-earlier reveal">
{education_rows}
        </ul>
        <p class="resume-athletics reveal">{RESUME_ATHLETICS}</p>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "education.html").write_text(html)


def render_nfl_media(case):
    """Reference-style framed media player for NFL case pages.

    Video cases render a poster + big centered play button that opens the
    click-to-play video (reusing the shared [data-video-click] JS handler).
    Image cases render the same white-framed box without a play button.
    When no media exists a tasteful placeholder is shown instead.
    """
    card = case.get("brand_card")
    if card:
        tagline = card.get("tagline", "")
        tagline_html = (
            f'<span class="case-nfl-brandcard-tagline">{tagline}</span>'
            if tagline
            else ""
        )
        divider_html = (
            '<span class="case-nfl-brandcard-divider" aria-hidden="true"></span>'
            if tagline
            else ""
        )
        return f"""      <figure class="case-nfl-media case-nfl-brandcard reveal">
        <div class="case-nfl-media-frame case-nfl-brandcard-frame">
          <span class="case-nfl-brandcard-facet" aria-hidden="true"></span>
          <div class="case-nfl-brandcard-inner">
            <img class="case-nfl-brandcard-logo" src="../media/{card['logo']}" alt="{card.get('logo_alt', '')}" />
            {divider_html}
            {tagline_html}
          </div>
        </div>
      </figure>"""

    v = case.get("video")
    if v:
        poster = v.get("poster")
        poster_src = f"../media/{poster}" if poster else ""
        poster_img = (
            f'<img class="video-click-poster" src="{poster_src}" alt="" loading="lazy" />'
            if poster
            else ""
        )
        vtype = v.get("type", "video/mp4")
        poster_attr = f' poster="{poster_src}"' if poster else ""
        caption = v.get("caption", "")
        cap_html = (
            f'<figcaption class="case-nfl-media-caption">{caption}</figcaption>'
            if caption
            else ""
        )
        return f"""      <figure class="case-nfl-media case-nfl-video reveal">
        <div class="case-nfl-media-frame video-click-frame" data-video-click>
          {poster_img}
          <video class="video-click-el" playsinline preload="none"{poster_attr} hidden>
            <source src="../media/{v['src']}" type="{vtype}" />
            Your browser does not support the video tag.
          </video>
          <button type="button" class="video-click-cta case-nfl-play" aria-label="Play video">
            <span class="case-nfl-play-icon" aria-hidden="true">&#9654;</span>
          </button>
        </div>
        {cap_html}
      </figure>"""

    img = case.get("media_image")
    if img:
        cap = img.get("caption", "")
        cap_html = (
            f'<figcaption class="case-nfl-media-caption">{cap}</figcaption>'
            if cap
            else ""
        )
        return f"""      <figure class="case-nfl-media case-nfl-image reveal">
        <div class="case-nfl-media-frame">
          <img class="case-nfl-media-img" src="../media/{img['src']}" alt="{img.get('alt', '')}" loading="lazy" />
        </div>
        {cap_html}
      </figure>"""

    return """      <figure class="case-nfl-media case-nfl-image reveal">
        <div class="case-nfl-media-frame case-nfl-media-placeholder">
          <span class="case-nfl-placeholder-text">Image coming soon</span>
        </div>
      </figure>"""


def render_nfl_gallery(case):
    """Render additional framed product screenshots for an NFL case.

    Each entry in ``media_gallery`` is either a single image (src/alt/caption)
    rendered in the standard white NFL frame, or a grouped row
    ({"row": [imgs], "caption": ...}) rendered as a side-by-side strip that
    shares one caption. This lets NFL cases keep their brand_card/video hero
    while still surfacing the source document's embedded screenshots.
    """
    gallery = case.get("media_gallery")
    if not gallery:
        return ""
    figs = []
    for item in gallery:
        caption = item.get("caption", "")
        cap_html = (
            f'<figcaption class="case-nfl-media-caption">{caption}</figcaption>'
            if caption
            else ""
        )
        if "row" in item:
            imgs = "\n".join(
                f'            <img class="case-nfl-gallery-img" src="../media/{im["src"]}" alt="{im.get("alt", "")}" loading="lazy" />'
                for im in item["row"]
            )
            figs.append(
                f"""      <figure class="case-nfl-media case-nfl-gallery-row reveal">
        <div class="case-nfl-gallery-strip">
{imgs}
        </div>
        {cap_html}
      </figure>"""
            )
        else:
            figs.append(
                f"""      <figure class="case-nfl-media case-nfl-image reveal">
        <div class="case-nfl-media-frame">
          <img class="case-nfl-media-img" src="../media/{item['src']}" alt="{item.get('alt', '')}" loading="lazy" />
        </div>
        {cap_html}
      </figure>"""
            )
    return "\n".join(figs)


def write_case_nfl(case, index):
    """Render an NFL case page using the blue geometric reference layout."""
    prev_c = CASES[index - 1] if index > 0 else None
    next_c = CASES[index + 1] if index < len(CASES) - 1 else None

    badge = product_badge(
        case["brand"], prefix="../", label_override=case.get("badge_label")
    )
    subtitle_html = (
        f'<p class="case-nfl-subtitle">{case["subtitle"]}</p>'
        if case.get("subtitle")
        else ""
    )
    insight_html = (
        f'<p class="case-nfl-insight">{case["insight"]}</p>' if case.get("insight") else ""
    )

    headline_html = ""
    if case.get("headline_kpis"):
        items = "\n".join(
            f"""            <div class="case-nfl-metric">
              <span class="case-nfl-metric-value">{value}</span>
              <span class="case-nfl-metric-label">{label}</span>
            </div>"""
            for label, value in case["headline_kpis"]
        )
        headline_html = f"""          <div class="case-nfl-metrics" aria-label="Headline results">
{items}
          </div>"""

    section_blocks = []
    for title, body in case["sections"]:
        section_blocks.append(
            f"""          <div class="case-nfl-block">
            <h2 class="case-nfl-lead">{title}</h2>
            <div class="case-nfl-block-body">{body}</div>
          </div>"""
        )

    brief_rows = []
    for key, label in (("role", "Role"), ("timeline", "Timeline"), ("methods", "Methods")):
        if case.get(key):
            brief_rows.append((label, case[key]))
    brief_html = ""
    if brief_rows:
        items = "\n".join(
            f"""            <div class="case-nfl-brief-item">
              <dt>{label}</dt>
              <dd>{value}</dd>
            </div>"""
            for label, value in brief_rows
        )
        brief_html = f"""          <dl class="case-nfl-brief">
{items}
          </dl>"""

    meta_html = f"""          <div class="case-nfl-meta">
            <span>{case['context']}</span>
            <span class="case-meta-dot" aria-hidden="true">·</span>
            <span>{case['year']}</span>
          </div>
{brief_html}"""

    stats_html = ""
    if case.get("stats"):
        normalized = [normalize_stat(s) for s in case["stats"]]
        cells = "\n".join(
            f"""          <div class="case-nfl-stat case-nfl-stat--{k}">
            <span class="case-nfl-stat-value">{v}</span>
            <span class="case-nfl-stat-label">{l}</span>
          </div>"""
            for v, l, k in normalized
        )
        stats_html = f"""      <div class="case-nfl-stats reveal" aria-label="Key outcomes">
{cells}
      </div>"""

    media_html = render_nfl_media(case)
    gallery_html = render_nfl_gallery(case)

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

    html = (
        header(
            active=case["title"],
            prefix="../",
            brand=case["brand"],
            nav_active="cases",
            body_classes=["case-nfl"],
        )
        + f"""
  <main class="case-page case-nfl-page">
    <div class="wrap case-nfl-wrap">
      <div class="crumb"><a href="../case-studies.html">Case studies</a> <span aria-hidden="true">/</span> {case['num']}</div>
      <div class="case-nfl-grid">
        <div class="case-nfl-left reveal">
          {badge}
          <h1 class="case-nfl-title">{case['title']}</h1>
          <span class="case-nfl-underline" aria-hidden="true"></span>
          {subtitle_html}
          <div class="case-nfl-box">
            {insight_html}
{headline_html}
{chr(10).join(section_blocks)}
{meta_html}
          </div>
        </div>
        <div class="case-nfl-right">
{media_html}
{gallery_html}
{stats_html}
        </div>
      </div>
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


def write_case(case, index):
    if case["brand"] == "nfl":
        write_case_nfl(case, index)
        return
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

    rail_parts = []
    if case.get("images"):
        imgs = case["images"]
        n = len(imgs)
        slides = []
        for idx, im in enumerate(imgs):
            alt = im.get("alt", "")
            cap = im.get("caption", "")
            active = " is-active" if idx == 0 else ""
            slides.append(
                f'            <img class="carousel-slide{active}" src="../media/{im["src"]}" alt="{alt}" data-caption="{cap}" loading="lazy" />'
            )
        controls_html = ""
        if n > 1:
            controls_html = f"""
          <div class="carousel-controls">
            <button type="button" class="carousel-btn" data-carousel-prev aria-label="Previous image">&#8249;</button>
            <span class="carousel-count"><span data-carousel-current>1</span> / {n}</span>
            <button type="button" class="carousel-btn" data-carousel-next aria-label="Next image">&#8250;</button>
          </div>"""
        first_cap = imgs[0].get("caption", "")
        img_caption_html = (
            f'\n          <figcaption class="carousel-caption" data-carousel-caption>{first_cap}</figcaption>'
            if any(im.get("caption") for im in imgs)
            else ""
        )
        rail_parts.append(
            f"""        <figure class="image-carousel reveal" data-carousel>
          <div class="carousel-stack">
{chr(10).join(slides)}
          </div>{controls_html}{img_caption_html}
        </figure>"""
        )
    if case.get("video"):
        v = case["video"]
        vtype = v.get("type", "video/mp4")
        poster = v.get("poster")
        poster_attr = f' poster="../media/{poster}"' if poster else ""
        caption = v.get("caption", "")
        vid_caption_html = (
            f'<figcaption class="video-loop-caption">{caption}</figcaption>'
            if caption
            else ""
        )
        if v.get("mode") == "click":
            cta_label = v.get("cta", "Click to watch video")
            poster_src = f'../media/{poster}' if poster else ""
            poster_img = (
                f'<img class="video-click-poster" src="{poster_src}" alt="" loading="lazy" />'
                if poster
                else ""
            )
            rail_parts.append(
                f"""        <figure class="video-click reveal">
          <div class="video-click-frame" data-video-click>
            {poster_img}
            <video class="video-click-el" playsinline preload="none"{poster_attr} hidden>
              <source src="../media/{v['src']}" type="{vtype}" />
              Your browser does not support the video tag.
            </video>
            <button type="button" class="video-click-cta" aria-label="{cta_label}">
              <span class="video-click-cta-icon" aria-hidden="true">&#9654;</span>
              <span>{cta_label}</span>
            </button>
          </div>
          {vid_caption_html}
        </figure>"""
            )
        else:
            rail_parts.append(
                f"""        <figure class="video-loop reveal">
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
          {vid_caption_html}
        </figure>"""
            )
    video_rail_html = ""
    if rail_parts:
        video_rail_html = (
            '      <aside class="case-media-rail">\n'
            + "\n".join(rail_parts)
            + "\n      </aside>"
        )

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
    write_research_tools_page()
    write_about_page()
    write_resume_page()
    write_education_page()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote home + section pages + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
