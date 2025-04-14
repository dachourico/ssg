from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value  # Raw text if no tag exists
        else:
            # Render attributes if present
            if self.props:
                # Convert props dictionary to HTML attributes
                attributes = " ".join(f'{key}="{value}"' for key, value in self.props.items())
                return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"