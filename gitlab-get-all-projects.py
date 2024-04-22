import os
import gitlab
from git import Repo

def get_non_archived_projects(base_url, token):
    gl = gitlab.Gitlab(base_url, private_token=token)
    projects = gl.projects.list(all=True)
    return [project for project in projects if not project.archived]

def clone_projects(base_path, projects):
    for project in projects:
        project_path = os.path.join(base_path, project.name_with_namespace.replace("/", "-"))
        repo_url = project.ssh_url_to_repo
        Repo.clone_from(repo_url, project_path)
        print(f"Cloned {project.name_with_namespace} to {project_path}")

def main():
    # Configure GitLab base URL and personal access token
    base_url = "GITLAB_BASE_URL"
    token = "GITLAB_TOKEN"

    # Directory where the script is located
    script_dir = os.path.dirname(__file__)

    non_archived_projects = get_non_archived_projects(base_url, token)

    clone_projects(script_dir, non_archived_projects)

if __name__ == "__main__":
    main()
