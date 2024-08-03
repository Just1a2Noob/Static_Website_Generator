import unittest
from splitdelimiter import split_nodes_delimiter 
from textnode import TextNode

class test_splitdelimiter(unittest.TestCase):
    def test_splitdelimiter(self):
        bold_test = TextNode("This should be **bolded** by natural law", "text_type_text")
        code_test = TextNode("This is text with a `code block` word", "text_type_text")
        italic_test = TextNode("This *maybe* an italic sentence by default", "text_type_text")

        bold_valid = [TextNode("This should be ", "text_type_text"), TextNode("bolded", "text_type_bold"), TextNode(" by natural law", "text_type_text")]
        code_valid = [TextNode("This is text with a ", "text_type_text"), TextNode("code block", "text_type_code"), TextNode(" word", "text_type_text")]
        italic_valid = [TextNode("This ", "text_type_text"), TextNode("maybe", "text_type_italic"), TextNode(" an italic sentence by default", "text_type_text")]

        self.assertEqual(split_nodes_delimiter([bold_test], "**", "text_type_bold"), bold_valid)
        self.assertEqual(split_nodes_delimiter([code_test], "`", "text_type_code"), code_valid)
        self.assertEqual(split_nodes_delimiter([italic_test], "*", "text_type_italic"), italic_valid)


    def test_delimiter_error(self):
        bold_test = TextNode("This should be **bolded** by natural law", "text_type_text")
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([bold_test], "??", "text_type_bold")
        self.assertEqual(str(context.exception), "Invalid delimiter")

    def test_text_type_error(self):
        bold_test = TextNode("This should be **bolded** by natural law", "text_type_text")
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([bold_test], "**", "text_type_header")
        self.assertEqual(str(context.exception), "Invalid text_type")

    def test_unmatched_closings(self):
        error_text = TextNode("This should *result in an error", "text_type_text")
        error_text2 = TextNode("This **lorem ipsum* shouldn't result in an error", "text_type_text")
        error_text3 = TextNode("This is another** lorem ipsum test", "text_type_text")

        with self.assertRaises(ValueError) as context1:
            split_nodes_delimiter([error_text], "*", "text_type_italic")
        self.assertEqual(str(context1.exception), "Unmatched delimiter found. Make sure each opening delimiter has a corresponding closing delimiter")

        with self.assertRaises(ValueError) as context2:
            split_nodes_delimiter([error_text2], "**", "text_type_bold")
        self.assertEqual(str(context2.exception), "Unmatched delimiter found. Make sure each opening delimiter has a corresponding closing delimiter")

        with self.assertRaises(ValueError) as context3:
            split_nodes_delimiter([error_text3], "**", "text_type_bold")
        self.assertEqual(str(context3.exception), "Unmatched delimiter found. Make sure each opening delimiter has a corresponding closing delimiter")



if __name__ == "__main__":
    unittest.main()
