import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class test_extract_links(unittest.TestCase):
    def test_extract_markdown_links(self):
        node1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node1_valid = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        self.assertEqual(extract_markdown_links(node1), node1_valid)
    
    def test_extract_markdown_images(self):
        node1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node1_valid = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(extract_markdown_images(node1), node1_valid)

    def test_extract_markdown_images_no_images(self):
        node1 = "This is text with no images"
        node1_valid = []

        self.assertEqual(extract_markdown_images(node1), node1_valid)
