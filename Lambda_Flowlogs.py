import boto3 
import os 


from botocore.exceptions import ClientError
ROLE_ARN = os.environ.get('ROLE_ARN')
BUCKET_ARN = os.environ.get('BUCKET_ARN') 


ec2 = boto3.client('ec2')
logs = boto3.client('logs')

def lambda_handler(event, context):
    print(event)
    
    try:
        #Extract the VPC id from event 
        vpc_id = event.get("detail").get("responseElements").get("vpc").get("vpcId")
        
        vpc_logs_group = "VPCFlowLogs-" + vpc_id
        
        print("VPC "+ vpc_id)
        
        try:
            response = logs.create_log_group(
                logGroupName=vpc_logs_group)
        except ClientError:
            print(f"Log group '{vpc_logs_group}' already exists...")
            
        response = ec2.describe_flow_logs(
            Filters=[
                {
                    'Name': 'resource-id',
                    'Values':[
                        vpc_id]
                }])
                
        if len(response['FlowLogs']) > 0:
            print('VPC Flow Logs are ENABLED')
        else:
            print('VPC Flow Logs are DISABLED. Enabling...')
            
        response = ec2.create_flow_logs(
            ResourceIds=[vpc_id],
            ResourceType='VPC',
            TrafficType='ALL',
            LogDestinationType='s3',
            LogDestination= BUCKET_ARN,
            DeliverLogsPermissionArn= ROLE_ARN
        )
            
        print('Created Flow Logs' )
    
    except Exception as e:
        print('Error - reason "%s"' % str(e))
