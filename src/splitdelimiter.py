from textnode import TextNode

# For reference (self, text=None, text_type=None, url=None)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass

t_string = "Testing the *limits* of a string"
t_string2 = "Does **double astarisks work?** If it doesn\'t this is gonna be bad"

def asterisks_f(sentence, asterisk_r = ""):
    word_list = sentence.split()
    if asterisk_r != "":
        if asterisk_r[-1:-2] == "**":
            return asterisk_r

    for i in word_list:
        if "**" in i:
            asterisk_r += i
            del word_list[:word_list.index(i)+1]
            return asterisks_f(" ".join(word_list), asterisk_r)

print(asterisks_f(t_string2))
