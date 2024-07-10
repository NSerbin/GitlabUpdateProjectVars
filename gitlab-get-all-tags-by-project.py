#!/usr/bin/env python3
import gitlab

# Configuration
project_id = "CHANGE-ME"  # Update your project ID
token = "CHANGE-ME"  # Update your access token
gitlab_url = "https://gitlab.com"  # Update your GitLab instance URL if different

# GitLab connection
gl = gitlab.Gitlab(gitlab_url, private_token=token)

# Project object
project = gl.projects.get(project_id)

def get_all_tags_by_project(project):
    # Fetch all tags with pagination
    tags = project.tags.list(all=True)
    
    for tag in tags:
        # Retrieve full details for each tag
        full_tag = project.tags.get(tag.name)
        commit = full_tag.commit
        
        # Output commit information
        print('Commit info:')
        print(f"Commit ID: {commit['id']}")
        print(f"Author Name: {commit['author_name']}")
        print(f"Created At: {commit['created_at']}")
        print('-' * 40)
        
        # Output release information
        print('Release info:')
        print(f"Tag Name: {full_tag.name}")
        print(f"Description: {full_tag.message}")
        print('=' * 40)

get_all_tags_by_project(project)
