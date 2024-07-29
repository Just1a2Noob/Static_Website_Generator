class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        return (
            other.text == self.text and
            other.text_type == self.text_type and
            other.url == self.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    print(TextNode("Nvim", "md", "www.boot.dev"))
