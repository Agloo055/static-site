from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            split_nodes.append(old_node)
            continue
        

        delimiter_start = False
        delimiter_found = False
        delimiter_texts = []
        text = ""

        d_len = len(delimiter)

        num = 0
        while num < len(old_node.text):
            extra = 0

            if d_len == 1 and old_node.text[num] == delimiter:
                    delimiter_found = True
            elif d_len == 2 and num + 1 < len(old_node.text) and old_node.text[num:num+d_len] == delimiter:
                    delimiter_found = True
                    num += 2
            
            if delimiter_found:
                delimiter_found = False
                delimiter_texts.append((text, delimiter_start))
                text = ""
                delimiter_start = not delimiter_start

            if num >= len(old_node.text):
                break
            text += old_node.text[num]

            num += 1

        delimiter_texts.append((text, delimiter_start))

        if delimiter_start:
            raise Exception("Missing closing delimiter")
        
        for split_text in delimiter_texts:
            clean = "".join(split_text[0].split(delimiter))

            new_node = None
            if clean == "":
                continue
            elif split_text[1]:
                new_node = TextNode(clean, text_type)
            else:
                new_node = TextNode(clean, TextType.TEXT)
            
            split_nodes.append(new_node)
            
    return split_nodes


def split_nodes_image(old_nodes):
    split_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if matches == []:
            split_nodes.append(old_node)
            continue

        spilt_text = re.split(r"\!\[(.*?)\]\((.*?)\)", old_node.text)
        sections = []
        num = 0

        while num < len(spilt_text):
            if spilt_text[num] == '':
                num += 1
                continue
            new_node = None
            if num == len(spilt_text) - 1 or (spilt_text[num], spilt_text[num+1]) not in matches:
                new_node = TextNode(spilt_text[num], TextType.TEXT)
            else:
                new_node = TextNode(spilt_text[num], TextType.IMAGE, spilt_text[num+1])
                num += 1
            
            sections.append(new_node)
            num += 1
                

        split_nodes.extend(sections)
                
    return split_nodes
        



def split_nodes_link(old_nodes):
    split_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        if matches == []:
            split_nodes.append(old_node)
            continue

        spilt_text = re.split(r"\[(.*?)\]\((.*?)\)", old_node.text)
        sections = []
        num = 0

        while num < len(spilt_text):
            if spilt_text[num] == '':
                num += 1
                continue
            new_node = None
            if num == len(spilt_text) - 1 or (spilt_text[num], spilt_text[num+1]) not in matches:
                new_node = TextNode(spilt_text[num], TextType.TEXT)
            else:
                new_node = TextNode(spilt_text[num], TextType.LINK, spilt_text[num+1])
                num += 1
            
            sections.append(new_node)
            num += 1
                

        split_nodes.extend(sections)
                
    return split_nodes