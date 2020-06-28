# **Databases On AWS**

- [**Databases On AWS**](#databases-on-aws)
  - [**Databases 101**](#databases-101)
    - [Relational databases (SQL - OLTP)](#relational-databases-sql---oltp)
      - [SQL server](#sql-server)
      - [Oracle](#oracle)
      - [MySQL](#mysql)
      - [MariaDB](#mariadb)
      - [Aurora](#aurora)
      - [PostgreSQL](#postgresql)
      - [Features](#features)
    - [Non relational Databases (NoSQL)](#non-relational-databases-nosql)
      - [DynamoDB](#dynamodb)
    - [Data warehousing - Redshift](#data-warehousing---redshift)
    - [OLTP](#oltp)
    - [OLAP](#olap)
    - [ElastiCache](#elasticache)
      - [Memcached](#memcached)
      - [Redis](#redis)
  - [**Database notes**](#database-notes)
  - [**Backups**](#backups)
    - [automated backups](#automated-backups)
    - [Database snapshots](#database-snapshots)
    - [backups notes](#backups-notes)
  - [**Encryption**](#encryption)
    - [Encryption at rest](#encryption-at-rest)
  - [**Multi AZ**](#multi-az)
  - [**Read replica**](#read-replica)
  - [**DynamoDB**](#dynamodb-1)
    - [Basics](#basics)
    - [eventual consistent reads (default)](#eventual-consistent-reads-default)
    - [strongly consistent read](#strongly-consistent-read)
    - [DAX](#dax)
    - [Transactions](#transactions)
    - [On-demand capacity](#on-demand-capacity)
    - [Backup and restore](#backup-and-restore)
      - [PITR (point in time recovery)](#pitr-point-in-time-recovery)
    - [streams](#streams)
    - [global tables](#global-tables)
    - [DMS dynamodb](#dms-dynamodb)
    - [security](#security)
  - [**Redshift**](#redshift)
    - [Configuration](#configuration)
    - [Advanced compression](#advanced-compression)
    - [massive parallel processing (MPP)](#massive-parallel-processing-mpp)
    - [backups](#backups-1)
    - [pricing](#pricing)
    - [redshift security](#redshift-security)
    - [availability](#availability)
  - [**Aurora**](#aurora-1)
    - [Scaling aurora](#scaling-aurora)
    - [Replicas](#replicas)
    - [aurora backups](#aurora-backups)
    - [Aurora serverless](#aurora-serverless)
  - [**Elasticache**](#elasticache-1)
    - [Memcached vs redis](#memcached-vs-redis)
  - [**DMS**](#dms)
    - [Homogenous migrations](#homogenous-migrations)
    - [heterogeneous migrations](#heterogeneous-migrations)
    - [Sources](#sources)
    - [targets](#targets)
  - [**Caching strategies**](#caching-strategies)
  - [**EMR**](#emr)
    - [cluster](#cluster)
    - [Master node](#master-node)
    - [Core node](#core-node)
    - [Task node](#task-node)

## **Databases 101**

---

### Relational databases (SQL - OLTP)

- traditional spreadsheet
  - database
  - tables
  - row
  - fields (columns)

#### SQL server

#### Oracle

#### MySQL

#### MariaDB

#### Aurora

#### PostgreSQL

#### Features

- multi AZ for DR
  - fail over is automatic with AZ
  - if dns fails, points to a different DB
- Read replicas for performance
  - every write is replicated to other DB
  - no automatic failover
  - up to 5 copies

### Non relational Databases (NoSQL)

- collection = table
- Document = row
- key value pairs = field (columns)
- new field doesn't affect other

#### DynamoDB

### Data warehousing - Redshift

- used for BI
- used to pull in very large and complex data sets
- do queries on data
- different type of architecture from a DB perspective and infrastructure layer

### OLTP

- queries are on a single record

### OLAP

- pull in large number of records
- huge number of queries

### ElastiCache

- Deploy, operate and scale an in-memory cache in the cloud
- improves performance of web apps by allowing to retrieve information from fast, managed, in memory cached
- caches the most common queries

#### Memcached

#### Redis

## **Database notes**

---

- RDS runs on VM
- cannot log in to these OS
- patching of OS and DN is AWS responsibility
- RDS is NOT serverless
  - except aurora serverless
- RDS automated backups by default
- you can select the AZ you are deploying
- with a DB security group the RDS instance port number is automatically applied to the RDS DB Security Group.

## **Backups**

---

### automated backups

- recover your db in any point in time, within a retention period
  - 1 - 35 days
- full daily snapshots
- store transaction logs
- enable by default
- store in s3
- free storage equal to the size of your DB
- taken within a defined window
- deleted with the instance

### Database snapshots

- manually
- they are stored after delete the RDS

### backups notes

- when restoring, the RDS will have a new DNS endpoint

## **Encryption**

---

### Encryption at rest

supported for:

- MySQL
- oracle
- SQL server
- PostgreSQL
- MariaDB
- Aurora

encryption is done using KMS
once the RDS is encrypted, the data stored is encrypted, automated backups, read replicas and snapshots

## **Multi AZ**

---

- allows you to have an exact copy of your production DB in another AZ
- AWS handles the replication
- RDS automatically failover to the standby in case of failures
  - no manual intervention
- for DR only
- only for
  - MySQL
  - oracle
  - SQL server
  - PostgreSQL
  - MariaDB

## **Read replica**

---

- allows read-only copy of the DB
- asynchronous replication form the primary RDS
- heavy read DB workload
- there can be a read replica from a read replica
- used for scaling or performance
- must have automated backup on
- up to 5 RR of any DB
- each RR will have its own DNS endpoint
- can create RR of Multi AZ
- RR can have Multi AZ
- can be promoted to its own DB
  - breaks the read replication
- can be in another region
- SQL server doesn't support read replicas

## **DynamoDB**

---

> fast and flexible NoSQL DB

- single digit millisecond latency at any scale
- supports data models
  - document
  - key-value

### Basics

- stored on SSD storage
- spread across 3 geographically distinct data centers

### eventual consistent reads (default)

- consistency across all copies of data is usually reached within a second
- repeating a read after a short time should return the updated data
- best read performance

### strongly consistent read

- less than a second
- reflects all writes that received a successful response prior to read

### DAX

- fully managed, HA, in-memory cache
- 10x performance improvement
- reduces request time from milliseconds to microseconds
- compatible with dynamo API calls
- no code changes to app
- write/read performance improvements

![dax](/aws/associate-level/solutions-architect/media/dax.PNG)

### Transactions

- multiple 'all or nothing' operations
  - when you need to debit from one account to another
  - financial transaction
  - fulfilling orders
- two underlying reads or write - prepare/commit
- up to 25 items or 4 MB of data

### On-demand capacity

- pay per request pricing
- balance cost and performance
- adapts rapidly to new workload
- no minimum capacity
- no read/write charges when table is idle
  - only pay for storage and backups
- pay more per request

### Backup and restore

- full backups at any time
- zero impact on table performance or availability
- consistent within seconds and retained until deleted
- operates within same region as the source table
  - not across regions

#### PITR (point in time recovery)

- protects against accidental write or deletes
- restore to any point within 35 days
- incremental backus
- not enable by default
- latest restorable: 5 minutes

### streams

- time ordered sequence of item level changes in a table
- stored for 24 hours
- inserts, updates, and deletes
- stream record
- shard
  - multiple stream records
- cross region replication
  - global tables
- relations between tables
- combine with lambda for functionality like stored procedures

### global tables

- managed multi-master, multi region replication
- globally distributed applications
- based on dynamodb streams
- for DR or HA
- no need to do changes in the application
- replication latency under once second
- must enable streams enabled

### DMS dynamodb

- source DB
  - completely operational during transfer
- target DB
  - can be DynamoDB
- configure all data transformation logic inside DMS and it preforms the migration automatically

### security

- encryption using KMS
- site to site VPN
- direct connect
- IAM policies and roles
- fine grained access
- cloudwatch and cloudtrail
- vpc endpoints

## **Redshift**

---

> fast and powerful, fully managed, petabyte-scale data warehousing

- can start 0.25 per hour
- scale to petabyte or more for $1000 per terabyte per year
- data warehousing use different type of architecture both from a db and infrastructure layer

### Configuration

- single node (160Gb)
- Multi-node
  - Leader node (manages client connections and receives queries)
  - compute node (store data and perform queries and computation) up to 128 compute nodes

### Advanced compression

- compress column, cause all the data is the same
- doesn't requires index
- selects the best compression scheme

### massive parallel processing (MPP)

- automatically distributes data and query load across all nodes
- easy to add nodes and enables fast queries performance as your data warehouse grows

### backups

- enables by default, 1 day
- 1-35 day retention period
- attempts to maintain 3 copies of your data
  - original on compute nodes
  - replica on compute nodes
  - backup on s3
- asynchronously replicate snapshots to s3 in another region for DR

### pricing

- compute node hours, 1 unit per compute node per hour
- backup
- data transfer (within a vpc, not outside it)

### redshift security

- encrypted in transit using SSL
- encrypted at rest using AES-256 encryption
- by default redshift manages keys

### availability

- 1 AZ
- can restore snapshots to ner AZs in failure

## **Aurora**

---

> amazon own database

- mysql and postgresql compatible relational db engine
- combines speed and HA with simplicity and cost-effectiveness
- up to 5 times better performance than MySQL and 3 times than PostgreSQL
  - much lower prices
- starts 10 Gb
  - scales 10Gb increment, up to 64 Tb (storage autoscaling)
- compute resources can scale up to 32vCPUs and 244 GB of memory
- 2 copies of your data is contained in each AZ, with minimum of 3 AZ. 6 copies of data

### Scaling aurora

- handle the loss of up to two copies of data, without affecting db write availability
- up to 3 copies of data without affecting read availability
- storage is self-healing
  - data blocks and disks are scanned for error and repaired automatically

### Replicas

- Aurora replicas (currently 15)
- MySQL ready replicas (currently 5)
- postgresql (currently 1)

![aurora](/aws/associate-level/solutions-architect/media/aurora.PNG)

### aurora backups

- automatic backups always enabled on aurora
  - do not impact performance
- also manual snapshots
- can share aurora snapshots cross accounts

### Aurora serverless

- on-demand, autoscaling for the configuration for the mysql and postgresql compatible editions of aurora
- aurora serverless DB cluster automatically starts up, shuts down, and scales capacity up or down based on app needs
- simple, cost-effective option, for infrequent, intermittent or unpredictable workloads

## **Elasticache**

---

> deploy, operate and scale an in-memory cache in the cloud

- improves the performance of webb app, by allowing to retrieve information from fast, managed, in-memory caches
- works on SSD
- caches the most common queries in elasticache

### Memcached vs redis

![memcached-redis](/aws/associate-level/solutions-architect/media/memcached-redis.PNG)

redis:

- backups and restore
- multi AZ
- advanced data types

memcached:

- multi-threaded performance
- scale horizontally
- simple to start with

## **DMS**

---

- facilitates the migration of relational db, data warehouses, NoSQL db, and other types of data stores
- between
  - on prem to cloud
  - on prem to on prem
  - cloud to cloud
  - cloud to prem
- server in the cloud, that runs a replication software
- source
- target
- schedule a task
- DMS creates tables, and associated pk
- you can pre-create the target tables, or use schema conversion tool (SCT)

### Homogenous migrations

- same engine
- oracle to oracle
- doesn't need SCT

![homogenous-dms](/aws/associate-level/solutions-architect/media/homogenous-dms.PNG)

### heterogeneous migrations

- different engine
- sql server to aurora
- needs SCT

![heterogenous-dms](/aws/associate-level/solutions-architect/media/heterogenous-dms.PNG)

### Sources

- on-prem and ec2 instances
  - oracle
  - sql
  - mysql
  - mariadb
  - postgre
  - sap
  - mongodb
  - db2
- azure sql database
- amazon rds (aurora)
- s2

### targets

- on-prem and ec2 instances
  - oracle
  - sql
  - mysql
  - mariadb
  - postgre
  - sap
- rds
- redshift
- dynamodb
- s3
- elasticsearch
- kinesis data stream
- documentDB

## **Caching strategies**

---

- cloudfront
  - caches origin (s3, ec2)
- API GW
- ElasticCache
  - Memcached
  - redis
- DAX
- the closer the caching to the end user you put in front, the lower the latency

## **EMR**

---

- big data platform
- uses tools such as
  - hive
  - spark
  - flink
  - hudi
  - presto
- run petabyte scale analysis at less half the cost of traditional on-prem solutions
- 3x faster that apache spark
- periodically archive log files stored on the master node to S3
  - 5 minutes intervals
  - only when creating cluster

### cluster

- collection of EC2
- each instance is called a node
- each node has a role
  - node type
- different sw components on each node type

### Master node

- manages the cluster
- every cluster has
- tracks the status of tasks
- monitor the health

### Core node

- run tasks and stores data in hadoop distributed file system (HDFS)
- multi-node have at least one core node

### Task node

- optional
- only runs tasks
- doesn't store data in HDFS
