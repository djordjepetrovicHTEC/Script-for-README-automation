import os

# Get the current directory
current_directory = os.getcwd()

# Specify the path to the file relative to the current directory
file_path = os.path.join(current_directory, ".github", "workflows", "README.md")

# Open the file in append mode
with open(file_path, "a") as file:
    # Append the desired text
    file.write("test\n")
