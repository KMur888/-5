n = int(input("Сколько слов ввести? "))

result = ""  

for i in range(n):
    word = input(f"Введите слово {i+1}: ")
    result = result + word + " "  

result = result[:-1]
print("Результат:", result)