#!/bin/python3
import typing
import os

import json5

os.chdir(os.path.dirname(__file__))
os.system("")

PATH_DATA: typing.Final = "./Data/LetterWord.json"
if not os.path.isfile(PATH_DATA):
    os.makedirs(os.path.dirname(PATH_DATA), exist_ok = True)
    with open(PATH_DATA, "w") as file:
        file.write("{}")
with open(PATH_DATA, "r") as file:
    json_data = json5.loads(file.read())
    ALPHABET: typing.Final[str] = (
        json_data['ALPHABET']
    if 'ALPHABET' in json_data else
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    COLLECTION : typing.Final[list[str]] = (
        json_data['COLLECTION']
    if 'COLLECTION' in json_data else
        ["EGG"]
    )
    del json_data
del file

def estimate(word: str, debug: bool = False):
    value = ["A" if letter in ALPHABET else letter for letter in word]
    total_count = 0
    current_pos = 0
    while "".join(value) != word:
        if value[current_pos] != word[current_pos]:
            value[current_pos] = chr(ord(value[current_pos]) + 1)
            total_count += 1
            if debug:
                print(
                    f"{total_count} "
                    f"\u001B[38;2;255;255;0m{''.join(value)}\u001B[0m"
                )
        else:
            current_pos += 1

    return total_count

if __name__ == "__main__":
    total_count = 0
    for item in COLLECTION:
        total_count += estimate(item, debug = True)
        print(f"\u001B[38;2;255;255;255mtotal_count({item!r}) = {total_count}\u001B[0m")
    
