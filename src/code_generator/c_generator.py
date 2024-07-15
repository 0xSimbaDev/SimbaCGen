from parser.parser import *

def generate_c_code(func, indent=0):
    indent_str = " " * indent

    def generate_expression(expr):
        if isinstance(expr, BinaryOperation):
            left = generate_expression(expr.left)
            right = generate_expression(expr.right)
            return f"({left} {expr.operator} {right})"
        elif isinstance(expr, UnaryOperation):
            operand = generate_expression(expr.operand)
            return f"{expr.operator}{operand}"
        elif isinstance(expr, Literal):
            return str(expr.value) 
        elif isinstance(expr, VariableReference):
            return expr.name
        elif isinstance(expr, FunctionCall):
            args = ", ".join(generate_expression(arg) for arg in expr.arguments)
            return f"{expr.name}({args})"

    def generate_statement(stmt, indent):
        indent_str = " " * indent
        if isinstance(stmt, VariableDeclaration):
            value = (
                f" = {generate_expression(stmt.value)}"
                if stmt.value is not None
                else ""
            )
            return f"{indent_str}{stmt.type} {stmt.name}{value};"
        elif isinstance(stmt, ExpressionStatement):
            return f"{indent_str}{generate_expression(stmt.expression)};"
        elif isinstance(stmt, ReturnStatement):
            value = (
                generate_expression(stmt.value) if stmt.value is not None else ""
            )
            return f"{indent_str}return {value};"
        elif isinstance(stmt, IfStatement):
            condition = generate_expression(stmt.condition)
            then_block = generate_block(stmt.then_block, indent + 4)
            else_str = (
                f" else {generate_block(stmt.else_block, indent + 4)}"
                if stmt.else_block
                else ""
            )
            return f"{indent_str}if ({condition}) {then_block}{else_str}"
        else:
            raise ValueError(f"Unknown statement type: {type(stmt).__name__}")

    def generate_block(block, indent):
        indent_str = " " * indent
        body_lines = [generate_statement(stmt, indent + 4) for stmt in block.statements]
        return "{\n" + "\n".join(body_lines) + f"\n{indent_str}}}"

    arg_str = ", ".join(f"{arg.type} {arg.name}" for arg in func.arguments)
    function_signature = f"{func.return_type} {func.name}({arg_str})"

    function_body = generate_block(func.block, indent)
    return f"{function_signature} {function_body}"
