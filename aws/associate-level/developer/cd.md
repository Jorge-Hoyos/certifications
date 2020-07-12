# **Continuos delivery**

- [**Continuos delivery**](#continuos-delivery)
  - [**Explanation**](#explanation)
  - [**Continuos delivery vs continuos deployment**](#continuos-delivery-vs-continuos-deployment)
  - [**Benefits**](#benefits)

## **Explanation**

> software development practice where code changes are automatically prepared for a release to production

- Expands upon CI by deploying all code changes to a testing environment and/or production environment after the build stage
- Automate testing beyond unit tests
  - UI testing
  - Load testing
  - Integration testing

## **Continuos delivery vs continuos deployment**

**Delivery**:

every code change is built, test and then push to a testing environment

Continuos delivery:
need manual approval

Continuos deployment:
doesn't need manual approval

![continuos integration](media/continuous_integration.png)
*Automates the entire software release process*

## **Benefits**

- Automate the software release process
  - Deliver efficiently and rapid
- Improve developer productivity
  - Freeing from manual tasks
- Find and address bugs quicker
- Deliver updates faster
  - Deliver to customer faster and frequently
