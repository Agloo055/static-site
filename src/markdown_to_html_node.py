from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype, BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

import re


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        b_type = block_to_blocktype(block)
        tag = block_to_tag(block, b_type)

        children = []

        if b_type == BlockType.CODE:
            codeblock = LeafNode(tag, block[4:-3])

            children.append(codeblock)
            html_nodes.append(ParentNode('pre', children))

        elif b_type == BlockType.ORDERED_LIST or b_type == BlockType.UNORDERED_LIST:
            children.extend(text_to_list_children(block, tag))
            html_nodes.append(ParentNode(tag, children))

        elif b_type == BlockType.QUOTE:
            children.extend(text_to_quote_children(block))
            html_nodes.append(ParentNode(tag, children))
        else:
            if len(tag) > 1:
                block = block[int(tag[1]) + 2:]
            children.extend(text_to_children(block))
            html_nodes.append(ParentNode(tag, children))


    container = ParentNode('div', html_nodes)
    return container


def block_to_tag(block, b_type):
    tag = ""
    match b_type:
        case BlockType.PARAGRAPH:
            tag = 'p'

        case BlockType.HEADING:
            num = 0
            for letter in block:
                if letter == "#":
                    num += 1
                else:
                    break
            
            tag = f'h{num}'
            
        case BlockType.CODE:
            tag = 'code'

        case BlockType.QUOTE:
            tag = 'blockquote'

        case BlockType.UNORDERED_LIST:
            tag = 'ul'

        case BlockType.ORDERED_LIST:
            tag = 'ol'

        case _:
            raise Exception("Invalid block type")
        
    return tag

def text_to_children(text):
    textnodes = text_to_textnodes(" ".join(text.split('\n')))
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    
    return children

def text_to_list_children(text, tag):
    lines = text.split('\n')
    delimiter = 2 if tag == 'ul' else 3

    children = []
    for line in lines:
        textnodes = text_to_textnodes(line[delimiter:])
        grand_children = []
        for textnode in textnodes:
            grand_children.append(text_node_to_html_node(textnode))

        children.append(ParentNode('li',grand_children))
   
    return children

def text_to_quote_children(text):
    text = "".join(text.split("> "))
    text = "".join(text.split(">"))
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    
    return children