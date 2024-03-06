from stack_vm.lexer import Lexer
from stack_vm.parser import Parser
from stack_vm.code_generator import CodeGenerator
from stack_vm.interpreter import StackMachine
import argparse


def get_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", type=str, help="The File to Execute.")
    ap.add_argument(
        "-v", "--verbose", action="store_true", help="Toggle The Interpreter Verbosity."
    )
    ap.add_argument(
        "--tickrate",
        "-t",
        type=float,
        default=0,
        help="Interpreter Sleep Time per Cycle in Seconds",
    )
    args = ap.parse_args()
    return args


def main() -> int:
    args = get_args()

    tokens = Lexer(args.file).parse_tokens(verbose=args.verbose)
    ast = Parser(tokens, verbose=args.verbose).parse()
    code = CodeGenerator(ast).generate(verbose=args.verbose)

    vm = StackMachine(code, tickrate=args.tickrate, verbose=args.verbose)
    vm.exec()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
