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

# Official brand marks (SVG) sourced into media/brands/. Rendered on a light
# "chip" so trademarked marks stay crisp and legible on the dark theme.
BRAND_LOGOS = {
    "robinhood": "brands/robinhood-official.svg",
    "fanduel": "brands/fanduel-official.svg",
    "nfl": "brands/nfl-official.svg",
    "ipsos": "brands/ipsos-official.svg",
    "intel": "brands/intel-official.svg",
    "verizon": "brands/verizon-official.svg",
    "usc": "brands/usc-trojans.svg",
    "stanford": "brands/stanford-cardinal.svg",
}


def brand_logo_chip(brand_key, prefix="", label=None, extra_class=""):
    """Official brand mark inside a light chip (crisp on the dark theme)."""
    logo = BRAND_LOGOS.get(brand_key)
    if not logo:
        return ""
    alt = label or BRANDS.get(brand_key, {}).get("label", brand_key)
    cls = f"brand-chip brand-chip-{brand_key}"
    if extra_class:
        cls += f" {extra_class}"
    return (
        f'<span class="{cls}">'
        f'<img src="{prefix}media/{logo}" alt="{alt} logo" loading="lazy" decoding="async" />'
        f"</span>"
    )

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
        "short": "Approved traders kept signing up for prediction markets but never placed a first trade—matched interviews traced it to findability on the home page, and five low-effort design changes brought hundreds of thousands of stalled customers back to a first trade.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "~1 week (vs. typical 3–4 weeks)",
        "methods": "AI-moderated interviews (Listen Labs) · Matched converter/non-converter design · Funnel analysis · Claude/Python/SQL deep dive",
        "summary": "A large group of approved customers went through every step to trade event contracts, then never placed a first trade. A one-week matched study showed the barrier was findability on the home page—and five low-effort changes brought hundreds of thousands of stalled customers back to a first trade.",
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
<li>Recruited both groups from a large internal list — all active futures, crypto, and stock traders.</li>
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
<li><strong>Half the stalled group finally traded.</strong> Of the hundreds of thousands of approved customers who had never traded, roughly half placed their first trade after the changes shipped.</li>
<li><strong>More people traded in the same sitting they signed up — a roughly nine-point lift.</strong> The company wanted customers to place their first trade in the same session they got approved, without leaving the app and coming back. (This measure counts only people who finish in one sitting, which usually takes a few minutes; it excludes new customers who need a manual review first.) This mattered because customers who trade in that first sitting go on to trade about 15% more than those who don’t.</li>
<li><strong>Nearly everyone who traded within a day did so quickly — roughly 9 in 10.</strong> A second measure looked at customers who placed a first trade within 24 hours of being approved; nearly all of them did. The 24-hour mark mattered because separate research showed that customers who trade within a day stay more engaged over time than those who take longer.</li>
</ul>"""),
        ],
    },
    {
        "slug": "first-trade-recovery",
        "num": "02",
        "brand": "robinhood",
        "title": "Turning a Dead End Into a Second Chance",
        "short": "A backend failure the company couldn’t fix was silently churning 1 in 5 first-time traders. Redesigning the moment around the error—a plain-language message and a path back to the trade—won back 6 of every 10 at-risk users and roughly 70% of the revenue that had been at risk.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Interview → data diagnosis → shipped fix",
        "methods": "In-depth interviews · Python/SQL prevalence analysis · Churn analysis · Message design with content partners",
        "summary": "A backend failure the company couldn’t control was silently churning 1 in 5 first-time traders. Redesigning the moment around the error—with no engineering fix or spend—kept 6 of every 10 at-risk users and recovered most of the revenue that had been at risk.",
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
<li>Used Python and SQL to diagnose prevalence across the first-trade funnel, confirming it affected 1 in 5 first-time users and was a major driver of onboarding abandonment and substantial monthly revenue loss.</li>
<li>Identified a rare and valuable population: the ~10% of affected users who returned and tried again despite the failure.</li>
<li>Interviewed that group specifically — asking what would have prevented everyone else from dropping off for good.</li>
<li>Their answer was consistent and specific: a brief explanation of what happened, plus a CTA that kept them inside the app and returned them to the event they’d been trying to trade.</li>
<li>Worked with content partners to design that messaging: a plain-language explanation of the failure and a recovery path straight back into the trade funnel.</li>
</ul>"""),
            ("Result", """<ul>
<li><strong>The problem was a failure the company couldn’t fix, and it was costing real money every month.</strong> New customers were hitting a technical error the company had no control over, and most of them left for good. The lost business was substantial — a revenue leak, not a rounding error.</li>
<li><strong>The fix was a simple message, not an engineering change.</strong> I recommended showing customers a short, plain explanation of what went wrong, plus a button that took them straight back to the event they’d been trying to trade — instead of leaving them stuck on a blank screen with no way forward.</li>
<li><strong>Far fewer people gave up.</strong> Before, about 9 out of 10 customers who hit the error abandoned the app. After the change, that dropped to about 3 out of 10 — meaning 6 of every 10 customers who would have been lost were kept.</li>
<li>This recovered roughly 70% of the revenue the company had been on track to lose each month.</li>
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
        "short": "Most users traded a single category, mostly sports. The real blocker wasn’t risk or knowledge but confidence—new decision tools (a limit order and a chart Tool Tip) made trying a new category feel informed and lifted multi-category trading 11%.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (study lead)",
        "timeline": "Follow-on deep dive",
        "methods": "In-depth interviews · Behavioral segmentation · Scenario-based probing · Usability testing · Concept testing · Competitive analysis · Prototyping (Figma)",
        "summary": "Single-category traders wouldn’t diversify because unfamiliar categories felt like a coin toss. Surfacing tools that were already in the app—a limit order and a chart Tool Tip—made trying a new category feel informed and lifted the share of multi-category traders 11%.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Previous research showed a large majority of users traded a single prediction-market category, overwhelmingly sports.</li>
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
<li><strong>Point users to the limit order.</strong> The limit order lets a trader set the price they’re willing to pay instead of taking whatever the market offers, but it was buried deep in the order form and few users ever reached it. After it was surfaced and added to the order form, limit orders became a meaningful share of all trading volume within two weeks.</li>
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
        "short": "A personalization algorithm looked like a win (+4% in its A/B test) but trade volume had plateaued. Re-analysis showed it couldn’t cold-start new users; the fixes I recommended cut post-first-trade drop-off by nearly a third.",
        "context": "Robinhood · Prediction Markets & Event Contracts",
        "year": "2026",
        "role": "UX Researcher (investigation lead)",
        "timeline": "Multi-week deep dive",
        "methods": "Behavioral segmentation · AI-moderated interviews · Factorial ANOVA (arm × segment) · Matched-sample analysis · Prototyping (Cursor · GitHub · Figma · Python)",
        "summary": "A personalization algorithm looked like a win (+4% in its A/B test), yet trade volume had plateaued. My re-analysis showed it couldn’t cold-start new users, and the fixes I recommended cut post-first-trade drop-off by nearly a third.",
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
<li>Preliminary analysis surfaced the risk immediately: a large majority of the base traded sports contracts only.</li>
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
<li><strong>The Watch List cut drop-off after a first trade.</strong> In the control group (no Watch List), more than half of users dropped off after placing a trade; with the Watch List, drop-off after a first trade fell by nearly a third.</li>
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
        "short": "More than half of prospective customers abandoned registration on every state launch, and they couldn’t be recruited. A simulated-app study localized the drop and a reordered flow lifted production completion by roughly a third.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2021–2023",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (simulation → A/B → production)",
        "methods": "Simulated-app experiment · Step-by-step intention measurement · Third-party panel recruitment · A/B testing · Behavioral theory (foot-in-the-door)",
        "summary": "More than half of prospective FanDuel customers abandoned registration on every state launch—and they couldn’t be recruited to study. A simulated-app experiment localized the drop, and reordering when SSN and banking are asked lifted production completion by roughly a third.",
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
<li><strong>The same fix worked just as well with real customers.</strong> Once the reordered flow went live, production completion climbed by roughly a third.</li>
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
        "short": "Customers avoided ACH—the safer deposit method—because bank numbers felt least secure. Reframing the message (not adding incentives) roughly doubled ACH adoption, draining a costly football-Sunday debit exploit.",
        "context": "FanDuel · Core Products & Experiences",
        "year": "2024–2026",
        "role": "UX Researcher (study lead)",
        "timeline": "Multi-phase (research → A/B → production)",
        "methods": "In-depth interviews · A/B message testing · Behavioral + sentiment pairing · Cross-functional work with content design",
        "summary": "Customers avoided ACH—the safer deposit method—because entering bank numbers felt least secure. Reframing the message rather than adding incentives roughly doubled ACH adoption, draining a costly football-Sunday debit exploit.",
        "stats": [],
        "sections": [
            ("Situation", """<ul>
<li>Customers frequently deposited via debit card on Sundays during football, when banks were closed.</li>
<li>Their other pending transactions hadn’t posted yet — so accounts looked funded when they weren’t.</li>
<li>Bets settled the next day as those transactions cleared, sometimes leaving the bank unable to transfer funds.</li>
<li>If the customer had lost, they were left with a negative balance many never repaid.</li>
<li>This cost the company directly and incentivized fraud, with bad actors opening new accounts under others’ information to keep exploiting the gap.</li>
<li>ACH deposits — tied to a verifiable bank balance — would close it, but adoption remained stubbornly low.</li>
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
<li><strong>Roughly twice as many customers started using bank transfers.</strong> Adoption of ACH (paying directly from a bank account) roughly doubled after the reframed messaging shipped.</li>
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
        "short": "Developed and shipped Fantasy features available via in-app purchase—nearly $1M in first-year revenue, most of it in launch week, bought by more than a million players (nearly half of active users).",
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
            ("First-Year Revenue", "~$1M"),
            ("Active Users Who Bought", "1M+ (nearly half)"),
        ],
        "context": "NFL · NFL Fantasy App · Fantasy Sports",
        "year": "2019–2021",
        "role": "UX Researcher (study lead) · 5-person cross-functional team (2 designers, 1 researcher, 1 PM, 1 engineer)",
        "methods": "In-depth interviews · Large-scale survey · MaxDiff · Design-thinking · Static-concept testing · A/B testing",
        "summary": "Developed and shipped Fantasy features sold via in-app purchase—nearly $1M in first-year revenue with most of it landing in launch week, bought by more than a million players (nearly half of active users), and later folded into NFL+.",
        "insight": "Fans would pay to win their league—as long as paying never changed the game itself.",
        "stats": [
            ("~$1M", "Direct-to-consumer revenue in year one", "revenue"),
            ("1M+", "Active Fantasy users who bought the Tools Package — nearly half of actives", "scale"),
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
<li>The Tools Package sold immediately — most of its first-year revenue landed in launch week.</li>
<li>It approached $1M in revenue in year one, bought by more than a million players — nearly half of active users.</li>
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
            ("~60%", "Super Bowl LX attendees connected to SuperStadium", "conversion"),
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
<li>Fans used it at the sport’s biggest event. At Super Bowl LX, roughly 60% of attendees were actively connected to the SuperStadium experience.</li>
</ul>""",
            ),
        ],
    },
]


SITE_URL = "https://samuelcweinberger-web.github.io/Case-Studies/"

DEFAULT_DESCRIPTION = (
    "Samuel Weinberger — applied cognitive and social psychologist turned UX Design "
    "Researcher and Research Engineer. Bridging human behavior, analytics, and "
    "interactive design."
)

FONTS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Inter:opsz,wght@14..32,400..750"
    "&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500"
    "&display=swap"
)

# Inline (pre-paint) theme resolution so the light theme never flashes dark
# and vice versa. Stored choice wins; otherwise follow prefers-color-scheme.
THEME_SCRIPT = (
    "(function(){try{var t=localStorage.getItem('theme');"
    "if(t!=='light'&&t!=='dark'){t=window.matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';}"
    "document.documentElement.setAttribute('data-theme',t);}catch(e){}})();"
)

SUN_ICON = (
    '<svg class="theme-icon theme-icon-sun" viewBox="0 0 24 24" width="16" height="16" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="4.4"/>'
    '<path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7"/>'
    "</svg>"
)

MOON_ICON = (
    '<svg class="theme-icon theme-icon-moon" viewBox="0 0 24 24" width="16" height="16" '
    'fill="currentColor" aria-hidden="true">'
    '<path d="M20.6 14.6A8.7 8.7 0 0 1 9.4 3.4a8.7 8.7 0 1 0 11.2 11.2z"/>'
    "</svg>"
)


def _meta_escape(text):
    return text.replace("&", "&amp;").replace('"', "&quot;")


def header(active=None, prefix="", brand=None, nav_active=None, body_classes=None,
           page_path="", description=None):
    classes = []
    if brand:
        classes.append(f"brand-{brand}")
    if body_classes:
        classes.extend(body_classes)
    brand_class = f' class="{" ".join(classes)}"' if classes else ""
    title = "Sam Weinberger" if not active else f"{active} — Sam Weinberger"
    desc = _meta_escape(description or DEFAULT_DESCRIPTION)
    og_title = _meta_escape(title)
    og_url = f"{SITE_URL}{page_path}"
    og_image = f"{SITE_URL}media/og-card.png"

    def nav_link(href, label, key):
        cls = ' class="is-active"' if nav_active == key else ""
        return f'<a href="{prefix}{href}"{cls}>{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="color-scheme" content="dark light" />
  <script>{THEME_SCRIPT}</script>
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Sam Weinberger" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{og_url}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{og_image}" />
  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="{prefix}favicon.png" type="image/png" sizes="64x64" />
  <link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="{FONTS_URL}" />
  <link rel="stylesheet" href="{FONTS_URL}" />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
</head>
<body{brand_class}>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{prefix}index.html">Sam Weinberger</a>
      <nav class="nav" aria-label="Primary">
        {nav_link("about.html", "About me", "about")}
        {nav_link("resume.html", "Professional Experience", "resume")}
        {nav_link("case-studies.html", "Case studies", "cases")}
        {nav_link("media.html", "Media", "media")}
        {nav_link("research-tools.html", "Tech Stack", "research-tools")}
        {nav_link("skills.html", "Skills", "skills")}
        {nav_link("education.html", "Education", "education")}
        {nav_link("contact.html", "Contact", "contact")}
        <button type="button" class="theme-toggle" data-theme-toggle aria-label="Switch between dark and light theme">
          {SUN_ICON}
          {MOON_ICON}
        </button>
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
          <p>I’m an applied cognitive and social psychologist turned UX Design Researcher and Research Engineer. My graduate work in human motivation, persuasion, and behavior change is the foundation for how I approach product strategy—bridging human behavior, data analytics, and interactive design. From FDA-regulated medical device research to the NFL Fantasy app, four years scaling FanDuel’s sportsbook, and now Robinhood’s prediction markets, I’ve run mixed-methods research across healthcare, sports media, and fintech—always tying insights to product and revenue outcomes.</p>
          <p>The “engineering” in my title isn’t backend software; it’s the research operation itself. I build automated pipelines that field studies in days, telemetry and dashboards that connect what users say to what they actually do, and interactive prototypes built mid-interview—increasingly augmented by generative AI. That infrastructure links research to analytics, design, and product, so insights arrive fast enough to shape strategy and turn complex human behavior into product momentum.</p>
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
        "details": "Ph.D., Cognitive &amp; Social Psychology (ABD) · Master of Arts in Psychology, GPA 3.45",
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

RESUME_ATHLETICS = [
    {"brand": "stanford", "label": "Stanford Cardinal", "text": "Division 1 Football — Linebacker"},
    {"brand": "usc", "label": "USC Trojans", "text": "Division 1 Baseball — Pitcher"},
]

# Flat, reverse-chronological list mirroring the "PROFESSIONAL EXPERIENCE" section of the
# source resume exactly — one entry per job (no earlier/later tiering, no nested roles).
RESUME_EXPERIENCE = [
    {
        "company": "Robinhood",
        "brand": "robinhood",
        "context": "Prediction Markets Team",
        "title": "User Experience Research Engineer",
        "dates": "Feb 2026 – July 2026",
        "bullets": [
            (
                "Growth &amp; Expansion",
                'Combined in-depth interviews and behavioral segmentation to identify key factors limiting prediction market engagement. Designed and tested multifaceted solutions that drove an <a href="cases/diversify-single-category.html">11% increase in engagement in new markets</a>, with the new tools quickly becoming a meaningful share of total trade volume.',
            ),
            (
                "Retention Strategy",
                'Diagnosed first-time-user friction outside company control that was driving substantial monthly losses from user abandonment; recommended a simple messaging strategy that reduced drop-off significantly, <a href="cases/first-trade-recovery.html">recovering roughly 70% of projected monthly losses</a>.',
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
                "Built and psychometrically validated a proprietary Responsible Gaming Sentiment Scale and the risk-prevention tools for users, raising the share of users that meet regulatory standards by double digits to more than 9 in 10.",
            ),
            (
                "Wallet Optimization",
                "Diagnosed steep drop-off at wallet/banking setup via triangulated mixed-methods research (Amplitude funnel analysis, moderated interviews, large scale survey) generating a multimillion-dollar boost in handle from first-time deposits.",
            ),
            (
                "ACH Adoption",
                'Identified barriers and developed targeted messaging that <a href="cases/ach-adoption.html">roughly doubled ACH adoption</a>, cutting account takeovers roughly in half.',
            ),
            (
                "Cross-sell Conversion",
                "Drove 100K+ new Sportsbook customers that generated a 7-figure increase in monthly revenue from solutions recommended to improve promotional offers (i.e., Bet $5 and Get $200).",
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
        "context": "",
        "title": "Senior UX Researcher",
        "dates": "March 2021 – Dec 2023",
        "bullets": [
            (
                "Onboarding &amp; Acquisition",
                "Identified onboarding friction and developed messaging strategies that cut support tickets by 30% and reduced annual costs by seven figures, helping grow the user base from 1.5M to +20M.",
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
                'Led generative and formative research on a small cross-functional team to develop and test in-app features that shipped — <a href="cases/fantasy-d2c-ideation.html">converting nearly half of active users and generating nearly $1M in revenue</a>.',
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
                'Authored the research protocol and ran end-to-end comparative usability testing of a biosimilar insulin pen with patients and clinic nurses — moderating simulated-injection sessions, filming, and analyzing behavioral and preference data.',
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
            (
                "Season-long Diary Studies",
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


def build_case_blocks(case_href_prefix="cases/", prefix=""):
    """Each company group is a horizontally scrollable carousel of case cards.

    The track is a native scroll-snap row (works with JS disabled); the
    prev/next buttons are progressively enhanced by the [data-pcarousel]
    handler in js/main.js. Group headers carry the official brand logo.
    """
    company_order = [
        ("robinhood", "Robinhood"),
        ("fanduel", "FanDuel"),
        ("nfl", "NFL"),
        ("ipsos", "Ipsos Healthcare"),
        ("burkmont", "Burkmont Analytics · Phoenix Suns"),
        ("cgu", "Claremont Colleges"),
    ]
    industries = {
        "robinhood": "fintech",
        "fanduel": "fintech",
        "nfl": "sports-media",
        "burkmont": "sports-media",
        "ipsos": "healthcare",
        "cgu": "healthcare",
    }
    case_blocks = []
    for brand_key, brand_label in company_order:
        brand_cases = [c for c in CASES if c["brand"] == brand_key]
        cards = []
        for c in brand_cases:
            badge = product_badge(c["brand"])
            card_chip = brand_logo_chip(
                c["brand"], prefix=prefix, extra_class="brand-chip-card"
            )
            cards.append(
                f"""            <a class="case-card case-{c['brand']} reveal" href="{case_href_prefix}{c['slug']}.html">
              <div class="case-card-top">
                <span class="case-num">{c['num']}</span>
                {card_chip}
              </div>
              {badge}
              <h3>{c['title']}</h3>
              <p>{c['short']}</p>
              <span class="case-card-cue">Read case <span aria-hidden="true">&rarr;</span></span>
            </a>"""
            )
        if not cards:
            continue
        logo_chip = brand_logo_chip(brand_key, prefix=prefix, label=brand_label)
        head_logo = (
            f'          {logo_chip}\n' if logo_chip else ""
        )
        industry = industries.get(brand_key, "other")
        case_blocks.append(
            f"""        <div class="company-group company-{brand_key} reveal" id="cases-{brand_key}" data-industry="{industry}">
          <div class="company-group-head">
{head_logo}            <h3 class="company-heading">{brand_label}</h3>
          </div>
          <div class="product-carousel" data-pcarousel>
            <button type="button" class="pcar-btn pcar-prev" data-pcar-prev aria-label="Scroll to previous {brand_label} cases">&#8249;</button>
            <div class="pcar-track" data-pcar-track tabindex="0" role="group" aria-label="{brand_label} case studies">
{chr(10).join(cards)}
            </div>
            <button type="button" class="pcar-btn pcar-next" data-pcar-next aria-label="Scroll to more {brand_label} cases">&#8250;</button>
          </div>
        </div>"""
        )
    return case_blocks


# One-line outcomes for the home-page case index. Kept faithful to each
# case's summary; shown when a row expands on hover/focus (always on touch).
HOME_INDEX_OUTCOMES = {
    "first-trade-conversion": "Five low-effort design changes brought hundreds of thousands of stalled traders back to a first trade.",
    "first-trade-recovery": "Redesigning one error moment&mdash;no engineering fix&mdash;kept 6 of every 10 at-risk users and recovered most of the revenue at risk.",
    "diversify-single-category": "Surfacing tools already in the app lifted the share of multi-category traders 11%.",
    "cold-start-personalization": "A re-analysis caught a cold-start blind spot; the recommended fixes cut post-first-trade drop-off by nearly a third.",
    "registration-dropoff": "A simulated-app experiment localized the drop; reordering when SSN and banking are asked lifted completion by roughly a third.",
    "benchmarking-decision-engine": "Cross-product benchmarking became the organization&rsquo;s investment reference point&mdash;and grew research into a 32-person team.",
    "ach-adoption": "Reframing the message&mdash;no incentives&mdash;roughly doubled ACH adoption and drained a costly football-Sunday debit exploit.",
    "fantasy-d2c-ideation": "Nearly $1M in first-year revenue from Fantasy features bought by more than a million players.",
    "nfl-d2c-packaging": "Formative research behind NFL+, launched to ~1.1M sign-ups and roughly 2.7M subscribers heading into 2024.",
    "intel-trueview": "Design studios on Intel&rsquo;s volumetric replay prototype delivered a clear read on fan appetite for interactive replay.",
    "verizon-superstadium": "Usability and in-stadium field research that helped seed SuperStadium, now built into the official NFL app.",
}

HOME_INDEX_BRAND_SHORT = {
    "robinhood": "Robinhood",
    "fanduel": "FanDuel",
    "nfl": "NFL",
}

HOME_INDEX_INDUSTRY = {
    "robinhood": "fintech",
    "fanduel": "fintech",
    "nfl": "sports-media",
}


def build_home_index_rows():
    """Title-first typographic index of the case studies for the home page."""
    rows = []
    for case in CASES:
        slug = case["slug"]
        outcome = HOME_INDEX_OUTCOMES.get(slug)
        if not outcome:
            continue
        brand_key = case["brand"]
        meta_label = case.get("badge_label") or HOME_INDEX_BRAND_SHORT.get(brand_key, brand_key)
        industry = HOME_INDEX_INDUSTRY.get(brand_key, "other")
        rows.append(
            f"""          <li class="idx-row reveal" data-industry="{industry}">
            <a href="cases/{slug}.html">
              <span class="idx-num" aria-hidden="true">{case["num"]}</span>
              <span class="idx-main">
                <span class="idx-title">{case["title"]}</span>
                <span class="idx-unfold"><span class="idx-outcome">{outcome}</span></span>
              </span>
              <span class="idx-meta">{meta_label} &middot; {case["year"]}</span>
              <span class="idx-arrow" aria-hidden="true">&rarr;</span>
            </a>
          </li>"""
        )
    return rows


def write_home():
    index_rows = build_home_index_rows()
    html = (
        header(nav_active="home", page_path="")
        + f"""
  <main>
    <section class="hero hero-page hero-cinema">
      <div class="hero-media" aria-hidden="true">
        <video
          class="hero-video"
          data-hero-video
          muted
          loop
          playsinline
          preload="none"
          poster="media/nfl-intel/sizzle-reel-poster.jpg"
          tabindex="-1"
          disablepictureinpicture
        >
          <source src="media/nfl-intel/sizzle-reel.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="hero-scrim" aria-hidden="true"></div>
      <div class="wrap hero-copy">
        <p class="hero-kicker">AI-Driven Insights</p>
        <h1 class="hero-brand">Sam<br />Weinberger</h1>
        <p class="hero-role">UX Design Research | Research Engineer</p>
        <p class="hero-status"><span class="hero-status-dot" aria-hidden="true"></span>Most recently: Prediction Markets @ Robinhood</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#work">Explore the work</a>
        </div>
      </div>
      <a class="hero-scroll-cue" href="#statement" aria-label="Scroll down to read more"><span class="hero-scroll-line" aria-hidden="true"></span></a>
    </section>

    <section class="home-statement" id="statement" aria-label="Introduction">
      <div class="wrap">
        <p class="statement-line reveal">9+ years of mixed-methods research across fintech, sports media, and healthcare.</p>
        <p class="statement-line reveal">Every study here ends the same way&mdash;</p>
        <p class="statement-line statement-em reveal">a shipped product decision and a measured outcome.</p>
      </div>
    </section>

    <section class="home-index" id="work" aria-label="Case study index">
      <div class="wrap">
        <header class="index-head reveal">
          <p class="index-kicker">Index &middot; Eleven case studies</p>
          <div class="index-paths" role="group" aria-label="Choose a path through the work">
            <button type="button" class="path-link is-active" data-path="all" aria-pressed="true">All</button>
            <button type="button" class="path-link" data-path="fintech" aria-pressed="false">Fintech</button>
            <button type="button" class="path-link" data-path="sports-media" aria-pressed="false">Sports &amp; Media</button>
          </div>
        </header>
        <ol class="idx-list" data-case-index>
{chr(10).join(index_rows)}
        </ol>
        <p class="index-foot reveal"><a href="case-studies.html">Prefer pictures? Browse the gallery view &rarr;</a></p>
      </div>
    </section>

    <section class="brand-band" aria-label="Brands worked with">
      <div class="wrap reveal">
        <p class="brand-band-label">Selected work across</p>
        <div class="brand-strip">
          <a href="case-studies.html#cases-robinhood" title="Robinhood case studies"><img class="brand-tile" src="media/brands/robinhood-home.png" alt="Robinhood" loading="lazy" decoding="async" /></a>
          <a href="case-studies.html#cases-fanduel" title="FanDuel case studies"><img class="brand-tile" src="media/brands/fanduel-home.png" alt="FanDuel" loading="lazy" decoding="async" /></a>
          <a href="cases/fantasy-d2c-ideation.html" title="NFL Fantasy case study"><img class="brand-tile" src="media/brands/nfl-fantasy-home.png" alt="NFL Fantasy" loading="lazy" decoding="async" /></a>
          <a href="cases/nfl-d2c-packaging.html" title="NFL+ case study"><img class="brand-tile" src="media/brands/nfl-plus-home.png" alt="NFL+" loading="lazy" decoding="async" /></a>
          <a href="cases/verizon-superstadium.html" title="Verizon 5G SuperStadium case study"><img class="brand-tile" src="media/brands/verizon-5g-home.png" alt="Verizon 5G" loading="lazy" decoding="async" /></a>
          <a href="cases/intel-trueview.html" title="Intel TrueView case study"><img class="brand-tile" src="media/brands/intel-home.png" alt="Intel" loading="lazy" decoding="async" /></a>
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
        header(
            active="Case studies",
            nav_active="cases",
            page_path="case-studies.html",
            description="Eleven case studies across Robinhood, FanDuel, and the NFL—each tied to a shipped product decision and a measured outcome.",
        )
        + f"""
  <main>
    <section class="section page-section" id="case-studies">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Case studies</h2>
          <p>Eleven studies across Robinhood, FanDuel, and the NFL—each tied to a shipped product decision and a measured outcome.</p>
        </div>
        <div class="filter-bar reveal" data-case-filters role="group" aria-label="Filter case studies by industry">
          <button type="button" class="filter-pill is-active" data-filter="all" aria-pressed="true">All</button>
          <button type="button" class="filter-pill" data-filter="fintech" aria-pressed="false">Fintech</button>
          <button type="button" class="filter-pill" data-filter="sports-media" aria-pressed="false">Sports &amp; Media</button>
        </div>
{chr(10).join(case_blocks)}
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "case-studies.html").write_text(html)


# --- Media / gallery page ----------------------------------------------------

# Featured "design studio" clip. Identified from frame analysis of the candidate
# Intel videos: this is the higher-quality source recording of the NFL Design
# "Research Design Studio" co-design session (name tents, "How might we
# enhance/upgrade NFL Game Replay Experiences?", group sketching / concept
# critique), compressed for the web. Duration of source ≈ 2:34.
# NOTE: `description` below is an editable DRAFT — refine the copy freely.
MEDIA_DESIGN_STUDIO = {
    "src": "nfl-intel/design-studio.mp4",
    "poster": "nfl-intel/design-studio-poster.jpg",
    "caption": "Running Design Studios: Watch this 2.5-min clip",
    "description": (
        "A design studio is a structured, collaborative co-design workshop where "
        "researchers, designers, cross-functional partners, and sometimes users "
        "rapidly sketch, share, and critique multiple solution concepts side by "
        "side—turning a room full of divergent ideas into an aligned product "
        "direction in a single working session."
    ),
}

MEDIA_SECTIONS = [
    {
        "id": "nfl-labs-prototypes",
        "title": "NFL Labs — Immersive Prototypes",
        "blurb": "Partner research with Intel and Verizon: the TrueView 360° replay prototype and the Verizon 5G in-stadium experience.",
        "items": [
            {
                "type": "video",
                "src": "nfl-intel/sizzle-reel.mp4",
                "poster": "nfl-intel/sizzle-reel-poster.jpg",
                "caption": "Intel TrueView — Sizzle Reel: the NFL Design “Research Design Studio” program and TrueView concept, cut as a highlight reel.",
            },
            {
                "type": "video",
                "src": "nfl-intel/intel-prototype.mp4",
                "poster": "nfl-intel/intel-prototype-poster.jpg",
                "caption": "Intel TrueView — “Be the Player.” The volumetric replay prototype fans tested hands-on: pick a player and see the play from their perspective.",
            },
            {
                "type": "video",
                "src": "nfl-intel/verizon-5g-prototype.mp4",
                "poster": "nfl-intel/verizon-5g-prototype-poster.jpg",
                "caption": "Verizon 5G SuperStadium — multi-angle in-stadium viewing, the raw camera angles behind the from-your-seat experience.",
            },
            {
                "type": "video",
                "src": "nfl-intel/superstadium-demo.mp4",
                "poster": "nfl-intel/superstadium-poster.jpg",
                "caption": "SuperStadium in the NFL app — multi-angle views and Next Gen Stats AR overlays on a phone.",
            },
        ],
    },
    {
        "id": "robinhood",
        "title": "Robinhood — Prediction Markets",
        "blurb": "Home-page findability and order-form changes that brought stalled traders back to a first trade and helped single-category traders diversify.",
        "items": [
            {"type": "image", "src": "01-non-converters/featured-before-change.png", "caption": "Before: the Featured card and category row sit flush to the edge — no signal that more exists off-screen."},
            {"type": "image", "src": "01-non-converters/featured-after-change.png", "caption": "After: offsetting the frame lets the next card peek in, cueing a sideways swipe."},
            {"type": "image", "src": "01-non-converters/featured-non-sports-carousel.png", "caption": "After: a dedicated non-sports carousel (Politics, Crypto, Technology, Commodities) added above Newly Listed."},
            {"type": "image", "src": "03-category-expansion/order-form-before-change.png", "caption": "Before: one lever — a dollar amount, buy at the market price or not at all."},
            {"type": "image", "src": "03-category-expansion/order-type-menu.png", "caption": "The new order-type menu introducing the Limit order — set your own price, good for the day."},
            {"type": "image", "src": "03-category-expansion/order-form-after-change.png", "caption": "After: full limit-order controls — set price, quantity, and expiry, with cost and payout shown before you commit."},
            {"type": "video", "src": "03-category-expansion/btc-scrub.mp4", "poster": "03-category-expansion/btc-scrub-poster.jpg", "caption": "Scrubbing the Bitcoin chart to inspect the price at any moment, sourced from CF Benchmarks’ BRTI."},
        ],
    },
    {
        "id": "fanduel",
        "title": "FanDuel — Quarterly Benchmarking",
        "blurb": "The product benchmarking program that turned SUPR-Q, Ease of Use, loyalty, and Responsible Gaming into a shared executive scorecard.",
        "items": [
            {"type": "image", "src": "benchmarking/q1-2022-supr-q-trend.jpg", "caption": "SUPR-Q trend line over quarters."},
            {"type": "image", "src": "benchmarking/q2-2023-all-products-a.jpg", "caption": "Cross-product comparison across the FanDuel portfolio."},
            {"type": "image", "src": "benchmarking/q1-2022-competitor-supr.jpg", "caption": "Competitor SUPR-Q comparison for the sportsbook category."},
            {"type": "image", "src": "benchmarking/q1-2022-rg-scores.jpg", "caption": "Responsible Gaming scores tracked alongside usability and loyalty."},
        ],
    },
    {
        "id": "nfl-fantasy",
        "title": "NFL Fantasy — The Tools Package",
        "blurb": "Fantasy features sold via in-app purchase — later folded into NFL+.",
        "items": [
            {"type": "image", "src": "fantasy/tools-package.png", "caption": "The Tools Package inside the Fantasy app — waiver tools, most-added players, and upgrade prompts."},
            {"type": "image", "src": "fantasy/lineup-view.png", "caption": "The all-new Lineup View."},
            {"type": "image", "src": "fantasy/player-lists.png", "caption": "Personalized player lists."},
            {"type": "image", "src": "fantasy/backups.png", "caption": "Set your backups to avoid last-minute inactives."},
            {"type": "image", "src": "fantasy/optimize-team.png", "caption": "Optimize-team tooling from the paid package."},
            {"type": "image", "src": "fantasy/personalized-lists.png", "caption": "Personalized recommendation lists surfaced to buyers."},
            {"type": "image", "src": "fantasy/fantasy-plus-upsell.png", "caption": "The in-app upsell used to convert free players — A/B tested for placement and messaging."},
        ],
    },
]

# Official + sub-brand marks shown at the foot of the gallery.
def render_media_video(item, big=False):
    poster = item.get("poster")
    poster_src = f"media/{poster}" if poster else ""
    poster_img = (
        f'<img class="video-click-poster" src="{poster_src}" alt="" loading="lazy" decoding="async" />'
        if poster
        else ""
    )
    poster_attr = f' poster="{poster_src}"' if poster else ""
    caption = item.get("caption", "")
    cap_html = f'<figcaption class="media-caption">{caption}</figcaption>' if caption else ""
    frame_cls = "media-frame video-click-frame"
    return f"""      <figure class="media-item media-video{' media-item-feature' if big else ''} reveal">
        <div class="{frame_cls}" data-video-click>
          {poster_img}
          <video class="video-click-el" playsinline preload="none"{poster_attr} hidden>
            <source src="media/{item['src']}" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <button type="button" class="video-click-cta media-play" aria-label="Play video">
            <span class="video-click-cta-icon" aria-hidden="true">&#9654;</span>
            <span>Play</span>
          </button>
        </div>
        {cap_html}
      </figure>"""


def render_media_image(item):
    caption = item.get("caption", "")
    alt = item.get("alt", caption)
    cap_html = f'<figcaption class="media-caption">{caption}</figcaption>' if caption else ""
    return f"""      <figure class="media-item media-image reveal">
        <div class="media-frame">
          <img class="media-img" src="media/{item['src']}" alt="{alt}" loading="lazy" decoding="async" />
        </div>
        {cap_html}
      </figure>"""


def render_media_item(item, big=False):
    if item["type"] == "video":
        return render_media_video(item, big=big)
    return render_media_image(item)


def write_media_page():
    ds = MEDIA_DESIGN_STUDIO
    featured = f"""        <section class="media-featured reveal" id="design-studio" aria-labelledby="design-studio-title">
          <div class="media-featured-head">
            <span class="media-kicker">Featured</span>
            <h3 id="design-studio-title">Running Design Studios</h3>
          </div>
          <figure class="media-item media-video media-item-feature">
            <div class="media-frame media-frame-feature video-click-frame" data-video-click>
              <img class="video-click-poster" src="media/{ds['poster']}" alt="" loading="lazy" decoding="async" />
              <video class="video-click-el" playsinline preload="none" poster="media/{ds['poster']}" hidden>
                <source src="media/{ds['src']}" type="video/mp4" />
                Your browser does not support the video tag.
              </video>
              <button type="button" class="video-click-cta media-play media-play-feature" aria-label="Play the design studio clip">
                <span class="video-click-cta-icon" aria-hidden="true">&#9654;</span>
                <span>{ds['caption']}</span>
              </button>
            </div>
            <figcaption class="media-caption media-caption-feature">{ds['description']}</figcaption>
          </figure>
        </section>"""

    section_blocks = []
    for sec in MEDIA_SECTIONS:
        items_html = "\n".join(render_media_item(it) for it in sec["items"])
        section_blocks.append(
            f"""        <section class="media-section reveal" id="media-{sec['id']}" aria-labelledby="media-{sec['id']}-title">
          <div class="media-section-head">
            <h3 id="media-{sec['id']}-title">{sec['title']}</h3>
            <p>{sec['blurb']}</p>
          </div>
          <div class="media-grid">
{items_html}
          </div>
        </section>"""
        )

    html = (
        header(
            active="Media",
            nav_active="media",
            page_path="media.html",
            description="Media and gallery — immersive prototypes with Intel and Verizon, Robinhood prediction-market design changes, FanDuel benchmarking, and NFL Fantasy tools.",
        )
        + f"""
  <main>
    <section class="section page-section" id="media">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Media &amp; gallery</h2>
        </div>
{featured}
{chr(10).join(section_blocks)}
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "media.html").write_text(html)


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
        header(
            active="Skills",
            nav_active="skills",
            page_path="skills.html",
            description="Quantitative UX, psychometrics, sports/in-the-wild methods, and engineered research infrastructure.",
        )
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
                f'<img src="media/tool-icons/{icon_file}" alt="{tool} logo" loading="lazy" decoding="async" />'
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
        header(
            active="Tech Stack",
            nav_active="research-tools",
            page_path="research-tools.html",
            description="Platforms and languages used across survey, analytics, experimentation, collaboration, and analysis.",
        )
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
        header(active="About me", nav_active="about", page_path="about.html")
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
        header(
            active="Professional Experience",
            nav_active="resume",
            page_path="resume.html",
            description="Professional experience — Robinhood, FanDuel, the NFL, Claremont Graduate University, and Ipsos Healthcare.",
        )
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
            <a class="btn btn-primary" href="Samuel-Weinberger-Resume.pdf" download="Samuel-Weinberger-Resume.pdf">Download resume</a>
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
    athletics_rows = "\n".join(
        f"""          <p class="resume-athletics">
            {brand_logo_chip(a['brand'], label=a['label'])}
            <span>{a['text']}</span>
          </p>"""
        for a in RESUME_ATHLETICS
    )
    html = (
        header(
            active="Education",
            nav_active="education",
            page_path="education.html",
            description="Graduate and undergraduate study in cognitive and social psychology, public policy, and communications—alongside a Division 1 athletics background.",
        )
        + f"""
  <main>
    <section class="section page-section resume-page" id="education">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Education</h2>
          <p>Graduate and undergraduate study in cognitive and social psychology, public policy, and communications—alongside a Division 1 athletics background.</p>
        </div>
        <ul class="resume-earlier reveal">
{education_rows}
        </ul>
        <div class="resume-athletics-list reveal">
{athletics_rows}
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "education.html").write_text(html)


def write_contact_page():
    c = RESUME_CONTACT
    contact_rows = [
        ("Email", f'<a href="mailto:{c["email"]}">{c["email"]}</a>'),
        (
            "LinkedIn",
            f'<a href="{c["linkedin_href"]}" target="_blank" rel="noopener">{c["linkedin_label"]}</a>',
        ),
        ("Phone", f'<a href="{c["phone_href"]}">{c["phone"]}</a>'),
        ("Location", f'<span>{c["location"]}</span>'),
    ]
    rows_html = "\n".join(
        f"""          <li>
            <span class="contact-label">{label}</span>
            <span class="contact-value">{value}</span>
          </li>"""
        for label, value in contact_rows
    )
    html = (
        header(
            active="Contact",
            nav_active="contact",
            page_path="contact.html",
            description="Get in touch — email, LinkedIn, and phone for Sam Weinberger.",
        )
        + f"""
  <main>
    <section class="section page-section resume-page" id="contact">
      <div class="wrap">
        <div class="section-head reveal">
          <h2>Contact</h2>
          <p>Always happy to talk research, UX engineering, and product strategy. The fastest way to reach me is email.</p>
        </div>
        <ul class="contact-list reveal">
{rows_html}
        </ul>
        <div class="resume-actions reveal">
          <a class="btn btn-primary" href="mailto:{c['email']}">Email me</a>
          <a class="btn btn-ghost" href="{c['linkedin_href']}" target="_blank" rel="noopener">Connect on LinkedIn</a>
        </div>
      </div>
    </section>
  </main>
"""
        + footer()
    )
    (ROOT / "contact.html").write_text(html)


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
            f'<img class="video-click-poster" src="{poster_src}" alt="" loading="lazy" decoding="async" />'
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
          <img class="case-nfl-media-img" src="../media/{img['src']}" alt="{img.get('alt', '')}" loading="lazy" decoding="async" />
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
                f'            <img class="case-nfl-gallery-img" src="../media/{im["src"]}" alt="{im.get("alt", "")}" loading="lazy" decoding="async" />'
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
          <img class="case-nfl-media-img" src="../media/{item['src']}" alt="{item.get('alt', '')}" loading="lazy" decoding="async" />
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
            page_path=f"cases/{case['slug']}.html",
            description=case.get("short") or case.get("summary"),
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


def _section_slug(title):
    slug = "".join(ch if ch.isalnum() else "-" for ch in title.lower())
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "section"


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
                f'            <img class="carousel-slide{active}" src="../media/{im["src"]}" alt="{alt}" data-caption="{cap}" loading="lazy" decoding="async" />'
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
                f'<img class="video-click-poster" src="{poster_src}" alt="" loading="lazy" decoding="async" />'
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
          <img src="../media/{c['src']}" alt="{c.get('alt', '')}" loading="lazy" decoding="async" />
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
    toc_items = []
    total = len(case["sections"])
    for i, (title, body) in enumerate(case["sections"]):
        sid = _section_slug(title)
        toc_items.append((sid, title))
        section_blocks.append(
            f"""        <section class="case-section reveal" id="{sid}">
          <div class="case-section-label">
            <h2>{title}</h2>
          </div>
          <div class="case-section-body">{body}</div>
        </section>"""
        )
    toc_html = ""
    if len(toc_items) > 1:
        links = "\n".join(
            f'      <a href="#{sid}">{title}</a>' for sid, title in toc_items
        )
        toc_html = f"""
    <nav class="case-toc" data-case-toc aria-label="On this page">
      <span class="case-toc-label">On this page</span>
{links}
    </nav>"""
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
        header(
            active=case["title"],
            prefix="../",
            brand=case["brand"],
            nav_active="cases",
            page_path=f"cases/{case['slug']}.html",
            description=case.get("short") or case.get("summary"),
        )
        + f"""
  <main class="case-page">{toc_html}
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
    write_media_page()
    write_skills_page()
    write_research_tools_page()
    write_about_page()
    write_resume_page()
    write_education_page()
    write_contact_page()
    for i, case in enumerate(CASES):
        write_case(case, i)
    print(f"Wrote home + section pages + {len(CASES)} case pages")


if __name__ == "__main__":
    main()
