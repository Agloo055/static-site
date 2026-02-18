import unittest

from block_to_blocktype import block_to_blocktype, BlockType

class TestBlockToBlocktype(unittest.TestCase):
    def test_block_header_min(self):
        block = """# 
Heading"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_block_header_max(self):
        block = """###### 
Heading"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.HEADING)

    def test_block_header_middle(self):
        block = """### 
Heading"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.HEADING)

    def test_block_header_fail(self):
        block = """####### 
Heading"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_code(self):
        block = """```
Code Block 
```"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.CODE)

    def test_block_code_fail(self):
        block = """```
Code Block 
"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_quote_one_line(self):
        block = """> Quote"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.QUOTE)

    def test_block_quote_multi_line(self):
        block = """> Quote
> Quote 2
> Quote 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.QUOTE)

    def test_block_quote_fail_start(self):
        block = """ Quote
> Quote 2
> Quote 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_quote_fail_middle(self):
        block = """> Quote
Quote 2
> Quote 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_quote_fail_end(self):
        block = """> Quote
> Quote 2
Quote 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_unordered_list_one_line(self):
        block = """- list"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)

    def test_block_unordered_list_multi_line(self):
        block = """- List
- List 2
- List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)

    def test_block_unordered_list_fail_start(self):
        block = """ List
- List 2
- List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_unordered_list_fail_middle(self):
        block = """- List
-List 2
- List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_unordered_list_fail_end(self):
        block = """- List
- List 2
 List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_ordered_list_one_line(self):
        block = """1. list"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

    def test_block_ordered_list_multi_line(self):
        block = """1. List
2. List 2
3. List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

    def test_block_ordered_list_fail_start(self):
        block = """ List
2. List 2
3. List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_ordered_list_fail_middle(self):
        block = """1. List
2.List 2
3. List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_ordered_list_fail_end(self):
        block = """1. List
2. List 2
 List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)
    
    def test_block_ordered_list_fail_wrong_order(self):
        block = """1. List
3. List 2
2. List 3"""
        blocktype = block_to_blocktype(block)

        self.assertEqual(blocktype, BlockType.PARAGRAPH)


    
    

if __name__ == "__main__":
    unittest.main()