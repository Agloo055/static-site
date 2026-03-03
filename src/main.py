from textnode import TextNode, TextType
import os
import shutil

def main():
    # text_type = TextType
    # temp = TextNode("This is some anchor text", text_type.LINK, "http://www.boot.dev")

    # print(temp)

    copy_directory('static','public')


def copy_directory(original_directory, final_directory):
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