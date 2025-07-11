import unittest
from src.models.textnode import TextNode, TextType
from src.functions.text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_basic_text(self):
        text = "Just some plain text"
        expected = [TextNode("Just some plain text", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_all_markdown(self):
        text = "This is **bold** and _italic_ and `code`"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_images_and_links(self):
        text = "Here is an ![image](http://img.url) and a [link](http://link.url)"
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "http://img.url"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "http://link.url"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_combined_example(self):
        text = "Hi **bold** _italic_ `code` ![img](img.png) [link](url)"
        expected = [
            TextNode("Hi ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "img.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)


if __name__ == '__main__':
    unittest.main()

