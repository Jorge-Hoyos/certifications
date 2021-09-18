# **RDS + Aurora + ElastiCache**

- [**RDS + Aurora + ElastiCache**](#rds--aurora--elasticache)
  - [**RDS overview**](#rds-overview)
    - [backups](#backups)
    - [db snapshot](#db-snapshot)
    - [storage auto scaling](#storage-auto-scaling)
  - [**Read replicas vs Multi AZ**](#read-replicas-vs-multi-az)
    - [Read replicas](#read-replicas)
    - [Multi AZ (DR)](#multi-az-dr)
    - [single AZ to multi AZ](#single-az-to-multi-az)
  - [**RDS Security**](#rds-security)
    - [Encryption](#encryption)
    - [Network](#network)
    - [access management](#access-management)
    - [IAM authentication](#iam-authentication)
  - [**Aurora**](#aurora)
    - [Aurora High availability](#aurora-high-availability)
    - [Aurora DB cluster](#aurora-db-cluster)
    - [security](#security)
  - [**ElastiCache**](#elasticache)
    - [redis](#redis)
    - [memcached](#memcached)
    - [considerations](#considerations)
    - [Lazy loading - Cache aside - lazy population](#lazy-loading---cache-aside---lazy-population)
    - [write through](#write-through)
    - [cache evictions and TTL](#cache-evictions-and-ttl)
    - [replication (redis)](#replication-redis)

## **RDS overview**

- Relational database services
- managed DB service
- use sql as a query language
- types
  - postgres
  - mysql
  - mariadb
  - oracle
  - microsoft sql
  - aurora
- restore in time
- monitoring dashboard
- read replicas improved read performance
- multi az for dr
- scaling capability
- storage backed by ebs
- cannot ssh to the instances

### backups

- automatically enabled
- daily full backups
- transaction logs backed up by rds every 5 mins
- restore any point in time up to 5 minutes ago
- 7 days retention (up to 35)

### db snapshot

- manually trigger by the user
- retention of backup for as long as you want

### storage auto scaling

- increase storage on you rds dynamically
- when rds detects you are running out of free database storage, it scales automatically
- avoid manually scaling your db storage
- set maximum storage threshold (max limit to increase)
- automatically modify storage if:
  - free storage is less than 10% of allocated storage
  - low storage last at least 5 minutes
  - 6 hours passed since last modification
- good for application with unpredictable workloads
- supported by all engines

## **Read replicas vs Multi AZ**

- difference between read replicas and Multi AZ

### Read replicas

- up to 5 read replicas
- within az, cross az, or cross region
- async replication between main and replicas
  - eventually consistent
- be promoted to their own db
- app must update the connection string to leverage read replicas
- run new workloads on the read replicas, not the production application
- read replicas are user for SELECT only
- if read replica is in the same region you don't pay network cost
  - across region, have to pay the fee
- read replicas can be setup as multi AZ for DR

### Multi AZ (DR)

- sync replication
  - when you write to master, it also needs to apply to standby to be accepted
- one DNS name
  - automatic failover to standby
- increase availability
- failover in case of loss of AZ, network or storage
- no manual interventions in apps
- not used for scaling

### single AZ to multi AZ

- zero downtime operation
- modify db and enable multi az
  - snapshot taken
  - restore in a new DB in a new AZ
  - sync is established between the DBs

## **RDS Security**

### Encryption

- at rest
  - encrypt master and read replicas with kms - aes-256
  - encrypt at launch time
  - if the master if not encrypted the read replicas cannot be encrypted
  - only when you first create the instance
- in flight encryption
  - ssl certificates to encrypt data to rds in flight
  - provide ssl option with trust certificate when connecting to db
- encrypt backups
  - snapshot of encrypted db is encrypted
  - snapshot on un encrypted db is un encrypted
  - can copy an un encrypted snapshot into an encrypted one
- encrypt an un encrypted db
  - create snapshot
  - copy snapshot and enable encryption
  - restore db from encrypted snapshot
  - migrate application to new db

### Network

- usually deployed in private subnet
- works by leveraging sg it control which ip can communicate with rds

### access management

- iam control who can manage aws rds
- traditional username and password can be used to login into the database
- MySQl and PostgreSQL can use IAM-based authentication

### IAM authentication

- only for mysql and postgres
- need an authentication token obtained through iam and rds api call
- lifetime of 15 mins
- benefits
  - network in/out must be encrypted using ssl
  - iam centrally manage users instead of db
  - can leverage iam roles and ec2 instances profiles for easy integration

## **Aurora**

- proprietary technology from aws
- postgres and mysql are both supported as aurora db
- cloud optimized
- storage automatically grows in increments of 10gb, up to 64tb
- can have 15 replicas, replication process is faster
- failover is instantaneous, its HA native
- 20% more cost of RDS
- automated patching with zero downtime
- backup and recovery
- advanced monitoring
- regional
  - single aws region
- global
  - multiple aws regions
  - writes are replicated to secondary regions in less than 1 sec
- always select either the writer endpoint or reader endpoint for the aurora cluster

### Aurora High availability

- 6 copies of your data across 3 AZ
  - 4 copies out of 6 for writes
  - 3 copies out of 6 for reads
  - self healing with peer-to-peer replication
- one aurora instances take writes (master)
- automated failover for master in less than 30seconds
- master + 15 read replicas for server reads
- any read replicas can become master
- support cross region replication

### Aurora DB cluster

- writer endpoint always pointing to the master
- there can be auto scaling in top of the read replicas
- reader endpoint
  - connection load balancing
  - connects automatically to all the read replicas

### security

- similar to rds, uses same engine
- encryption at rest with kms
- automated backups, snapshots and replicas are encrypted
- encryption in flight using ssl
- authentication using iam token

## **ElastiCache**

- managed redis or memcached
- cache are in memory databases with really high performance, low latency
- help reduce load off databases for read intensive workloads
- make application stateless
- involves heavy application code changes
- cache must have an invalidation strategy to make sure only the most current data is used there
- user logs into application
  - application writes session data into elasticache
  - application stateless

### redis

- multi az
- auto-failover
- read replicas to scale read and HA
- data durability
- backup and restore features
- encryption in transit with redis token

### memcached

- multi node for partitioning of data (sharding)
- no HA (replication)
- non persistent
- no backup and restore
- multi threaded architecture

### considerations

- is safe to cache data, but it may be out of date, eventually consistent
- is caching effective for data?
  - pattern: data changing slowly, few keys are frequently needed
  - anti pattern: data changing rapidly
- is data structured well for caching?
  - key value or aggregation results, yes

### Lazy loading - Cache aside - lazy population

- application ask for data in cache
  - cache hit
    - cache miss
- only requested data is cached
- node failures are not fatal
- cache miss penalty is 3 round trips
- stale data
  - possible to have outdated data in the elasticache

### write through

- add or update the cache when db is updated
- data in cache is never stale
- write penalty, each write requires 2 calls
- missing data until it is added
- cache churn, a lot of the data will never be read

### cache evictions and TTL

- cache evictions
  - delete item from cache
  - item is evicted because memory is full and not recently used
  - set a TTL
- if too many evictions

### replication (redis)

- cluster mode disabled
  - one primary node, up o 5 replicas
  - asynchronous replication
  - primary is used for read/writes
  - other nodes read only
  - multi az
  - guard against data loss
- cluster mode enabled
  - data is partitioned across shard (helpful to scale writes)
  - each shard has a primary and up to 5 replicas
