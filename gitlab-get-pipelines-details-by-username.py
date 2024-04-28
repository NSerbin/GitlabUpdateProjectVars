import json
import gitlab

def get_user_pipelines(gitlab_url, private_token, project_id, username):
    # Initialize a GitLab instance
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token)

    output_data = {"pipelines": []}

    try:
        # Get user by username
        users = gl.users.list(username=username)
        if not users:
            output_data["error"] = f"User with username {username} not found."
            print(json.dumps(output_data, indent=2))
            return

        user_id = users[0].id

        # Get project
        project = gl.projects.get(project_id)

        # Get pipelines for the user
        pipelines = project.pipelines.list(user_id=user_id, all=True)
        output_data["pipiles"] = [pipeline.attributes for pipeline in pipelines]

    except Exception as e:
        output_data["error"] = str(e)

    # Convert the output_data to JSON and print it
    print(json.dumps(output_data, indent=2))

# Replace these variables with your own values
gitlab_url = "https://gitlab.com"
private_token = "CHANGE-ME"
project_id = "CHANGE-ME"
username = "CHANGE-ME"  # Replace with the actual username

get_user_pipelines(gitlab_url, private_token, project_id, username)
