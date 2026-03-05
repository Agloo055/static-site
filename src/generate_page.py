from markdown_to_blocks import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node

import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)

    if content_list == []:
        return
    
    for item in content_list:
        content_path = os.path.join(dir_path_content,item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(content_path):
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
        else:
            dest_path = dest_path.replace('md', 'html')
            generate_page(content_path, template_path, dest_path, basepath)

    


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    try:
        with open(from_path, 'r') as f:
            markdown = f.read()
    except Exception as e:
        print(e)

    try:
        with open(template_path, 'r') as f:
            template = f.read()
    except Exception as e:
        print(e)
    
    # print(markdown)
    # print(template)
    
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    content = ""
    content = template.replace("{{ Title }}", title).replace("{{ Content }}",html)
    content = content.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    try:
        path, file = dest_path.rsplit('/', 1)
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception as e:
        print(e)

    try:
        with open(dest_path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(e)

    

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = None
    for block in blocks:
        if block.startswith('# '):
            title = block[2:]
            break

    if title == None:
        raise Exception("No h1 header found")
    
    return title
