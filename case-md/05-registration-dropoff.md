# 05. Studying the Users You Can’t Recruit: Fixing Registration Drop-Off

**Company:** FanDuel  
**Context:** FanDuel · Core Products & Experiences  
**Year:** 2021–2025
**Role:** UX Researcher (study lead)  
**Timeline:** Multi-phase (simulation → A/B → production)  
**Methods:** Simulated-app experiment · Step-by-step intention measurement · Third-party panel recruitment · A/B testing · Behavioral theory (foot-in-the-door)

**Listing blurb:** Studied an unrecruitable, churned population through a simulated signup—reordering when SSN and banking are asked lifted registration completion from ~50% to ~65%.

## Summary
More than half of prospective FanDuel customers abandoned registration on every state launch, and they couldn’t be recruited. A simulated-app study localized the drop and a reordered flow lifted completion from ~50% to ~65% in production.

## Situation
- Every time FanDuel launched in a new state, more than half of prospective customers failed to complete the registration funnel.
- The people who abandoned were the ones the business most needed to understand—but because they never finished signing up, they couldn’t be recruited for any study.
- Users who did complete registration couldn’t explain the drop-off either; they hadn’t experienced it as a blocker.
- This was a top priority because benchmarking had flagged registration and login as the two highest-leverage steps in the entire experience.
- The company was scaling fast, growing from ~1.5M users when I began to 20M+ by the time I left.

## Task
- Understand friction in a funnel I couldn’t observe directly, with a population I couldn’t recruit.
- Ethical and compliance constraints meant no real people could attempt a real signup.
- Find what was driving abandonment and prove a fix that would raise completion on future launches.

## Action
- Had engineers build a simulated onboarding flow mirroring our real registration steps, framed as an e-commerce app.
- Recruited a screened third-party panel across three interest levels (strong, medium, minimal).
- Participants moved through the flow one step at a time, giving qualitative feedback and rating behavioral intention to continue after each step—localizing the drop to exactly two steps: providing Social Security details and banking information.
- Key insight: our live funnel asked for SSN first and banking last—participants described deep distrust at handing over an SSN before they’d even seen the product, judging fraud and identity-theft risk not worth it for an unfamiliar sportsbook.
- Hypothesized that the order of requests was itself driving abandonment (foot-in-the-door: small, easily accepted requests first increase the likelihood of a larger request later) and tested it with an A/B experiment (two homogeneous samples, N=500) comparing SSN-first against SSN-later.

## Result
- Asking for email, name, and address before SSN and banking nearly doubled completion in simulation—from 30% to 58% (N=500 per arm).
- The reordered flow shipped to production and held up on real launches, lifting completion from ~50% to ~65%.
- Became the reordered standard applied to every subsequent state rollout.
- Method breakthrough: studied an unrecruitable, churned population via a simulated-app proxy—ethically and compliance-safe.
- Registration and login were a top investment area as FanDuel scaled from ~1.5M to 20M+ users during this period.
