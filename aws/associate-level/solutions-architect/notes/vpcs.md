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

## **VPC Overview**

---

> virtual data center in the cloud

- provision a logically isolated section of the AWS where you can launch resources in a virtual netowrk you define
- total control over virtual netowrking enviroment
  - IP address range
  - creation subnets
  - route table configuration
  - network gateways
- easily customize network configuration
  - public subnet for webservers
  - backend systems private subnet
- you can create a virtual private network (VPN) connection between datacenter and your VPC

![vpc](/aws/associate-level/solutions-architect/media/vpc.PNG)

- can conect via
  - internet gateway
  - virtual private gateway
- both connect to router
- router directs traffic to route tables
- route tables direct traffic through network ACL
  - first line of defense
  - act like FW
  - stateles
- then move in to SG
- subnets
  - private, cannot acces to internet
  - public, can be accessed via internet
- private ranges
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
- https://cidr.xyz/

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

### Peering

- connect 1 vpc to another
  - via direct network route, using private ip addresses
- instances behave as if they were on the same network
- peer VPCs with other accounts
  - peer across regions
- peering is in a star configuration: ie 1 central VPC peers with 4 others
  - NO TRANSITIVE PEERING!

### VPC notes

- logical datacenter in AWS
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

- The allowed block size is between a /28 netmask and /16 netmask
- creates
  - RT
  - NACLs
  - SG
  - router
- deosnt create
  - subnets
  - IGW

### creating subnet

- The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC), or a subset of the CIDR block for the VPC (for multiple subnets). The allowed block size is between a /28 netmask and /16 netmask. If you create more than one subnet in a VPC, the CIDR blocks of the subnets cannot overlap.
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

- can have subnets comunicating between each other
- have 2 route table
  - 1 for private subnets
  - 1 for public subnets
    - route out 0.0.0.0/0 to be public
    - target is IGW
- main route tables, is where subnets are created

### Creating notes

- new VPCs create RT, NACL and a default SG
- it wotn create subnets nor IGW
- only 1 IGW per VPC
- SG cant span VPCs
- by default sg dont communicate with each other

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
- behing a SG

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
- doesnt need SG
- automatically assigned a public ip address

## **NACLs**

---

> layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

- use increments of 100 to create rules
- newly created NACLs have inbound/outbound denied by default
- associate subnets to the NALC
  - subnets can only be associated to 1 NACL
  - multiple subnets can eb associated to a NACL
- stateless
  - inboud rules are not created as outbout rules
  - must be especified
- ephemeral port
  - inbound/outbound
  - 1024 - 65535
- rules are evaluated incrementally
  - first evaluates rule 100, then 200 ...
  - a deny must be before an allow

### NACL notes

- changes take place inmediatly
- evaluated before SG
- default VPC comes with NACL that allows all outbound/inbound traffic
- every subnet must have a NACL associated
  - default NACL if not
- can block specific ip address