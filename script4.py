import os
import re
import yaml

README_FILE = 'README.md'
WORKFLOW_FILES = ['workflow1.yaml', 'workflow2.yaml']

SECTION_PATTERN = re.compile(r'## `(.+?)`', re.DOTALL)

def extract_sections(content):
    sections = SECTION_PATTERN.split(content)[1:]
    sections = [(sections[i], sections[i+1]) for i in range(0, len(sections), 2)]
    return sections

def format_variable(var_name, description):
    if description:
        return f"- `{var_name}`: {description}"
    else:
        return f"- `{var_name}`: TODO"

def update_readme(content, workflow_name, new_vars):
    pattern = fr'(## `{workflow_name}`.*?Environment Variables\n.*?)(?:\n\n- `.*?`)*\n'
    replace_text = f'\\1\n' + '\n'.join(new_vars) + '\n'
    updated_content = re.sub(pattern, replace_text, content, flags=re.DOTALL)
    return updated_content

def update_workflow_readme():
    with open(README_FILE, 'r') as readme_file:
        readme_content = readme_file.read()

    for workflow_name, new_env_vars, new_input_params in get_workflow_changes():
        new_vars = []
        for var_name in new_env_vars:
            with open(f'{workflow_name.lower().replace(" ", "_")}.yaml', 'r') as workflow_file:
                workflow_data = yaml.safe_load(workflow_file)

            var_data = workflow_data.get('env', {}).get(var_name)
            var_description = var_data.get('description') if var_data and 'description' in var_data else None

            new_vars.append(format_variable(var_name, var_description))

        for param_name in new_input_params:
            with open(f'{workflow_name.lower().replace(" ", "_")}.yaml', 'r') as workflow_file:
                workflow_data = yaml.safe_load(workflow_file)

            param_data = workflow_data.get('inputs', {}).get(param_name)
            param_description = param_data.get('description') if param_data and 'description' in param_data else None

            new_vars.append(format_variable(param_name, param_description))

        readme_content = update_readme(readme_content, workflow_name, new_vars)

    with open(README_FILE, 'w') as readme_file:
        readme_file.write(readme_content)

def get_workflow_changes():
    # Implementation of retrieving workflow changes
    # Return the workflow name, new environment variables, and new input parameters
    # For testing purposes, you can hardcode the values

    workflow_changes = [
        {
            'name': 'Workflow 1',
            'new_env_vars': ['result_repo'],
            'new_input_params': []
        },
        {
            'name': 'Workflow 2',
            'new_env_vars': [],
            'new_input_params': ['input_param1']
        }
    ]

    return [(w['name'], w['new_env_vars'], w['new_input_params']) for w in workflow_changes]

update_workflow_readme()
