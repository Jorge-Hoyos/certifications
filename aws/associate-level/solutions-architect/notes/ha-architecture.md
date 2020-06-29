# **HA Architecture**

- [**HA Architecture**](#ha-architecture)
  - [**Load Balancers**](#load-balancers)
    - [Application load balancers](#application-load-balancers)
      - [sticky sessions alb](#sticky-sessions-alb)
    - [Network load balancers](#network-load-balancers)
    - [Classic load balancers](#classic-load-balancers)
      - [sticky sessions clb](#sticky-sessions-clb)
    - [Target group](#target-group)
    - [x-forwarded-for header](#x-forwarded-for-header)
    - [cross zone load balancing](#cross-zone-load-balancing)
    - [Path patterns](#path-patterns)
    - [ELB notes](#elb-notes)
  - [**Auto scaling**](#auto-scaling)
    - [groups](#groups)
    - [configuration template](#configuration-template)
    - [scaling options](#scaling-options)
      - [maintain current instance levels at all times](#maintain-current-instance-levels-at-all-times)
      - [manually](#manually)
      - [based on schedule](#based-on-schedule)
      - [based on demand](#based-on-demand)
      - [use predictive scaling](#use-predictive-scaling)
  - [**HA Architecture notes**](#ha-architecture-notes)
  - [**Elastic Beanstalk**](#elastic-beanstalk)

## **Load Balancers**

---

- physical or virtual device that helps balance loads
- balance loads across web servers

### Application load balancers

- best suited for HTTP and HTTPS traffic
- intelligent routing decisions
- operate at layer 7
- application aware
- advanced request routing, sending specified requests to specific web servers

#### sticky sessions alb

- traffic will be sent at the target group level

### Network load balancers

- best suited for load balancing of TCP traffic where extreme performance is required
- operates at layer 4 (connection level)
- millions of request per second, with ultra low latencies
- use for extreme performance

### Classic load balancers

- Legacy ELB
- low cost
- balance HTTP/HTTPS
- layer 7 features
  - sticky sessions
  - X forwarded
- also layer 4 balancing
- doesn't use target groups
- routes each request independently to the registered ec2 with the smallest load

#### sticky sessions clb

- bind a user session to a specific ec2
- all request are sent to the same instance
- if an ec2 is not receiving any traffic, disable sticky session

### Target group

- groups of EC2 instances
  - can be one for NA
  - another for EU
- routes requests to the targets
- using setting you specify
- performs health checks on the targets
- target type
  - instance
  - IP
  - Lambda

### x-forwarded-for header

- passes the IPv4 address from the user to the EC2

### cross zone load balancing

- load balancer are able to send traffic to other AZs
- if you want to get traffic from a load balancer in another AZ

### Path patterns

- listener with rules to forward request based on the url path
- route traffic to back-end services using path based routing
- traffic to <mrurl.com> goes to us-east-1a
- traffic to <mrurl.com/images/> goes to us-east-1b

### ELB notes

- 504 error, gateway has timed out
  - application not responding within the idle timeout period
  - ec2 or db error, not the balancer
- ELB can be inside a private subnet (not internet facing)
- health check the instance by talking to it
- load balancer have their own DNS
- instances monitored by ELB are reported as
  - InService
  - OutOfService

## **Auto scaling**

---

- ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application

### groups

- logical components
- webserver groups, db group

### configuration template

- groups use a launch configuration
- instructions on what instance to launch, size, OS, SG, etc.

### scaling options

- way to scale you ASG
  - dynamic scaling (CPU utilization)
  - schedule

#### maintain current instance levels at all times

- performs a periodic health check on the instances within the ASG
- when it finds an unhealthy instance, terminates it and launch a new one

#### manually

- minimum
- maximum
- desired capacity
- AS manages the process of creating/terminating to maintain the updated capacity

#### based on schedule

- scaling actions are performed automatically as a function of time and date
- when you know your workload

#### based on demand

- using scaling policies
- define parameters that control the scaling process
  - \>50% CPU

#### use predictive scaling

- use EC2 Auto Scaling with AWS Auto Scaling
- help maintain optimal availability and performance
- predictive scaling and dynamic scaling

## **HA Architecture notes**

---

- always plan for failure
- always design for failure
- multiple AZs and regions when you can
- consider the cost element

![ha-architecture](/aws/associate-level/solutions-architect/media/ha-architecture.PNG)

## **Elastic Beanstalk**

---

- upload your code, and AWS provision your infrastructure
- can use auto scaling with elastic beanstalk
- can modify thing like
  - capacity
  - security
  - software
- don't have to worry about the infrastructure that runs the applications
