result = ""
word = input("Введите слово (или 'СТОП' для завершения): ")

while word != "СТОП":
    result = result + word + " "
    word = input("Введите слово (или 'СТОП' для завершения): ")

result = result[:-1]
print("Результат:", result)