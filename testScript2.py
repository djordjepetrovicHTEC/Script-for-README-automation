import os
import difflib

# Get the current directory
current_directory = os.getcwd()

# Specify the path to the testWorkflow1.yaml file relative to the current directory
workflow_file_path = os.path.join(current_directory, ".github", "workflows", "testWorkflow1.yaml")

# Specify the path to the README.md file relative to the current directory
readme_file_path = os.path.join(current_directory, ".github", "workflows", "README.md")

# Read the diff of the last commit that modified the testWorkflow1.yaml file
diff_command = f"git diff HEAD^ -- {workflow_file_path}"
diff_output = os.popen(diff_command).read().splitlines()

# Filter out the lines representing additions from the diff output
added_lines = [line[1:] for line in diff_output if line.startswith('+') and not line.startswith('+++')]

# Append each added line to the README.md file
with open(readme_file_path, 'a') as readme_file:
    for line in added_lines:
        readme_file.write(line + '\n')
