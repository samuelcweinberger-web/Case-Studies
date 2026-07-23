# 02. The Cold-Start Problem: A Deep Dive Into a Personalization Experiment

**Company:** Robinhood  
**Context:** Robinhood · Prediction Markets & Event Contracts  
**Year:** 2026
**Role:** UX Researcher (investigation lead)  
**Timeline:** Multi-week deep dive  
**Methods:** Behavioral segmentation · AI-moderated interviews · Factorial ANOVA (arm × segment) · Matched-sample analysis · Prototyping (Cursor · GitHub · Figma · Python)

**Listing blurb:** Re-examined a celebrated personalization A/B test, proved it couldn’t cold-start new users, and reframed the roadmap—cutting one-and-done churn from 54% to 37%.

## Summary
A personalization algorithm looked like a win (+4% in its A/B test) but trade volume had plateaued. My re-analysis showed it couldn’t cold-start new users, and the fixes I recommended cut one-and-done churn from 54% to 37%.

## Situation
- Data Science built and launched a personalization algorithm; its A/B test showed the experimental group trading ~4% more than control (p

## Task
- Map what actually drives and suppresses trade volume, and diagnose the plateau.
- Preliminary analysis surfaced the risk immediately: ~70% of the base traded sports contracts only.
- Higher-value multi-category traders—who trade significantly more—were shrinking fast.
- That set up a seasonal cliff: once college basketball and the NBA season ended, volume had nowhere to go.

## Action
- Working from a defined research plan, ran behavioral segmentation and interviewed the top 2% of four groups: sports-only traders, multi-category traders, former-multi-category traders who had retreated, and net-new “cold-start” users the algorithm had no history for.
- In-app, users showed me the mechanism directly: the algorithm kept re-surfacing the same events and buried inventory they’d have loved.
- One high-value trader had defected to a competitor for WNBA contracts that Robinhood actually offered but hid so deep in the UI he assumed they didn’t exist.
- Went back to Data Science for the raw experiment data and found the aggregate +4% couldn’t support “personalization works”: the treatment window overlapped the NBA Finals (a major confound), the test was heavily overpowered, and the lift was carried by users with existing trading history.
- A planned cold-start contrast (factorial ANOVA, arm × segment) told the opposite story—for net-new users, control outperformed the personalized experience by 24%.

## Result
- Core finding: personalization alone can’t cold-start. With no history to draw on, the algorithm funneled new users into the same popular-sports events, starving discovery and manufacturing the seasonal cliff.
- Recommended pairing personalization with explicit customization—users select categories during onboarding and toggle them on or off as interests change, a need ~90% of interviewees raised unprompted.
- Recommended a Watch List giving traders a cross-category home to return to.
- Prototyped both (Cursor, GitHub, Figma, Python); the Watch List shipped in a variant form.
- One-and-done churn among crossover first-traders fell from 54% to 37% in one month.
- The improvement held even as the cohort grew by ~300K new signups; churned users overwhelmingly had not adopted the Watch List (~3% had).
- Onboarding customization step recommended and pending product adoption.
