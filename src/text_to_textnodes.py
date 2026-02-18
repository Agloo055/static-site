from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

delimiters = [
    (TextType.BOLD, "**"),
    (TextType.ITALIC, "_"),
    (TextType.CODE, "`")
]

def text_to_textnodes(text):
    textnodes = [TextNode(text, TextType.TEXT)]

    for (type,delimiter) in delimiters:
        textnodes = split_nodes_delimiter(textnodes, delimiter, type)
    
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)

    return textnodes
