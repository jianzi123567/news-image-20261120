#!/usr/bin/env python3
"""news-image-20261120: write the 20 November 2026 world-news image.

The entry image lives in this repository as entry.png. This program
only copies those bytes to the output directory, so every run writes
exactly the same bytes: no network, no clock, no randomness, no
environment input beyond the output directory override.
"""

import os


def load_image():
    """Read the bundled image bytes from beside this file.

    Kept separate from writing so the copy step can be tested on its
    own: load, check, then write, in that order.
    """
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "entry.png")
    with open(path, "rb") as handle:
        return handle.read()


def check_image(payload):
    """Refuse anything that is not a small PNG or JPEG image."""
    if len(payload) > 1024 * 1024:
        raise SystemExit("entry.png is larger than 1 MiB")
    is_jpeg = payload[:2] == b"\xff\xd8"
    is_png = payload[:8] == b"\x89PNG\r\n\x1a\n"
    if not is_jpeg and not is_png:
        raise SystemExit("entry.png is neither a JPEG nor a PNG")


def write_image(payload):
    """Write the bytes to /output/entry.png and confirm the copy."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.png")
    with open(target, "wb") as handle:
        handle.write(payload)
    with open(target, "rb") as handle:
        copied = handle.read()
    if copied != payload:
        raise SystemExit("written entry.png does not match the source")


def main():
    payload = load_image()
    check_image(payload)
    write_image(payload)


if __name__ == "__main__":
    main()
