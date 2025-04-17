from htmlnode import HTMLNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)

        text = old_node.text

        if delimiter not in text:
            new_nodes.append(old_node)
            continue

        start_index = text.find(delimiter)
        end_index = text.find(delimiter, start_index + len(delimiter))

        if end_index == -1:
            raise Exception(f"No closing delimiter found for {delimiter}")
        
        before_text = text[:start_index]
        delimited_text = text[start_index + len(delimiter):end_index]
        after_text = text[end_index + len(delimiter):]

        if before_text:
            new_nodes.append(TextNode(before_text, TextType.NORMAL))
        new_nodes.append(TextNode(delimited_text, text_type))
        
        if after_text:
            after_node = TextNode(after_text, TextType.NORMAL)
            result_nodes = split_nodes_delimiter([after_node], delimiter, text_type)
            new_nodes.extend(result_nodes)


    
    return new_nodes
