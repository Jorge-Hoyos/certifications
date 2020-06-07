# Notes for the course of certified solutions architect professional given by a cloud.guru

Course given by A Cloud Guru [AWS Certified Solutions Architect - Professional 2020](https://acloud.guru/learn/aws-certified-solutions-architect-professional)

- [Notes for the course of certified solutions architect professional given by a cloud.guru](#notes-for-the-course-of-certified-solutions-architect-professional-given-by-a-cloudguru)
  - [**Migrations**](#migrations)
    - [**Migration strategies**](#migration-strategies)
    - [**Cloud adoption framework**](#cloud-adoption-framework)
    - [**Hybrid architectures**](#hybrid-architectures)
      - [Example](#example)
    - [**Migration Tool**](#migration-tool)
    - [**Network migrations and cutovers**](#network-migrations-and-cutovers)
    - [**Amazon Snow family**](#amazon-snow-family)
    - [**Pro Tips**](#pro-tips)

## **Migrations**

---

### **Migration strategies**

|Strategy|Description|Example|Effort|Opportunity to optimize
|----|----|----|----|----|
|Re-host|Lift and shift; simply move assets with no change|Move on-prem MySQL database to EC2 Instance|***|*|
|Re-platform|Lift and reshape; Move assets but change underlying platform|Migrate on-prem MySQL database to RDS MySQL|\****|\***|
|Re-purchase|Drop and shop; Abandon existing and purchase new|Migrate legacy on-prem CRM to salesforce.com|***|*|
|Rearchitect|Redesign application in a cloud-native manner|Create a server-less version of a legacy application|*****|*****
|Retire|Get rid of applications which are not needed|End-of-life the label printing app because no-one uses it anymore|||
|Retain|Do nothing; Decide to reevaluate at a future date|Good news servers, you'll live to see another day|*||

### **Cloud adoption framework**

---

> Framework: is some information to help you get your mind around a problem
> is not a perfect step-by-step recipe to success

There's more to cloud adoption than technology, a holistic approach must be considered

|Business|Platform|
|--|--|
|People|Security|
|Governance|Operations|

**Business**
: Creating a strong bushiness case, bushiness goals, measure benefits

**People**
: Underestimated, powerful factor, reevaluate existing roles, career management with those evolving roles, training options

**Governance**
: how are we gonna manage the project and process, use the PMO, use existing processes

**Platform**
: Standardizing things, standard architectural patterns, develop skills and processes

**Security**
: Figure out how to handle identity and access management, logging and audit capabilities, understand the shared responsibility model

**Operations perspective**
: Monitor cloud assets, measure performance, react when performance gets below ans SLA, think about business continuity

Notes:

- Doesn't need to communicate the change to external stakeholders.
- Be sure that existing software can be migrated to the cloud, licence wise
- The Cloud Adoption Framework focuses on the early stages of cloud adoption. Therefore, any reinvention of business processes is not inherently considered part of the CAF.

### **Hybrid architectures**

---

- makes use of cloud resource along with on-premises resources
- First step as pilot for cloud migrations
- Ideally, hybrid architectures are loosely coupled - each side can exist with out knowledge of the other side

#### Example

AWS storage gateway have a locally cashed volume in a corporate HQ and offices

![Hybrid architecture example](/aws/certified-solutions-architect-professional/media/hybrid-architecture-example.PNG)

- Seamless to end users
- Benefit from storing in S3
- Common first step
- Easy to implement

![Hybrid architecture example 2](/aws/certified-solutions-architect-professional/media/hybrid-architecture-example-2.PNG)

- Middleware often a great way to leverage cloud services
- Loosely-coupled architecture, the ERP system doesn't have to know about DynamoDB, and vice versa

### **Migration Tool**

---

- Storage migration
  - AWS storage gateway
  - AWS Snowball

- Server migration service:
  - Automates migration of on-premises VMware vSphere or microsoft VM to AWS
  - Replicate VMs to AWS, syncing volumes and creating periodically AMIs (Disaster recovery Sync VM volumes to cloud AMIs)
  - Minimize cut over downtime by syncing VMs incrementally
  - Windows and linux VMs
  - Downloaded as a virtual appliance into on-prem setup

- Database migration service
  - Along with Schema conversion tool (SCT) helps customers migrate DBs to AWS RDS or EC2-based databases
  - The SCT can copy databases schema for homogenous migrations (same DB), and convert schemas for heterogenous migrations (different DB)
  - It can migrate from oracle to Aurora
  - DMS is used for smaller, simpler conversions and also supports MongoDB and DynamoDB
  - SCT is used for larger more complex, like data warehouses
  - DMS has replication function for on-prem to AWS or to snowball or S3

![DMS](/aws/certified-solutions-architect-professional/media/dms.PNG)

- Application discovery service
  - Gathers information about on-prem data centers to help in cloud migration planning
  - Help customer know the full inventory and status of their data centers
  - Collects config, usage and behavior data from your servers to help in estimating TCO of running on AWS
  - Run as agent-less (VMware env) or agent-based (non-VMware env)
  - Only supports OS that AWS supports

- AWS migration HUB

Notes:

- Informix is not supported by either DMS or SCT

### **Network migrations and cutovers**

---

Don't have any overlaps between IP addresses in your VPC or on-premise

>An overlapping IP address is an IP address that is assigned to more than one device or logical unit, such as an event source type, on a network.

VPC support IPv4 netmasks ranges from /16 to /28

> 5 IPs are reserved in every VPC subnet

/28 = 255.255.255.240
= 16 addresses

- First address is the network address
- Last address is the broadcast address
- Three other reserved addresses for the router, DNS, and the address reserved for AWS

= 14 "usable" minus 3 reserved addresses in a VPC = 11 available in VPC

Design network taking into account these reserved addresses

- Most organizations start with VPN
- Moving to Direct Connect bur keep the VPN as backup
- Transition from VPD to DC using BGP routing
- Once DC is set-up, configure botch VPN and DC within the same BGP prefix
- DC side is always preferred on AWS
- Make sure the DC pathing is preferred on on-prem

### **Amazon Snow family**

---

Sometimes can't beat the bandwidth of a delivery truck.

- Evolution of the AWS Import/Export process
- Design to move massive amounts of data to and from AWS
- Data transfer is fast or slow depending on the carrier (UPS, DHL, etc.)
- AWS sends the device, and the load data onto it
  - Encrypted at rest
- Send back to AWS.
  - Encrypted in transit

|Name|Definition|
|---|---|
|AWS Import/Export|Ship an HD to AWS, someone plugs it and copies files to S3|
|AWS Snowball|Ruggedized NAS in a box that AWS ships. Copy over 80TB of data and ship back. They copy the data to S3|
|AWS Snowball Edge|Same as snowball, but with onboard computing power such as lambda and clustering, "portable AWS" capture and process data in a very remote location|
|AWS Snowmobile|A literal shipping container full of storage (up to 100PB) and a truck to transport it, then load it to S3|

> ruggedized: designed or improved to be hard-wearing or shock-resistant.

### **Pro Tips**

---

- Technology is often a minor part of a cloud migration project
- Project management discipline is a must
- Adapt the cloud adoption framework for your own organization culture
