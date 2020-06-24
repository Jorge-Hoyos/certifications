# **VPCs**

- [**VPCs**](#vpcs)
  - [**VPC Overview**](#vpc-overview)
    - [VPC features](#vpc-features)
    - [Default VPC](#default-vpc)
    - [Peering](#peering)
    - [VPC notes](#vpc-notes)
  - [**create VPC**](#create-vpc)
    - [creating a VPC](#creating-a-vpc)
    - [creating subnet](#creating-subnet)
    - [creating IGW](#creating-igw)
    - [Configuring route table](#configuring-route-table)
    - [Creating notes](#creating-notes)
  - [**NAT instances**](#nat-instances)
  - [**NAT gateway**](#nat-gateway)
  - [**NACLs**](#nacls)
    - [NACL notes](#nacl-notes)
  - [**VPC Flow logs**](#vpc-flow-logs)
  - [**Bastion Hosts**](#bastion-hosts)
  - [**Direct connect**](#direct-connect)
    - [How to create direct connect](#how-to-create-direct-connect)
  - [**global accelerator**](#global-accelerator)
    - [components](#components)
  - [**VPC endpoint**](#vpc-endpoint)
    - [Interface endpoints](#interface-endpoints)
    - [Gateway endpoints](#gateway-endpoints)

## **VPC Overview**

---

> virtual data center in the cloud

- provision a logically isolated section of the AWS where you can launch resources in a virtual network you define
- total control over virtual networking environment
  - IP address range
  - creation subnets
  - route table configuration
  - network gateways
- easily customize network configuration
  - public subnet for webserver
  - backend systems private subnet
- you can create a virtual private network (VPN) connection between datacenters and your VPC

![vpc](/aws/associate-level/solutions-architect/media/vpc.PNG)

- can connect via
  - internet gateway
  - virtual private gateway
- both connect to router
- router directs traffic to route tables
- route tables direct traffic through network ACL
  - first line of defense
  - act like FW
  - stateless
- then move in to SG
- subnets
  - private, cannot access to internet
  - public, can be accessed via internet
- private ranges
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
- <https://cidr.xyz/>

### VPC features

- launch ec2 into subnets
- assign custom IP address ranges in each subnet
- configure RT between subnets
- create IGW and attach to VPC
- better security
- individual SG
- subnet network access control lists (ACLS)

### Default VPC

- user friendly
- all subnets have route out to the internet
- ec2 have public and private IP
- can be recovered if deleted
- comes with a default ACL, by default allows all inbound and outbound traffic

### Peering

- connect 1 vpc to another
  - via direct network route, using private ip addresses
- instances behave as if they were on the same network
- peer VPCs with other accounts
  - peer across regions
- peering is in a star configuration: ie 1 central VPC peers with 4 others
  - NO TRANSITIVE PEERING!

### VPC notes

- logical datacenters in AWS
- resources
  - IGWs (VPGW)
  - RT
  - NACLs
  - subnets
  - SG
- 1 subnet = 1 AZ
  - can have multiple subnets in 1 AZ
  - 1 subnet cannot be in multiple AZs

## **create VPC**

---

### creating a VPC

- The allowed block size is between a /28 netmasks and /16 netmasks
- creates
  - RT
  - NACLs
  - SG
  - router
- doesn't create
  - subnets
  - IGW

### creating subnet

- The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC), or a subset of the CIDR block for the VPC (for multiple subnets). The allowed block size is between a /28 netmasks and /16 netmasks. If you create more than one subnet in a VPC, the CIDR blocks of the subnets cannot overlap.
- can choose AZ
- assign CIDR block
- auto-assign public ip address is off by default
- reserve 5 ip addresses, For example, in a subnet with CIDR block 10.0.0.0/24, the following five IP addresses are reserved
  - 10.0.0.0: Network address.
  - 10.0.0.1: Reserved by AWS for the VPC router.
  - 10.0.0.2: Reserved by AWS. The IP address of the DNS server is the base of the VPC network range plus two. For VPCs with multiple CIDR blocks, the IP address of the DNS server is located in the primary CIDR. We also reserve the base of each subnet range plus two for all CIDR blocks in the VPC. For more information, see Amazon DNS server.
  - 10.0.0.3: Reserved by AWS for future use.
  - 10.0.0.255: Network broadcast address. We do not support broadcast in a VPC, therefore we reserve this address.

### creating IGW

- when created is detached
- attach to vpc
- only one IGW per VPC

### Configuring route table

- can have subnets communicating between each other
- have 2 route table
  - 1 for private subnets
  - 1 for public subnets
    - route out 0.0.0.0/0 to be public
    - target is IGW
- main route tables, is where subnets are created

### Creating notes

- new VPCs create RT, NACL and a default SG
- it wont create subnets nor IGW
- only 1 IGW per VPC
- SG cant span VPCs
- by default sg don't communicate with each other

## **NAT instances**

---

- created from NAT AMI
- source/destination checks must be disabled
- acting as a gateway
- edit RT to allow destination through our instance
- connects instances in a private subnet to the internet
- since is an instance is a bottleneck
- must be in public subnet
- the amount of traffic the instance supports depends on the instance
- behind a SG

## **NAT gateway**

---

- created in a public subnet
- need an EIP
- update RT
  - add route pointing the internet (0.0.0.0/0) to our NAT GW
- redundant inside the AZ
- only 1 NAT gw inside a AZ
  - should have 1 nat for each AZ
- 5 - 45 Gbps throughput
  - automatically scales
- no need to patch
- doesn't need SG
- automatically assigned a public ip address

## **NACLs**

---

> layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

- use increments of 100 to create rules
- newly created NACLs have inbound/outbound denied by default
- associate subnets to the NACL
  - subnets can only be associated to 1 NACL
  - multiple subnets can eb associated to a NACL
- stateless
  - inbound rules are not created as outbound rules
  - must be specified
- ephemeral port
  - inbound/outbound
  - 1024 - 65535
- rules are evaluated incrementally
  - first evaluates rule 100, then 200 ...
  - a deny must be before an allow
- have separate inbound and outbound rules

### NACL notes

- changes take place immediately
- evaluated before SG
- default VPC comes with NACL that allows all outbound/inbound traffic
- every subnet must have a NACL associated
  - default NACL if not
- can block specific ip address

## **VPC Flow logs**

---

> logs about the ip traffic going to and from network interfaces in your VPC

- stored using cloudwatch logs
- cen be viewed and retrieved in cloudwatch logs
- levels
  - vpc
  - subnet
  - network interface
- filter
  - accepted
  - reject
  - all
- destination
  - cloudwatch logs
    - destination log group
  - s3
- need an IAM role
- cannot enable flow logs for VPCs that are peered with your VPC, unless the peer VPC is in your account
- tag flow logs
- cannot change configuration once created
- not all traffic is monitored
  - to and from 169.254.169.254

## **Bastion Hosts**

---

- a way to connect to your instances
- cannot use a NAT gw as a bastion host

## **Direct connect**

---

> dedicated network connection from your premises to AWS

- private connectivity
- reduce network cost
- increase bandwidth throughput
- consistent network

![direct-connect](/aws/associate-level/solutions-architect/media/direct-connect.PNG)

### How to create direct connect

- Create a public virtual interface
- Create customer gateway
- create virtual private gateway
- attach virtual private gateway to the desired VPC
- create new VPN connection
- select virtual private gateway and the customer gateway
- set up VPC on the customer gateway or firewall

## **global accelerator**

---

> create accelerators to improve availability and performance of your application for local and global users

- directs traffic over optimal endpoints over the AWS global network
- by default global accelerator provides two static ip addresses
  - you can bring your own

### components

- static ip addresses
- accelerator
- DNS name
  - assign each accelerator a default DNS a4542121.awsglobalaccelerator.com
  - points to the static ip addresses
- network zone
  - isolated unit, availability zone
- listener
  - ports
  - protocol
  - processes inbound connection form clients to global accelerator
- endpoint group
  - associated with region
  - one or more endpoint in the region
  - increase/reduce the percentage of traffic that would be otherwise directed to and endpoint group - traffic dial
  - blue/green testing
- endpoint
  - NLB
  - ALB
  - EC2 instances
  - EIP
  - weighted endpoints

## **VPC endpoint**

---

> privately connect your VPC to supported AWS services and VPC endpoint services powered by private link

- doesn't require
  - IGW
  - NAT devices
  - VPC connection
  - Direct connect
- connect an ENI to a EC2 to be able to communicate to other AWS services without needing to transfers the internet
- traffic doesn't leave the amazon network

### Interface endpoints

- ENI with a private IP that serves as an entry point for traffic destined to a supported service
- services
  - API GW
  - CFN
  - cloudwatch

### Gateway endpoints

- services
  - S3
  - Dynamo
