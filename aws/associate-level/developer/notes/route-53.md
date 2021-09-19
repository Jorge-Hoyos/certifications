# **Route 53**

- [**Route 53**](#route-53)
  - [**DNS**](#dns)
    - [terminologies](#terminologies)
  - [**Route 53 Overview**](#route-53-overview)
    - [Records](#records)
    - [record types](#record-types)
    - [hosted zones](#hosted-zones)
  - [**Records TTL**](#records-ttl)
  - [**CNAME vs Alias**](#cname-vs-alias)
    - [CNAME](#cname)
    - [Alias](#alias)
      - [targets](#targets)
  - [**Routing policies**](#routing-policies)

## **DNS**

- Domain name system
- translate human friendly hostnames into the machine ip addresses
- uses hierarchical naming structure

### terminologies

- domain registrar: amazon r53, GoDaddy ...
- dns records: a, aaaa ...
- zone file: contains dns records
- name server: resolves dns queries
- top level domain (TLD): .com, .us
- second level domain (SLD): amazon.com, google.com

## **Route 53 Overview**

- HA, scalable, fully managed and authoritative DNS
  - authoritative customer can update the dns records
- domain registry
- ability to check the health of your resources
- only service with 100% SLA

### Records

- domain/subdomain name
- record type
  - a
  - aaaa
  - cname
  - ns
- value
- routing policy
- ttl

### record types

- A
  - maps a hostname to IPv4
- AAAA
  - maps a hostname to IPv6
- CNAME
  - maps a hostname to another hostname
  - target must have an A or AAAA record
- NS
  - name servers for the hosted zones

### hosted zones

- container for records that define how to route traffic to a domain and subdomains
- public hosted zone
  - answer queries from public clients
- private hosted zone
  - allow to identify private resources with private domains
- pay $0.50 per month per hosted zone

## **Records TTL**

- Cache the result of the record for a certain time
- high ttl
  - less traffic on r53
  - possibly outdated record
- low ttl
  - more traffic on r53 ($$)
  - records are outdated for less time
  - easy to change record
- Mandatory for every record except Alias
- if the record is cached and it changes ip address, you will get the previous record

## **CNAME vs Alias**

- AWS resources expose hostname
  - lb-us-eat-2-elb.amazonaws.com and you want my.domain.com

### CNAME

- points a hostname to any other hostname
  - app.mydomain.com -> example.mydomain.com
- only for non root domain (mydomain.com)

### Alias

- Point a hostname to an AWs resource
  - app.mydomain.com -> example.amazonaws.com
- works for root domain and non root domains
- free of charge
- health check
- maps a hostname to an aws resource
- an extension to dns functionality
- unlike cname can be used for top node of a dns (zone apex)
- Alias records is always of type A/AAAA for aws resources
- you cant set the ttl

#### targets

- elb
- cloudfront distributions
- api gateway
- elastic beanstalk env
- s3 websites
- vpc interface endpoints
- global accelerator accelerator
- route 53 records in the same hosted zone
- NOT FOR ec2 dns name

## **Routing policies**

- routing policies
- anothers
