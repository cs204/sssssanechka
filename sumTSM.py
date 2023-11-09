import sm

print("Часть 1.")

class SumTSM(sm.SM):
    """
    Ввод числа, вывод их сумма, завершает работу,
    когда сумма > 100
    """

    startState = 0

    def getNextState(self, state, inp):
        return state+inp

    def done(self, state):
        return state > 100

    # Здесь должен быть ваш код

#Для проверки раскомментируйте следующие 2 сторки
s = SumTSM()
print(s.transduce(range(20)))

#Правильный вывод
#[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105]
#------------------------------------—
print("Часть 2. Повторяет SumTSM 4 раза.")
# Создайте автомат fourTimes, который повторяет SumTSM четыре раза и затем завершается.
fourTimes = sm.Repeat(SumTSM(), 4) # Здесь должен быть ваш код


#Для проверки раскомментируйте следующию сторку
print(fourTimes.transduce(range(200)))
#---------------------------------------------—
print("Часть 3. Считающий автомат.")

class CountUpTo(sm.SM):
    """
    считает от 1 до заданного числа и завершает работу
    """
# Здесь должен быть ваш код
    startState = 0
    def __init__(self, nMax):
        self.nMax= nMax

    def getNextState(self, state, inp):
        return state + 1

    def done(self, state):
        return state == self.nMax


#Для проверки раскомментируйте следующие 2 сторки
m = CountUpTo(3)
print(m.run(20))

# правильный вывод
#[1, 2, 3]
#-------------------------------------—
print("Часть 4. Несколько считающих машин.")

def makeSequenceCounter(nList):
    """nList список чисел возвращает заканчивающийся автомат,
    который считает от 1 до первого числа, затем от 1 до следующего и т.д.
    Он завершается после счтёта до последнего числа.
    """
#Здесь должен быть ваш код

    return sm.Sequence([CountUpTo(k) for k in nList])

#Для проверки раскомментируйте следующию сторку
print(makeSequenceCounter([2, 5, 3]).run(20))

#правильны вывод [1, 2, 1, 2, 3, 4, 5, 1, 2, 3 ]

