class Fib:
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


fib = Fib()


iterator = iter(fib)


for number in iterator:
    if number > 4_000_000:
        break
    print(number)  # Выводим число в консоль
