# **Continuos integration**

[What is Continuous Integration?](https://aws.amazon.com/devops/continuous-integration/)

## **Explanation**

- Continuos integration is a DevOps software practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
- Refers to build or integration stage
- Goals
  - Find bugs quicker
  - improve software quality
  - Reduce time it takes to validate an release new updates

## Why is needed

- Reduce time merging codes from developers
- Reduce complexity

## How does it work

- Commit to a shared repository
- Run local unit tets before integrating
- A CI service automatically build an runs unit test on the new code changes to immediately surface any errors

![continuos integration](media/continuous_integration.png)
*Refers to the build and unit testing stages of the software release process*

- Every code change is build, tested and prepared for a release to production.

## Benefits

- Improve developer productivity
  - Freeing developers from manual tasks
- Find and address bugs quicker
- Deliver updates faster
