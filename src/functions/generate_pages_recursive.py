import os
from src.functions.generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if filename.endswith(".md"):
                md_path = os.path.join(root, filename)
                rel_path = os.path.relpath(md_path, dir_path_content)
                html_rel_path = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, html_rel_path)
                generate_page(md_path, template_path, dest_path, basepath=basepath)
