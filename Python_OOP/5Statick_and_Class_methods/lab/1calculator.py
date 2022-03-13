class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(initional,*args):
        result = initional
        for el in args:
            result /= el
        return result

    @staticmethod
    def subtract(initional, *args):
        r = initional
        for el in args:
            r -= el
        return r


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
