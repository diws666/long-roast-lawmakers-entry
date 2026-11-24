#!/usr/bin/env python3
"""Writes one satirical roast sentence to /output/entry.txt."""

ROAST = (
    "They want to regulate AI, crypto, and the entire internet, "
    "but ask them to convert a Word file to PDF and suddenly "
    "the committee needs a six-month study."  # 153 characters
)

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)

print(f"Wrote {len(ROAST.encode('utf-8'))} bytes to /output/entry.txt")
