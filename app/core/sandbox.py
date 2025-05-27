import ast

def is_script_safe(code: str) -> bool:
    dangerous_nodes = (ast.Import, ast.ImportFrom, ast.Exec, ast.Call)
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, dangerous_nodes):
            return False
    return True
