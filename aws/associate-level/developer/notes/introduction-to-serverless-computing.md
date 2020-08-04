# Introduction to Serverless Computing

- [Introduction to Serverless Computing](#introduction-to-serverless-computing)
  - [**Lambda**](#lambda)
    - [**Lambda notes**](#lambda-notes)

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