from math import sqrt

print("Введите число для подсчета итеративным способом: ")
number = int(input())

i = 0

if number == 0:
    print("Решение итеративным способом: 1")
else:
    while number:
        i += 1
        number //= 10
    print("Решение итеративным способом: " + str(i))

print("Введите число для решения рекурсивным способом: ")
number = int(input())


def recursion(num):
    if num // 10:
        return recursion(num // 10) + 1
    return 1


print("Решение рекурсивным способом: " + str(recursion(number)))

#####################################################################


a = int(input("Введите глубину вложенного корня: "))

i = 0


def recur(i, num):
    if num != 0:
        return sqrt(6 + i + (2 + i) * recur(i + 1, num - 1))
    else:
        return True


print(recur(0, a))
