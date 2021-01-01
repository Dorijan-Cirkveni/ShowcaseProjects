from LineOperation import LineOperation, BulkString, CheckIfRead


class LineProcessor:
    def __init__(self):
        self.lines = list()
        return

    def load(self, filename: str):
        F = open(filename, "r")
        self.lines = F.read().split("\n")
        return

    def goThroughAll(self, op: LineOperation):
        for i in range(len(self.lines)):
            self.lines[i] = op.runOn(self.lines[i])
        return

    def getBulks(self, bulkSize):
        proc = BulkString(bulkSize)
        self.goThroughAll(proc)
        return proc.res


if __name__ == "__main__":
    LP = LineProcessor()
    CIR = CheckIfRead()
    inp = input("Filename:")
    LP.load(inp)
    LP.goThroughAll(CIR)
    res = LP.getBulks(40)
    F = open(inp + "_result.txt", "w")
    F.write(res)
    F.close()
