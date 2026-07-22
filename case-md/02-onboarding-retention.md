# 02. Turning First-Trade Rejection Into Retention

**Company:** Robinhood  
**Context:** Robinhood · Prediction Markets & Event Contracts  
**Year:** 2026


**Listing blurb:** Cut post-rejection drop-off 60%+ with survival analysis and loss-aversion messaging—retaining ~900K users and ~$17M monthly.

## Summary
One in five first trades was rejected and 90% of those users left. Survival analysis plus loss-aversion messaging cut that drop-off 60%+—retaining ~900K users and ~$17M monthly.

> The most dangerous moment in the funnel wasn’t signup—it was the silence right after a first trade failed.

## Impact KPIs
- **60%+ reduction** — Post-first-trade-rejection drop-off  _[conversion]_
- **$17M** — Monthly revenue retained from recovered traders  _[revenue]_
- **~900K** — Users retained per month  _[scale]_
- **18% increase** — Trade volume among top-tier customers  _[conversion]_

## Situation
- 1 in 5 first-time trades (~450K/month) was rejected by backend matching mechanics.
- Users read rejection as a platform failure; 90% abandoned—often to competitors.
- Churned first-time traders were hard to recruit for research.

## Task
- Pinpoint when post-rejection drop-off happened and why different mental models churned.
- Ship messaging and product changes that stabilize retention for Growth & Acquisition.

## Action
- Used survival analysis to isolate the peak churn window after rejection.
- Segmented users (KMeans + MaxDiff) and interviewed churned traders who had defected.
- Shipped personalized, loss-aversion-framed messaging that explained the rejection and routed users back into the first-trade flow.

## Result
- Cut post-first-trade-rejection drop-off by over 60% (~900K users/month; ~$17M monthly revenue).
- Drove 4–12% engagement/retention lifts and an 18% trade-volume increase among top-tier customers.
- Showed a first-trade loss decreases LTV 20–25%, launching a responsible-trading first-trade initiative.
