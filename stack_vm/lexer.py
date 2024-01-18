from pathlib import Path
from typing import Generator

from stack_vm.token import Tokens, Token


class Lexer:
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)
        assert self.file_path.exists() is True, f"{self.file_path} does not exist"

    def _read_file(self) -> str:
        with open(self.file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    def parse_tokens(self, silent=False) -> Generator[Token, None, None]:
        if not silent:
            print("Starting Generating Tokens...")

        content = self._read_file()
        c_len = len(content)

        pos = 0
        while pos < c_len:
            char = content[pos]

            if char.isspace():
                pos += 1
                continue

            elif char.isalpha() or char == "_":
                c_pos = pos
                curr = char
                while (curr.isalnum() or curr == "_") and c_pos < c_len:
                    c_pos += 1
                    curr = content[c_pos]

                yield Token(Tokens.Identifier, "".join(content[pos:c_pos]))
                pos += c_pos - pos

            elif char.isdigit():
                c_pos = pos
                curr = char
                while (curr.isdigit() or curr == ".") and c_pos < c_len:
                    c_pos += 1
                    curr = content[c_pos]

                result = "".join(content[pos:c_pos])
                pos += c_pos - pos
                if "." in result:
                    yield Token(Tokens.Float, float(result))
                    continue

                yield Token(Tokens.Integer, int(result))

            else:
                if char == "=":
                    pos += 1
                    yield Token(Tokens.Equal, char)
                elif char == "+":
                    pos += 1
                    yield Token(Tokens.Plus, char)
                elif char == "-":
                    pos += 1
                    yield Token(Tokens.Minus, char)
                elif char == "/":
                    pos += 1
                    yield Token(Tokens.Slash, char)
                elif char == "*":
                    pos += 1
                    yield Token(Tokens.Star, char)
                elif char == ".":
                    pos += 1
                    yield Token(Tokens.Dot, char)
                elif char == ";":
                    pos += 1
                    yield Token(Tokens.EOL, char)
                else:
                    pos += 1
                    yield Token(Tokens.Illegal, char)
