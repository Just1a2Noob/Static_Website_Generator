class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag 
       self.value = value
       self.children = children
       self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            if len(self.props) == 2:
                return f"href=\"{self.props.get("href")}\" target=\"{self.props.get("target")}\""
            if len(self.props) == 1:
                return f"href=\"{self.props.get("href")}\""
        return f""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        props_to_html = super().props_to_html()
        if self.value == None or len(self.value) <= 0:
            raise ValueError("Value cannot be None or empty")
        
        if self.tag == None or len(self.tag) <= 0:
            return f"{self.value}"
        
        if self.props != None:
            if len(self.props) > 0:
                return f"<{self.tag} {props_to_html}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag was not supplied")
        
        if not self.children:
            raise ValueError("Children cannot be empty")
        else:
            temp = ""
            for node in self.children:
                if isinstance(node, LeafNode) or isinstance(node, ParentNode):
                    node_str = node.to_html()
                    temp += str(node_str)
                else:
                    raise ValueError("List contains invalid class")

        return (f"<{self.tag}>{temp}</{self.tag}>")

def text_node_to_html_node(text_node):
    pass