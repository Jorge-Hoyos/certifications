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