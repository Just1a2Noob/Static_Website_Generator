from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in "```**":
        raise Exception("Invalid delimiter")

    valid_text_types = ["text_type_text", "text_type_bold", "text_type_italic", "text_type_code"]
    if text_type not in valid_text_types:
        raise Exception("Invalid text_type")

    result = []
    for node in old_nodes:
        text = node.text 
        parts = text.split(delimiter)

        # Error checker 
        delimiter_count = text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise ValueError("Unmatched delimiter found. Make sure each opening delimiter has a corresponding closing delimiter")
        
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Even index parts are outside the delimiter, so they are "text_type_text"
                if part:
                    result.append(TextNode(part, "text_type_text"))
            else:
                # Odd index parts are inside the delimiter, so they are special text_types
                if part:
                    result.append(TextNode(part, text_type))
    return result
