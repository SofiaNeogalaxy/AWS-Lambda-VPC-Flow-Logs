
# VPC Flow Logs Lambda Function

**AWS Lambda function** that automatically enables Amazon VPC flow logs when a new VPC is created.

The function is triggered by an **Amazon CloudWatch Event** that is set to respond to the  **'CreateVpc'** event. When a new VPC is created, the function extracts the VPC ID from the event and uses it to create a **new log group** for the VPC flow logs in Amazon CloudWatch Logs. It then checks if **flow logs** are already enabled for the VPC, and if not, it **enables** them. The flow logs are delivered to an **Amazon S3** bucket that is specified as an environment variable in the function.

**This function can be useful for ensuring that flow logs are always enabled for new VPCs, which can help with network monitoring and security analysis.**


![App Screenshot](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/main/awsdiagramlambda.png?raw=true)


## Prerequisites
- AWS account
- IAM roles with permissions for Lambda and CloudTrail
- S3 bucket to store the flow logs
- Enable AWS CloudTrail

## Usage
1. In CloudTrail Create New Trail with enabled CloudWatch Logs, if you choose New IAM Role AWS create policy automaticaly (AWS CloudTrail assumes this role to send CloudTrail events to your CloudWatch Logs log group).
2. Create an IAM role with permissions for Lambda [Policy for Lambda Flow Logs](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/ee0738852125c210b6bb2e6ff5f662e74d2da9d4/Policy%20for%20Lambda%20Flow%20Logs), [Policy Access to S3 Bucket for Lambda](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/ee0738852125c210b6bb2e6ff5f662e74d2da9d4/Policy%20Access%20to%20S3%20Bucket), [Trust Policy for Lambda Role](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/ee0738852125c210b6bb2e6ff5f662e74d2da9d4/Trust%20Policy%20for%20Lambda%20Role)
3. Create an S3 bucket to store the flow logs.
4. Create a new lambda function:
 + Runtime: Python 3.7
 + Architecture: x86_64
 + Permissions:Use an existing role (ref. section 2 )
  and paste the code from [Lambda_Code_Flowlogs.py](https://github.com/SofiaNeogalaxy/AWS-Lambda-VPC-Flow-Logs/blob/338eb74286783c98d168e5864d286a4c9faa85c6/Lambda_Code_Flowlogs.py)  into the code editor.
5. In Configuration go to Enviroment variables and add **ROLE_ARN** variable with Lambda IAM Role arn and **BUCKET_ARN** with bucket (ref. section 3) arn.
6. In Function overview add trigger EventBridge(CloudWatch Events)
 +  Create a new rule
 + Rule type: Event pattern
 + Choose EC2 than AWS API Call via CloudTrail
 + Check Detail Operation 
 + Choose from Operation window 'CreateVpc' event and Add.

 ## Output
The function will create a new log group in CloudWatch Logs with the name VPCFlowLogs-vpc-id, where vpc-id is the ID of the VPC for which flow logs are enabled. It will also create a new flow log in the specified S3 bucket with the name vpc-id.log. The flow log will contain information about the traffic flow in the VPC.

## Note
If VPC flow logs are already enabled for the VPC, the function will not create any new flow logs.
If the log group or flow log already exists, the function will not create them again.

I hope this helps! Let me know if you have any other questions.
