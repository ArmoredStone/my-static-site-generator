import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

def copy_static(src: str, dest: str):
    """Recursively copy static assets from src to dest, wiping dest first."""
    
    # Clean destination
    if os.path.exists(dest):
        shutil.rmtree(dest)
        logging.info(f"Deleted existing directory: {dest}")

    os.makedirs(dest)
    logging.info(f"Created directory: {dest}")

    # Walk through the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            # Recursively copy subdirectory
            copy_static(src_path, dest_path)
        else:
            # Copy file
            shutil.copy(src_path, dest_path)
            logging.info(f"Copied file: {src_path} -> {dest_path}")


def main():
    copy_static("static", "public")


if __name__ == "__main__":
    main()

