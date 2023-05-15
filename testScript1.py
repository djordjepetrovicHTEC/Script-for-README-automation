import os
import difflib

# Get the current directory
current_directory = os.getcwd()

# Specify the path to the testWorkflow1.yaml file relative to the current directory
workflow_file_path = os.path.join(current_directory, ".github", "workflows", "testWorkflow1.yaml")

# Specify the path to the README.md file relative to the current directory
readme_file_path = os.path.join(current_directory, ".github", "workflows", "README.md")

# Read the contents of the testWorkflow1.yaml file
with open(workflow_file_path, 'r') as workflow_file:
    workflow_contents = workflow_file.readlines()

# Read the previous version of the testWorkflow1.yaml file from the git history
prev_version_command = f"git diff {workflow_file_path}"
prev_version_output = os.popen(prev_version_command).read().splitlines()

# Find the differences between the previous and current versions of the testWorkflow1.yaml file
diff = difflib.unified_diff(prev_version_output, workflow_contents, lineterm='', n=0)

# Filter out the lines that were present in the previous version
filtered_diff = [line for line in diff if line.startswith('+')]

# Append the filtered differences to the README.md file
with open(readme_file_path, 'a') as readme_file:
    readme_file.write('\n'.join(filtered_diff))
