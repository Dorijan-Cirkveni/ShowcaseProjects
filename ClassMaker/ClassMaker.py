def MakeClass(impF: dict):
    class X:
        RawFunctions = impF
        GeneratedFunctions = dict()

        def __init__(self):
            self.x = 1
            return

        def cc(self, name) -> callable:
            if name in X.GeneratedFunctions:
                    return X.GeneratedFunctions[name]
            raise NotImplementedError
    return X


def main():
    def X(this):
        return 1

    TEST = MakeClass({"Test": X})
    TX = TEST()
    e = TX.cc("Test")()
    return


if __name__ == "__main__":
    main()
