import ast


def simplify(inpt: str) -> str:
    tree = ast.parse(inpt, mode='eval').body

    def walk(node, parent_op=None):
        if isinstance(node, ast.Constant):
            return str(node.value)

        ops = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/'}
        current_op = type(node.op)

        left_str = walk(node.left, current_op)
        right_str = walk(node.right, current_op)

        expr = f"{left_str} {ops[current_op]} {right_str}"

        if parent_op is None:
            return expr

        if current_op == parent_op and current_op in [ast.Add, ast.Mult]:
            return expr

        return f"({expr})"

    return walk(tree)
