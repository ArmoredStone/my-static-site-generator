from src.models.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split nodes that are plain text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # If there's no delimiter found, leave it as-is
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        # Alternate between TEXT and the given text_type
        for i, part in enumerate(parts):
            if part == "":
                continue  # Skip empty strings caused by leading/trailing delimiters
            if i % 2 == 0:
                # Even index → outside delimiters → plain text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index → inside delimiters → special type
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

