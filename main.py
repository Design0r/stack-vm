from stack_vm.lexer import Lexer
from stack_vm.parser import Parser


def main() -> int:
    file = "./test.txt"
    lexer = Lexer(file)
    tokens = lexer.parse_tokens()

    parser = Parser(tokens)
    tree = parser.parse()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
