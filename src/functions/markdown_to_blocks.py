def markdown_to_blocks(markdown: str) -> list[str]:
    # Split by two or more newlines to separate blocks
    raw_blocks = markdown.split("\n\n")

    # Strip leading/trailing whitespace and filter out empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip()]

    return blocks

