class Calc:

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def mult(a,b):
        return a * b

    @staticmethod
    def leveling(a,b):
        return a ** b

    @staticmethod
    def division(a,b):
        if a == 0:
            raise TypeError("TypeError,can't divide by zero")
        return a / b

    @staticmethod
    def intdiv(a,b):
        if a == 0:
            raise TypeError("TypeError,can't divide by zero")
        return a // b

    @staticmethod
    def remofdiv(a,b):
        return a % b

