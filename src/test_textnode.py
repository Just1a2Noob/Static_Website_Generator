import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("Nvim", "italic", None)
        node4 = TextNode("Nvim", "italic", None)
        self.assertEqual(node3, node4)

        node5 = TextNode("Neofecth", "bold", "github.neofetch")
        node6 = TextNode("Fastfetch", "bold", "github.fastfetch")
        self.assertEqual(node5, node6)

        node7 = TextNode("google fonts", "italic", "googlefonts.com")
        node8 = TextNode("google fonts", "italic", "google/fonts.com")
        self.assertEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
