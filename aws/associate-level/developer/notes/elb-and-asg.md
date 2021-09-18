# **AWS Fundamentals: ELB + ASG**

- [**AWS Fundamentals: ELB + ASG**](#aws-fundamentals-elb--asg)
  - [**High Availability and Scalability**](#high-availability-and-scalability)
    - [scalability](#scalability)
      - [vertical](#vertical)
      - [horizontal](#horizontal)
    - [high availability](#high-availability)
  - [**Elastic load balancer ELB**](#elastic-load-balancer-elb)
    - [health checks](#health-checks)
    - [Classic load balancer (v1 old generation)](#classic-load-balancer-v1-old-generation)
    - [application load balancer](#application-load-balancer)
    - [network load balancer](#network-load-balancer)
  - [**Classic load balancer**](#classic-load-balancer)
  - [**Application load balancers ALB**](#application-load-balancers-alb)
    - [Route routing](#route-routing)
    - [target groups](#target-groups)
  - [**Network load balancer NLB**](#network-load-balancer-nlb)
  - [**Sticky sessions - session affinity**](#sticky-sessions---session-affinity)
  - [**cross zone load balancing**](#cross-zone-load-balancing)
  - [**SSL/TLS Certificates**](#ssltls-certificates)
    - [SNI](#sni)
  - [**Connection draining / de registration delay**](#connection-draining--de-registration-delay)
  - [**Auto scaling group (ASG)**](#auto-scaling-group-asg)
    - [attributes](#attributes)
    - [alarms](#alarms)
    - [rules](#rules)
    - [dynamic scaling policies](#dynamic-scaling-policies)
    - [predictive scaling](#predictive-scaling)
    - [metrics to scale](#metrics-to-scale)
    - [scaling cooldown](#scaling-cooldown)

## **High Availability and Scalability**

### scalability

- application can handle a bigger load by adapting

#### vertical

- increase size of instance
- scale from t2.micro to t2.large
- common for non distributed systems, such as db
- limit to how much you can scale

#### horizontal

- elasticity
- increase the number of instances for your applications
- 1 instance, to 5 instances
- distributed systems
  - web applications
- scale out increase number of instances
- scale in decrease number of instances

### high availability

- hand in hand with horizontal scaling
- running application in at least 2 azs
- survive the loss of a data center
- can be passive (RDS multi AZ)
- can be active (horizontal scaling)

## **Elastic load balancer ELB**

- Server that will forward internet traffic to multiple servers
- spread lead across multiple instances
- single point of access (DNS) to your application
- handles failure on instances
- do health checks on instances
- provide SSL termination (HTTPS) foy your websites
- enforce stickiness with cookies
- HA across AZ
- separate public traffic from private traffic
- managed load balancer
  - AWS takes care of upgrades, maintenance, HA
  - provides a few configuration knobs
- use newer generation
- it is integrated with many aws services
- internal
  - only from the vpc
- external
  - accessed from the internet
- can have an sg group attached
- load balancer talks to instances through HTTP
- can scale, but not instantaneously
- troubleshooting
  - 4xx error are client induced errors
  - 5xx error are application induced errors
  - 503 means at capacity or no registered targets
- monitoring
  - elb access logs will log all access requests
  - cloudwatch will give aggregate statistics

### health checks

- enable load balancer to know if instance is healthy, are available to reply to requests
- needs port and a route
- if the response is not 200, the instance is unhealthy

### Classic load balancer (v1 old generation)

- supports http, https, tcp

### application load balancer

- supports http, https, websocket

### network load balancer

- tcp, tls (secure tcp) and udp

## **Classic load balancer**

- support layer 4 and layer 7
- tcp, http and https
- fixed hostname

## **Application load balancers ALB**

- application lb is layer 7 (http)
- load balancing to multiple http application across machines (target groups)
- balance multiple applications on the same machine (ex: container)
- supports http/2 and websocket
- supports redirects http to https
- great for microservice and container based application
- redirect to a dynamic port in ecs
- fixed hostname
  - not not static private ip
- app servers don't see the ip of the client
  - ip is inserted in the header X-Forwarded-For
  - port and proto

### Route routing

- routing to different target groups
- routing based on path in url
- routing based on hostname in url
- routing based on query string, headers

### target groups

- ec2 instances (managed by an ASG) - http
- ecs tasks
- lambda functions
- ip addresses
- can route to multiple target groups
- health checks are at the target group level

## **Network load balancer NLB**

- layer 4
  - forward TCP and UDP traffic to your instances
  - handle millions request per second
  - less latency than others
- NLB has one static IP per AZ and support Elastic IP
- extreme performance, tcp or udp traffic
- the nlb forwards traffic direct to the ec2 instances, ports must be open to the world

## **Sticky sessions - session affinity**

- same client is always redirected to the same instance behind the lb
- works for CLB and ALB
- cookie used for stickiness has an expiration date you control
- make sure user doesn't lose his session data
- may bring imbalance load over the backend ec2
- application based cookies
  - custom cookie
    - generated by the target
    - custom name
    - include attributes required by the app
  - application cookie
    - generated by the lb
    - name is AWSALBAPP
- duration based cookies

## **cross zone load balancing**

- each lb instance distributes evenly across all registered instances in all az
- ALB
  - always on (cant be disabled)
  - no charges for inter az data
- NLB
  - disabled by default
  - pay charges for inter AZ if enabled
- CLB
  - console enabled
  - cli/api disabled
  - no charges for inter AZ data if enabled

## **SSL/TLS Certificates**

- SSL (secure sockets layer) allows traffic between client and lb to be encrypted in transit (in flight encryption)
- TLS (transport layer security) newer version of SSL
- public ssl are issued by certificate authorities
  - GoDaddy, Symantec
- have an expiration date
- LB does SSL termination, talks to instance using HTTP
- LB uses an X.509 certificate
- manage certificates using ACM
- create upload own certificates
- https listener:
  - must specify default certificate
  - list of certificates to support multiple domains
  - clients can use SNI (server name indication) specify the hostname they reach
- CLB
  - only one ssl
- ALB and NLB
  - support multiple listener with multiple ssl
  - uses sni to make it work

### SNI

- solves problem loading multiple ssl certificates onto one web server
- client indicate the hostname of the target server
- server will find the certificate, or return default one
- only works for ALB and NLB, cloudfront

## **Connection draining / de registration delay**

- CLB
  - connection draining
- ALB and NLB
  - de registration delay
- time to compile in flight request while the instance is de-registering or unhealthy
  - default 300s, between 1 - 3600
- stops sending new request to the instances that is de registering
- can be disabled (set value to 0)

## **Auto scaling group (ASG)**

- scale out and in ec2 instances
- ensure we have a min and max number of machines running
- automatically register new instances to a lb
- use launch configuration or launch templates
- IAM role gets passed to the instances launched
- free, pay for the resources
- replaces terminates instances
- unhealthy instances can be terminated and replace them

### attributes

- launch configuration
  - ami
  - instance type
  - ec2 user data
  - ebs volumes
  - SG
  - ssh key pair
- min/max/initial capacity
- network and subnet information
- load balancer information
- scaling policies

### alarms

- possible to scale on cloudwatch alarms
- tiger ASG
- an alarm monitors a metric (cpu, memory, etc)
- average of instances

### rules

- target average cpu
- number request on the elb per instance
- custom metrics

### dynamic scaling policies

- target tracking scaling
  - average cpu at 40%
- simple and step scaling
  - cloudwatch alarm triggered do something
- scheduled actions
  - anticipate scaling based on known usage pattern

### predictive scaling

- forecast load and schedule scaling ahead

### metrics to scale

- cpu utilization
- request count per target
- average network in/out
- custom metrics

### scaling cooldown

- after scaling you are in cooldown (default 300s)
- asg will not launch or terminate additional instances (metrics to stabilize)
