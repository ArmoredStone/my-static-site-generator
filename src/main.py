import shutil
import os
import sys

from src.functions.generate_pages_recursive import generate_pages_recursive 

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        # Ensure basepath ends with a slash
        if not basepath.endswith("/"):
            basepath += "/"

    # Use docs directory for GitHub Pages
    output_dir = "src/docs"


    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Delete everything inside public
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    shutil.copytree("src/static", output_dir, dirs_exist_ok=True)
    generate_pages_recursive("src/content", "template.html", output_dir, basepath=basepath)



if __name__ == "__main__":
    main()

