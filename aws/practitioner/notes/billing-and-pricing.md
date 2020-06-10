# Billing & Pricing

Second part of the A Cloud Guru course

- [Billing & Pricing](#billing--pricing)
  - [**How AWS pricing works**](#how-aws-pricing-works)
    - [CAPEX](#capex)
    - [OPEX](#opex)
    - [Pricing policies](#pricing-policies)
    - [Best practices](#best-practices)
      - [Understand the fundamentals of pricing](#understand-the-fundamentals-of-pricing)
      - [start early with cost optimization](#start-early-with-cost-optimization)
      - [maximize the power of flexibility](#maximize-the-power-of-flexibility)
      - [use the right pricing moduel for the jobs](#use-the-right-pricing-moduel-for-the-jobs)
    - [Free tier](#free-tier)
      - [free services](#free-services)
    - [EC2 pricing](#ec2-pricing)
      - [EC2 pricing models](#ec2-pricing-models)
    - [Lambda pricing](#lambda-pricing)
    - [EBS pricing](#ebs-pricing)
    - [S3 pricing](#s3-pricing)
    - [Glacier pricing](#glacier-pricing)
    - [Snowball pricing](#snowball-pricing)
    - [RDS pricing](#rds-pricing)
    - [DynamoDB pricing](#dynamodb-pricing)
    - [Cloudfronmt pricing](#cloudfronmt-pricing)
  - [**Budget**](#budget)
  - [**Cost explorer**](#cost-explorer)
  - [**Support plans**](#support-plans)
    - [Basic](#basic)
    - [Developer](#developer)
    - [Business](#business)
    - [Enterprise](#enterprise)
    - [TAM](#tam)
    - [Response times](#response-times)
  - [**Tagging and resource groups**](#tagging-and-resource-groups)
    - [Tags](#tags)
      - [Tags information](#tags-information)
    - [Resource group](#resource-group)
      - [Create groups (SSM)](#create-groups-ssm)
    - [Tag Editor](#tag-editor)

## **How AWS pricing works**

---


### CAPEX

> capital expenditure, where you pay up front

### OPEX

> operational expenditure, pay for what you use

### Pricing policies

- You pay as you go
- pay for what you use
- pay less as you use more
- pay even less when reserve

### Best practices

#### Understand the fundamentals of pricing

- compute
- storage
- data outbound

#### start early with cost optimization

- put cost visibility
- control mechanisims
  - before the enviroment grows large and complex

#### maximize the power of flexibility

- no minimum commtment
- pay for service on an as-needed basis
  - focus on innovation and invention
  - reducing procurement complexity
  - enabling business to be fully elastic
- Dont pay for them when not using

#### use the right pricing moduel for the jobs

- on demand
- dedicated instances
- spot instances
- reservations

### Free tier

> help new customers, run free amazon resources

#### free services

- VPC (virtual data center in the cloud)
- Elastic Beanstalk (resources that it provisions are not free)
- Cloudformation
- IAM
- Auto Scaling
- OpsWorks
- Consolidated billing

### EC2 pricing

What determines price:

- clock hours of server time
- instance type
- pricing mode
- number of instances
- load balancing
- detailed monitoring (if enabled)
- Auto scaling (if creates instances)
- Elastic IP Addresses
- Operating systems and software packages

#### EC2 pricing models

- on demand
  - fixed rates
- reserved
  - discount based on contract time and up front payment ![reserved 3 years contract](media/reserved-3-year-contract.PNG)
- spot
  - bid on capacity
- dedicated hosted
  - physical EC2 server

### Lambda pricing

- Request pricing
  - Free tier: 1 million requests per month
  - $0.20 per 1 million request thereafter
- duration pricing
  - 400.000 GB-seconds per month free, up to 3.2 million seconds of compute time
- aditional charges
  - Reads and write data to s3

### EBS pricing

- Volumes (per GB)
- snapshots (per GB)
- data transfer

### S3 pricing

- Storage class (standar, intelligent-tiering, etc.)
- Storage
- Requets (GET, PUT COPY)
- data transfer

### Glacier pricing

- Storage
- data retrieval time ![glacier pricing](media/glacier-pricing.PNG)

### Snowball pricing

> PB-scale data transport solution, gigantic disk used to move data in to AWS

- service fee per job
  - 50 TB: $200
  - 80 TB: $250
- daily charge
  - first 10 days free, after $15 a day
- data transfer
  - in to AWS free, out is not

### RDS pricing

- Clock hours of server time
- DB characteristic (if SQL)
- DB purchase type
- number of DB instances
- provisioned storage (how big in GB)
- additional storage
- requests
- deployment type
- data transfer

### DynamoDB pricing

![dynamodb pricing](media/dynamodb-pricing.PNG)

### Cloudfronmt pricing

- traffic distribution
- requests
- data transfer out

## **Budget**

---

> gives the abulity to set custom budgets that alert yo when your costs or usage exceed or are near

- Use it to budget cost BEFORE they have been icurred
- has to be enabled

## **Cost explorer**

---

> interface that allows to visualize, understand and manage AWS cost over time

- Used to explore cost AFTER they have been incurred

## **Support plans**

---

![support-plans](media/support-plans.PNG)

### Basic

- Free

### Developer

- $29

### Business

- $100

### Enterprise

- $15000

### TAM

Someone who is dedicated at AWS for your business

### Response times

![support-plans2](media/support-plans2.PNG)

## **Tagging and resource groups**

---

### Tags

- Key value pairs attached to AWS resources
- metadata
- tags can be inherited

#### Tags information

- EC2 - public and ip address
- ELB - port configurations
- RDS - DB engine

### Resource group

> make it easy to group resources using tags assigned to them, can group resources that share one or more tags

- group resources by
  - Region
  - name
  - employee ID
  - env
- resources can be grouped

#### Create groups (SSM)

> query based group

- per region basis
- Lets you run SSM automations on the resource groups

### Tag Editor

> great way to find all your tags, and resources, and create new tags

- Global service

- Select
  - regions
  - resource types
  - tags
