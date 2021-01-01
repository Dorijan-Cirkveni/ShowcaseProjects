class LineOperation:
    def runOn(self, line: str) -> str:
        return line


class CheckIfRead(LineOperation):
    def __init__(self):
        return

    def runOn(self, line: str) -> str:
        X = input(line)
        if X == "Y":
            line += " --"
        return line


class BulkString(LineOperation):
    def __init__(self, size):
        self.count = 0
        self.size = size
        self.res = ""
        return

    def runOn(self, line: str) -> str:
        self.count += 1
        self.res += line
        self.res += "\n"
        if self.count == self.size:
            self.count = 0
            self.res += "\n"
        return line
