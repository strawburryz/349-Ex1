import re


def count_unique_properties(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find css properties
    # Formatted as  " property: value; "
    # properties = re.findall(r'(\w+)\s*:', content)
    # properties = re.findall(r'([\w-]+)\s*:', content)
    properties = re.findall(r'([\w-]+)\s*:(?:.*?);', content)

    unique_properties = set(properties)

    return len(unique_properties), unique_properties


if __name__ == "__main__":
    file_path = "stylesheetmobile.css"

    count, properties = count_unique_properties(file_path)

    print(f"The CSS file contains {count} unique properties.")
    print(f"Unique Properties: {properties}")
