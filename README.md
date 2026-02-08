# Automating_Python_Boto3
Python project using boto3 to interact with AWS EC2 services. The script retrieves EC2 instance IDs, extracts security groups attached to instances, and lists all security groups in the ca-central-1 region with names, descriptions, and VPC IDs using IAM profile-based authentication.

This project demonstrates how to use Python with boto3 to interact with AWS EC2 services and extract infrastructure details programmatically.

The script connects to AWS using a configured IAM profile and performs the following actions in the ca-central-1 region:

	•	Lists all EC2 Instance IDs in the region
	•	Extracts security groups attached to EC2 instances
	•	Lists all security groups in the account, including:
	•	Security Group Name
	•	Description
	•	VPC ID

  Features
	•	Lists all EC2 Instance IDs in the region
	•	Extracts security groups attached to EC2 instances
	•	Lists all security groups in the account, including:
	•	Security Group Name
	•	Description
	•	VPC ID
  
  Technologies Used
	•	Python
	•	boto3 (AWS SDK for Python)
	•	AWS EC2
	•	IAM (profile-based authentication)

  What This Project Demonstrates?
	•	Understanding of nested AWS API responses
	•	Traversing complex dictionary and list structures
	•	Practical use of boto3 EC2 client
	•	Real-world AWS automation and inventory scripting
	•	Clear handling of Reservations --> Instances --> SecurityGroups

  •	AWS infrastructure auditing
	•	Security group visibility and validation
	•	Learning boto3 and AWS SDK patterns
	•	DevOps automation practice

  
