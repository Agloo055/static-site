from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        elif self.children == None:
            raise ValueError("Value Error: No Children found")
        else:
            html = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                html += child.to_html()
            html += f"</{self.tag}>\n"

            return html