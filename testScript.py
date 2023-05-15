import os

# Specify the path to the file relative to the runner's environment
file_path = os.path.join(os.environ["GITHUB_WORKSPACE"], "README.md")

# Open the file in append mode
with open(file_path, "a") as file:
    # Append the desired text
    file.write("test\n")
