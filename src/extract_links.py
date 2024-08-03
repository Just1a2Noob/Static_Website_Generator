import re
from textnode import TextNode

def extract_markdown_images(text):
    pattern = re.compile(r"!\[(.*?)\]+\((.*?)\)")
    match = pattern.findall(text)
    return match

def extract_markdown_links(text, r_pattern=False):
    pattern = re.compile(r"\[(.*?)\]+\((.*?)\)")
    match = pattern.findall(text)
    if r_pattern == True:
        return (match, pattern) 
    return match

def split_nodes_image(old_nodes):
    pass 

def split_nodes_link(old_nodes):
    for node in old_nodes:
        text = node.text 
        m_pattern = extract_markdown_links(text, r_pattern=True)
    
    parts = pattern.split(text)
    result = []
    for part in parts:
        for i, j in find_all:
            if i in part:
                print(f"{part} is in here")
                break
            else:
                print(part)
                break
        pass



node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text_type_text"
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", text_type_text),
#     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode(
#         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
text =  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

pattern = re.compile(r"\[(.*?)\]+\((.*?)\)")
find_all = pattern.findall(text)
parts = pattern.split(text)
list_parts = [part for part in parts if part]
print(list_parts)
