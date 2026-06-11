import sys
import re

SUBSTITUTIONS = [
    ("ch'", "c"),
    ("ts'", "dz"),
    ("Ch'", "C"),
    ("Ts'", "Dz"),
    ("CH'", "C"),
    ("TS'", "DZ"),
    ("p'",  "f"),
    ("t'",  "d"),
    ("k'",  "g"),
    ("P'",  "F"),
    ("T'",  "D"),
    ("K'",  "G"),
    ("'",   "h"),
]

def almg_to_nueva(text):
    for almg, nueva in SUBSTITUTIONS:
        text = text.replace(almg, nueva)
    return text

def nueva_to_almg(text):
    # reverse — approximate, not perfect for all cases
    rev = [
        ("dz", "ts'"),
        ("Dz", "Ts'"),
        ("DZ", "TS'"),
        ("c",  "ch'"),
        ("C",  "Ch'"),
        ("f",  "p'"),
        ("F",  "P'"),
        ("d",  "t'"),
        ("D",  "T'"),
        ("g",  "k'"),
        ("G",  "K'"),
    ]
    for nueva, almg in rev:
        text = text.replace(nueva, almg)
    return text

def process_file(input_path, output_path, direction="to_nueva"):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    if direction == "to_nueva":
        result = almg_to_nueva(content)
    else:
        result = nueva_to_almg(content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Done: {input_path} -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python almg_to_nueva.py input.txt output.txt [--reverse]")
        sys.exit(1)

    direction = "to_nueva"
    if "--reverse" in sys.argv:
        direction = "to_almg"

    process_file(sys.argv[1], sys.argv[2], direction)
