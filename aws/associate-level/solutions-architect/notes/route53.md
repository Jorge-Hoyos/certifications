# **Route53**

- [**Route53**](#route53)
  - [**DNS 101**](#dns-101)
    - [top level domains](#top-level-domains)
    - [Domain registrars](#domain-registrars)
    - [Start of authority record (SOA)](#start-of-authority-record-soa)
    - [NS (name server) records](#ns-name-server-records)
    - [A Records](#a-records)
    - [TTL](#ttl)
    - [CName](#cname)
    - [Alias records](#alias-records)
    - [R53 Notes](#r53-notes)
  - [**Register a domain name**](#register-a-domain-name)
  - [**Route 53 - Routing policies**](#route-53---routing-policies)
    - [Simple routing](#simple-routing)
    - [Weighted routing](#weighted-routing)
    - [Latency-based routing](#latency-based-routing)
    - [Failover routing](#failover-routing)
    - [Geo location routing](#geo-location-routing)
    - [Geo proximity routing](#geo-proximity-routing)
    - [Multi value answer routing](#multi-value-answer-routing)
    - [Health checks](#health-checks)

## **DNS 101**

---

> DNS is like a phone book

- used to convert human friendly domain names, into an internet protocol (IP) address
- IP address are used by computers to identify each other on the network
- forms
  - IPv4
    - 32 bit field
    - over 4 billion different addresses
    - finite number of addresses
  - IPv6
    - address space of 128 bits
    - in theory 3.4×1038 addresses

### top level domains

- las word on a domain represents the top-level domain (.com, .edu, .gov)
- second level domain name ( .co.uk, .gov.uk)
- these are controlled by IANA
  - database of all available top level domains

### Domain registrars

- authority that can assign domain names
- registered with InterNIC, service of ICANN
  - enforces uniqueness of domain names
- each domain becomes registered in a central DB known as WhoIS DB

### Start of authority record (SOA)

- where the DNS is going to start
- name of the server that supplied the data for the zone
- administrator of the zone
- current version of data file
- default number of seconds for the ttl on resource records

### NS (name server) records

- used by top level domain server to direct traffic to the content DNS server which contain the authoritative DNS records
- give us the SOA

![ns-record](/aws/associate-level/solutions-architect/media/ns-record.PNG)

### A Records

- Address
- used by computers to translate de domain to an IP address

### TTL

- time to live in seconds
- length that a DNS record is cached
- the lower the TTL, the faster changes to DNS records take to propagate throughout the internet
- if some one goes to your website, they cache your ip address, and if you change the DNS can take 48 hours to take effect

### CName

- canonical name
- used to resolve one domain name to another
- m.acloud.guru, mobile.acloud.guru both resolve to the same another reference
- cant be used for naked domains (zone apex record)
  - you cant have a CName for acloud.guru must be either A record or Alias

### Alias records

- map resource records sets in your hosted zone to ELB, cloudfront, or S3 buckets that are configured as website
- works like a cname
- map one DNS (example.com) to another target DNS name (elb1234.elb.amazonaws.com)

### R53 Notes

- ELBs do not have a pre-defined IPv4 addresses; you resolve to them using a DNS name
- understand difference between Alias record and a CName
  - always choose alias record
- DNS types
  - SOA records
  - NS
  - A records
  - CNAMES
  - MX Records
  - PTR Records

## **Register a domain name**

---

- you must first register a domain, to be able to create alias, or cnames
- can buy domain names from AWS

## **Route 53 - Routing policies**

---

### Simple routing

- one record with multiple IP addresses
- if multiple values, route 53 returns all values in a random order

### Weighted routing

- allows to split traffic based on different weights assigned
- 10% to us-east-1 and 90% to us-east-2
- one ip address per record
  - you assign a weight
  - and ID

### Latency-based routing

- route traffic based on the lowest network latency for your end user
- latency resource record set

### Failover routing

- active/passive set up
- primary site in us-east1
  - secondary site DR in eu-west-2
- R53 monitor health of primary site
  - health check monitors the health of your endpoints

### Geo location routing

- choose where your traffic will be sent based on the geographic location of your users
- send europeans customer to european servers (language, symbols, etc.)
- send us customer to us servers

### Geo proximity routing

- route traffic to you recourses based in the geographic location of your users and your resources
- must use traffic flow
- coordinates

### Multi value answer routing

- return multiple values, such as IP addresses for your web servers, in response to DNS queries
- simple routing with health checks

### Health checks

- set health checks on individual record sets
- can assign health checks
- if fails, removed from r53 until it passes the health check
  - SNS notification
