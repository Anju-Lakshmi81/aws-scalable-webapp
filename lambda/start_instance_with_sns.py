import boto3

# --- Configuration ---
region = 'us-west-1'
instances = ['i-08ce9b2d7eccf6d26']  # This is Web B's instance
sns_topic_arn = 'arn:aws:sns:us-west-1:123456789012:MyWebAlertTopic'  # Replace with your actual SNS topic ARN

# --- Clients ---
ec2 = boto3.client('ec2', region_name=region)
sns = boto3.client('sns', region_name=region)

def lambda_handler(event, context):
    # Start Web B EC2 instance
    ec2.start_instances(InstanceIds=instances)
    print(f'Started your instances: {instances}')

    # Send notification email via SNS
    subject = "Private Web B Started"
    message = f"The EC2 instance {instances[0]} (Web B) has been started as scheduled."
    response = sns.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=subject
    )
    print("SNS notification sent:", response)
