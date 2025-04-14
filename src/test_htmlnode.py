import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):  # Fixed class name typo
    def test_props_to_html_empty(self):  # Added self parameter
        # Test when props is None
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")  # Using unittest assertion

    def test_props_to_html_single_prop(self):  # Added self parameter
        # Test with a single property
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')  # Using unittest assertion

    def test_props_to_html_multiple_props(self):  # Added self parameter
        # Test with multiple properties
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        # The order might vary, so we need to check for both possible orderings
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)  # Using unittest assertion
        self.assertIn(' target="_blank"', result)  # Using unittest assertion
        self.assertEqual(len(result), len(' href="https://www.google.com" target="_blank"'))  # Using unittest assertion

    def test_node_representation(self):  # Added self parameter
        # Test the __repr__ method
        node = HTMLNode("p", "Hello, world!", None, {"class": "text"})
        self.assertNotEqual