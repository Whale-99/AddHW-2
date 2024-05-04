import random

code = random.randint(3, 21)
print("Код: " + str(code))
print()

password = list()
for i in range(0, 21):
    for j in range(i, 21):
        if i + j != 0:
            if code % (i + j) == 0:
                password.append(f"{i}{j}")
        else:
            continue

el = " ".join(password)
print("Пароль: " + el)
print()

print("Пары чисел:")
for i in range(0, 21):
    for j in range(i, 21):
        if i + j != 0:
            if code % (i + j) == 0:
                password.append(f"{i}{j}")
                print(f"{i} + {j}")
        else:
            continue
