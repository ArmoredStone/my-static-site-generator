import unittest

from src.models.htmlnode import HTMLNode, LeafNode, ParentNode
from src.models.textnode import TextNode, TextType
from src.functions.text_node_to_html_node import text_node_to_html_node
from src.functions.split_nodes_delimiter import split_nodes_delimiter

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

    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert [n.text for n in new_nodes] == ["This is text with a ", "code block", " word"]
        assert [n.text_type for n in new_nodes] == [TextType.TEXT, TextType.CODE, TextType.TEXT]

    def test_bold_split(self):
        node = TextNode("Normal **bold text** normal", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert [n.text for n in new_nodes] == ["Normal ", "bold text", " normal"]
        assert [n.text_type for n in new_nodes] == [TextType.TEXT, TextType.BOLD, TextType.TEXT]

    def test_italic_split_multiple(self):
        node = TextNode("_first_ and _second_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        assert [n.text for n in new_nodes] == ["first", " and ", "second"]
        assert [n.text_type for n in new_nodes] == [TextType.ITALIC, TextType.TEXT, TextType.ITALIC]

    def test_no_delimiters(self):
        node = TextNode("Just normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert new_nodes == [node]

    def test_non_text_nodes_untouched(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert new_nodes == [node]
