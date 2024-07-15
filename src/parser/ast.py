class FunctionDeclaration:
    def __init__(self, name, return_type, arguments, block):
        self.name = name
        self.return_type = return_type
        self.arguments = arguments
        self.block = block

class Argument:
    def __init__(self, name, arg_type):
        self.name = name
        self.type = arg_type

class VariableDeclaration:
    def __init__(self, name, var_type, value=None):
        self.name = name
        self.type = var_type
        self.value = value

class BinaryOperation:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class UnaryOperation:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class Literal:
    def __init__(self, value):
        self.value = value

class VariableReference:
    def __init__(self, name):
        self.name = name

class FunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class ExpressionStatement:
    def __init__(self, expression):
        self.expression = expression

class ReturnStatement:
    def __init__(self, value):
        self.value = value

class Block:
    def __init__(self, statements):
        self.statements = statements

class IfStatement:
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block