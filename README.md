# GitLab Scripts

This repository contains a set of Python scripts to interact with GitLab. Below are the details for each script:

## GitLab Clone All Repositories

This script clones all repositories from a specified GitLab group, including those in subgroups, into a local directory.

### Requirements
- Python 3.x
- `python-gitlab` library

### Setup

1. Clone the repository.
2. Install the required Python package:
   ```sh
   pip install python-gitlab
   ```

### Configuration

- Set up the following variables in the script with your GitLab information:
  ```sh
  GITLAB_URL = 'GITLAB_URL'         # Your GitLab server URL
  AUTH_TOKEN = 'GITLAB_TOKEN'       # Your GitLab private token
  GROUP_ID = 'GITLAB_GROUP_ID'      # The ID of the GitLab group you want to clone
  DESTINATION_DIR = 'PATH_FOR_REPOSITORIES'  # Path to the directory where repositories will be cloned
  ```

### Usage

- Run the script:
  ```sh
  python gitlab-clone-all-repositories.py
  ```


## gitlab-delete-pipelines.py

This script deletes all pipelines created by a specific user in a given GitLab project.

### Requirements
- Python 3.x
- `python-gitlab` library

## Setup

1. Clone the repository.
2. Install the required Python package:
   ```sh
   pip install python-gitlab
   ```

### Configuration

- Before running the script, update the following variables in the script with your GitLab information:
   ```sh
   gitlab_url: The URL of your GitLab instance (e.g., https://gitlab.com).
   private_token: Your GitLab personal access token.
   project_id: The ID of the GitLab project where the pipelines should be deleted.
   username: The username of the user whose pipelines should be deleted.
   ```

### Usage

- Run the script:
  ```sh
  python gitlab-clone-all-repositories.py
  ```

## gitlab-get-all-projects.py

This script fetches and clones all non-archived projects from a GitLab instance.

### Requirements
- Python 3.x
- `python-gitlab` library
- `GitPython` library

## Setup

1. Clone the repository.
2. Install the required Python package:
   ```sh
   pip install python-gitlab GitPython
   ```

### Configuration

- Before running the script, update the following variables in the script with your GitLab information:
   ```sh
   gitlab_url: The URL of your GitLab instance (e.g., https://gitlab.com).
   private_token: Your GitLab personal access token.
   project_id: The ID of the GitLab project where the pipelines details should be fetched.
   username: The username of the user whose pipelines details should be fetched.
   ```

### Usage

- Run the script:
  ```sh
  python gitlab-get-all-projects.py
  ```


## gitlab-update-project-vars.py

This script updates GitLab CI variables for a specified project.

### Requirements
- Python 3.x
- `python-gitlab` library

## Setup

1. Clone the repository.
2. Install the required Python package:
   ```sh
   pip install python-gitlab
   ```

### Configuration

- Before running the script, update the following variables in the script with your GitLab information:
   ```sh
   project_id: The ID of the GitLab project where the variables should be updated.
   token: Your GitLab personal access token.
   gitlab_url: The URL of your GitLab instance (e.g., https://gitlab.com).
   ```

### Usage

- Run the script:
  ```sh
  python gitlab-update-project-vars.py
  ```   
