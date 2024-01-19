from stack_vm.lexer import Lexer
from stack_vm.parser import Parser
from stack_vm.code_generator import CodeGenerator
from stack_vm.interpreter import StackMachine
import sys
import argparse


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", type=str, help="The File to Execute.")
    ap.add_argument(
        "-v", "--verbose", action="store_true", help="Toggle The Interpreter Verbosity."
    )
    ap.add_argument(
        "--tickrate",
        "-t",
        type=float,
        default=0.5,
        help="Interpreter Sleep Time per Cycle in Seconds",
    )
    args = ap.parse_args()

    tokens = Lexer(args.file).parse_tokens()
    ast = Parser(tokens).parse()
    code = CodeGenerator(ast).generate()

    vm = StackMachine(code, tickrate=args.tickrate, verbose=args.verbose)
    vm.exec()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
