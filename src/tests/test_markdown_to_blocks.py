import unittest
from src.functions.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        md = "This is a single block without any blank lines."
        self.assertEqual(markdown_to_blocks(md), ["This is a single block without any blank lines."])

    def test_multiple_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_trailing_and_leading_spaces(self):
        md = """

    This is a block with spaces


    Another block with indentation    

        """
        expected = [
            "This is a block with spaces",
            "Another block with indentation",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_extra_newlines(self):
        md = """Block one


Block two




Block three
"""
        expected = [
            "Block one",
            "Block two",
            "Block three",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)


if __name__ == "__main__":
    unittest.main()

