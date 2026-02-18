from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_blocktype(block):
    if re.match(r'\#{1,6} \n', block):
        return BlockType.HEADING
    
    elif block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    
    elif block.startswith('>') and not re.search(r'\n(?!>)', block):
        return BlockType.QUOTE
    
    elif block.startswith('- ') and not re.search(r'\n(?!- )', block):
        return BlockType.UNORDERED_LIST
    
    elif block.startswith('1. '):
        line_num = 1
        for line in block.split('\n'):
            if not line.startswith(f'{line_num}. '):
                return BlockType.PARAGRAPH
            line_num += 1
        
        return BlockType.ORDERED_LIST
    
    else:
        return BlockType.PARAGRAPH

