from src.models.textnode import TextNode, TextType
from src.functions.split_nodes_delimiter import split_nodes_delimiter
from src.functions.split_nodes_image import split_nodes_image
from src.functions.split_nodes_link import split_nodes_link


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # Order matters — first bold, then italic, then code
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Images and links last because they match different patterns
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

