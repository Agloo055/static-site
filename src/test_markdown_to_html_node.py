import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        # print(node)
        # print(html)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node)
        # print(html)
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- apple
- no _banana_
- cherry
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node)
        # print(html)
        self.assertEqual(
            html,
            "<div><ul><li>apple</li><li>no <i>banana</i></li><li>cherry</li></ul></div>",
        )

    def test_ordered_list_with_heading(self):
        md = """
#### 
Needed Items

1. item 1
2. item 2
3. item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node)
        # print(html)
        self.assertEqual(
            html,
            "<div><h4>Needed Items</h4><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>",
        )

    def test_quoteblock(self):
        md = """
> quote 1
>quote 2
> **quote** 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node)
        # print(html)
        self.assertEqual(
            html,
            "<div><blockquote>quote 1\nquote 2\n<b>quote</b> 3</blockquote></div>",
        )

    
    

if __name__ == "__main__":
    unittest.main()