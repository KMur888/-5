import random

ошибки = 0
правильно = 0

while ошибки < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    print(a, "+", b, "= ", end="")
    ответ = int(input())
    
    if ответ == a + b:
        print("Правильно!")
        правильно = правильно + 1
    else:
        print("Ответ неверный!")
        ошибки = ошибки + 1

print("Игра окончена. Правильных ответов:", правильно)