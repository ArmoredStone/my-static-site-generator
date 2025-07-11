import unittest

from src.functions.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extracts_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#  Hello World  "), "Hello World")
        self.assertEqual(extract_title("# Hello\n## Subtitle"), "Hello")
    
    def test_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("No title here\n## Subtitle")
        with self.assertRaises(ValueError):
            extract_title("## Subtitle\n### Another")

if __name__ == "__main__":
    unittest.main()

