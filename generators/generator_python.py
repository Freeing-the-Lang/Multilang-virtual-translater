from core.universal_ast import Node

class PythonGenerator:
    def generate(self, node: Node) -> str:
        if node.type == "Module":
            return "\n".join(self.generate(c) for c in node.children)
        elif node.type == "FunctionDecl":
            args = ", ".join(a.value for a in node.children[0].children)
            body = "\n".join("    " + self.generate(b) for b in node.children[1].children)
            return f"def {node.value}({args}):\n{body}"
        elif node.type == "Return":
            return f"return {self.generate(node.children[0])}"
        elif node.type == "BinaryExpr":
            left, right = map(self.generate, node.children)
            op = { "Add": "+", "Sub": "-", "Mult": "*", "Div": "/" }.get(node.value, "?")
            return f"({left} {op} {right})"
        elif node.type == "Identifier":
            return node.value
        elif node.type == "Literal":
            return repr(node.value)
        else:
            return f"# Unsupported: {node.type}"
