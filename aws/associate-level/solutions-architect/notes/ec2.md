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
    - [Saving plans](#saving-plans)
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
    - [Provisioned IOPS SSD (io2)](#provisioned-iops-ssd-io2)
    - [throughput optimized HDD (st1)](#throughput-optimized-hdd-st1)
    - [cold hard disk drive HDD (sc1)](#cold-hard-disk-drive-hdd-sc1)
    - [magnetic](#magnetic)
    - [EBS Notes](#ebs-notes)
  - [**Spot instances**](#spot-instances)
    - [Spot prices](#spot-prices)
    - [spot blocks](#spot-blocks)
    - [Not good for](#not-good-for)
    - [Spot request](#spot-request)
    - [Spot fleets](#spot-fleets)
      - [spot flees strategies](#spot-flees-strategies)
  - [**Hibernate**](#hibernate)
    - [start from hibernation](#start-from-hibernation)
    - [Useful for](#useful-for)
  - [**ENI**](#eni)
    - [ENI scenarios](#eni-scenarios)
  - [**ENA**](#ena)
    - [ENA scenarios](#ena-scenarios)
    - [Enabling](#enabling)
  - [**EFA**](#efa)
  - [**CloudWatch**](#cloudwatch)
    - [Cloudwatch and EC2](#cloudwatch-and-ec2)
  - [**CloudTrail**](#cloudtrail)
  - [**CLI**](#cli)
  - [**Roles**](#roles)
  - [**Boot strap scripts**](#boot-strap-scripts)
  - [**Instance metadata**](#instance-metadata)
  - [**EFS - Elastic file system**](#efs---elastic-file-system)
    - [How to mount](#how-to-mount)
    - [EFS notes](#efs-notes)
  - [**FSx for windows**](#fsx-for-windows)
  - [**FSx for luster**](#fsx-for-luster)
  - [**Placement groups**](#placement-groups)
    - [Clustered placement groups](#clustered-placement-groups)
    - [spread placement groups](#spread-placement-groups)
    - [partitioned placement groups](#partitioned-placement-groups)
    - [placement groups notes](#placement-groups-notes)
  - [**HPC**](#hpc)
    - [Data transfer](#data-transfer)
    - [Compute](#compute)
    - [networking](#networking)
    - [storage](#storage)
    - [Orchestration and automation](#orchestration-and-automation)
      - [BATCH](#batch)
      - [ParallelCluster](#parallelcluster)
  - [**WAF**](#waf)
    - [behaviors](#behaviors)
    - [Protection](#protection)

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
- Regional, meaning that you reserve capacity in a specific region

##### standard RI

- up to 72%
- the more you pay up front and the longer the contract the greater the discount
- cannot change the region

##### convertible RI

- up to 54%
- allows to change between instance types

##### schedule RI

- launch within time windows you reserve
- match your capacity reservation to a predictable recurring schedule

#### spot

- bid for execs capacity
- discount up to 90%
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

- psychical EC2 server dedicated for you
- reduce cost by allowing you to use existing server-bound sw licenses
- regulatory requirements
- licensing does not support multi tenancy
- can be purchased
  - on demand
  - reservation

### Saving plans

- save up to 72% on all compute usage regardless of instance type or region
- commit to one or three years to use a specific amount of compute
- super flexible (lambda and fargate)

### instance types

![EC2 instance types](/aws/foundational-level/cloud-practitioner/notes/media/EC2-instances-types.PNG)

- Hardware, instance type determines the hardware of the host computer for your instance
- Capabilities, differente compute memory and storage capabilities, group on instance families
- Application requirements, select an instance type based on the requirements of the app

### EC2 Notes

- termination protection off by default
- EBS-backed instance default action if for the root EBS to be deleted
- shared AZ with EBS volume
- EC2 underlying hypervisor is
  - XEN
  - Nitro

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
- any number of EC2 instances in a SG
- can attach more than 1 sg to EC2 instances

## **EBS**

---

> elastic block store, provides persistent block storage volumes for use with amazon EC2

- virtual hard disk in the cloud
- at least 1 ebs attached, where the OS is installed
- HA and replicated by default
- scalable, dynamically increase capacity and change volume type with no downtime
- each ebs is replicated withins itz AZ to protect from failure
- root device volume, where the OS is installed
  - can only by gp2, io1, magnetic standard
  - can be encrypted
- IOPS = Inputs Outputs per Second, how fast is the HDD
- extra volumes can be gp2, io1, magnetic standard, cold HDD (sc1), throughput optimized HDD (st1)
- Shares AZ with EC2 instances
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
- 3 IOS per GiB
- most workloads
- Boot volumes
- not latency sensitive
- up to 16000 IOPS

### provisioned iops (SSD - io1)

- really fast IOPS
- high performance option, most expensice
- 50 IOPS per GiB
- mission critical applications
- databases
- 64000 IOPS
- 99.9% durability

### Provisioned IOPS SSD (io2)

- higher durability
- and more IOPS
- still 64000 max per volume
- same price as io1
- 500 iops per GiB
- 99.999% durability

### throughput optimized HDD (st1)

- physical hard disk drive (magnetic)
- low cost
- huge ammount in data
- baseline througput of 40 MB/s per TB
- big data and data warehouses, ETL, log processing
- cannot be a boot volume
- 500 IOPS

### cold hard disk drive HDD (sc1)

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
- volumes restored from encrypted snapshots are encrypted automatically
- can shared unencrypted snapshots
  - other aws accounts
- can not be shared trough multiple EC2 instances
- termination protection off by default
- EBS snapshots of registered AMIs cannot be deleted

## **Spot instances**

---

- take advantage of unused EC2 capacity
- up to 90% discount
- stateless, fault tolerant or flexible applications
  - big data
  - containerized workloads
  - CI/CD and testing
  - HPC
  - web service

### Spot prices

- decide maximum spot price
- instance will be provisioned so long as the spot price is below your maximum spot price
- hourly spot price varies on capacity and region
- if the spot price goes above your maximum, you have two minutes to stop or terminate instance

### spot blocks

- stop spot instance from being terminated
- one to six hours

### Not good for

- persistent workloads
- critical jobs
- databases
- persistent storage
  - ephemeral computer

### Spot request

- maximum price
- desired number of instances
- launch specification
- request type
  - persistent
  - one-time
- valid from, until
- if its persistent tries to provision another instance when the price goes below again
- if its one-time terminates the instances

![spot-instance](/aws/associate-level/solutions-architect/media/spot-instance.PNG)

### Spot fleets

- collection of spot instances
  - optionally on-demand instances
- attempts to launch the desired capacity of spot/on-demand instances to meet target capacity
- is fulfilled if
  - available capacity
  - maximum price you specified in the request exceed the current spot price
- different launch pool
  - OS
  - instance type
  - AZ
- multiple pools

#### spot flees strategies

- capacity optimized
  - comes from the pool optimal capacity for the number of instances launching
- lowest price
  - comes from the pool lowest with the lowest price, default strategy
- diversified
  - comes from all the pools
- instance pools to use count
  - distributed across the number of spot instances pools you specify
  - only valid in combination with lowest price

## **Hibernate**

---

- stop instance data is kept on the disk (EBS)
- if the instance is terminated, by default so will the root volume
- hibernate our EC2 instance
- OS is suspended to disk
  - saves the content from the instances memory (RAM) to the EBS
  - a lot faster to boot up
- the EBS must be big enough to store the RAM
- Root device **MUST BE ENCRYPTED**
- instance RAM must be less than 150GB
- cant be hibernated for more that 60 days
- available for on-demand and RI

### start from hibernation

- EBS is restored to its previous state
- RAM contents are reloaded
- the processes resumes
- previously attached volumes are reattached and the instances retains its ID
  - If we stop or restart the instances losses the ID

### Useful for

- long running processes
- services that take time to initialize

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

- network device attached to EC2 to accelerate HPC and machine learning apps
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

### Cloudwatch and EC2

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

## **Instance metadata**

---

- bootstrap script can be seen from the instance

```shell
curl http://169.254.169.254/latest/user-data
```

- metadata can be seen from the instance

```shell
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/local-ipv4
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

- meta data is used to get information from the instances

## **EFS - Elastic file system**

---

> file storage service for EC2

- can be shared trough multiple EC2 instances
- create and configure file systems quickly and easily
- storage capacity is elastic
  - growing and shrinking automatically as you add files
- great for files servers
- great for sharing files
- has lifecycle policies
  - moving files to EFS IA which is cheaper
- throughput
  - bursting
  - provisioned
- performance modes
  - general purpose
  - Max I/O
- communicates trough NFS - port 2049

### How to mount

- run commands
- its mounted through the server

```shell
sudo yum install -y amazon-efs-utils
# without encryption at transit
sudo mount -t efs fs-12345678:/ /dir/to/share
# with encryption at transit
sudo mount -t efs -o tls fs-12345678:/ /dir/to/share
```

### EFS notes

- supports network file system version 4 (NFSv4) protocol
- you only pay for the storage used (no pre-provisioning required)
- can scale up to petabytes
- can support thousand of concurrent NFS connections
- Data is stored across multiple AZ within a region
- Read after write consistency

## **FSx for windows**

---

> fully managed native MS windows file system, so you can move you windows-based apps that require file storage to AWS

- windows file server
- designed for microsoft applications
- runs windows server message block (SMB)
- doesn't work on linux instances, windows only

## **FSx for luster**

---

> file system optimized for compute intensive workload

- HPC, ML, media data processing workflows, big data
- run lustre file systems that can process massive data sets at up to hundreds of Gbps of throughput, millions of IOPS and sub-millisecond latencies
- can store data directly to s3

## **Placement groups**

---

- way of placing your EC2 instances
- no charge for creating placement groups

### Clustered placement groups

- grouping of instances in a single AZ
- low network latency high network throughput
- only certain instances
- very close to each other

### spread placement groups

- grouping of instances placed on distinct underlying hardware
- small number of critical instances that should be separate
- can be in different AZs
- individual instances
- up to 7 instances per AZ

![spread-placement-group](/aws/associate-level/solutions-architect/media/spread-placement-group.PNG)

### partitioned placement groups

- divides each group into logical segments called partitions
- each partition has its own set of rack
  - own network
  - own power source
- multiple EC2 within a partition
- HDS, HBase and cassandra

![partitioned-placement-group](/aws/associate-level/solutions-architect/media/partitioned-placement-group.PNG)

### placement groups notes

- clustered cant span multiple AZs
  - spread and partitioned can
- name for placement group must be unique in the AWS account
- only certain instances can be launch in a placement group
- it is recommended homogenous instances within clustered placement groups
- cant merge placement groups
- cant move an instance to a placement group
  - create AMI from instance
  - then launch instance from AMI in the placement fr

## **HPC**

---

### Data transfer

- snowball, snowmobile (tb/pb worth of data)
- DataSync store on s3, EFS, FSx for windows
- Direct connect

### Compute

- EC2 instances CPU or GPU optimized
- EC2 fleets
- placement groups (cluster)

### networking

- enhanced networking
- elastic network adapters
- elastic fabric adapters

### storage

- instance-attached storage
  - EBS: up to 64000 IOPS (io1)
  - instance store: scale to millions of IOPS: low latency

- network storage
  - s3: distributed object-based storage
  - EFS: scale IOPS based on total size, or use provisioned IOPS
  - FSx for luster: HPC-optimized distributed file system; millions of IOPS, backed by s3

### Orchestration and automation

#### BATCH

- easily run hundreds of thousand of batch computing jobs on AWS
- supports multi-node parallel jobs
  - single jobs, across multiple EC2
- schedule jobs and launch EC2 instances

#### ParallelCluster

- open source cluster management tool
- makes it easy to deploy and manage HPC clusters on AWS
- simple text file to model and provision all the resources needed
- Automate create of VPCs, subnets, cluster type, and instances types

## **WAF**

---

> allows to monitor HTTP and HTTPS requests that are forwarded to cloudfront, ALB and API GW

- lets control access to your content
- HTTP and HTTPS at layer 7
- lvl 7 aware FW
  - can see info sended to your web server
  - query string parameters

conditions such as:

- Allowed IP address to make request
- what query string parameters need to be passed to allow the request
- the ALB, cloudfront or API GW will allow content, or give HTTP 403

### behaviors

- Allow all request expect the ones you specify
- Block all requests except the ones you specify
- Count the requests that match the properties you specify
  - passive mode

### Protection

- IP addresses that request originate from
- country
- values in request headers
- string in the requests
  - specific
  - regex
- length of request
- presence of SQL code (SQL injection)
- presence of a script (cross-site scripting)
