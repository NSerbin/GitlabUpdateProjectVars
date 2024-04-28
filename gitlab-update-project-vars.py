#!/usr/bin/env python3
import gitlab

# Configuration
project_id = "CHANGE-ME"  # Update your project ID
token = "CHANGE-ME"       # Update your access token
gitlab_url = "https://gitlab.com"  # Update your GitLab instance URL if different

# GitLab connection
gl = gitlab.Gitlab(gitlab_url, private_token=token)

# Project object
project = gl.projects.get(project_id)

# Variables to be set in GitLab CI
variables = [
    {"key": "AWS_SG_ID", "value": "AWS-SG-ID-VALUE"},
    {"key": "AWS_SUBNET_1", "value": "AWS-SUBNET-1-VALUE"},
    {"key": "AWS_SUBNET_2", "value": "AWS-SUBNET-2-VALUE"},
    {"key": "AWS_SUBNET_3", "value": "AWS-SUBNET-3-VALUE"},
    {"key": "AWS_BUCKET_KMS_KEY", "value": "AWS-BUCKET-KMS-KEY-VALUE"},
    {"key": "AWS_LAMBDA_KMS_KEY", "value": "AWS-LAMBDA-KMS-KEY-VALUE"}
]

# Function to add or update a variable
def set_gitlab_ci_variable(var):
    try:
        # Check if the variable already exists
        existing_var = project.variables.get(var['key'])
        # Update the variable if it exists
        existing_var.value = var['value']
        existing_var.save()
        print(f"Updated variable {var['key']}")
    except gitlab.exceptions.GitlabGetError:
        # Create the variable if it does not exist
        project.variables.create({
            'key': var['key'],
            'value': var['value'],
            'variable_type': 'env_var',
            'protected': False,
            'masked': True,
            'environment_scope': 'ENVIRONMENT-VALUE'
        })
        print(f"Created variable {var['key']}")

# Add/update GitLab CI variables
for var in variables:
    set_gitlab_ci_variable(var)
