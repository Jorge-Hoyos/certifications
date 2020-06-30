# Applications

- [Applications](#applications)
  - [**SQS**](#sqs)
    - [Standard queues](#standard-queues)
    - [FIFO queues](#fifo-queues)
    - [Visibility timeout](#visibility-timeout)
    - [Long polling](#long-polling)
    - [SQS notes](#sqs-notes)
  - [**SWF - Simple work flow service**](#swf---simple-work-flow-service)
    - [workflow starters](#workflow-starters)
    - [deciders](#deciders)
    - [activity workers](#activity-workers)
  - [**SNS**](#sns)
    - [Topics](#topics)
    - [Benefit](#benefit)
  - [**Elastic Transcoder**](#elastic-transcoder)
  - [**API Gateway**](#api-gateway)
    - [Configuration](#configuration)
    - [Deployment](#deployment)
    - [Caching](#caching)
    - [Same origin policy](#same-origin-policy)
    - [CORS - cross origin resource sharing](#cors---cross-origin-resource-sharing)
      - [CORS Example](#cors-example)
    - [API GW Notes](#api-gw-notes)
  - [**Kinesis**](#kinesis)
    - [Kinesis Streams](#kinesis-streams)
      - [Shards](#shards)
    - [Kinesis Firehose](#kinesis-firehose)
    - [Kinesis Analytics](#kinesis-analytics)
  - [**Cognito**](#cognito)
    - [Cognito user Pools](#cognito-user-pools)
    - [Cognito identity pools](#cognito-identity-pools)
    - [synchronization](#synchronization)

## **SQS**

---

> message queue that can be used to store messages while waiting for a computer to process them

- oldest service in AWS
- distributed queue system that enables web services apps to quickly and reliably queue messages from one component to the other
- queue: temporary repository of messages waiting for processing
- messages are not lost, if the compute component becomes unavailable while processing the message
- decouple the components of an app so they run independently
- messages can contain up to 256 KB of text in any format
  - not a hard limit, but it wont be stored in sqs (s3)
- acts as a buffer between the component producing and saving data, and the component receiving the data for processing
- resolves issues like
  - producing work faster than consuming
  - consuming work faster than producing

### Standard queues

- default
- nearly unlimited number of transaction per second
- guarantee that a message is delivered at least once
- occasionally
  - more than one copy of a message might be delivered
  - messages might deliver out of order
- best effort ordering, messages are generally delivered in the same order as they are sent

### FIFO queues

- complements the standard queue
- delivery
- exactly once processing
- the order of the messages are sent and receive is strictly preserved
- messages are always delivered once
  - remains available until a consumer processes and deletes it
  - no duplicate messaged
- support message groups, that allow multiple ordered message groups within a single queue
- limited to 300 TPS
  - but have all the capabilities of standard

### Visibility timeout

- amount of time the message is invisible in the queue after a reader pick up the message
- if the job is processed before the time out the message will be deleted form the queue
  - if the job is not processed, the message will become available again and another reader will process it
- this could result in the same message delivered twice
  - the job is taking longer than the visibility timeout
  - increase the visibility timeout
- maximum 12 hours

### Long polling

- short polling
  - return messages immediately
- long polling doesn't return a response until a message arrives in the queue, or times out
- ec2 asking constantly for messages incurs a cots
  - implement long polling

### SQS notes

- pull based, not pushed based
- can be kept in the queue from 1 minute to 14 days; default is 4 days
- guarantees that a message will be processed at least once
- decoupling your infrastructure use SQS
- message oriented API

## **SWF - Simple work flow service**

---

> coordinate work across distributed app components

- use cases
  - media processing
  - web app back ends
  - business process workflows
- coordination of tasks
- task represent invocation of various processing steps in an app, which can be performed by code, web service calls, human actions and scripts
- combining your digital environment with manual work
- used by amazon in warehouses
- workflow execution can last up to 1 year
- task oriented API
- ensures that a task is assigned once, and not duplicated
- keeps track of all the task and events in an app
- implement own application-level tracking
- a domain is a collection of related workflows

### workflow starters

- application that can initiate a workflow

### deciders

- control the flow of activity tasks in a workflow execution
- decides what to do next

### activity workers

- carry out the tasks

## **SNS**

---

> set up, operate, and send notification from the cloud

- scalable, flexible and cost effective capability to publish messages from an application and immediately deliver them to subscribers or other apps
- push notification
  - apple
  - google
  - windows devices
- push to mobile devices using SMS
- all messages published to sns are stored redundantly across multiple AZ

### Topics

- group multiple recipients using topics
- access point for allowing recipients to dynamically subscribe for identical copies of the same notification
- types
  - billing topic
  - scaling topic

### Benefit

- instantaneous push based delivery
- simple APIs and easy integration with applications
- pay as you go model

## **Elastic Transcoder**

---

> media transcoder in the cloud

- convert media files from their original sources in to different formats
- transcoding presets for popular output formats
- pay based on the minutes and resolution you transcode

## **API Gateway**

---

> publish, maintain, monitor and secure APIs at any scale

- doorway to your AWS environment
- application to access
  - data
  - business logic
- can be passes to
  - lambda
  - ec2
  - dynamodb
- what can do
  - expose HTTPS endpoint to define a RESTful API
  - serverless-ly connect to service like lambda and dynamo
  - send each API endpoint to a different target
  - low cost
  - scale effortlessly
    - automatically
  - track and control usage by API key
  - throttle requests to prevent attacks
  - connect to cloudwatch to log requests
  - maintain multiple versions of your API

### Configuration

- define an API (container)
- define resources and nested resources (URL paths)
- for each resource
  - select supported HTTP methods
  - set security
  - choose target (ec2, lambda, dynamo)
  - set request and response transformation

### Deployment

- deploy API to a stage
  - use API GW domain by default
  - can use custom domain
  - now supports AWS certificate manager: free SSL/TLS certs

### Caching

- cache your endpoints response
- reduce the number of call made to the endpoints
- reduce latency of requests to your API
- uses a TTL (in seconds)
- responds to the requests by looking the response from the cache
  - doesn't go to the lambda for a response

### Same origin policy

- a web browser permits scripts contained in a first web page to access data in a second web page, but only if both pages have the same origin
- prevents cross site scripting (XSS)
- enforced by web browsers
- ignored by postman and curl
- in AWS we are using different domain names
  - cloudfront domain name
  - s3 domain name

### CORS - cross origin resource sharing

- the server at the end can relax the same origin policy
- allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served
- web page in one domain, talk to a web page in another domain

#### CORS Example

- make HTTP option for a url (GET, PUT, POTS)
- server response: "these other domains are approved to GET this URL"
- Error - "origin policy cannot be read at the remote resource?"
  - enable CORS on API GW

### API GW Notes

- caching capabilities to increase performance
- low cost and scales automatically
- log results to cloudwatch
- CORS is enforced by the client

## **Kinesis**

---

stream data:
is data that is generated continuously by thousands of data sources, send the data simultaneously, usually in small size

- platform on AWS to send your streaming data to
- load and analyze streaming data

### Kinesis Streams

- persistently store your data up to 7 days
- by default store 24 hours, up to 7 days
- data producers
  - ec2, iot, mobile
  - Stream data to kinesis
- store data from the producers
- data is contained in shards
- data stored in shards is latter analyzed by ec2, called consumers
- once the data is analyzed it can be stored in (s3, dynamo, EMR, redshift)

#### Shards

- 5 transactions per second for reads
- up to a maximum total data read of 2MB per second
- 1000 records per second for write
- maximum total data write rate of 1 MB per second

### Kinesis Firehose

- no persistent storage
- data has to be analyzed as it comes in
- example used lambda to process data
- Key components:
  - delivery streams
  - records of data
  - destinations
- load streaming data into data stores and analytics tools
- capture, transform, and load streaming data into Amazon S3

### Kinesis Analytics

- works with firehose and streams
- analyze data on the fly, inside firehose and streams
- then stores the data (s3, redshift, elasticsearch cluster)

## **Cognito**

---

web identity federation:
lets you give your users access to resources after they have successfully authenticated with a web based identity provider

- sign up and sign in to your apps
- access for guests users
- acts as an identity broker between your app and web id providers
  - no need for additional code
- synchronize your user data for multiple devices
- recommended for all mobile applications aws services
- provides temporary credential which map to a role allowing access to the resources

### Cognito user Pools

- user based
- handles thins like user registration, authentication and account recovery
- user directories used to manage sign up and sign in functionality
- usernames, password, etc.
- can sign in
  - directly
  - using fb, amazon, google
- successful authentication generation a JSON web token (JWTs)

### Cognito identity pools

- enable provide temporary credentials to access aws services
- grants IAM role

### synchronization

- track association between user identity and the various different devices they sign in from
- uses push synchronization to push updates and synchronize user data across multiple devices
- use SNS to send a notification to all the devices associated with a given user
