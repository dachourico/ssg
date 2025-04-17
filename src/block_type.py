from enum import Enum
from split_blocks import *
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith('#'):
        pound_count = 0
        for char in block:
            if char == '#':
                pound_count += 1
            else: break
        
        if 1 <= pound_count <= 6 and block[pound_count] == ' ':
            return BlockType.HEADING
        
    if block.startswith('```') and block.endswith ('```'):
        return BlockType.CODE
    
    lines = block.split('\n')
    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        expected_prefix = f"{i}. "

        if not line.startswith(expected_prefix):
            is_ordered_list = False
            break

    if is_ordered_list and lines:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH