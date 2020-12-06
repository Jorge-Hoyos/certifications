# **Beginners Guide to IAM**

---

- [**Beginners Guide to IAM**](#beginners-guide-to-iam)
  - [**IAM 101**](#iam-101)
    - [Terms](#terms)

## **IAM 101**

---

- Identity fedaration (including AD, Facebook, linkedIn)
- Provides temporary access fro user/devices and services, as necessary
- support PCI DSS compliance
- IAM is Universal
- Root account is the email address used when created the account, shouldnt be used
- new user have no permissions at all
- new users get assigned a access key id and secret access key
- set up MFA on root account

### Terms

- Users - End Users
- Groups - collection of users under one set of permissions
- Roles - Assign roles to AWS resources, used to assign permissions
- Policies - Document that define one or more permissions
