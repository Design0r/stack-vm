from __future__ import annotations
from typing import Generator
from stack_vm.token import Tokens, Token
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VariableNode:
    name: str


@dataclass(frozen=True, slots=True)
class ValueNode:
    value: int | float | str


@dataclass(frozen=True, slots=True)
class BinOpNode:
    left: BinOpNode | ValueNode | VariableNode
    operator: Token
    right: BinOpNode | ValueNode | VariableNode


@dataclass(frozen=True, slots=True)
class AssignmentNode:
    varibale_name: str
    expression: BinOpNode | ValueNode | VariableNode


class Parser:
    def __init__(self, tokens: Generator[Token, None, None]):
        self.tokens = tokens
        self.curr_token = next(tokens)

    def next_token(self):
        self.curr_token = next(self.tokens)

    def parse(self):
        while True:
            try:
                yield self.parse_statement()
            except StopIteration:
                return

    def parse_statement(self):
        if self.curr_token.type == Tokens.EOL:
            self.next_token()

        if self.curr_token.type == Tokens.Identifier:
            varibale_name = self.curr_token.value
            self.next_token()

            if self.curr_token.type == Tokens.Equal:
                self.next_token()
                expression = self.parse_expression()
                return AssignmentNode(varibale_name, expression)

            else:
                raise SyntaxError(f'Expected "=", got {self.curr_token}')

    def parse_expression(self):
        left = self.parse_term()

        while self.curr_token.type in (Tokens.Plus, Tokens.Minus):
            operator = self.curr_token
            self.next_token()
            right = self.parse_term()
            left = BinOpNode(left, operator, right)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.curr_token.type in (Tokens.Star, Tokens.Slash):
            operator = self.curr_token
            self.next_token()
            right = self.parse_factor()
            left = BinOpNode(left, operator, right)

        return left

    def parse_factor(self):
        if self.curr_token.type == Tokens.Integer:
            node = ValueNode(self.curr_token.value)
            self.next_token()
            return node
        elif self.curr_token.type == Tokens.Float:
            node = ValueNode(self.curr_token.value)
            self.next_token()
            return node
        elif self.curr_token.type == Tokens.Identifier:
            node = VariableNode(self.curr_token.value)
            self.next_token()
            return node
        else:
            raise SyntaxError(
                f"Expected a number or identifier, but got {self.curr_token.type}"
            )
