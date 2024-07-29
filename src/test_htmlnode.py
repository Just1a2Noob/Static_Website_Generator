import unittest

from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", 
                        "This is a paragraph", 
                        None, {
                            "href": "https://www.google.com", 
                            "target": "_blank"
                            }
                        )
        node2 = "href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), node2)