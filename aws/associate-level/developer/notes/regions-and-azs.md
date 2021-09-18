# **Regions and AZs**

---

- [**Regions and AZs**](#regions-and-azs)
  - [**Regions**](#regions)
    - [Choosing regions](#choosing-regions)
  - [**Availability zones**](#availability-zones)
  - [**Edge location**](#edge-location)
  - [**Global services**](#global-services)
  - [**Region scoped**](#region-scoped)

## **Regions**

- Cluster of data centers
- All around the world
- Most AWS services are region-scoped

### Choosing regions

- Compliance
- Proximity
- Available services
- Pricing

## **Availability zones**

- Each region has many AZ
  - usually 3
  - 2 min
  - 6 max
- each AZ is one or more discrete data center
  - redundant power
  - networking
  - connectivity
- separate from each others
- connected with high bandwidth

## **Edge location**

- content is delivered to end users with low latency
- all over the world

## **Global services**

- IAM
- R53
- Cloudfront
- WAF

## **Region scoped**

- EC2
- EBS
- lambda
- Rekognition
