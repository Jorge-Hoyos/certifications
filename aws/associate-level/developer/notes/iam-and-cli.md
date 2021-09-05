# **IAM And AWS CLI**

- [**IAM And AWS CLI**](#iam-and-aws-cli)
  - [**IAM Introduction: Users, Groups, Policies**](#iam-introduction-users-groups-policies)
    - [Permissions](#permissions)
  - [**IAM Policies**](#iam-policies)
  - [**IAM MFA Overview**](#iam-mfa-overview)
    - [Password policy](#password-policy)
    - [MFA](#mfa)
    - [MFA devices options](#mfa-devices-options)
  - [**Access keys, CLI and SDK**](#access-keys-cli-and-sdk)
    - [CLI](#cli)
    - [SDK](#sdk)
  - [**Cloud shell**](#cloud-shell)
  - [**IAM Roles**](#iam-roles)
  - [**IAM Security tools**](#iam-security-tools)
    - [Credentials report (account-level)](#credentials-report-account-level)
    - [IAM Access Advisor (user-level)](#iam-access-advisor-user-level)
  - [**IAM Best practices**](#iam-best-practices)

## **IAM Introduction: Users, Groups, Policies**

- Global service
- Root account, shouldn't be used
- Users represents one person, can be grouped
  - Developers
  - Operations
- Groups only contain users, not other groups
- User can be in multiple groups

### Permissions

- User or groups can be assigned JSON document called policies
- Define permissions of the users
- least privilege principle

## **IAM Policies**

- All policies assign to a group are inherited by everyone on the group
- inline policies is only attached to a user
- consist of
  - version number
  - id - identifier (optional)
  - statement one or more (requires)
    - Sid - identifier
    - effect - allow or deny
    - Principal - account, user or role this policy applies to
    - action - api call that allows or deny
    - resource - list of aws resource the action applies to
    - condition - when the statement is in effect
- policies get inherited in different ways

## **IAM MFA Overview**

### Password policy

- Minimum password length
- required specific character types
  - uppercase
- allow user to change their password
- password expiration
- prevent password re-use

### MFA

- Must and recommended
- Protect root account and iam users
- MFA = password you know + security device you own

### MFA devices options

- Google authenticator
- Authy
  - support for multiple tokens on a single device (root accounts, iam users, etc.)
- universal 2nd factor Yubikey
- Hardware key fob MFA device - gemalto
- Hardware key fob MFA device for aws GovCloud (US) - SuerPassID

## **Access keys, CLI and SDK**

- three options
  - management console
  - CLI
  - SDK - for code
- access keys are generated from the console
- users manage their own access keys
- AK are secrets. Do not share

### CLI

- allows to interact with aws apis through the command line shell
- direct access to the public apis of aws services
- can work with scripts

### SDK

- software development kit
- Language specific APIS
- set of libraries
- supports
  - python
  - java

## **Cloud shell**

- Only available in certain regions
- Can execute aws commands
- terminal in the cloud of aws
- free to use
- uses your console role to make the cli calls
- you have a full repository of files
- download and upload files

## **IAM Roles**

- aws services need to perform actions on your behalf
- they are like users
- need precisions assigned
- not to be used by people, but by aws resources
- common roles:
  - ec2 instance roles
  - lambda function roles
  - cloudformation deployment roles
- used to grant permissions to entities that you trust

## **IAM Security tools**

### Credentials report (account-level)

- a report that lists all your accounts users and the status of their credentials

### IAM Access Advisor (user-level)

- shows permissions granted to a user and when those were last accessed
- Revise your policies

## **IAM Best practices**

- Do not use the root account
- One physical user = onw aws users
- assign user to groups and assign permissions to groups
- create a strong password policy
- Use and enforce MFA
- Create and use roles for AWS services
- Audit permission use the IAM credentials report
- never share iam suers and access keys
