import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Retrieve all running EC2 instances
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    # Collect all instance IDs that are running
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop all running instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances: {instance_ids}')
    else:
        print('No running instances found.')
