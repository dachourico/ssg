def markdown_to_blocks(markdown):
    block_list = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        # Clean up leading/trailing newlines and excessive spaces within each block
        block = "\n".join(line.strip() for line in block.split("\n")).strip()
        if block:  # Skip over any completely empty results
            block_list.append(block)
    return block_list

    