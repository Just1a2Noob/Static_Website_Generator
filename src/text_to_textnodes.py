from splitdelimiter import split_nodes_delimiter 
from extract_links import split_nodes_image, split_nodes_link
from textnode import TextNode    

def text_to_textnodes(text):
    text_node = TextNode(text, "text_type_text")

    result = split_nodes_image([text_node])
    result = split_node_link([result])
    result = split_nodes_delimiter([result], "**", "text_type_bold")
    result = split_nodes_delimiter([result], "*", "text_type_italic")
    result = split_nodes_delimiter([result], "`", "text_type_code")

    return result

print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))


