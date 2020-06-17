# **Identity Access Management & S3**

- [**Identity Access Management & S3**](#identity-access-management--s3)
  - [**IAM**](#iam)
    - [Features](#features)
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
    - [s3 Features](#s3-features)
    - [Storage classes](#storage-classes)
      - [S3 standard](#s3-standard)
      - [S3 - IA](#s3---ia)
      - [S3 one zone - IA](#s3-one-zone---ia)
      - [S3 - intelligent tiering](#s3---intelligent-tiering)
      - [S3 - glacier](#s3---glacier)
      - [S3 - glacier deep archive](#s3---glacier-deep-archive)
      - [RRS (Reduce Redundance storage)](#rrs-reduce-redundance-storage)
    - [charges](#charges)
    - [Cross region replication](#cross-region-replication)
    - [transfer acceleration](#transfer-acceleration)
    - [Access control list (ACLs)](#access-control-list-acls)
    - [Bucket policies](#bucket-policies)
    - [pricing tiers](#pricing-tiers)
    - [Security](#security)
    - [encryption](#encryption)
    - [versioning](#versioning)
    - [lifecycle management](#lifecycle-management)
    - [Sharing s3 buckets across accounts](#sharing-s3-buckets-across-accounts)
    - [Cross region replication (CRR)](#cross-region-replication-crr)
    - [Transfer acceleration](#transfer-acceleration-1)
    - [s3 notes](#s3-notes)
  - [**Organizations**](#organizations)
    - [Consolidated billing](#consolidated-billing)
    - [organization notes](#organization-notes)
  - [**CloudFront**](#cloudfront)
    - [Edge location](#edge-location)
    - [Origin](#origin)
    - [Distribution](#distribution)
    - [Web distribution](#web-distribution)
    - [RTMP](#rtmp)

## **IAM**

---

> allows to manage users and their level of access to the AWS account

- Global basis

### Features

- centralized control of AWS account
- Shared access to AWS account
- Granular permissions
- Identity federation (active directory, facebook, etc.)
- MFA
- Temporary access for users/devices
- Set up password rotation policy
- Integrates with many AWS services
- Supports PCI DSS compliance

#### Users

- People
- employee
- can user console and programmatic access

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
- Apply an IAM password policy

### IAM notes

- new users have no permissions when first created
- new user are assigned Access key ID and secret access keys when created (if specified)
  - Not the same as password
  - you only view them once

## **Billing alarm**

---

> amount set once that the bill goes over a threshold

- Send the alarm through SNS topic
- a way to get automatic notifications if account goes over a certain amount
  - Go to cloudwatch and create billing alarm

## **S3**

---

> provides secure, durable, highly-scalable object storage

- safe place to store files
- object-based storage
  - pics
  - videos
  - text
- data is spread through multiple devices and facilities

### Basics

- Object-based
  - files
  - key (name of the object)
  - value (data, sequence of bytes)
  - version ID (multiple versions of the file)
  - metadata
  - subresources
    - Access control list
    - torrent
- from 0 bytes to 5 TB
- Unlimited storages
- Files are stored in bucket
  - "folder"
- Universal namespace
  - Must be unique globally
  - creates a web address
- uploading files respond with http code
  - 200 if successful

### Data Consistency model for s3

- read after write consistency for PUTS of new object
- eventual consistency for overwrite PUTS and DELETES (can take time to propagate)

### Guarantees

- built for 99.99& availability
- amazon guarantee 99.9% availability
- amazon guarantee 99.999999999 durability (11 x 9s)

### s3 Features

- tiered storage
- lifecycle management
- versioning
- encryption
- MFA for delete
- secure data using access control lists and bucket policies

### Storage classes

- you can change storage class object-level or bucket level

#### S3 standard

- 99.99% availability
- 99.999999999 durability
- designed to sustain the loss of 2 facilities

#### S3 - IA

- data that is access less frequently
- rapid access when needed
- lower charge than s3, charged a retrieval fee

#### S3 one zone - IA

- not require multiple AZ data resilience
- lower cost

#### S3 - intelligent tiering

- uses ML
- moves objects to the most cost-effective access tier

#### S3 - glacier

- data archiving
- super cheap
- retrieval time configurable

#### S3 - glacier deep archive

- cheapest
- long retrieval times

#### RRS (Reduce Redundance storage)

- being phased out

![s3 comparison](/aws/foundational-level/cloud-practitioner/notes/media/s3-comparison.PNG)

### charges

- Storage
- requests and data retrievals
- storage management pricing
  - tiers
- data transfer pricing
- transfer acceleration
- Cross region replication (CRR)

### Cross region replication

- replicates objects from a bucket from a region to another bucket at another region

### transfer acceleration

- fast, easy, secure transfer of files over long distances between users and s3
- uses cloudfront edge locations
  - objects go to the edge location than routed to s3 using amazon network

### Access control list (ACLs)

> allows setting fine grain permissions all the way down to individual object

### Bucket policies

> allows setting permission to the bucket level

### pricing tiers

- prices from expensive to cheapest
  - standard, intelligent tiering, IA, 1Z - IA, glacier, deep archive

### Security

- by default all newly created bucket are private
- control access to bucket by
  - bucket policies
  - access control lists
- Can be configured to create access logs, which log all requests made to the s3 bucket
  - this logs can be sent to another bucket or another bucket in another account

### encryption

> if you go https, means the traffic is encrypted in transit

- in transit achieved bye
  - SSL/TLS
- at rest (server side)
  - s3 managed keys - SSE - s3 (aws manages the keys, AES-256)
  - aws key management service, managed keys, SSE - KMS (you and AWS manage keys together)
  - server side encryption with customer provided keys - SSE - C (you manage the keys, give it to aws to encrypt bucket)
  - client side encryption (encrypt the object before uploading)

### versioning

> stores all version of an object (including all writes even delete objects)

- backup tool
- once enabled, cannot be disabled, only suspended
- integrates with lifecycle rules
- MFA delete capability, additional layer of security
- size of a bucket is a sum of all the versions of the objects in the bucket
  - have in mind large files
- deleting the object, just puts a "delete marker"
  - simply a new version
  - to restore a version, just delete the delete marker
- versions can be deleted

### lifecycle management

> automates transition of objects to different tiers of storage

- it could expire objects as well
- works with object tags
- storage class transition
  - current version
    - transition for current version
    - select a tier of storage and days
  - previous version
    - transition for previous version
- configure expiration
  - current and previous versions
  - select days after object creation
  - clean up incomplete multipart uploads
- works in conjunction with versioning

### Sharing s3 buckets across accounts

- ways to share buckets across accounts
  - using bucket policies and IAM (applies entire bucket)
    - programmatic access only
  - using ACLs and IAM (individual object)
    - programmatic access only
  - IAM roles
    - programmatic and console access
    - you create a role in the account sharing the buckets, and give permission to the account you want to access the buckets

### Cross region replication (CRR)

- requires versioning to be enable in source and destination
- doesn't replicated objects previously created
- Replication level
  - entire bucket
  - prefix or tags
- destination bucket
  - same account
  - different account
  - new bucket, or existing
  - change storage class
  - change ownership
- iam role
  - enables the replication between buckets
  - new
  - exiting
- doesn't replicate
  - delete markers
  - deleted version

### Transfer acceleration

> utilizes the cloudfront edge network to accelerate uploads to s3

- instead uploading to a bucket, uses a distinct url to upload to an edge location
  - bucket.s3-accelerate.amazonaws.com

### s3 notes

- not suitable to install an OS on
- not suitable to host DB
- protect object by turning MFA delete
- object-level logging, records object level API activity
- private by default
- overwriting a object changes the permissions of the latest version

## **Organizations**

---

> account management service that enables to consolidate multiple aws accounts into an organization that you create and centrally manage

- root account
  - master account
  - use this for billing only
- within organization we have OUs
- apply permission using policies document (SCP)
  - inherited by OUs
  - individual accounts
- creating an organization makes the account a root account
- invite or create accounts

### Consolidated billing

- takes into account the aggregated of all the accounts
  - the more you use S3 the less you pay
- paying account
  - independent
- linked accounts
  - independent
- monthly bill
  - add all the accounts
  - best price possible
  - volume pricing discount

### organization notes

- enable MFA and strong password on root account
- paying account only for billing

## **CloudFront**

---

> CDN content delivery network, system of distributed servers (network) that deliver webpages and other web content to a user based on the geographic location of the user, the origin of the webpage, and content delivery server

- user query to the edge location
  - if the edge location doesn't have a copy of the file will cached the file to the edge location in a TTL (time to live) in seconds
  - if the edge location has a copy of the file, the user will download it from the edge location, faster
- deliver entire website
  - dynamic
  - static
  - streaming
- not just read only, you can write to them too (put object)
- objects are cached for the TTL
- can clear cached objects, but has a charge, invalidation cache
  - entire directories
  - certain objects
  - good for new version of the object
- global service
- restrict bucket to only use cloudfront urls
  - useful for signed urls
- restrict access using signed URLs or cookies
- can use WAFs

### Edge location

- location where the content is cached
- separated to an AWS region/az

### Origin

- origin of the files that the CDN distributes
  - s3
  - ec2 instance
  - elb
  - r53

### Distribution

- name given to the CDN
- collection of edge locations

### Web distribution

- used for websites

### RTMP

- used for media streaming
- adobe flash media servers
