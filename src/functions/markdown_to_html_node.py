from src.models.htmlnode import ParentNode, LeafNode, HTMLNode
from src.models.blocktype import BlockType
from src.models.textnode import TextNode, TextType
from src.functions.markdown_to_blocks import markdown_to_blocks
from src.functions.block_to_block_type import block_to_block_type
from src.functions.text_to_textnodes import text_to_textnodes
from src.functions.text_node_to_html_node import text_node_to_html_node


def text_to_children(text: str) -> list[HTMLNode]:
    """Convert inline markdown to HTMLNode children."""
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode(tag="div", children=[])

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            collapsed_text = block.replace("\n", " ")
            children = text_to_children(collapsed_text)
            node = ParentNode(tag="p", children=children)
            parent.children.append(node)

        elif block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))
            content = block[level + 1:]
            children = text_to_children(content)
            node = ParentNode(tag=f"h{level}", children=children)
            parent.children.append(node)

        elif block_type == BlockType.CODE:
            code_text = block.removeprefix("```").removesuffix("```").strip() + "\n"
            code_node = text_node_to_html_node(TextNode(code_text, TextType.TEXT))
            node = ParentNode(tag="pre", children=[
                ParentNode(tag="code", children=[code_node])
            ])
            parent.children.append(node)

        elif block_type == BlockType.QUOTE:
            quote_lines = [line.lstrip("> ") for line in block.split("\n")]
            quote_text = "\n".join(quote_lines)
            children = text_to_children(quote_text)
            node = ParentNode(tag="blockquote", children=children)
            parent.children.append(node)

        elif block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                item_text = line.removeprefix("- ")
                children = text_to_children(item_text)
                li_nodes.append(ParentNode(tag="li", children=children))
            node = ParentNode(tag="ul", children=li_nodes)
            parent.children.append(node)

        elif block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                item_text = line.split(". ", 1)[1]
                children = text_to_children(item_text)
                li_nodes.append(ParentNode(tag="li", children=children))
            node = ParentNode(tag="ol", children=li_nodes)
            parent.children.append(node)

        else:
            raise ValueError(f"Unsupported block type: {block_type}")

    return parent

