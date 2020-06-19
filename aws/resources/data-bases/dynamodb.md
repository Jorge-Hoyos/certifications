# **DynamoDB**

- [**DynamoDB**](#dynamodb)
  - [**DynamoDB Links**](#dynamodb-links)
  - [**DynamoDB courses notes**](#dynamodb-courses-notes)
  - [**DynamoDB notes**](#dynamodb-notes)
    - [features](#features)
    - [how tables works](#how-tables-works)
    - [limitis](#limitis)
    - [Horizontal scaling with dynamo](#horizontal-scaling-with-dynamo)
    - [DynamoDB table](#dynamodb-table)
    - [Global secondary index](#global-secondary-index)
    - [Data types](#data-types)
    - [Item distribution](#item-distribution)
    - [GetItem Consistency](#getitem-consistency)
    - [Auto Admin](#auto-admin)
    - [Managing Throughput](#managing-throughput)
    - [On-demand](#on-demand)
    - [Adaptive capacity](#adaptive-capacity)
    - [Features](#features-1)
  - [**Takeaways**](#takeaways)
  - [Notes](#notes)

## **DynamoDB Links**

- [DynamoDB](https://aws.amazon.com/DynamoDB/)
- [DynamoDB Docs](https://docs.aws.amazon.com/DynamoDB/)

## **DynamoDB courses notes**

- [DynamoDB cloud practitioner notes](/aws/foundational-level/cloud-practitioner/notes/file.md#DynamoDB)
- [DynamoDB solutions architect notes](/aws/associate-level/solutions-architect/notes/file.md#DynamoDB)

## **DynamoDB notes**

- breakes the schema of DB to scale horizontally
- used for amazon for almost everything
- very important service in aws
- Elastic burst capacity
  - provioned capacity
  - peak consumed capacity
- performance at any scale
  - The higher the number of request the lowest latency
  - many millions of request per second - millisecond in responses
- fully managed, cloud-native NoDSQL DB
- designed for mission-critical OLTP
  - where you know access patterns
- operational DB that provides
  - extreme scale with horizontal scaling
  - consistent performance at any scale
  - HA and reliability with zero downtime
  - global availability and CRR features
  - full serverless experience
  - integrates with lambda and other AWS services

![sql vs nosql](/aws/resources/media/sqlvsnosql.PNG)

- SQL scales up
- No SQL scales horizontally by sharding

### features

- users 1M
- data volume
  - TB
  - PB
  - EB

### how tables works

- a table can be cut into multiple servers
- in a server can be one or more tables

### limitis

- 1K WCU (for a single server)
- 3K RCU (for a single server)
- up to 10GB (for a single server)

### Horizontal scaling with dynamo

![horizontal scaling](/aws/resources/media/horizontal-scaling.PNG)

### DynamoDB table

- Table
- Items (rows)
  - goes to 3 AZs
- partition key (mandatory)
  - every consult must use partition key
  - unique
  - does sharding from the partition key
- sort key (optional)
  - model 1:N relationships
  - enable rich query capabilities
    - pagination
    - top
    - sort
- Global secondary index (GSI)
  - up to 20 GSI per table
  - alternate partition and or sort key
  - RCUs/WCUs provisioned separately for GSIs

### Global secondary index

- another dynamo table

### Data types

![data-operation-types](/aws/resources/media/data-operation-types.PNG)

### Item distribution

- takes partition key, and hash

### GetItem Consistency

- Consistent read
  - on storage node leader
- eventually consistent
  - on storage node

### Auto Admin

- create tables and indexes

### Managing Throughput

- Scaling
  - Throughput
    - Write capacity unit (WCU) - 1 KB per second
      - if an item is 2KB, takes 2 WCU no write it
    - Read capacity unit (RCU) - 4 KB per second
    - Independent of each other
- Size
  - Add any number of items to a table
    - max item size is 400KB
- scaling is achieved through partitionin
  - each virtual partition deliver 1009 w/s or 3000 r/s
  - by capacity = (total RCU/3000) + (total WCU/1000)
  - by size = total size / 10GB

### On-demand

Features
- no capacity planning, provisioning or reservation
- pay only fot the read and writes you perform

Key benefits
- eliminates traoff of provisioning or underprovisioning

Base Throughput
- up to 4000 WRU: 4000 r/s
- up to 12000 RRU: 24000 r/s

"up to twice your previous peak"

### Adaptive capacity

balancea particiones muy calientes
- safety net

### Features

![dynamo-features](/aws/resources/media/dynamo-features.PNG)


## **Takeaways**

- 

## Notes

- Scan is inefiently for big DB
- an item maximun can be 400

