# **Identity Access Management & S3**

- [**Identity Access Management & S3**](#identity-access-management--s3)
  - [**IAM**](#iam)
    - [Features](#features)
    - [Terminology](#terminology)
      - [Users](#users)
      - [Groups](#groups)
      - [Policies](#policies)
      - [Roles](#roles)
    - [Root account](#root-account)
    - [IAM Security status](#iam-security-status)
    - [IAM notes](#iam-notes)
  - [**Billing alarm**](#billing-alarm)
  - [**S3**](#s3)
    - [Basics](#basics)
    - [Data Consistency model for s3](#data-consistency-model-for-s3)
    - [Guarantees](#guarantees)
    - [Features](#features-1)
    - [Storage classes](#storage-classes)
      - [S3 standard](#s3-standard)
      - [S3 - IA](#s3---ia)
      - [S3 one zone - IA](#s3-one-zone---ia)
      - [S3 - inteligent tiering](#s3---inteligent-tiering)
      - [S3 - glacier](#s3---glacier)
      - [S3 - glacier deep archive](#s3---glacier-deep-archive)
      - [RRS (Reduce Redundanc storage)](#rrs-reduce-redundanc-storage)
    - [S3 charges](#s3-charges)
    - [Cross region replication](#cross-region-replication)
    - [s3 transfer acceleration](#s3-transfer-acceleration)
    - [s3 notes](#s3-notes)

## **IAM**

---

> allows to manage users and their level of access to the AWS account

- Global basis

### Features

- centralised control of AWS account
- Shared access to AWS account
- Granular permissions
- Identity federation (active directory, facebook, etc.)
- MFA
- Temporary access for users/devices
- Set up password rotation policy
- Integrates with many AWS services
- Supports PCI DSS compliance

### Terminology

#### Users

- People
- employee
- can user console and programatic access

#### Groups

- Collection of users
- each user inherit the permissions of the group

#### Policies

- Made up documents
  - Policy documents
- Json format
- Give permissions what a user/group/role can do

#### Roles

- Create a role and assign to AWS resources
- way for one AWS service to use another AWS service

### Root account

- Is the email the one the account was created
- God-mode
  - Can do anything
- Enable MFA
  - Store the QR code in case you lose the device
  - Re-enable MFA

### IAM Security status

- Delete root access keys
- Enable MFA on root
- Create individual users
- Use groups to assign permissions
- Apply an IAM pswword policy

### IAM notes

- new users have no permissions when first created
- new user are assigned Access key ID and secret access keys when created (if specified)
  - Not the same as password
  - you only view them once

## **Billing alarm**

---

> amount set once that the bill goes over a threshhold

- Send the alarm through SNS topic
- a way to get automatic notifications if account goes over a certain amount
  - Go to cloudwatch and create billing alarm

## **S3**

---

> provides secure, durable, highly-scablable object storage

- safe place to store files
- object-based storage
  - pics
  - videos
  - text
- data is spread trhough multiple devices and facilities

### Basics

- Object-based
  - files
  - key (name of the object)
  - value (data, sequence of bytes)
  - version ID (multiple versions of the file)
  - metadata
  - subresources
    - Access control list
    - torren
- from 0 bytes to 5 TB
- Unlimited storages
- Files are stored in bucket
  - "folder"
- Universal namescape
  - Must be unique globally
  - creates a web address
- uploading files respond with http code
  - 200 if succesful

### Data Consistency model for s3

- read after write consistency for PUTS of new object
- eventual consistency for overwrite PUTS and DELETES (can take time to propagate)

### Guarantees

- built for 99.99& availability
- amazon guarantee 99.9% availability
- amazon guarantee 99.999999999 durability (11 x 9s)

### Features

- tiered storage
- lifecycle management
- versioning
- encryption
- MFA for delete
- secure data using access control lists and bucket policies

### Storage classes

#### S3 standard

- 99.99% availability
- 99.999999999 durability
- designed to sustain the loss of 2 facilities

#### S3 - IA

- data that is access less frequently
- rapid access when needed
- lower charge than s3, charged a retreival fee

#### S3 one zone - IA

- not require multiple AZ data resilience
- lower cost

#### S3 - inteligent tiering

- uses ML
- moves objects to the most cost-effective access tier

#### S3 - glacier

- data archiving
- super cheap
- retrieval time configurable

#### S3 - glacier deep archive

- cheapest
- long retrieval times

#### RRS (Reduce Redundanc storage)

- being phased out

![s3 comparison](/aws/foundational-level/cloud-practitioner/notes/media/s3-comparison.PNG)

### S3 charges

- Storage
- requests
- storage management pricing
  - tiers
- data transfer pricing
- transfer acceleration
- Cross region replication (CRR)

### Cross region replication

- replicates bjects from a bucket from a region to another bucket at another region

### s3 transfer acceleration

- fast, easy, secure transfer of files over long distances netween users and s3
- uses cloudfront edge locations
  - objects go to the edge location than routed to s3 using amazon network

### s3 notes

- not suitable to install an OS on
- not suitable to host DB
- protect object by turning MFA delete
- 