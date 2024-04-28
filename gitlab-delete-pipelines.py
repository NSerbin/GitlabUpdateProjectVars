import gitlab
from concurrent.futures import ThreadPoolExecutor

def delete_pipeline(pipeline):
    try:
        pipeline.delete()
        print(f"Pipeline {pipeline.id} deleted successfully.")
        return 1
    except Exception as e:
        print(f"Failed to delete pipeline {pipeline.id}. Error: {str(e)}")
        return 0

def delete_user_pipelines(gitlab_url, private_token, project_id, username):
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token)

    try:
        # Get user by username
        users = gl.users.list(username=username)
        if not users:
            print(f"User with username {username} not found.")
            return
        
        user_id = users[0].id

        try:
            project = gl.projects.get(project_id)
        except gitlab.exceptions.GitlabGetError as e:
            print(f"Project with ID {project_id} not found. Error: {str(e)}")
            return

        # Use ThreadPoolExecutor for parallel deletion
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            deleted_count = 0
            pipelines = project.pipelines.list(user_id=user_id, as_list=False)  # Use iterator to fetch all pipelines

            # Only proceed if there are pipelines to delete
            if not pipelines:
                print(f"No pipelines found for user {username} in project ID {project_id}.")
                return

            for pipeline in pipelines:
                futures.append(executor.submit(delete_pipeline, pipeline))

            # Wait for all threads to finish and calculate the total deleted count
            for future in futures:
                deleted_count += future.result()

            print(f"Total pipelines deleted for user {username}: {deleted_count}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace these variables with your own values
gitlab_url = "https://gitlab.com"
private_token = "CHANGE-ME"
project_id = "CHANGE-ME"
username = "CHANGE-ME"  # Replace with the actual username

delete_user_pipelines(gitlab_url, private_token, project_id, username)
