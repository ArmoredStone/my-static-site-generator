#!/bin/bash
uv run src/main.py /my-static-site-generator/

cd docs && uv run -m http.server 8888
