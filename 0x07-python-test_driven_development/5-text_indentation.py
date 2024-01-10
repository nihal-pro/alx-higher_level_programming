#!/usr/bin/python3
def text_indentation(text):
    """
    Args:
        text (str): a string tha will divied
    Return: new text divied by .?:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    while idx < len(text) and text[idx] == ' ':
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
