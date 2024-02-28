from neuroparser import TokenType, AST

class Environment:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def lookup(self, name):
        if name in self.values:
            return self.values[name]
        elif self.enclosing:
            return self.enclosing.lookup(name)
        raise RuntimeError(f"Variable '{name}' no definida")

class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def visit(self, node):
        method = f"visit_{type(node).__name__}"
        visitor = getattr(self, method, None)
        if visitor is None:
            raise RuntimeError(f"No hay método para visitar el nodo '{type(node).__name__}'")
        return visitor(node)

    def visit_BinaryExpression(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator == TokenType.PLUS:
            return left + right
        elif node.operator == TokenType.MINUS:
            return left - right
        elif node.operator == TokenType.STAR:
            return left * right
        elif node.operator == TokenType.SLASH:
            return left / right
        elif node.operator == TokenType.EQUAL_EQUAL:
            return left == right
        elif node.operator == TokenType.NOT_EQUAL:
            return left != right
        elif node.operator == TokenType.LESS:
            return left < right
        elif node.operator == TokenType.LESS_EQUAL:
            return left <= right
        elif node.operator == TokenType.GREATER:
            return left > right
        elif node.operator == TokenType.GREATER_EQUAL:
            return left >= right
        raise RuntimeError(f"Operador desconocido: {node.operator}")

    def visit_UnaryExpression(self, node):
        operand = self.visit(node.operand)
        if node.operator == TokenType.PLUS:
            return operand
        elif node.operator == TokenType.MINUS:
            return -operand
        elif node.operator == TokenType.NOT:
            return not operand
        raise RuntimeError(f"Operador desconocido: {node.operator}")

    def visit_Literal(self, node):
        return node.value

    def visit_Variable(self, node):
        return self.environment.lookup(node.name)

    def visit_FunctionCall(self, node):
        function = self.environment.lookup(node.name)
        new_env = Environment(enclosing=function.environment)
        for param, arg in zip(function.parameters, node.arguments):
            new_env.define(param, self.visit(arg))
        return self.execute_block(function.body, new_env)

    def visit_Assignment(self, node):
        value = self.visit(node.value)
        if isinstance(node.target, Variable):
            self.environment.define(node.target.name, value)
        else:
            raise RuntimeError("Asignación a un objetivo no válido")

    def visit_IfStatement(self, node):
        condition = self.visit(node.condition)
        if condition:
            self.execute_block(node.then_branch)
        elif node.else_branch:
            self.execute_block(node.else_branch)

    def visit_WhileStatement(self, node):
        while self.visit(node.condition):
            self.execute_block(node.body)

    def visit_ForStatement(self, node):
        # TODO: Implementar manejo de inicializador e incremento
        for value in node.iterable:
            self.environment.define(node.target.name, value)
            self.execute_block(node.body)

    def visit_Block(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_ReturnStatement(self, node):
        return self.visit(node.expression)

    def visit_FunctionDefinition(self, node):
        self.environment.define(node.name, node)

    def visit_ClassDefinition(self, node):
        # TODO: Implementar la definición de clases
        pass

    def visit_ImportStatement(self, node):
