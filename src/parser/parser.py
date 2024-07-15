import json
from .ast import *

def parse_json(json_str):
    data = json.loads(json_str)
    

    def parse_expression(expr):
        if expr['type'] == 'binary_operation':
            left = parse_expression(expr['left'])
            right = parse_expression(expr['right'])
            return BinaryOperation(expr['operator'], left, right)
        elif expr['type'] == 'unary_operation':
            operand = parse_expression(expr['operand'])
            return UnaryOperation(expr['operator'], operand)
        elif expr['type'] == 'literal':
            return Literal(expr['value'])
        elif expr['type'] == 'variable_reference':
            return VariableReference(expr['name'])
        elif expr['type'] == 'function_call':
            arguments = [parse_expression(arg) for arg in expr['arguments']]
            return FunctionCall(expr['name'], arguments)
        else:
            raise ValueError(f"Unknown expression type: {expr['type']}")

    def parse_statement(stmt):
        if stmt['type'] == 'variable_declaration':
            declarations = [
                VariableDeclaration(
                    decl['name'],
                    decl['type'],
                    parse_expression(decl['value']) if 'value' in decl else None,
                )
                for decl in stmt['declarations']
            ]
            return declarations
        elif stmt['type'] == 'expression_statement':
            expression = parse_expression(stmt['expression'])
            return ExpressionStatement(expression)
        elif stmt['type'] == 'return_statement':
            value = parse_expression(stmt['value']) if 'value' in stmt else None
            return ReturnStatement(value)
        elif stmt['type'] == 'if_statement':
            condition = parse_expression(stmt['condition'])
            then_block = parse_block(stmt['then_block'])
            else_block = (
                parse_block(stmt['else_block']) if 'else_block' in stmt else None
            )  
            return IfStatement(condition, then_block, else_block)
        else:
            raise ValueError(f"Unknown statement type: {stmt['type']}")

    def parse_block(block):
        statements = []
        for stmt in block:
            result = parse_statement(stmt)
            if isinstance(result, list): 
                statements.extend(result)
            else:
                statements.append(result)
        return Block(statements)

    arguments = [Argument(arg['name'], arg['type']) for arg in data['arguments']]
    block = parse_block(data['block'])
    func = FunctionDeclaration(data['name'], data['return_type'], arguments, block)

    return func