import unittest
from block_type import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test different heading levels
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        # Test that we don't detect headings without a space
        self.assertNotEqual(block_to_block_type("#NoSpace"), BlockType.HEADING)
    
    def test_code(self):
        self.assertEqual(
            block_to_block_type("```\nSome code here\n```"), 
            BlockType.CODE
        )
    
    def test_quote(self):
        self.assertEqual(
            block_to_block_type(">This is a quote\n>Another line"), 
            BlockType.QUOTE
        )
    
    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2\n- Item 3"), 
            BlockType.UNORDERED_LIST
        )
    
