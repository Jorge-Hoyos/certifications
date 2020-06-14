# Security In The Cloud notes

Third part of the a cloud guru course

- [Security In The Cloud notes](#security-in-the-cloud-notes)
  - [**Compliance and AWS artifact**](#compliance-and-aws-artifact)
    - [Programs](#programs)
    - [Artifact](#artifact)
  - [**Shared responsibility model**](#shared-responsibility-model)
    - [AWS responsibilities](#aws-responsibilities)
    - [Customer responsibilities](#customer-responsibilities)
    - [shared responsibility tips](#shared-responsibility-tips)
  - [**WAF**](#waf)
  - [**Shield**](#shield)
    - [Standard](#standard)
    - [Advanced](#advanced)
  - [**Inspector**](#inspector)
  - [**Trusted advisor**](#trusted-advisor)
    - [cost optimization](#cost-optimization)
    - [security](#security)
    - [fault tolerance](#fault-tolerance)
    - [performance](#performance)
    - [Service limits](#service-limits)
    - [core checks and recommendations](#core-checks-and-recommendations)
    - [full trusted advisor](#full-trusted-advisor)
  - [**Cloudtrail**](#cloudtrail)
  - [**Config**](#config)
  - [**Athena**](#athena)
    - [Used for](#used-for)
  - [**Macie**](#macie)

## **Compliance and AWS artifact**

---

[amazon.com/compliance](https://aws.amazon.com/compliance/)

### Programs

- CSA
Cloud Security Alliance Controls

- ISO 9001
Global Quality Standard

- ISO 27001
Security Management Controls

- ISO 27017
Cloud Specific Controls

- ISO 27018
Personal Data Protection

- PCI DSS Level 1
Payment Card Standards

- SOC 1
Audit Controls Report

- SOC 2
Security, Availability, & Confidentiality Report

- SOC 3
General Controls Report

### Artifact

> comprehensive list of access-controlled documents relevant to compliance and security in the AWS cloud

## **Shared responsibility model**

---

[aws-shared-responsibility-model](https://aws.amazon.com/compliance/shared-responsibility-model/)

- AWS manages the security OF the Cloud
- customers manage the security IN the cloud

![shared-responsibility-model](media/shared-responsibility-model.PNG)

### AWS responsibilities

- data centers
- region
- edge locations
- hardware
- AZs
- software (hypervisor)
  - RDS OS

### Customer responsibilities

- EC2 instances patches
- client side data
- server side encryption
- networking traffic
- OS
- network
- FW
- IAM

### shared responsibility tips

- can it be done in the aws console or in ec2?
  - if yes, you are responsible (SG, IAM, patching OS)
  - if not, AWS is responsible
- encryption is a shared responsibility
  - you are responsible for turning encryption
  - aws is responsible for the encryption
- AWS takes responsibility for managing all the hardware (including access, patching and other maintenance).
  - AWS responsibility to make sure that they never run out of storage.
  - Replication to another AZ is also AWS's responsibility in an applicable storage tier
  - AWS is also responsible for managing data corruption and resolving it if corruption is detected - however if it cannot fix the corruption, or if data is lost, AWS bears no responsibility for the loss - therefore it is a customer's responsibility to make sure there data is backup up as needed - either though versioning in S3, or through 3rd party tools.

## **WAF**

---

> web application firewall

- helps you protect your web application from common web exploits
- firewall that inspects web traffic, looking for malicious things
  - cross-site scripting
  - SQL injections
- normal firewall work at layer 4
- WAF works at layer 7, can see the traffic of the application layer

![waf](media/waf.PNG)

## **Shield**

> managed DDos protection service that safeguard web applications running on aws

DDoS:
Someone sends a lot of traffic, so much traffic that the server goes down

### Standard

- turns in automatically

### Advanced

- $3000 a month
- offers automated application layer monitoring.

## **Inspector**

---

> automated security assessment service that helps improve the security and compliance of applications deployed on AWS

- assess apps for vulnerabilities
- detailed list of findings
- agent installed on ec2, looking for common vulnerabilities
  - port open
  - OS patches
  - produce a report

## **Trusted advisor**

---

[Trusted advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)

[Trusted advisor best practice checklist](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)

> Helps reduce cost, increase performance, and improve security by optimizing your aws environment

- real time guidance
- entire AWS environment
- global

### cost optimization

- Amazon EC2 Reserved Instances optimization
- Low utilization Amazon EC2 instances
- Idle load balancers
- Underutilized Amazon EBS volumes

### security

- Security groups - Specific ports unrestricted (free)

### fault tolerance

- Amazon EBS snapshots

### performance

- High utilization Amazon EC2 instances

### Service limits

- Checks for service usage that is more than 80% of the service limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes.

### core checks and recommendations

free

### full trusted advisor

business and enterprise only

## **Cloudtrail**

---

- monitors API call
- records everything on the AWS environment
- record management console and API calls

## **Config**

---

> detailed view of the configuration of aws resources

- how are they related
- how were they in the past
- monitors your configuration of the environment

## **Athena**

---

> interactive query service which enables you to analyse and query data in S3 using standard SQL

- interactive query service
- querying data in S3
- Serverless
  - pey per requests
  - per TB scanned
- no need to set up complex (ETL)
- works directly with data stored in S3

### Used for

- Generates business reports
- cost and usage report
- query log files stored in s3

## **Macie**

---

> PII (personal identifiable information)

- personal data used to establish an individuals identity
- can be exploited by criminals

> Macie: Security service which uses MI and NLP to discover classify and protect sensitive data in s3

- uses AI to recognize if s3 have sensitive data
- dashboard, reportings and alerts
- works with data in s3
- can analyze cloudtrail logs
- great for PCI-DSS compliance
