import unittest
from src.functions.block_to_block_type import block_to_block_type
from src.models.blocktype import BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code(self):
        code_block = "```\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

    def test_quote(self):
        quote_block = "> Quote line 1\n> Quote line 2"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

    def test_unordered_list(self):
        ul_block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(ul_block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol_block = "1. first item\n2. second item\n3. third item"
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        paragraph = "This is just a block of text.\nIt continues on the next line."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

    def test_mixed_lines_fallback_to_paragraph(self):
        mixed = "1. first\n- second\n> third"
        self.assertEqual(block_to_block_type(mixed), BlockType.PARAGRAPH)

    def test_bad_heading_no_space(self):
        bad_heading = "###No space after hashes"
        self.assertEqual(block_to_block_type(bad_heading), BlockType.PARAGRAPH)

    def test_incomplete_code_block(self):
        incomplete_code = "```\nnot closed properly"
        self.assertEqual(block_to_block_type(incomplete_code), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

