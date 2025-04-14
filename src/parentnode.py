from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, props, value=None, children=children)

    def to_html(self, tag, children):
        if not self.tag:
            raise ValueError("Must have a tag")
        if not self.children:
            raise ValueError("Must have children")
        
        html = f"<{self.tag}"

        if self.props:
            pass

        html += ">"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html