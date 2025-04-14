import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leafnode_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)  # No value provided
            node.to_html()