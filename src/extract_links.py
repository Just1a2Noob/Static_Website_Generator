import re
from textnode import TextNode

def extract_markdown_images(text, r_pattern=False):
    pattern = re.compile(r"!\[(.*?)\]+\((.*?)\)")
    match = pattern.findall(text)
    if r_pattern == True:
        return (match, r_pattern)
    return match

def extract_markdown_links(text, r_pattern=False):
    pattern = re.compile(r"\[(.*?)\]+\((.*?)\)")
    match = pattern.findall(text)
    if r_pattern == True:
        return (match, pattern) 
    return match

def split_nodes_image(old_nodes):
    for node in old_nodes:
        text = node.text 
        m_pattern = extract_markdown_images(text, r_pattern=True)
        pattern = m_pattern[1]
        parts = pattern.split(text)


        result = []
        k = 0
        for i, j in m_pattern[0]:
            while k < len(parts):
                if i in parts[k] and j in parts[k + 1]:
                    result.append(TextNode(i, "text_type_link", j))
                    if k < len(parts):
                        k += 2
                    break
                result.append(TextNode(parts[k], "text_type_text"))
                k += 1
    return result

def split_nodes_link(old_nodes):
    for node in old_nodes:
        text = node.text 
        m_pattern = extract_markdown_links(text, r_pattern=True)
        pattern = m_pattern[1]
        parts = pattern.split(text)


        result = []
        k = 0
        for i, j in m_pattern[0]:
            while k < len(parts):
                if i in parts[k] and j in parts[k + 1]:
                    result.append(TextNode(i, "text_type_link", j))
                    if k < len(parts):
                        k += 2
                    break
                result.append(TextNode(parts[k], "text_type_text"))
                k += 1

    return result



node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text_type_text"
)
new_nodes = split_nodes_link([node])
print(new_nodes)
# [
#     TextNode("This is text with a link ", text_type_text),
#     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode(
#         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
text =  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
