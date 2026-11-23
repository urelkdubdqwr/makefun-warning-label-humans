"""Write the make.fun warning-label entry to entry.txt in the output directory."""

import os
import sys

TEXT = "WARNING: This unit will say 'one more episode' with no technical basis for the estimate.\n"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {out_dir!r}: {exc}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
