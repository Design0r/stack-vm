from typing import Generator, Optional
from stack_vm.parser import (
    ASTNode,
    AssignmentNode,
    BinOpNode,
    PrintNode,
    ValueNode,
    VariableNode,
)
from stack_vm.token import Tokens


class CodeGenerator:
    def __init__(self, ast: Generator[Optional[ASTNode], None, None]):
        self.ast = ast
        self.binary_code = []

    def generate(self, silent=False):
        if not silent:
            print("Generating Stack Machine Code...")

        for node in self.ast:
            if not node:
                continue
            self.traverse(node)

        return self.binary_code

    def traverse(self, curr_node: ASTNode):
        if isinstance(curr_node, AssignmentNode):
            self.traverse(curr_node.expression)
            self.binary_code.append(("store", curr_node.variable_name))
        elif isinstance(curr_node, PrintNode):
            self.binary_code.append(("load", curr_node.varibale_name))
            self.binary_code.append(("print",))
        elif isinstance(curr_node, BinOpNode):
            if isinstance(curr_node.left, BinOpNode):
                self.traverse(curr_node.left)
            elif isinstance(curr_node.left, ValueNode):
                self.binary_code.append(("const", curr_node.left.value))
            elif isinstance(curr_node.left, VariableNode):
                self.binary_code.append(("load", curr_node.left.name))

            if isinstance(curr_node.right, BinOpNode):
                self.traverse(curr_node.right)
            elif isinstance(curr_node.right, ValueNode):
                self.binary_code.append(("const", curr_node.right.value))
            elif isinstance(curr_node.right, VariableNode):
                self.binary_code.append(("load", curr_node.right.name))

            if curr_node.operator.type == Tokens.Plus:
                self.binary_code.append(("add",))
            elif curr_node.operator.type == Tokens.Star:
                self.binary_code.append(("mul",))
            elif curr_node.operator.type == Tokens.Minus:
                self.binary_code.append(("sub",))
            elif curr_node.operator.type == Tokens.Slash:
                self.binary_code.append(("div",))
        elif isinstance(curr_node, VariableNode):
            self.binary_code.append(("load", curr_node.name))
        elif isinstance(curr_node, ValueNode):
            self.binary_code.append(("const", curr_node.value))

        return self.binary_code
