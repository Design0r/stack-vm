from stack_vm.lexer import Lexer
from stack_vm.parser import Parser
from stack_vm.code_generator import CodeGenerator
from stack_vm.interpreter import StackMachine


def main() -> int:
    file = "./examples/test.txt"
    tokens = Lexer(file).parse_tokens()
    ast = Parser(tokens).parse()
    code = CodeGenerator(ast).generate()

    vm = StackMachine(code, tickrate=0.1, verbose=True)
    vm.exec()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
