# **EC2**

- [**EC2**](#ec2)
  - [**EC2 101**](#ec2-101)
    - [pricing models](#pricing-models)
      - [on demand](#on-demand)
      - [reserved](#reserved)
        - [standard RI](#standard-ri)
        - [convertible RI](#convertible-ri)
        - [schedule RI](#schedule-ri)
      - [spot](#spot)
      - [dedicated hosts](#dedicated-hosts)
    - [instance types](#instance-types)
    - [EC2 Notes](#ec2-notes)
  - [**AMI**](#ami)
    - [EBS volumes](#ebs-volumes)
    - [instance store volumes (ephemeral storage)](#instance-store-volumes-ephemeral-storage)
  - [**Security groups**](#security-groups)
  - [**EBS**](#ebs)
    - [encrypt unencrypted volumes](#encrypt-unencrypted-volumes)
    - [General purpose (SSD gp2)](#general-purpose-ssd-gp2)
    - [provisioned iops (SSD - io1)](#provisioned-iops-ssd---io1)
    - [throughput optimized HDD (st1)](#throughput-optimized-hdd-st1)
    - [cold hard disk drive (sc1)](#cold-hard-disk-drive-sc1)
    - [magnetic](#magnetic)
    - [EBS Notes](#ebs-notes)
  - [**ENI**](#eni)
    - [ENI scenarios](#eni-scenarios)
  - [**ENA**](#ena)
    - [ENA scenarios](#ena-scenarios)
    - [Enabling](#enabling)
  - [**EFA**](#efa)
  - [**CloudWatch**](#cloudwatch)
    - [Cloudwatch and ec2](#cloudwatch-and-ec2)
  - [**CloudTrail**](#cloudtrail)
  - [**CLI**](#cli)
  - [**Roles**](#roles)
  - [**Boot strap scripts**](#boot-strap-scripts)

## **EC2 101**

---

> web service that provides resizable compute capacity in the cloud

- reduces time to obtain and boot new servers

### pricing models

#### on demand

- pay a fixed rate
- no commitment
- great for testing if the develop works and shut down machine
- low cost and flexibility, with out up-front commitment
- app with short term, spiky or unpredictable workload that cannot be interrupted

#### reserved

- capacity reservation
- significant discount
- contract 1 or 3 years
- the more you pay up front the more you save
- app with steady state or predictable usage
- users that able to make up front payment reducing costs

##### standard RI

- up to 75%
- the more you pay up front and the longer the contract the greater the discount

##### convertible RI

- up to 54%
- allows to change between instance types

##### schedule RI

- launch within time windows you reserve
- match your capacity reservation to a predictable recurring schedule

#### spot

- bid for execs capacity
- you set the price you want to bid up
  - if it hits the price you have the instance
  - if it goes above you will lose the instances
- apps with flexible start and end times
- app only feasible on very low compute prices
- user with urgent computing need for large amounts of additional capacity
- if terminated
  - by aws you don't get charged partially for the hour
  - by you, you get charged for the hour

#### dedicated hosts

- psychical ec2 server dedicated for you
- reduce cost by allowing you to use existing server-bound sw licenses
- regulatory requirements
- licensing does not support multi tenancy
- can be purchased
  - on demand
  - reservation

### instance types

![ec2 instance types](/aws/foundational-level/cloud-practitioner/notes/media/ec2-instances-types.PNG)

### EC2 Notes

- termination protection off by default
- EBS-backed instance default action if for the root EBS to be deleted
- shared AZ with EBS volume

## **AMI**

---

> amazon machine image

- choosing virtual machine
- can be based on
  - region
  - OS
  - architecture
  - launch permissions
  - storage for the root device (root device volume)
    - instance store (ephemeral storage)
    - EBS backed volume
- all AMIs are categorized as either backed by EBS or instance store

### EBS volumes

- the root device is an amazon EBS created from a EBS snapshot
- persistent storage

### instance store volumes (ephemeral storage)

- root device is an instance store volume created from a template stored in S3
- restricts the number of instance types
- can attach additional instance store volumes in the moment of creations, but not after
- cannot be seen from the console
- cant stop instances
- instance stored backed
- if the underlying host fails, all data is lost

## **Security groups**

---

- changes in SG take effect immediately
- SG are stateful
- when you create an inbound rule, an outbound rules is created automatically
  - if you enable inbound 80, outbound 80 is automatically enabled
- only works with whitelist, not blacklist
  - you cant block ports, or ips
- all inbound traffic is blocked by default
- all outbound traffic is allowed
- any number of ec2 instances in a SG
- can attach more than 1 sg to ec2 instances

## **EBS**

---

> elastic block store, provides persistent block storage volumes for use with amazon ec2

- virtual hard disk in the cloud
- each ebs is replicated withins itz AZ to protect from failure
- root device volume, where the OS is installed
  - can only by gp2, io1, magnetic standard
  - can be encrypted
- IOPS = Inputs Outputs per Second, how fas is the HDD
- extra volumes can be gp2, io1, magnetic standard, cold HDD (sc1), throughput optimized HDD (st1)
- Shares AZ with ec2 instances
- can change values on the fly (storage, volume type, iops)
- can be moved from AZ
  - create snapshot
  - create image from snapshot(AMI)
  - launch instance from AMI
  - the AMI can be copied to other regions or shard to other accounts
- extra volumes by default are not erased when the EC2 is terminated
  - this comes as an extra charge

### encrypt unencrypted volumes

- create snapshot
- copy snapshot
  - select encryption
- create AMI from encrypted snapshot
- launch EC2 from AMI
  - when launching the instances eht ebs volume will already be encrypted

![ebs-types](/aws/associate-level/solutions-architect/media/ebs-types.png)

### General purpose (SSD gp2)

- ssd volumes of balanced price and performance
- most workloads
- up to 16000 IOPS

### provisioned iops (SSD - io1)

- really fast IOPS
- mission critical applications
- databases
- 64000 IOPS

### throughput optimized HDD (st1)

- physical hard disk drive (magnetic)
- big data and data warehouses
- 500 IOPS

### cold hard disk drive (sc1)

- file servers
- lowest cost
- less frequently accessed workloads
- 250 IOPS

### magnetic

- previous generation
- data is infrequently accessed
- 40-200 IOPS

### EBS Notes

- snapshots exist on s3
- snapshots are point in time copies of volumes
- snapshots are incremental - only the block that have changed since your last snapshot are moves to s3
- to create an snapshot of the root is better to stop the instance
  - you can take while the instance is running to
- create AMI from snapshots
- always be in the same AZ as the EC2
- can be migrated to other AZ
- snapshots of encrypted volumes are encrypted automatically
- can shared unencrypted snapshots
  - other aws accounts

## **ENI**

---

> elastic network interface

- virtual network card
- comes by default on the EC2, can have more
- primary private IPv4 address from the range of the VPC
- one or more secondary private IPv4
- one Elastic IP address per IPv4
- one public IPv4 address
- one or more IPv6 address
- one or more SG
- a MAC address
- a source/destination check flags
- description

### ENI scenarios

- management network
- network and security appliances in VPC
- low-budget HA solution
- separate management network to your production network, use multiple ENIs for each network

## **ENA**

---

> enhanced networking

- single root I/O virtualization (SR-IOV)
- high performance network capabilities on supported instance types
- provides higher bandwidth, packer per second performance, and consequently lowe inter-instances latencies
- no additional charges for using ENA
  - but the EC2 instance has to support it

### ENA scenarios

- good network performance
- 10-100 Gbps

### Enabling

elastic network adapter (ENA)

- up to 100GBs
intel 82599 virtual function (VF)
- up to 10 Gbps
- older instances

## **EFA**

---

> elastic fabric adapter

- network device attached to ec2 to accelerate HPC and machine learning apps
- lower and more consistent latency and higher throughput's
- can use OS-bypass, enabling HPC and ML apps, to bypass OS kernel and communicate directly with the EFA device, a lot faster/latency
- only for linux

## **CloudWatch**

---

> monitoring service

- monitors aws resources
- monitors app running on the resources
- monitors performance
- monitor things like
  - compute
    - EC2 instances
    - ASG
    - ELB
    - R53 health check
  - storage and CDN
    - EBS volumes
    - storage gateways
    - cloudfront
- Create cloudwatch alarms, trigger notifications
- every 5 minutes by default
- 1 minute interval with detailed monitoring
- create dashboards
- create alarms
- events - help respond to state changed in aws
- logs . helps you to aggregate, monitor and store logs

### Cloudwatch and ec2

host level metrics

- cpu
- network
- disk
- status check

## **CloudTrail**

---

> records console actions and API calls

- increases visibility
- monitor API calls
- auditing

## **CLI**

---

- global
- storing credential in the credentials file is risky
- need access in IAM

## **Roles**

---

- far more secure that storing access keys
- easier to manage
- can be assigned to EC2
- universal

## **Boot strap scripts**

---

- always begins with

```shell
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1> web </h1></html>" > index.html
aws s3 mb s3://my-awesome-bucket-jorge
aws s3 cp index.html s3://my-awesome-bucket-jorge
```
