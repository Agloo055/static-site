import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_only_title(self):
        md = """
# Title
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Title",
        )

    def test_title_with_more(self):
        md = """
# Title

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Title",
        )

    def test_with_multiple_headers(self):
        md = """
# Title

#### Header

## Headers

# Title 2
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Title",
        )

        


    
    

if __name__ == "__main__":
    unittest.main()