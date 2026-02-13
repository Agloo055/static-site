import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode('This is text with a ', TextType.TEXT, None), TextNode('code block', TextType.CODE, None), TextNode(' word', TextType.TEXT, None)
            ])
        
    def test_split_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode('This is text with a ', TextType.TEXT, None), TextNode('bold', TextType.BOLD, None), TextNode(' word', TextType.TEXT, None)
            ])

    def test_split_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode('This is text with an ', TextType.TEXT, None), TextNode('italic', TextType.ITALIC, None), TextNode(' word', TextType.TEXT, None)
            ])
        
    def test_split_code_at_start(self):
        node = TextNode("`code block` starts this text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode('code block', TextType.CODE, None), TextNode(' starts this text', TextType.TEXT, None)
            ])
    
    def test_split_code_at_end(self):
        node = TextNode("This text ends with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode('This text ends with a ', TextType.TEXT, None), TextNode('code block', TextType.CODE, None)
            ])
        
    def test_split_bold_at_start(self):
        node = TextNode("**Bold** starts this text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode('Bold', TextType.BOLD, None), TextNode(' starts this text', TextType.TEXT, None)
            ])
    
    def test_split_bold_at_end(self):
        node = TextNode("This text ends with **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode('This text ends with ', TextType.TEXT, None), TextNode('bold', TextType.BOLD, None)
            ])

if __name__ == "__main__":
    unittest.main()