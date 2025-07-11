from src.models.blocktype import BlockType


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Check for code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check for heading (line starts with 1-6 '#' followed by a space)
    if lines[0].startswith("#"):
        hash_count = 0
        for char in lines[0]:
            if char == "#":
                hash_count += 1
            else:
                break
        if 1 <= hash_count <= 6 and lines[0][hash_count:hash_count + 1] == " ":
            return BlockType.HEADING

    # Check for quote block (every line starts with '>')
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Check for unordered list (every line starts with '- ')
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check for ordered list (lines start with incrementing number + ". ")
    is_ordered_list = True
    for idx, line in enumerate(lines, start=1):
        if not line.startswith(f"{idx}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    # Default is paragraph
    return BlockType.PARAGRAPH

