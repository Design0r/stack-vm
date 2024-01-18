from stack_vm.lexer import Lexer
from stack_vm.parser import Parser
from stack_vm.code_generator import CodeGenerator
from stack_vm.interpreter import StackMachine


def main() -> int:
    file = "./examples/test.txt"
    lexer = Lexer(file)
    tokens = lexer.parse_tokens()

    parser = Parser(tokens)
    tree = parser.parse()

    gen = CodeGenerator(tree)
    code = gen.generate()

    vm = StackMachine(code, tickrate=0.5, verbose=True)
    vm.exec()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
