# Notes for the course of certified solutions architect professional given by a cloud.guru

- [Notes for the course of certified solutions architect professional given by a cloud.guru](#notes-for-the-course-of-certified-solutions-architect-professional-given-by-a-cloudguru)
  - [Migrations](#migrations)
    - [Migration strategies](#migration-strategies)
    - [Cloud adoption framework](#cloud-adoption-framework)

## Migrations

### Migration strategies

|Strategy|Description|Example|Effort|Opportunity to optimize
|----|----|----|----|----|
|Re-host|Lift and shift; simply move assets with no change|Move on-prem MySQL database to EC2 Instance|***|*|
|Re-platform|Lift and reshape; Move assets but change underlying platform|Migrate on-prem MySQL database to RDS MySQL|\****|\***|
|Re-purchase|Drop and shop; Abandon existing and purchase new|Migrate legacy on-prem CRM to salesforce.com|***|*|
|Rearchitect|Redesign application in a cloud-native manner|Create a server-less version of a legacy application|*****|*****
|Retire|Get rid of applications which are not needed|End-of-life the label printing app because no-one uses it anymore|||
|Retain|Do nothing; Decide to reevaluate at a future date|Good news servers, you'll live to see another day|*||

### Cloud adoption framework

> Framework: is some information to help you get your mind around a problem
> is not a perfect step-by-step recipe to success

There's more to cloud adoption than technology, a holistic approach must be considered

|Business|Platform|
|--|--|
|People|Security|
|Governance|Operations|

Business
: Creating a strong bushiness case, bushiness goals, measure benefits

People
: Underestimated, powerful factor, reevaluate existing roles, career management with those evolving roles, training options

Governance
: how are we gonna manage the project and process, use the PMO, use existing processes

Platform
: Standardizing things, standard architectural patterns, develop skills and processes

Security
: Figure out how to handle identity and access management, logging and audit capabilities, understand the shared responsibility model

Operations perspective
: Monitor cloud assets, measure performance, react when performance gets below ans SLA, think about business continuity
