# **Serverless**

- [**Serverless**](#serverless)
  - [**Lambda**](#lambda)
    - [Pricing](#pricing)
    - [X-ray](#x-ray)
    - [Lambda notes](#lambda-notes)
  - [**Alexa skills**](#alexa-skills)
    - [Skill service](#skill-service)
    - [skill interface](#skill-interface)
  - [**SAM - serverless application model**](#sam---serverless-application-model)
  - [**Elastic Container Service - ECS**](#elastic-container-service---ecs)
    - [Contianer](#contianer)
    - [ECS](#ecs)
    - [Cluster](#cluster)
    - [task definition](#task-definition)
    - [container definition](#container-definition)
    - [task](#task)
    - [service](#service)
    - [registry](#registry)
    - [Fargate](#fargate)
    - [EKS](#eks)
    - [ECR](#ecr)
    - [ECS + ELB](#ecs--elb)
    - [ECS security](#ecs-security)

## **Lambda**

---

- upload you code and create a lambda function
- lambda takes care of provisioning and managing the server
  - dont have to worry about OS, patching, scaling
- use lambda in
  - event(triggers) driven
    - response to events (data changed in s3)
  - response to HTTP requests using API GW

### Pricing

- number of request
- duration
- memory

### X-ray

serverless architectures can get extremely complicated
x-ray allows you to debug what is happening

### Lambda notes

- lmabda scales out (not up) automatically
- independent, 1 event = 1 function
- can do things globally

## **Alexa skills**

### Skill service

- lambda

### skill interface

- invocation name
- intent schema
- slot type
- utterances

## **SAM - serverless application model**

---

- open source framework that allows you to build serverless applications easily
- cloudformation extension optimized for serverless applications
- new types: functions, APIs, tables
- supports anyhting that cloudformation supports
- run serverless application locally using docker
- package and deploy using CodeDeploy

## **Elastic Container Service - ECS**

---

### Contianer

- software package that contains
  - application
  - libraries
  - runtime
  - tools
- required to run an application
- containerized application are portable, and offer a consistent environment

### ECS

- managed container orchestration service
  - run and scale containerized applications
- create clusters to manage floots of container deployments
  - ec2
  - fargate
- monitor resource utilization
- deploy, update, roll back containers
- free
- integrates with VPC, sg, EBS, ELB
- cloudtrail and cloudwatch

### Cluster

- logical collection of ec2 resources
- either ec2, or fargate instances

### task definition

- defines your application
- similar to dockerfile, but for containers in EC2
- can contain multiple containers
  - containers that always need to run together, place them in the same definition

### container definition

- inside task definition
- defines individual containers a task uses
- cpu, memory, and port

### task

- single running copy of any containers defined by a definition
- one working copy of an application

### service

- allows task definitions to be scaled by adding tasks
- defines minimum and maximum values

### registry

- storgae repository or container images
- ecr
- docker hub
- download images to create container

### Fargate

- serverless compute engine for containers
- works with
  - ecs
  - eks
- eliminated need to provision and manage servers
- each workload (task, pod) runs in its own kernel
- isolation and security

### EKS

- K8s open source softwar that lets you deploy and manage containerized applications at scale
- containers are grouped in pods

### ECR

- managed docker container registry
- store manage and deploy images
- HA
- pay for storage and data transfer

### ECS + ELB

- distribute traffic evenly across taks
- supports
  - ALB
  - NLB
  - CLB
- ALB (recommended) allows
  - dynamic host port mapping
  - path based routing

### ECS security

- ec2 instance role
  - all task running on the instance will inhereit the role permissions
- task role
  - applies policy per task
