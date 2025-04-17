from htmlnode import HTMLNode
from textnode import TextNode, TextType
from extract import *

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for image_alt, image_url in images:

            image_markdown = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(image_markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            remaining_text = parts[1] if len(parts) > 1 else ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            parts = remaining_text.split(link_markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            remaining_text = parts[1] if len(parts) > 1 else ""
            
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.NORMAL))