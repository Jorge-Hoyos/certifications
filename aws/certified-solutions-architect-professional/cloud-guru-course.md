# Notes for the course of certified solutions architect professional given by acloud.guru

- [Notes for the course of certified solutions architect professional given by acloud.guru](#notes-for-the-course-of-certified-solutions-architect-professional-given-by-acloudguru)
  - [Migrations](#migrations)
    - [Migration strategies](#migration-strategies)

## Migrations

### Migration strategies

|Strategy|Description|Example|Effort|Oportunity to optimize
|----|----|----|----|----|
|Re-host|Lift and shift; simply move assets with no change|Move on-prem MySQL database to EC2 Instance|***|*|
|Re-platform|Lift and reshape; Move assets but change underlying platform|Migrate on-prem MySQL database to RDS MySQL|\****|\***|
|Re-purchase|Drop and shop; Abandon existing and purchase new|Migrate legacy on-prem CRM to salesforce.com|***|*|
|Rearchitect|Redesign application in a cloud-native manner|Create a server-less version of a legacy application|*****|*****
|Retire|Get rid of applications which are not needed|End-of-life the label printing app because no-one uses it anymore|||
|Retain|Do nothing; Decide to reevaluate at a future date|Good news servers, youll live to see another day|*||

