def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):  # Only a single # followed by a space
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown")

