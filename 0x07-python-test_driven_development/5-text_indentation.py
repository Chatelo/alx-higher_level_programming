#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    if len(text) == 0:
        return

    result = ""
    for char in text:
        result += char
        if char in [".", "?", ":"]:
            result += "\n\n"

    print("\n".join([line.strip() for line in result.split("\n")]))
