import unittest
from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_textnode_equality_same_properties(self):
        node1 = TextNode("example", TextType.TEXT)
        node2 = TextNode("example", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_textnode_not_equal_different_text(self):
        node1 = TextNode("example1", TextType.TEXT)
        node2 = TextNode("example2", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_textnode_not_equal_different_type(self):
        node1 = TextNode("example", TextType.BOLD)
        node2 = TextNode("example", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_textnode_not_equal_different_url(self):
        node1 = TextNode("example", TextType.LINK, url="https://example.com")
        node2 = TextNode("example", TextType.LINK, url="https://different.com")
        self.assertNotEqual(node1, node2)

    def test_textnode_equality_with_none_url(self):
        node1 = TextNode("example", TextType.TEXT, url=None)
        node2 = TextNode("example", TextType.TEXT)
        self.assertEqual(node1, node2)



if __name__ == '__main__':
    unittest.main()

