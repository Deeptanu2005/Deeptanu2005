import json

# Load the organizations from the JSON file
with open('orgs.json', 'r') as file:
    orgs = json.load(file)

# Build the organization section
org_section = "## 🏢 Organizations\n"
for org in orgs:
    # Check if the 'html_url' key exists in the organization data
    if 'html_url' in org:
        org_section += f'<a href="{org["html_url"]}"><img src="{org["avatar_url"]}" width="50" height="50"> {org["login"]}</a><br/>\n'
    else:
        # Handle the case where 'html_url' key is missing
        org_section += f'<img src="{org["avatar_url"]}" width="50" height="50"> {org["login"]}<br/>\n'

# Read the current README
with open('README.md', 'r') as file:
    readme = file.read()

# Replace the placeholder with the new organization section
new_readme = readme.replace("<!-- ORG_SECTION_START -->", "<!-- ORG_SECTION_START -->\n" + org_section)

# Write the new README
with open('README.md', 'w') as file:
    file.write(new_readme)
