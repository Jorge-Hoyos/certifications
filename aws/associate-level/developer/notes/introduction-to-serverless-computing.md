# Introduction to Serverless Computing

- [Introduction to Serverless Computing](#introduction-to-serverless-computing)
  - [**Lambda**](#lambda)
    - [**Lambda notes**](#lambda-notes)
  - [**API Gateway**](#api-gateway)
    - [**Types of APIs**](#types-of-apis)
    - [**Functions**](#functions)
    - [**Configure API GW**](#configure-api-gw)
    - [**API catching**](#api-catching)
    - [**Same origin policy**](#same-origin-policy)
    - [**Cross-origin resource sharing (CORS)**](#cross-origin-resource-sharing-cors)

## **Lambda**

---

> compute service where you can upload your code and create a lambda function

- takes care of provisioning server
- ways
  - event-driven compute service (trigger)
  - run code response to http request
- languagues
  - node.js
  - java
  - python
  - c#
  - go
- pricing
  - number of requests (1 million free)
  - duration (rounded up to the nearest 100ms)

### **Lambda notes**

- scales out
- lambda functions are independent, 1 event = 1 function
- lambda is serverless
- lambda functions can trigger other lambda functions
- lambda can do things globally

## **API Gateway**

---

> API: Application programming interface, comunication between systems

Fully managed service that makes it easy for developer to publish, maintain, monitor and secure APIs at any scale. APIs acts as a front door for applications to access data, business logic, or functionality from your back-end services.

### **Types of APIs**

REST APIs (REpresentational State Transfer):

- 70% of the internet
- newer API
- Uses JSON

SOAP APIs (Simple Object Access Protocol):

- late 90's
- uses XML

### **Functions**

- Expose HTTPS endpoints to define a RESTful API
  - Give us a HTTPS URL that we can make calls to, and how the API respond to those calls
- Serverless-ly connect to services like Lambda and DynamoDB
- Send each API endpoint to a different target
- Run efficiently with low cost
- Scale effortlessly
- Track and control usage by API key
- Throttle request to prevent attacks
- Connect to CloudWatch to log all requests for monitoring
- Maintain multiple versions of your API

### **Configure API GW**

- Define an API (Container)
- Define resources and nested resources (URL paths)
- For each resource:
  - select supported HTTP methods (verbs, get, delete, post)
  - set security
  - choose target (ec2, lambda, etc)
  - set request and response transformation
- Deploy API to a stage (prod, stage, etc)
  - Uses API GW domain by default
  - can use custom domain
  - Support AWS certificate manager: free SSL/TLS certs

### **API catching**

- Cache your endpoint's response
- Reduce he number of calls made to the endpoint and improve latency
- It has to be enabled for a stage
- It has a TTL in seconds
- Checks if the request is cached or not
  - if it is returns the resposne
  - if not goes to the service for the response

### **Same origin policy**

- Web browser permits scripts contained in a first web page to access data in a second web page, but only if both web pages hace the same origin
- Prevent cross-site scripting (XSS) attack
- Enforced by web browsers
- Ignored by tools like postman and curl

### **Cross-origin resource sharing (CORS)**

- On way the server at the other end (not the client code in the browser) can relax the same-origin policy
- a way for API GW to talk to S3
- CORS is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served
- allowing code that is in one bucket, reference code that is in another bucket
- by default objects cannot reach each other in other buckets
