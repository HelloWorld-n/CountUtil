#!/bin/python3
from decimal import Decimal, getcontext

from Utils.simplify import simplify

getcontext().prec = 50


def solve_exhaustive(nums: list[Decimal], target: Decimal = Decimal(0)) -> set[str]:

    def get_results(n_list: list[Decimal]) -> dict[str, Decimal]:
        if len(n_list) == 1:
            return {str(n_list[0]): Decimal(n_list[0])}

        res = {}
        for i in range(1, len(n_list)):
            left = get_results(n_list[:i])
            right = get_results(n_list[i:])

            for left_expr, left_value in left.items():
                for right_expr, right_value in right.items():
                    ops = [
                        (
                            f"({left_expr} + {right_expr})",
                            left_value + right_value,
                        ),
                        (
                            f"({left_expr} - {right_expr})",
                            left_value - right_value,
                        ),
                        (
                            f"({left_expr} * {right_expr})",
                            left_value * right_value,
                        ),
                    ]
                    if right_value != 0:
                        ops.append(
                            (
                                f"({left_expr} / {right_expr})",
                                left_value / right_value,
                            )
                        )

                    for value, expr in ops:
                        if value not in res:
                            res[value] = expr

        return res

    results = get_results(nums)
    solutions = set()
    for expr, value in results.items():
        if value == target:
            solutions.add(expr)
    return solutions


if __name__ == "__main__":
    solutions = solve_exhaustive(
        nums=[Decimal(inp.strip()) for inp in input("nums: ").split(",")],
        target=Decimal(input("target: ")),
    )
    
    for solution in solutions:
        print(simplify(solution))
