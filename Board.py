#!/bin/python3
from __future__ import annotations
from typing import Callable



def dist_by_formula(
    board_size: list[
        #  [min ... max]
        tuple[int, int]
    ] = [(0, 8), (0, 8)], *,
    formula: Callable[[list[int]], int | float] = lambda * args: sum( arg ** 2 for arg in args )
) -> int | float:
    value = tuple(dim[0] for dim in board_size)
    while True:
        yield formula(* value)
        pointer = -1
        while value[pointer] >= board_size[pointer][1]:
            value = list(value)
            value[pointer] = board_size[pointer][0]
            value = tuple(value)
            pointer -= 1
            try:
                value[pointer]
            except IndexError:
                yield StopIteration
        value = list(value)
        value[pointer] += 1
        value = tuple(value)

if  __name__ == "__main__":
    collection = dist_by_formula()
    prev_item = 0
    for item in collection:
        if item == StopIteration:
            print()
            break
        print("" if prev_item < item else "\n", end = f"{item: >6}")
        prev_item = item

        