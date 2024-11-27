import math


class StepValueError(ValueError):
    pass


class Iterator:
    def __new__(cls, start: int, stop: int, step=1):
        try:
            if step == 0:
                raise StepValueError
            return super().__new__(cls)
        except:
            print('Шаг не может быть равен 0. Итератор не был создан')

    def __init__(self, start: int, stop: int, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        self.__flag = False

    def __iter__(self):
        self.pointer = self.start - self.step
        self.__flag = abs(self.stop - self.pointer) < abs(self.stop - self.start)
        return self

    def __next__(self):
        if self.__flag:
            raise StopIteration()
        self.pointer += self.step
        if self.pointer == self.start:
            return self.start
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
        else:
            if self.pointer < self.stop:
                raise StopIteration()
        return self.pointer



iter1 = Iterator(100, 200, 0)
print(iter1)
try:
    for i in iter1:
        print(i, end=' ')
except TypeError:
    print('Невозможно перебрать пустой объект')
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()