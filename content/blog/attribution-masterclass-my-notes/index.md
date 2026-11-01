---
title: "Attribution Masterclass: My Notes"
date: "2024-11-05T23:00:00.000Z"
draft: false
tags: []
source: "beehiiv"
original_url: "https://blog.giancampo.com/p/attribution-masterclass-my-notes"
---

## Table of Contents

1. [Intro to Attribution](#intro-to-attribution)

   1. [Attribution journeys](#attribution-journeys)
   2. [Debunking Attribution Myths](#debunking-attribution-myths)
   3. [Why we attribute](#why-we-attribute)
   4. [Attribution and Business Strategy](#attribution-and-business-strategy)
   5. [Types of Attribution](#types-of-attribution)
2. [Multi-Touch Attribution](#multi-touch-attribution)

   1. [UTM parameters](#utm-parameters)
   2. [User journeys and user stitching](#user-journeys-and-user-stitching)
   3. [How to analyze Multi-Touch Attribution (w/ Amplitu …](#how-to-analyze-multi-touch-attribut)
3. [MMM, Incrementality](#mmm-incrementality)

   1. [Intro](#intro)
   2. [Incrementality](#incrementality)
   3. [MMM](#mmm)
4. [How to approach Attribution](#how-to-approach-attribution)

   1. [People](#people)
   2. [Tools](#tools)
   3. [Checklist](#checklist)

The Attribution Masterclass is a series about marketing attribution organized by [Timo Dechau](https://www.blogger.com/u/1/blog/post/edit/4558571487857691249/8327132209806996838#) and [Barbara Galiza](https://www.blogger.com/u/1/blog/post/edit/4558571487857691249/8327132209806996838#). I'm thrilled to share I've been in the first cohort taking the masterclass with regular meetups every Thursday in November 2024.

Here follow my notes with the most important concepts shown during the masterclass. Some of the notions would be better explained using the slides the authors have made: For that, you need to actually enroll in the Masterclass: [here's the page where you can sign up](https://www.blogger.com/u/1/blog/post/edit/4558571487857691249/8327132209806996838#).

Let me recommend you to follow Timo and Barbara on Linkedin to know more about the masterclass and in general to get interesting insights and opinions on marketing attribution.

## Intro to Attribution

### Attribution journeys

1. Typical attribution models: First Touch, Last Touch, Data-Driven
2. Warning: These attribution models are all click-based so some viewed ads up in the funnel will be ignored

### Debunking Attribution Myths

1. Multi-Touch Attribution is actually not there anymore, since today it has limitations
2. There are no tools that can solve all your attribution problems
3. The best attribution method actually depends on specific needs
4. Attribution is a model, with strategy and operations layer
5. There’s not just one method and that’s it so no Single Source of Truth

### Why we attribute

1. To understand customer journeys, key touchpoints to allocate mktg budget
2. To measure impact and optimize our strategy

### Attribution and Business Strategy

1. Business strategy is the higher-level vision informing the following (e.g. grow revenue from new customers by 10%)
2. Marketing strategy outlines initiatives and campaigns (e.g. test new channels, involve new influencers and so on)
3. Attribution strategy (e.g. dimensions for campaigns with new influencers: measure impressions, discount codes, run an uplift test)
4. Major takeaway: When you plan your mktg strategy you should also plan your attribution stategy

### Types of Attribution

1. Click-Based models

   1. Last-Click, First-Click, Linear, Position-Based
   2. Data-Driven: Comprehensive Analysis, Markov Chain, Fractional Attribution, Optimization Insights
2. View-Based models

   1. You consider also if the user has viewed an ad (for instance a view-through conversion window can be set in GAds)
   2. You can also track this by adding a pixel anywhere the user could view an ad
3. MMM (Mktg Mix Modeling)

   1. Economic approach
   2. Channel agnostic
   3. Measuring impact
4. Zero-Party Data

   1. How you did you hear about us? (HDYHAU), this simple question can make a difference
   2. The earlier you gather Zero-Party Data the better
   3. Customer perspective is what you get in this case
   4. Compared to other attribution types, ROI in this case is not as easy to calculate but other data/datasets about users can help with this
5. Enhancing Attribution

   1. Rule-Based Approaches, e.g. zero-party data can weight mktg channels or activities
   2. Combination of Models, multiple form of attribution are combined
   3. Click Prediction, data models predicting which campaign sessions have come from organic or direct clicks

## Multi-Touch Attribution

### UTM parameters

1. It’s an old topic but still one of the most important ones

2. We still have issues with UTMs:

   1. Sometimes are missing

   2. They are inconsistent

3. This is why you need a UTM strategy:

   1. When you own a link remember to tag it!

   2. You need a process

   3. You can do it manually

   4. But even automatically, defining rules on the 3rd party platforms

4. Techniques for UTM paramaters definition

   1. Random ID in utm\_campaign

   2. Don’t use UTM parameters inside your own website
   3. [More on this available in video recordings]

5. References about UTM parameters

   1. [Campaign (UTM) Parameter Naming Conventions revisited: Cryptic vs. Positional vs. Key-Value Notation | by Lukas Oldenburg | Medium](https://www.blogger.com/blog/post/edit/4558571487857691249/59657827273504101#) by Lukas Oldenburg

   2. [How to Improve Paid Media Analysis and Performance with Naming Conventions](https://www.blogger.com/blog/post/edit/4558571487857691249/59657827273504101#) By Barbara Galiza.

### User journeys and user stitching

1. Simplest example of user journey: landing page > conversion

   1. No issues with this

   2. UTMs are probably there

   3. Hard for cookies to be missed (but see below about this point)

2. SAAS example: landing page on www.\* > user creates an account on app.\* > user buys a subscription through Stripe

   1. Issues:

      1. Most marketers take care of the account creation and stop there but this still doesn’t tell what mktg initiative lead to subscriptions

      2. This is based on IPs or cookies but we actually have no real control about them (e.g. Safari changing settings).

   2. The solution to these issues is the use of user\_id (GA), hubspot\_lead\_id (Hubspot), hashed emails or email domain IDs, and so on

3. Ways to do user stitching is storing all the IDs you have

   1. In a Data Warehouse (DWH)

   2. Or in a leading system, for instance you decide GA is your primary platform and get Hubspot IDs data in there

4. In the case of guest checkouts you can join client\_id and transaction\_id. In general it depends if we’re talking about user level attribution or order level attribution

5. How does server-side tagging fits in this?

   1. Users using different devices are treated as separate users in client-side tracking systems

   2. This is why server-side tagging systems can help vendors - such as Meta with Facebook CAPI - optimize their campaigns

   3. One tricky issue with server-side tagging is how to handle legal consent.

### How to analyze Multi-Touch Attribution (w/ Amplitude)

1. Amplitude gives the chance to connect different data sources (e.g. BigQuery, GAds and so on)

2. We tried the attribution models comparison with a custom table where we added a First Touch, Last Touch and Data-Driven views of the demo dataset, side by side

   1. Unfortunately this is not available with other tools - such as GA - unless you build it on your own - with BigQuery

3. Amplitude gives the chance to create a free account and explore a demo dataset with custom charts.

# MMM, Incrementality

## Intro

1. Shortcomings of click-based attribution

   1. Digital campaigns w/o clicks, e.g. video campaigns

   2. Dark social

   3. Cross-device attribution, since click attribution can be made only in the same session

   4. Long sales journeys, conversions happening outside of lookback windows

## Incrementality

1. Click incrementality

   1. It’s not just sales or conversions, it can also be paid brand search clicks per se

   2. This is interesting also to understand cannibalization btw Paid and Organic

   3. There’s a study by Google showing how many clicks were incremental and how many were cannibalized to Organic Search

   4. Here’s another case history by Barbara Galiza [Measuring incremental impressions, clicks and conversions for Paid Search (Methodology + Google Sheet Template)](https://www.blogger.com/blog/post/edit/4558571487857691249/4992278503374398255#)

2. Conversion incrementality

   1. There are cases where clicks are not incremental but conversions are

   2. This tries to estimate conversions that wouldn’t have happened without a specific mktg initiative

3. How incrementality is measured

   1. Holdout tests are performed turning off a campaign to all or certain audiences

   2. Geofencing is a technique similar to the previous one but in this case campaigns are turned off based on geographical areas. GeoLift is an R package made by Meta helping with this [GeoLift Walkthrough | GeoLift](https://www.blogger.com/blog/post/edit/4558571487857691249/4992278503374398255#)

   3. Causal inference, is a statistical model measuring correlation btw campaigns and sales.

4. Design a test

   1. Control targeting, be sure you can select audiences precisely

   2. Experiment control, start and stop the experiment as needed

   3. Conversion event tracking, it’s important to measure frequency of conversions within the test group and overall

   4. Campaign metrics, analyze spend and impressions for both control and test group

## MMM

1. MMM in layman’s terms way

   1. There are a bunch of inputs and outputs

   2. MMM tries to find the correlation btw inputs and outputs

2. Understanding Bayesian models

   1. Prior knowledge, Bayesian models need historical data, for instance for daily data you need at least 1 year or even more

   2. Data updates, the model gets updated when new data arrives

   3. Probabilistic approach, probabilities are assigned to different outcomes based on input data

3. MMM and Bayesian models

   1. Simulations: MMM runs simulations

   2. Statistical analysis: Correlation is calculated for each simulation

   3. Channel impact: Finally MMM isolates the impact of each mktg channel

4. Requirements for MMM

   1. Date-level datasets, data granularity should be daily or weekly depending on mktg activities involved and the type of business

   2. Mktg activity data, all media activities should be included

   3. Target metric, of course this depends especially on the business

   4. Historical data, at least 1 or 2 years of data are needed

   5. Sample dataset generator by Timo Dechau <https://replit.com/@TimoDechau/Marketing-Mix-Model-Playground>

5. When to use MMM and limitations

   1. There’s a need for extensive enough datasets

   2. Time and understanding to fine tune MMM is important

   3. It’s good for high-level channel decisions

   4. Barbara recommends 6 figures per month is the minimum recommended spend for those who want to use MMM

# How to approach Attribution

In this 4th session I missed some content, however I believe there’s enough to understand the topics covered by Barbara and Timo.

1. [missed]
2. Constraints

   1. Discussion loops?
   2. It’s my conversion
   3. [missed]
   4. Which model/tool do we pick?
3. Core metrics to measure to understand if attribution is working

   1. Mktg spend
   2. CAC (Customer Acquisition Cost)
   3. Cost/revenue ratio
   4. Revenue of new customers
   5. Revenue VIP customers (CLV, Customer Lifetime Value)
   6. Customer payback period
4. Weekly checks on the core metrics is important

   1. You should log
   2. Then you can experiment

      1. incrementality kicks in here
5. Rule-based attribution

   1. DWH where you collect information
   2. You take all the insights from different models (last-click, data-driven and so on)
   3. Decide what indications override or calibrate the others (e.g. you override last-click with post-purchase survey indications)

## People

1. You should implement it for yourself at first
2. Be public about it, explaining inside the company how your tests are going
3. Share insights
4. [missed]

## Tools

1. Marketing Analytics platform
2. Tools to analyze uplift in case you’re doing incrementality
3. Planning and documentation
4. Surveys and asking customers can also be crucial

## Checklist

1. Where to start

   1. [missed]
   2. Understand business strategy
   3. Make sure event tracking is OK for what you need
   4. ID resolution an user stitching
   5. Naming conventions an UTM parameters
   6. One testing roadmap for the experiments you need
   7. Post-purchase surveys
   8. Rule-based attribution
   9. MMM vendors (potentially)
   10. Vouchers (Stripe gives the chance to use vouchers OOTB
2. In the next 4 weeks

   1. Document the financial risk of poor attribution
   2. What to achieve and by when
   3. What does delay decision making?
   4. What tools do you have in place? What are you missing?
   5. What stakeholders should be involved?
3. Recommendations

   1. Prioritize strategies impacting historical data
   2. Use MVPs where possible, think small what you want is answers so you should focus on that
   3. Know your abilities
   4. Engage stakeholders needing data early, document a lot and let people understand what you’re doing: The more you share the more stakeholders are involved
