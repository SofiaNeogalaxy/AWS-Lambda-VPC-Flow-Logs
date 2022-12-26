
# VPC Flow Logs Lambda Function

**AWS Lambda function*** that automatically enables Amazon VPC flow logs when a new VPC is created.

The function is triggered by an **Amazon CloudWatch Event** that is set to respond to the  **'CreateVpc'** event. When a new VPC is created, the function extracts the VPC ID from the event and uses it to create a **new log group** for the VPC flow logs in Amazon CloudWatch Logs. It then checks if **flow logs** are already enabled for the VPC, and if not, it **enables** them. The flow logs are delivered to an **Amazon S3** bucket that is specified as an environment variable in the function.

**This function can be useful for ensuring that flow logs are always enabled for new VPCs, which can help with network monitoring and security analysis.**

## Screenshots

![App Screenshot](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/main/awsdiagramlambda.png?raw=true)

