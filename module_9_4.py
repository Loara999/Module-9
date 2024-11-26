import random


#1 блок
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


#2 блок
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


#3 блок
class MysticBall:
    def __init__(self, *words):
        self.words = [w for w in words]

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())