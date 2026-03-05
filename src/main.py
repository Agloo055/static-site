from textnode import TextNode, TextType
import os
import shutil
import sys

from generate_page import generate_pages_recursive

def main():
    cli_arg = sys.argv
    basepath = '/' if len(cli_arg) == 0 else cli_arg[0]

    copy_directory('static','docs')

    generate_pages_recursive('content','template.html','docs',basepath)

    # generate_page('content/index.md','template.html','public/index.html')
    # generate_page('content/blog/glorfindel/index.md','template.html','public/blog/glorfindel/index.md')
    # generate_page('content/blog/tom/index.md','template.html','public/blog/tom/index.md')
    # generate_page('content/blog/majesty/index.md','template.html','public/blog/majesty/index.md')
    # generate_page('content/contact/index.md','template.html','public/contact/index.md')




def copy_directory(original_directory, final_directory):
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    delete_directory_helper(final_directory, os.listdir(final_directory))

    copy_directory_helper(original_directory, final_directory, os.listdir(original_directory))

def delete_directory_helper(directory_path, directory_list):
    if directory_list == []:
        return
    
    for item in directory_list:
        path = os.path.join(directory_path,item)
        print(path)
        if os.path.isdir(path):
            delete_directory_helper(path, os.listdir(path))
            os.rmdir(path)
        else:
            os.remove(path)
        

def copy_directory_helper(original_directory_path, final_directory_path, directory_list):
    if directory_list == []:
        return
    
    for item in directory_list:
        original_path = os.path.join(original_directory_path, item)
        final_path = os.path.join(final_directory_path,item)
        print(original_path, final_path)

        if os.path.isdir(original_path):
            os.mkdir(final_path)
            copy_directory_helper(original_path, final_path, os.listdir(original_path))
        else:
            shutil.copy(original_path, final_path)


main()