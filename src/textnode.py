class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text 

        text_type_cases = {
                "text_type_text":"text",
                "text_type_bold":"bold",
                "text_type_italic":"italic",
                "text_type_code":"code",
                "text_type_link":"link",
                "text_type_image":"image"
            }
        if text_type[0:9] == "text_type_":
            self.text_type = text_type_cases.get(text_type)
        else:
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
