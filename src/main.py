from textnode import TextNode, TextType


def main():
    text_type = TextType
    temp = TextNode("This is some anchor text", text_type.Link, "http://www.boot.dev")

    print(temp)

main()