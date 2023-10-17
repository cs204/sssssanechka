import sm
class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1)

    def getNextValues(self, state, inp):
        (prevPrevS, prevS) = state
        return ((prevS, inp), prevPrevS)


if __name__ == "__main__":
    sm = Delay2Machine(100, 10)
    print(sm.transduce([1, 2, 10, 20, 30, 35]))
