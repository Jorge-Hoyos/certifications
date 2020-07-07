# **Security**

- [**Security**](#security)
  - [**Reducing security threats**](#reducing-security-threats)
    - [Bad actors](#bad-actors)
      - [Benefits of preventing bad actors](#benefits-of-preventing-bad-actors)
    - [NACL](#nacl)
    - [host based fw](#host-based-fw)
    - [ALB](#alb)
    - [NLB](#nlb)
    - [WAF - threat](#waf---threat)
  - [**Key management service - KMS**](#key-management-service---kms)
    - [AWS managed CMK](#aws-managed-cmk)
    - [Customer managed CMK](#customer-managed-cmk)
    - [AWS owned CMK](#aws-owned-cmk)
    - [Symmetric](#symmetric)
    - [Asymmetric](#asymmetric)
    - [KMS policy](#kms-policy)
    - [KMS notes](#kms-notes)
  - [**CloudHSM**](#cloudhsm)
  - [**Systems Manager Parameter Store - SSM**](#systems-manager-parameter-store---ssm)
    - [hierarchies](#hierarchies)
    - [Standard](#standard)
    - [Advanced](#advanced)
  - [**Secrets manager**](#secrets-manager)
  - [**Shield**](#shield)
    - [Shield Standard](#shield-standard)
    - [Shield Advanced](#shield-advanced)
  - [**WAF**](#waf)
    - [Behaviors](#behaviors)
    - [request properties](#request-properties)
  - [**Firewall manager**](#firewall-manager)

## **Reducing security threats**

---

### Bad actors

- automated processes
- content scrapers
- bad bots
- fake user agent
- DoS

#### Benefits of preventing bad actors

- reduce security threats
- lower overall costs

### NACL

- deny user access based on their IP
- block a certain IP or a range of IPs
- operates at layer 4

### host based fw

- linux fws
- windows fw

### ALB

- connection terminates at ALB

### NLB

- traffic passes through NLB
- client IP is visible end to end
- should use NACL to block IP

### WAF - threat

- IP blocking and filtering
- operates at layer 7
- block common attack like
  - sql injection
  - cross site scripting
- can be attached to cloudfront and ALB

## **Key management service - KMS**

---

- regional secure key management, encryption and decryption
- keys are regional
  - if you need to move an encrypted object from one region to another, you must decrypt it and encrypt it with a different key
- manages customer managed keys (CMKs)
- ideal for
  - s3 objects
  - db password
  - API keys stored in ssm
- can encrypt data up to 4 KB in size
- integrated with most AWS services
- pay per API call
- audit capability using cloudtrail
- FIPS 140-2 Level 2
  - level 3 HSM
- multi tenant
- select key administrator and key user

### AWS managed CMK

- free
- used by default in most services

### Customer managed CMK

- you create
- symmetric by default
- allows key rotation
- key policies
  - who can use it

### AWS owned CMK

- used by AWS on a shared basis across many accounts
- you wont see these

### Symmetric

- same key used for encryption and encryption
- AES-256
- never leases AWS unencrypted
- must call the KMS APIs to use
- services integrated with KMS use symmetric CMKs
- encrypt, decrypt and re-encrypt data
- import your own key material

### Asymmetric

- mathematically related public/private key pair
- based on RSA and ECC algorithms
- private key never leaves AWS unencrypted
- must call the KMS APIs to use private keys
- used outside AWS by users who cant call KMS APIs
- AWS services integrated with KMS do not support asymmetric CMKs

### KMS policy

- grants permission to certain identities to used the key

### KMS notes

- can have an alias
  - must have alias/ prefix
- keys are created with a default policy that allows access to the root user
- when decrypting a file you don't specify the key
  - when you encrypt it, it saves the key id in the meta data

```shell
aws kms encrypt --key-id id --plaintext file://file.txt --output text --query CiphertextBlob | base64 --decode > topsecret.txt.encrypted
aws kms decrypt --ciphertext-blob id fileb://topsecret.txt.encrypted --output text --query Plaintext | base64 --decode > topsecret.txt
```

## **CloudHSM**

---

- dedicated hardware security module (HSM)
- FIPS 140-2 level 3
- manage your own keys
- offers a single tenant multi AZ cluster dedicated to you
- managed service
  - no access to the AWS component
- runs within a VPC in you account
- industry-standard APIs - no AWS APIs
- compliant with
  - PKCS#11
  - JCE
  - CNG
- irretrievable if lost
- not HA by default

## **Systems Manager Parameter Store - SSM**

---

- serverless storage for configuration and secrets
  - passwords
  - db connection strings
  - API keys
- values can be stored encrypted (KMS) or plaintext
- store parameters in hierarchies
- track versions
- set TTL to expire values such as passwords
  - password rotation

### hierarchies

- up to 15 levels deep
- use hierarchies to store parameters
- grant identities to certain levels
  - /prod
  - /dev
  - /prod/db
- GetParametersByPath to retrieve all parameters in a hierarchy
  - /dev

### Standard

- limit of 10000 parameters
- up to 4 KB
- no additional charges
- parameter policies not available
- types
  - string
  - stringList
  - secureString
    - encrypted by KMS key

### Advanced

- more that 10000 parameters
- up to 8 KB
- parameter policies available
- charges apply

## **Secrets manager**

---

- rotate, manage and retrieve all kind of secrets
  - db credentials
  - API keys
- secure, audit and manage secrets to access resources in aws, on perm, third party services
- charge per secret stored and per 10000 API calls
- automatically rotate secrets
- apply new password in RDS for you
- generate random secrets
- shared cross accounts

## **Shield**

---

- protect against common attacks like
  - DDoS
  - cross site scripting
- sits at the edge of AWS perimeter network

### Shield Standard

- automatically enabled for all customer at no cost
- protect against common layer 3 and 4 attacks
  - SYN/UDP floods
  - reflection attacks

### Shield Advanced

- 3000 per month per org
- enhanced protection for
  - ec2
  - elb
  - cloudfront
  - global accelerator
  - r53
- 24x7 access to the DDoS response team
- DDoS cost protection

## **WAF**

---

- monitor HTTP, and HTTPS request to
  - cloudfront
  - ALB
  - API GW
- control access to content
- configure filtering rules to allow/deny traffic
  - IP address
  - query string parameters
  - SQL query injection
- block traffic return 403 forbidden code

### Behaviors

- allow all request, except the ones you specify
- block all request, except the ones you specify
- count the request that match the properties you specify

### request properties

- origination IP address
- originating country
- request size
- values in request headers
- regex patterns
- sql code injection
- cross site scripting

## **Firewall manager**

- centrally configure and manage fw rules across an organization
- waf rules
  - ALB
  - API GW
  - cloudfront
- shield advanced protections
  - alb
  - elb classic
  - eip
  - cloudfront distributions
- enable security groups for ec2 and ENIs
