import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

        node3 = HTMLNode(
            "h1",
            "This is a title",
            ["p", "a"],
            {
                "href": "www.duckduckgo.com"
            }
        )
        node4 = "href=\"www.duckduckgo.com\"" 
        self.assertEqual(node3.props_to_html(), node4)

        node5 = HTMLNode(
            "h4",
            "This is a subheader",
            ["p", "a"],
            {}
        )

        node6 = ""
        self.assertEqual(node5.props_to_html(), node6)
    
    def test_LeafNode(self):
        node = LeafNode("p",
                        "This is a paragraph",
                        {})
        node2 = "<p>This is a paragraph</p>"
        self.assertEqual(node.to_html(), node2)

        node3 = LeafNode("i",
                         "fastfetch",
                         {
                             "href": "github/fastfetch"
                         })
        node4 = "<i href=\"github/fastfetch\">fastfetch</i>"
        self.assertEqual(node3.to_html(), node4)

        node5 = LeafNode("",
                         "Lorem Ipsum"
                         )
        node6 = "Lorem Ipsum"
        self.assertEqual(node5.to_html(), node6)
    
    def test_ParentNode(self):
        node = ParentNode("p", 
                          [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text")
                            ]
                          )
        node1 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), node1)
        
        node2 = ParentNode("p",
                            [LeafNode(None, "Loremp Ipsum"), 
                            LeafNode("b", "Bolded text"),
                            LeafNode("i", "boot.dev", {"href":"www.boot.dev"})
                            ])
        node3 = "<p>Loremp Ipsum<b>Bolded text</b><i href=\"www.boot.dev\">boot.dev</i></p>"
        self.assertEqual(node2.to_html(), node3)

        node4 = ParentNode("p",
                           [
                               ParentNode("b", [LeafNode("i", "Bold and Italic"), LeafNode(None, "Just bold")]),
                               LeafNode(None, "MORE TEXT")
                           ])
        node5 = "<p><b><i>Bold and Italic</i>Just bold</b>MORE TEXT</p>"
        self.assertEqual(node4.to_html(), node5)

        node6 =  ParentNode("h1",
                            [])
        with self.assertRaises(ValueError) as context:
            node6.to_html()
        self.assertEqual(str(context.exception), "Children cannot be empty")



if __name__ == "__main__":
    unittest.main()