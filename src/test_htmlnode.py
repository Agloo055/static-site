import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_1(self):
        props = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        
        node = HTMLNode(props=props)
        self.assertEqual(node.__repr__(), "HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


    
    def test_node_2(self):
        node = HTMLNode()

        self.assertEqual(node.__repr__(), "HTMLNode(None, None, None, None)")
        self.assertEqual(node.props_to_html(), '')

    def test_node_3(self):
        props = {
                    "href": "https://www.google.com",
                }
        node = HTMLNode("p", "this is the body", None, props)

        self.assertEqual(node.__repr__(), "HTMLNode(p, this is the body, None, {'href': 'https://www.google.com'})")
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

if __name__ == "__main__":
    unittest.main()