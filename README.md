# GitLab Clone All Repositories

This script clones all repositories from a specified GitLab group (including subgroups) to a local directory. It is useful for backing up all repositories or working with them locally.

## Requirements

- Python 3.x
- `python-gitlab` library
- Git

## Installation

1. Clone the repository or download the script.
2. Install the required Python package:
   ```sh
   pip install python-gitlab
   ```

## Usage
1. Set up the following variables in the script with your GitLab information:
    ```sh
    GITLAB_URL = 'GITLAB_URL'         # Your GitLab server URL
    AUTH_TOKEN = 'GITLAB_TOKEN'       # Your GitLab private token
    GROUP_ID = 'GITLAB_GROUP_ID'      # The ID of the GitLab group you want to clone
    DESTINATION_DIR = 'PATH_FOR_REPOSITORIES'  # Path to the directory where repositories will be cloned
    ```
2. Run the script:
  ```sh
    python gitlab-clone-all-repositories.py
  ```

## Script Details

### Functionality
1. Initialize GitLab connection: Connect to the GitLab server using the provided URL and authentication token.
2. Create directory: Ensure the destination directory for cloning repositories exists.
3. Clone or update repository: Clone the repository if it doesn't exist locally; otherwise, skip it.
4. Process group: Recursively clone all repositories within the specified group and its subgroups.

### Script Flow
1. Main function: Fetch the root group using the provided GROUP_ID and process it.
2. Process group function:
2.1 Create a directory for the group.
2.2 Fetch all projects within the group and clone them.
2.3 Recursively process subgroups.
3. Clone or update repository function: Clone the repository if it isn't already cloned.

### Example
Here's an example of how the script works:

1. The script fetches the root group and processes it.
2. For each project in the group, it clones the repository if it doesn't exist locally.
3. For each subgroup, it processes the subgroup similarly.

### Customization
You can customize the script to suit your needs by modifying the following:

1. Change the GITLAB_URL, AUTH_TOKEN, GROUP_ID, and DESTINATION_DIR to your specific values.
2. Modify the clone_or_update_repo function to include additional logic if needed.

### Troubleshooting
1. Authentication issues: Ensure your GitLab URL and private token are correct.
2. Permission issues: Make sure your GitLab token has sufficient permissions to access the group and repositories.
3. Git issues: Ensure Git is installed and accessible from your command line.

### Contributions
Contributions are welcome! Please open an issue or submit a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
