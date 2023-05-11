import os
import re
import yaml

README_FILE = '.github/workflows/README.md'
WORKFLOW_FILES = ['workflow1.yaml', 'workflow2.yaml']

SECTION_PATTERN = re.compile(r'## `(.+?)`', re.DOTALL)

def extract_sections(content):
    sections = SECTION_PATTERN.split(content)[1:]
    sections = [(sections[i], sections[i+1]) for i in range(0, len(sections), 2)]
    return sections

def update_readme(content, workflow_name, new_vars):
    pattern = fr'(## `{workflow_name}`.*?Environment Variables\n.*?)(?:\n\n- `.*?`)*\n'
    replace_text = f'\\1\n' + '\n'.join(new_vars) + '\n'
    updated_content = re.sub(pattern, replace_text, content, flags=re.DOTALL)
    return updated_content

with open(README_FILE, 'r') as readme_file:
    readme_content = readme_file.read()

sections = extract_sections(readme_content)

for workflow_name, workflow_content in sections:
    env_vars = re.findall(r'- `([^`]+?)`:', workflow_content)

    workflow_yaml_file = f'{workflow_name.lower().replace(" ", "_")}.yaml'
    if workflow_yaml_file in WORKFLOW_FILES:
        with open(workflow_yaml_file, 'r') as yaml_file:
            workflow_yaml = yaml.safe_load(yaml_file)

        workflow_input_params = workflow_yaml.get('inputs', [])
        workflow_env_vars = workflow_yaml.get('env', {}).keys()

        new_vars = [f'- `{var}`: Text.' for var in workflow_env_vars if var not in env_vars]

        readme_content = update_readme(readme_content, workflow_name, new_vars)

with open(README_FILE, 'w') as readme_file:
    readme_file.write(readme_content)
