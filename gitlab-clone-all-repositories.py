import gitlab
import os
import subprocess

# Replace these variables with your GitLab information
GITLAB_URL = 'GITLAB_URL'  # or your GitLab server URL
AUTH_TOKEN = 'GITLAB_TOKEN'
GROUP_ID = 'GITLAB_GROUP_ID'
DESTINATION_DIR = 'PATH_FOR_REPOSITORIES'

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=AUTH_TOKEN)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def clone_or_update_repo(repo_url, destination):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = os.path.join(destination, repo_name)

    if not os.path.exists(repo_path):
        print(f"Cloning {repo_name} into {repo_path}...")
        subprocess.run(['git', 'clone', repo_url, repo_path])
    else:
        print(f"Repository {repo_name} already cloned. Skipping...")

def process_group(group, base_path, main_group_name):
    # Create directory for the group, removing the main group name prefix
    group_path = os.path.join(base_path, group.full_path.replace(main_group_name + '/', ''))
    create_directory(group_path)
    
    # Fetch all projects in the group
    projects = group.projects.list(all=True, include_subgroups=False)
    for project in projects:
        repo_url = project.ssh_url_to_repo
        clone_or_update_repo(repo_url, group_path)
    
    # Recursively process subgroups
    subgroups = group.subgroups.list(all=True)
    for subgroup in subgroups:
        subgroup = gl.groups.get(subgroup.id)  # Get full subgroup details
        process_group(subgroup, base_path, main_group_name)

def main():
    # Fetch the root group
    root_group = gl.groups.get(GROUP_ID)
    main_group_name = root_group.full_path.split('/')[-1]
    
    # Process the root group and its subgroups
    process_group(root_group, DESTINATION_DIR, main_group_name)

if __name__ == "__main__":
    main()
