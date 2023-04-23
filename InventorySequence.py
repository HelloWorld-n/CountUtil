#!/bin/python3
import typing
import os

os.chdir(os.path.dirname(__file__))
os.system("")

def calc(required_value_number: int):
    values = {}
    current_count = 0
    new_value = 0
    for i in range(required_value_number):
        if current_count not in values:
            values[current_count] = 0
        new_value = values[current_count]
        if new_value not in values:
            values[new_value] = 0
        values[new_value] += 1
        if new_value == 0:
            current_count = 0
        else:
            current_count += 1
    return new_value

if __name__ == "__main__":
    values = {}
    current_count = 0
    new_value = 0
    i = 0
    while True:
        if current_count not in values:
            values[current_count] = 0
        new_value = values[current_count]
        if new_value not in values:
            values[new_value] = 0
        values[new_value] += 1
        if new_value == 0:
            current_count = 0
        else:
            current_count += 1
        print(f"calc({i}) == {new_value}")
        i += 1

