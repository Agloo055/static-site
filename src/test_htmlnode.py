import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_1(self):
        props = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        
        node = HTMLNode(props=props)
        print(f"node = {node}")
        print(f"node.props_to_html = {node.props_to_html()}\n\n")
    
    def test_node_2(self):
        node = HTMLNode()

        print(f"node = {node}")
        print(f"node.props_to_html = {node.props_to_html()}\n\n")

    def test_node_3(self):
        props = {
                    "href": "https://www.google.com",
                }
        node = HTMLNode("p", "this is the body", None, props)

        print(f"node = {node}")
        print(f"node.props_to_html = {node.props_to_html()}\n\n")

if __name__ == "__main__":
    unittest.main()