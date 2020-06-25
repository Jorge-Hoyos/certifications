# **Advanced IAM**

- [**Advanced IAM**](#advanced-iam)

## **Directory service**

---

> connects AWS resources with on-premises Active directory

- log into aws using existing corporate credentials

### Active directory

- on-premises directory service
- hierarchical database of users, groups, computers
- group policies
- LDAP and DNS

### managed microsoft AD

- AD domain controllers (DCs) running windows server
- reachable by application in your VPC
- add DCs for HA and performance
- private
- extend existing AD to on-premises using AD trust

#### Customer responsibilities

- users, groups, GPOs
- standard AD tools
- scale out DCs
- trust
- certificate authorities (LDAPS)
- federation

### Simple AD

- stand along managed directory
- basic AD features
- 500-5000 users
- easier to manage EC2
- do not support trusts (cant join on-premises AD)

### AD connector

- use exiting on premises directory with compatible AWS services
- directory gateway for on-premises AD
- avoid caching information in the cloud
- allow on premises users to log in to AWS using AD
- scale multiple AD connectors

### Cloud directory

- directory based store for developers
- multiple hierarchies with hundreds of millions of objects
- use cases
  - org charts
  - course catalog
- fully managed

### Cognito user pools

- managed user directory for SaaS apps
- sign-up and sign-in for web or mobile
- work with social media identities

![ad-compatible-non](/aws/associate-level/solutions-architect/media/ad-compatible-non.PNG)

## **IAM policies**

---

### ARN

- uniquely identifies amazon resources
- arn:partition:service:region:account_id:resource...
  - arn:aws:iam::1234567890123:user/mark
    - doesn't have region, cause iam is not regional
  - arn:aws:s3:::bucket/image.png
    - doesn't have region, or account, because s3 is global

### IAM policies

- JSON documents that defines permissions
- identity policy
  - what an identity can do
- resource policy
  - who has access to the resource
  - what actions can perform
- no effect until attached
- list of statements
  - each statement matches an AWS API request
    - create-ec2-instance
- parts
  - Effect
  - Action
  - Resource
- types of policies
  - customer managed
    - max of 6144 characters
  - aws managed

### Permission boundaries

- don't allow or denied permission on its own
- define the maximum permission an entity can have
- used to delegate administration to other users
- for users or roles
- prevent privilege escalation or unnecessarily broad permissions
- only allows to perform the actions allowed bye the entity based policies and its permission boundaries
- control maximum permission an IAM policy can grant
- use cases:
  - developers creating roles for lambda
  - app owners creating roles for ec2 instances

### IAM Notes

- not explicitly allowed = implicitly denied
- explicit deny overrides any other permission
- AWS joins all applicable policies

## **Resource access manager (RAM)**

---

> helps you to share cross account resources

- create resources centrally, and shared them with other accounts using RAM
- can only share
  - app mesh
  - aurora
  - codebuild
  - ec2
  - ec2 image builder
  - license manager
  - resource groups
  - route53
- works with invitation with the account

## **SSO**

---

> centrally manage access to AWS accounts and business applications

- centrally manage accounts
- use existing corporate identities
- manage user permissions across all accounts
- works with any SAML 2.0 identity provider
