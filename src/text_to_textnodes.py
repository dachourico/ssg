from split_img_links import *
from split_text import *
from textnode import *
from extract import *

def text_to_textnodes(text):
    textnodes = []
    chunks = split_nodes_delimiter(text)

    for chunk in chunks:
        if is_image(chunk):
            image_alt, image_url = extract_markdown_images(chunk)[0]
            textnodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

        elif is_link(chunk):
            link_text, link_url = extract_markdown_links(chunk)[0]
        
        elif is_code(chunk):
            code_text = chunk[1:-1]
            textnodes.append(TextNode(code_text, TextType.CODE))

        elif is_bold(chunk):
            bold_text = chunk[2:-2]
            textnodes.append(TextNode(bold_text, TextType.BOLD))
            
        else:
            textnodes.append(TextNode(chunk, TextType.TEXT))

    return textnodes