#!/bin/python3
from __future__ import annotations
from typing import Callable, Generator


def dist_by_formula(
    board_size: (
        list[
            #  [min ... max]
            tuple[int, int]
        ]
        | None
    ) = None,
    *,
    formula: Callable[[int], int | float] = lambda *args: sum(arg**2 for arg in args),
) -> Generator[int | float, None, None]:
    if board_size is None:
        board_size = [(0, 8), (0, 8)]
    value = tuple(dim[0] for dim in board_size)
    while True:
        yield formula(*value)
        pointer = -1
        while value[pointer] >= board_size[pointer][1]:
            value = list(value)
            value[pointer] = board_size[pointer][0]
            value = tuple(value)
            pointer -= 1
            try:
                value[pointer]
            except IndexError:
                return
        value = list(value)
        value[pointer] += 1
        value = tuple(value)


if __name__ == "__main__":
    collection = dist_by_formula()
    prev_item = 0
    for item in collection:
        if item == StopIteration:
            print()
            break
        print("" if prev_item < item else "\n", end=f"{item: >6}")
        prev_item = item
