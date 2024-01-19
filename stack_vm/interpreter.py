import time


class StackMachine:
    def __init__(self, commands: list[tuple], tickrate=1.0, verbose=False) -> None:
        self._stack = []
        self._commands = commands
        self._memory = {}
        self.tickrate = tickrate
        self.verbose = verbose

    def store(self, addr):
        val = self.pop()
        self._memory[addr] = val

    def load(self, addr):
        self.push(self._memory[addr])

    def push(self, item):
        self._stack.append(item)

    def pop(self, num: int = 1) -> list:
        if num == 1:
            return self._stack.pop()
        return [self._stack.pop() for _ in range(num)]

    def exec(self, silent=False) -> None:
        if not silent:
            print("Starting Code Execution...")

        for idx, (op, *args) in enumerate(self._commands, 1):
            if op == "const":
                self.push(args[0])
            elif op == "add":
                r, l = self.pop(2)
                self.push(r + l)
            elif op == "mul":
                r, l = self.pop(2)
                self.push(r * l)
            elif op == "sub":
                r, l = self.pop(2)
                self.push(r - l)
            elif op == "div":
                r, l = self.pop(2)
                self.push(r / l)
            elif op == "mod":
                r, l = self.pop(2)
                self.push(r % l)
            elif op == "exp":
                r, l = self.pop(2)
                self.push(r**l)
            elif op == "store":
                self.store(args[0])
            elif op == "load":
                self.load(args[0])
            elif op == "print":
                print(self.pop())
            else:
                raise RuntimeError(f"Unknown Instruction: {op}")

            if self.verbose:
                print(
                    f"cycle: {self.format(idx, 5)}",
                    f"op: {self.format(op, 8)}",
                    f"args: {self.format(args, 15)}",
                    f"stack: {self.format(self._stack, 15)}",
                    f"memory: {self._memory}",
                )
            time.sleep(self.tickrate)

    def format(self, val, width: int) -> str:
        return str(val) + " " * (width - len(str(val)))
