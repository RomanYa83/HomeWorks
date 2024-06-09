class EvenNumbers:
    def __init__(self, start=0, stop=1):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.current = self.start if self.start % 2 == 0 else self.start +1
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        number = self.current
        self.current += 2
        return number


en = EvenNumbers(10, 25)
for i in en:
    print(i)
