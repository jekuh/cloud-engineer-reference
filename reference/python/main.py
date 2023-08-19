import boto3

ec2 = boto3.resource('ec2')

isinstance_id = "ami-0c4c4bd6cf0c5fe52"


def start_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.start()
    print('Instance started', instance_id)

def stop_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.stop()

    print('Instance stopped', instance_id)

def delete_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.terminate()
    print('Instance terminated', instance_id)        



