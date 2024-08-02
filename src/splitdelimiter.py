import re
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    bold_pattern = re.compile(r'(\*\*[^*]+\*\*)')
    italic_pattern = re.compile(r'(\*[^*]+\*)')

    for node in old_nodes:
        # This checks for any non-valid closing markers or mismatched markers
        if closing_markers(node.text) == False:
            raise Exception("Unmatched closing markers")

        if node.text_type == "text_type_bold":
            matches = bold_pattern.findall(node.text)

def closing_markers(text):
    stack = []
    i = 0 
    while i < len(text):
        # For bold text
        if text[i:i+2] == "**":
            if stack and stack[-1] == "**":
                # Matched bold closing
                stack.pop()
            else:
                # Found bold opening
                stack.append("**")
            i += 2

        # For italic text
        elif text[i] == "*":
            if stack and stack[-1] == "*":
                # Matched italic closing
                stack.pop()
            else:
                # Found italic opening
                stack.append("*")
            i += 1

        # For code text
        elif text[i] == "`":
            if stack and stack[-1] == "`":
                # Matched code closing 
                stack.pop()
            else:
                # Found code opening
                stack.append("`")
            i += 1
        
        else:
            i += 1

        if stack:
            return False
    return True



error_text = "This should *result in an error"
error_text2 = "This **lorem ipsum* shouldn't result in an error"
error_text3 = "This is another** lorem ipsum test"
bold_text = "This should be **bolded** by natural law"
code_text = "This is text with a `code block` word"

b_pattern = re.compile(r'(\*\*[^*]+\*\*)')

parts = b_pattern.split(error_text3)
b_list = [part for part in parts if part]
print(b_list)
for text in b_list:
    if "**" in text:
        temp = text.replace("**","")
        print(temp)
    else:
        print(text)
