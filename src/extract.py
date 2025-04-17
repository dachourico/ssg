import re

def extract_markdown_images(text):
    
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def is_image(chunk):
    return len(extract_markdown_images(chunk)) > 0

def is_link(chunk):
    return len(extract_markdown_links(chunk)) > 0

def is_code(chunk):
    return chunk.startswith("`") and chunk.endswith("`")

def is_bold(chunk):
    return chunk.startswith("**") and chunk.endswith("**")