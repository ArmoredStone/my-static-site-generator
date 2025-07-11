#!/bin/bash
uv run src/main.py

cd src/docs && uv run -m http.server 8888
