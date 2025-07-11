import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.functions.text_node_to_html_node import text_node_to_html_node
from src.textnode import TextNode, TextType

class TestFunctions(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag is None
        assert html_node.value == "This is a text node"

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b"
        assert html_node.value == "bold text"

    def test_link(self):
        node = TextNode("click here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "a"
        assert html_node.value == "click here"
        assert html_node.props == {"href": "https://example.com"}

    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, url="image.png")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "image.png", "alt": "An image"}
