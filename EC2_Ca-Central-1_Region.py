# Import all modules and libraries
import boto3
from pprint import pprint

# Open AWS Console Management
aws_management_console = boto3.session.Session(profile_name = "default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name = "ec2", region_name = "ca-central-1")
# Use boto3 Documentation for more information.

results = ec2_console.describe_instances()
results2 = ec2_console.describe_security_groups()

#pprint(results)


# Extracting EC2 ID
for value_1 in results["Reservations"]:
    for value_2 in value_1["Instances"]:
        pprint(value_2['InstanceId'])



# Extracting EC2 Security Group.
for value1 in results['Reservations']:
    for value2 in value1['Instances']:
        for value3 in value2['SecurityGroups']:
            print(value3['GroupId'])
            

# Extracting all the security groups in this account.

for value_one in results2["SecurityGroups"]:
    pprint(value_one['GroupName'])
    pprint(value_one['Description'])
    pprint(value_one['VpcId'])