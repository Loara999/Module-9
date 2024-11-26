import  math

first= ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(i[1])-len(i[0])) for i in zip(first, second) if len(i[1]) != len(i[0]))
second_result = (len(first[a]) == len(second[a]) for a in range(3))
print(f'{list(first_result)}\n'
      f'{list(second_result)}')