import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equality_with_default_url(self):
        node = TextNode("Hello, world!", TextType.BOLD)
        node2 = TextNode("Hello, world!", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("Hello dude!", TextType.BOLD)
        node2 = TextNode("Hello man!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_equality_when_url_is_none(self):
        node = TextNode("Test text", TextType.ITALIC, url=None)
        node2 = TextNode("Test text", TextType.ITALIC)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()