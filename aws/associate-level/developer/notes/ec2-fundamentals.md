# **EC2 Fundamentals**

- [**EC2 Fundamentals**](#ec2-fundamentals)
  - [**EC2 Basic**](#ec2-basic)
    - [Configuration options](#configuration-options)
    - [User data](#user-data)
    - [Instances types](#instances-types)
  - [**Instance types**](#instance-types)
    - [General purpose](#general-purpose)
    - [Compute optimized](#compute-optimized)
    - [Memory optimized](#memory-optimized)
    - [Storage optimized](#storage-optimized)
  - [**Security groups**](#security-groups)
    - [Ports](#ports)
  - [**SSH Overview**](#ssh-overview)
  - [**Instance purchasing options**](#instance-purchasing-options)
    - [On demand](#on-demand)
    - [Reserved instances](#reserved-instances)
      - [Convertible](#convertible)
      - [Schedule reserved instance](#schedule-reserved-instance)
    - [Spot instances](#spot-instances)
    - [Dedicated host](#dedicated-host)
    - [Dedicated instances](#dedicated-instances)

## **EC2 Basic**

- EC2 = Elastic cloud compute = Infrastructure as a Service
- Multiple Services:
  - Rent virtual machines EC2
  - Store data on virtual drives EBS
  - Distribute load across machines ELB
  - Scaling the services using an auto-scaling group ASG
- when you stop and start an ec2 instance the public ip address changes, private ip stays the same

### Configuration options

- OS
- CPU
- RAM
- Storage
  - EBS
  - EFS
- Network
- Firewall rules
- Bootstrap script (User data)

### User data

- bootstrapping instance when it launches
- launching commands when the machine starts
- run once at the instance first start
- automate boot tasks:
  - install updates
  - install software
  - download
- runs with the root user

### Instances types

- many types:
  - t2.micro
  - t2.xlarge
  - m5.medium

## **Instance types**

- Naming convention
  - m5.2xlarge
  - m: instance class
  - 5: generation
  - 2xlarge: size within the class

### General purpose

- Great for diversity of workloads
- balance between
  - compute
  - memory
  - storage

### Compute optimized

- Great for compute-intensive tasks, that require high performance processors
  - batch processing workload
  - media transcoding
  - high performance web servers
  - HPC
  - machine learning
  - dedicated gaming servers
- C names

### Memory optimized

- fast performance for workloads that process large data sets in memory
- use cases
  - high performance, relational and non relational dbs
  - distributed web scale cache stores
  - in memory dbs optimized for BI
  - application performing real-time processing of big unstructured data
- R, X1, high memory, Z

### Storage optimized

- Storage intensive tasks that require high, sequential read and write access to large data sets on local storage
- use cases:
  - OLTP
  - relational and No-Sql
  - cache for in-memory dbs (redis)
  - data warehousing applications
  - distributed file systems
- I, D, H1

## **Security groups**

- Control how traffic is allow into or out of our instances
- only contains allow rules
- rules can reference ips or other sgs
- Firewall on our instances
- regulate
  - access to ports
  - authorized ip ranges - ipv4 and ipv6
  - control inbound network
  - control outbound network
- by default allow inbound traffic is blocked
- by default allow outbound traffic is allowed
- can be attached to multiple instances
- an instance can have multiple SGs
- lock down to a region/vpc combination
- lives outside the ec2
- application not accessible (time out) its a SG issue
- referencing other SGs don't have to worry about IPs

### Ports

- 22 SSH (secure shell) - log into linux instances
- 21 FTP (file transfer protocol) - upload files into a file share
- 22 SFTP (Secure file transfer protocol) - upload files using SSH
- 80 HTTP - unsecured websites
- 443 HTTPS - secured websites
- 3389 RDP - log into windows instance

## **SSH Overview**

- command line interface
- ec2 instance connect (aws, amazon linux 2)
- private key has permission 0644 when downloaded, too open, chmod 0400 to fix it

## **Instance purchasing options**

- On-demand: short workload, predictable pricing
- Reserved: minimum 1 year
  - Reserved instances: long workloads
  - Convertible reserved instances: flexible instances
  - schedule reserved instances: example every thursday between 3-6pm
- Spot instances: short workload, cheap can lose instances
- Dedicated hosts: entire physical server

### On demand

- pay for what you used
  - linux billed per second
  - other os by hour
- highest cost no upfront payment
- no long term commitment
- recommended for short term and un interrupted workloads
- unknown workload

### Reserved instances

- up to 75% discount
- 1 or 3 years reservation, more time more discount
- no upfront, partial upfront, all upfront more discount
- reserve specific instance type
- steady state usage application (db)

#### Convertible

- change instance type
- up to 54%

#### Schedule reserved instance

- launch within time window you reserve
- When you require a fraction day, week, month
- still commitment 1 or 3 yr

### Spot instances

- up to 90% of discount
- can lose them if the price you are paying is less of the current spot price
- most cost efficient in aws
- workload that are resilient to failure
  - batch jobs
  - image processing
  - data analysis
  - distributed workloads
  - flexible start and end time
- not good for critical or DB

### Dedicated host

- physical server with ec2 instance capacity fully dedicated to your use
- compliance requirement
- server bound software licenses
- 3 year reservation
- more expensive

### Dedicated instances

- Instances running on hw thats dedicated to you
- may share hw with other instances in same account
- no control over instance placement
- similar to dedicated host
