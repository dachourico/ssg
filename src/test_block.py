import unittest
from split_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_blocks(self):
        md = """
        This is a block.

        This is another block.
        """

        result = markdown_to_blocks(md)
        self.assertEqual(result, ["This is a block.", "This is another block."])

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )