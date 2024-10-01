#!/bin/python3

import sys

def main() -> None:
    try:
        value = sys.argv[1]
    except IndexError:
        print("ERROR: No font_size value given")
        return

    try:
        num_value: float = float(value)
    except Exception:
        print(f"ERROR: Could not convert {value} into a float!")
        return

    if num_value < 6:
        print("ERROR: Font size can't be below 6!")
        return

    if num_value > 24:
        print("ERROR: Font size can't be above 24")
        return

    lines: list[str] = []
    with open("alacritty.toml", "r") as file:
        lines = file.read().splitlines(True)
        for i, line in enumerate(lines):
            if "size = " in line:
                lines[i] = f"size = {num_value}\n"

    with open("alacritty.toml", "w") as file:
        file.writelines(lines)

if __name__ == "__main__":
    main()
