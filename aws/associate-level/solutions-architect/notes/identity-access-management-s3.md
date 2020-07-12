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
    - [URLs](#urls)
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
        - [retrievals](#retrievals)
      - [S3 - glacier deep archive](#s3---glacier-deep-archive)
      - [RRS (Reduce Redundance storage)](#rrs-reduce-redundance-storage)
    - [charges](#charges)
    - [Cross region replication](#cross-region-replication)
    - [transfer acceleration](#transfer-acceleration)
    - [Datasync](#datasync)
    - [Access control list (ACLs)](#access-control-list-acls)
    - [Bucket policies](#bucket-policies)
    - [pricing tiers](#pricing-tiers)
    - [Security](#security)
    - [encryption](#encryption)
    - [versioning](#versioning)
    - [Object lock](#object-lock)
    - [glacier vault lock](#glacier-vault-lock)
    - [prefixes](#prefixes)
    - [Performance](#performance)
      - [KMS Limits](#kms-limits)
      - [Multipart uploads](#multipart-uploads)
      - [S3 byte-range fetches](#s3-byte-range-fetches)
    - [Select](#select)
    - [Glacier Select](#glacier-select)
    - [lifecycle management](#lifecycle-management)
    - [Sharing s3 buckets across accounts](#sharing-s3-buckets-across-accounts)
    - [Cross region replication (CRR)](#cross-region-replication-crr)
    - [Transfer acceleration](#transfer-acceleration-1)
    - [limits](#limits)
    - [S3 signed URL](#s3-signed-url)
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
    - [Signed URLs](#signed-urls)
    - [Signed cookies](#signed-cookies)
    - [Signed policy](#signed-policy)
  - [**Snowball**](#snowball)
    - [snowball edge](#snowball-edge)
    - [snowmobile](#snowmobile)
  - [**Storage gateway**](#storage-gateway)
    - [Types](#types)
      - [file gateway (NFS and SMB)](#file-gateway-nfs-and-smb)
      - [volume gateway (iSCSI)](#volume-gateway-iscsi)
      - [tape gateway (VTL)](#tape-gateway-vtl)
  - [**Athena**](#athena)
    - [used for](#used-for)
  - [**Macie**](#macie)

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

### URLs

- Virtual style puts your bucket name 1st, s3 2nd, and the region 3rd.
- Path style puts s3 1st and your bucket as a sub domain.
- Legacy Global endpoint has no region.
- S3 static hosting can be your own domain or your bucket name 1st, s3-website 2nd, followed by the region.
- AWS are in the process of phasing out Path style, and support for Legacy Global Endpoint format is limited and discouraged. However it is still useful to be able to recognize them should they show up in logs.

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

##### retrievals

- Cost of retrieval of information from Glacier can go up dependent on how quickly you require the data and how much data is to be retrieved.
- Expedited retrievals allow you to quickly access your data stored in the S3 Glacier storage class when occasional urgent requests for a subset of archives are required, but at the highest cost.
- Standard retrievals allow you to access any of your archived objects within several hours, this is faster than bulk (averaging around 12 hours) but more expensive.
- Bulk retrievals are the lowest-cost retrieval option in Amazon S3 Glacier, enabling you to retrieve large amounts, even petabytes, of data inexpensively.

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

### Datasync

- allows you to move large amounts of data into AWS
- use on premise data center
- install datasync agent
  - server that connects to a NAS or FS
- copy data from and to AWS
- encrypts data
- performs
- connections to
  - s3
  - EFS
  - FSx for windows
- copy data/metadata
- replicate EFS to EFS

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

- in transit achieved by
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

### Object lock

- store objects using a write once, read many model (WORM)
- can be on individual objects or applied across the bucket
- prevent objects from being deleted or modified, for a period of time or indefinitely
- governance
  - users cant overwrite or delete an object version or alter its lock setting, unless they have special permissions, some user can alter retention settings
- compliance
  - a protected object version cant be overwritten or deleted by any user, including the root user
- retention period
  - protects an object version for a fixed amount of time, with a timestamp in the metadata, after the time the object can be deleted unless you place a legal hold on the object version
- legal hold
  - prevent an object version from being overwritten, doesn't have an associated retention period, works until removed bye any user

### glacier vault lock

- easily deploy and enforces compliance control for individual s3 glacier vaults with a vault lock policy
- controls such as worm
- locking objects inside glacier
- once locked the policy cannot be changed

### prefixes

- the pathway between our bucket and our object
- mybucket/folder1/subfolder1/file.jpg
  - /folder1/subfolder1

### Performance

- first byte out of s3 within 100-200 ms
- 3500 PUT/COPY/POST/DELETE per second per prefix
- 5500 GET/HEAD per second per prefix
- get better performance spreading actions across prefixes
  - two prefixes achieve 11000 requests per second
  - four prefixes achieve 22000 requests per second

#### KMS Limits

- uploading file GenerateDataKey API
- downloading file Decrypt API
- uploading/downloading will count toward the KMS quota
- region specific
  - 5500, 10000 or 30000
- cannot request quota increase

#### Multipart uploads

- recommended for files over 100 MB
- required for files over 5 GB
- parallelize uploads (increases efficiency)

#### S3 byte-range fetches

- parallelize downloads by specifying byte ranges
- if failure, only for a specific byte range
- speed up downloads

### Select

- enables application to retrieve only a subset of data from an object by using simple SQL
- achieve performance increases
- 400% faster
- 80% cheaper

### Glacier Select

- run SQL queries against glacier directly

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

### limits

- 100 buckets
- 3500 PUTS

### S3 signed URL

- issues a request as the IAM user who created the presigned URL
- limited lifetime

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
- enable/disable AWS services using SCP either on OU or on individual accounts

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

#### Web distribution

- used for websites

#### RTMP

- used for media streaming
- adobe flash media servers

### Signed URLs

- way to secure content so only certain people can access it
- individual files
- 1 file = 1 url
- use OAI (origin access identity) to access the file
- use SDK to generate signed URL
- Key-pair is account wide and managed by the root user
- can have multiple origins

### Signed cookies

- multiple files
- 1 cookie = multiple files

### Signed policy

- URL expiration
- IP ranges
- trusted signers

## **Snowball**

---

> petabyte scale data transfer solutions

- transfer large amounts of data into and out of AWS
- address challenges like
  - high network costs
  - long transfer times
  - security concerns
- Sizes
  - 50TB
  - 80TB
- security
  - tamper-resistant enclosure
  - 265-bit encryption
  - industry trusted platform module (TPM)
- AWS performs software erase of the snowball
- import to s3
- export from s3
- needs a client to connect
- needs credential to authenticate
- needs a role to transfer information

![snowball](/aws/foundational-level/cloud-practitioner/notes/media/snowball.PNG)

### snowball edge

- 100TB
- on board computing and storage capabilities
- support local workloads
- connects to existing apps and infrastructure using standard storage interfaces
- can cluster together

### snowmobile

- exabyte-scale data transfer
- up to 100PB per snowmobile
- complete data center

## **Storage gateway**

---

> service that connect an on premise software appliance with cloud-based storage to provide seamless and secure integration

- securely store data to the aws cloud for scalable cost and effective storage
- virtual or physical devices
- that replicates data to aws
- download as a VM
  - supports VMware ESXi
  - microsoft Hyper-V

### Types

#### file gateway (NFS and SMB)

- storing flat files directly in S3
- files are stored as objects in the bucket, accessed through a network file system
- once transferred they are managed as native s3 objects

#### volume gateway (iSCSI)

- presents applications with disk volumes using the iSCSI protocol
- data written can be asynchronously backed up as in-time snapshots, and stored in amazons ebs snapshots
- storing copies of your hard drives or HDD in s3 as EBS snapshots
- stored volumes
  - store primary data locally
  - backing data to AWS
  - entire data set is store on site
- cached volumes
  - entire dataset is stored on s3
  - most frequently access data is cached on site

#### tape gateway (VTL)

- durable, cost-effective solution to archive your data in the AWS cloud
- getting rid of tapes

## **Athena**

---

> interactive query service, which enables you to analyse and query data located in S3 using standard SQL

- serverless, nothing to provision
- turn s3 into a giant database
- pay per query / per TB scanned
- no need to set up complex ETL
- works directly with data on s3
- supports
  - json
  - apache parquet
  - apache ORC

### used for

- query log files
  - ELB logs
  - S3 access logs
- generate business reports on data stored in s3
- analyse AWS cost and usage reports
- run queries on click-stream data

## **Macie**

---

> security service that uses MI and NLP to discover, classify and protect sensitive data stored in s3

- uses AI to recognize if your s3 objects contain sensitive data such as PII
- dashboard, reporting and alerts
- works with data stored in s3
- can also analyze trail logs
- great for PCI-DSS
