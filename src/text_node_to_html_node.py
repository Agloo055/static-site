from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    tag = ""
    props = {}
    is_image = False
    leaf = None

    match text_node.text_type:
        case TextType.TEXT:
            tag = None
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
            props["href"] = text_node.url
        case TextType.IMAGE:
            tag = "img"
            is_image = True
            props["src"] = text_node.url
            props["alt"] = text_node.text
        case _:
            raise Exception("Invalid text_type")
    
    if is_image:
        leaf = LeafNode(tag, None, props=props)
    else:
        leaf = LeafNode(tag, text_node.text, props)
    
    return leaf
    