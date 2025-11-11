import ast
from core.universal_ast import Node

class PythonParser:
    def parse(self, code: str) -> Node:
        tree = ast.parse(code)
        return self._convert(tree)

    def _convert(self, node) -> Node:
        if isinstance(node, ast.Module):
            return Node("Module", children=[self._convert(n) for n in node.body])
        elif isinstance(node, ast.FunctionDef):
            return Node("FunctionDecl", value=node.name, children=[
                Node("Args", children=[Node("Param", value=a.arg) for a in node.args.args]),
                Node("Body", children=[self._convert(b) for b in node.body]),
            ])
        elif isinstance(node, ast.Return):
            return Node("Return", children=[self._convert(node.value)])
        elif isinstance(node, ast.BinOp):
            return Node("BinaryExpr", value=type(node.op).__name__,
                        children=[self._convert(node.left), self._convert(node.right)])
        elif isinstance(node, ast.Name):
            return Node("Identifier", value=node.id)
        elif isinstance(node, ast.Constant):
            return Node("Literal", value=node.value)
        else:
            return Node(type(node).__name__)
