import os
from src.functions.markdown_to_html_node import markdown_to_html_node
from src.functions.extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    root_node = markdown_to_html_node(markdown_content)
    html_content = root_node.to_html()

    title = extract_title(markdown_content)

    # Replace placeholders
    page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Replace href="/ and src="/ with href="{basepath} and src="{basepath}
    page = page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)
