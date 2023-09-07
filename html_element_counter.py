from bs4 import BeautifulSoup
import os

def count_unique_elements(file_path, unique_elements):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    for tag in soup.find_all(True): # Loops through all the tags in the HTML file
        unique_elements.add(tag.name)

    return len(unique_elements), unique_elements
    

def check_directory(directory_path):
    global_unique_elements = set() # Set to store unique elements across all files

    for filename in os.listdir(directory_path):
        if filename.endswith('.html'):
            file_path = os.path.join(directory_path, filename)
            count_unique_elements(file_path, global_unique_elements)
            print(f"Checked {filename}...")

    count = len(global_unique_elements)

    if count >= 30:
        print(f"The HTML files contain at least 30 different kinds of HTML elements. It has {count} unique elements.")
    else:
        print(f"The HTML files contain less than 30 different kinds of HTML elements. It has {count} unique elements.")

    print("Unique elements: ", global_unique_elements)

if __name__ == "__main__":
    directory_path = "./" # Put directory path here
    # directory_path2 = "./my foods"
    check_directory(directory_path)
    # check_directory(directory_path2)

