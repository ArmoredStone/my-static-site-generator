import unittest
from src.functions.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraphs(self):
        md = (
            "This is **bolded** paragraph\n"
            "text in a p\n"
            "tag here\n"
            "\n"
            "This is another paragraph with _italic_ text and `code` here\n"
            "\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = (
            "```\n"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "```\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_and_quote(self):
        md = (
            "# Heading 1\n"
            "\n"
            "> Quote line 1\n"
            "> Quote line 2\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><blockquote>Quote line 1\nQuote line 2</blockquote></div>",
        )

    def test_unordered_list(self):
        md = (
            "- Item 1\n"
            "- Item 2\n"
            "- **Bolded item**\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li><b>Bolded item</b></li></ul></div>",
        )

    def test_ordered_list(self):
        md = (
            "1. First item\n"
            "2. _Second item_\n"
            "3. Third item\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li><i>Second item</i></li><li>Third item</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()

