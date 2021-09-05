# **EC2 Instance storage**

- [**EC2 Instance storage**](#ec2-instance-storage)
  - [**EBS Overview**](#ebs-overview)
  - [**EBS Snapshots**](#ebs-snapshots)
  - [**AMI Overview**](#ami-overview)
    - [AMI Process](#ami-process)
  - [**EC2 instance store**](#ec2-instance-store)
  - [**EBS Volume types**](#ebs-volume-types)
    - [GP2 and GP3 (SSD)](#gp2-and-gp3-ssd)
    - [io1 and io2 (SSD)](#io1-and-io2-ssd)
    - [st1 (HHD)](#st1-hhd)
    - [sc1 (HDD)](#sc1-hdd)
  - [**EBS multi attach - io1/io2 family**](#ebs-multi-attach---io1io2-family)
  - [**EFS - Elastic file system**](#efs---elastic-file-system)
    - [Performance mode](#performance-mode)
    - [throughput mode](#throughput-mode)
    - [Storage tier](#storage-tier)
  - [**EFS vs EBS**](#efs-vs-ebs)
    - [EBS](#ebs)
    - [EFS](#efs)

## **EBS Overview**

- EBS elastic block store volume is a network drive you can attach to your instances while they run
- persist data after instance is terminated
- multi attach feature for some EBS
- bound to a specific AZ
  - cannot be attached to an ec2 in another AZ
- Network drive, not physical drive
  - uses the network to communicate to the instances might be latency
  - it can be detached and reattached
- have provisioned capacity (GBs, IOPS)
  - billed by capacity
  - increase capacity
- can be unattached
- Delete on termination
  - controls ebs behavior when an ec2 is terminated
  - by default it is ticked for root volume
  - by default any other ebs volume is not deleted
  - this can be controlled

## **EBS Snapshots**

- make a backup at any point in time
- not necessary to detach volume to do snapshot, but recommended
- can copy snapshot across az or region
  - transfer data to another region

## **AMI Overview**

- amazon machine image
- customization of an ec2
  - own software, config, os, etc
  - faster boot/configuration because the sw is prepacked
- provided by aws or own
- AMI are built for specific region (can be copied across regions)
- Types
  - Public
  - Own
  - Marketplace AMI

### AMI Process

- start instance
- customize it
- stop instance
- build ami - also create ebs snapshot
- launch instances from other AMIs

## **EC2 instance store**

- EBS Volumes are network drives with good but limited performance
- instance store are high performance hw disk
  - Directly connect to the ec2 instance
- Better I/O performance
- ephemeral, lose their storage if stopped
- buffer, cache, scratch data
- not for long store storage
- risk of data loss if hw fails
- needs backup and replication

## **EBS Volume types**

- only gp2/gp3 and io1/io2 can be used as boot volumes

### GP2 and GP3 (SSD)

- General purpose ssd balance prince and performance
- cost effective storage, low latency
- system boot volumes
- 1GiB - 16 TiB
- gp3:
  - baseline 3000 IOPs and throughput of 125 MiB/s
  - increase IOPs up to 16000 and throughput up to 1000 MiB/s independently
- gp2:
  - small gp2 volumes they can burst up to 3000 IOPS.
  - Size and IOPs are linked, max 16000 IOPs
  - 3 IOPs per GB, 5334 GB at max IOPs

### io1 and io2 (SSD)

- highest performance SSD volume for mission critical low latency or high throughput workload
- critical business applications with sustained IOPS performance
- application that needs more than 16000 IOPS
- great for DB workload
- io1/io2 (4GiB - 16 TiB)
  - max PIOPS 64000 for Nitro EC2 and 32000 for other
  - can increase PIOPS independently from storage
  - io2 more durability and more IOPS per GiB (at the same price of io1)
- io2 block express (4GiB - 64 TiB)
  - sub millisecond latency
  - max PIOPS 256000 with an IOPS:GiB ratio of 1000:1
- supports EBS multi attach

### st1 (HHD)

- low cost HDD volume designed for frequently accessed, throughput intensive workloads
- cannot be boot volume
- up to 16TiB
- use cases
  - data warehouses, log processing, big data

### sc1 (HDD)

- lowest cost HDD
- designed for less frequently accessed workload
- archive data
- lowest cost is important

## **EBS multi attach - io1/io2 family**

- attach the same ebs volume to multiple ec2 instance in the same az
- each ec2 instance has full read and write permission to the volume
- use case:
  - higher application availability
  - must manage concurrent write operation
- must use a file system thats cluster aware (not xfs, ex4)

## **EFS - Elastic file system**

- manage NFS (network file system) that can be mounted on many ec2
- EFS works with ec2 in multi az
- highly available, scalable, expensive (3x gp2), pay per data use
- has a SG attached, to control connection to it
- use cases
  - content management, web serving, data sharing, wordpress
- use NFSv4.1 protocol
- only compatible with linux based AMI (not windows)
- encrypt at rest with KMS
- no capacity planning
- each AZ needs an SG, can be the same one, can be different

### Performance mode

- general purpose (default): latency sensitive use cases (web server)
- Max I/O: higher latency, throughput, highly parallel (big data)

### throughput mode

- bursting
  - throughput will scale with file system size
- provisioned
  - very small file system, but very high throughput

### Storage tier

- lifecycle management feature
- standard: frequently accessed files
- infrequent access: cost to retrieve files, lower price to store

## **EFS vs EBS**

### EBS

- only one instance
- locked to AZ
- gp2: IO increases if the disk size increases
- io1: can increase IO independently
- to migrate across AZ
  - take snapshot
  - restore from snapshot to another AZ
  - backups use IO
- by default root volumes of instances get terminated with the ec2
- pay fr the provisioned capacity

### EFS

- mounted to multiple instances across AZ
- only for linux
- EFS share website files (wordpress)
- more expensive
- leverage infrequently access for cost savings
- you get billed for the capacity you use
