import boto3

def lambda_handler(event, context):
    awsregion = ['ca-central-1','us-east-1','us-east-2','us-west-1','us-west-2']

    for aws_reg in awsregion:
        ec2 = boto3.resource('ec2', region_name=aws_reg)
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for instance in instances:
            ec2.instances.filter(InstanceIds=[instance.id]).stop()
            print("Instance ID {} in {} is stopped.".format(instance.id,aws_reg))