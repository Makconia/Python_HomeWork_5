# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
 
# *Пример:*
 
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
 
def exponentiation (a,b):
    if b==1:
        return a
    a = a * number1
    return (exponentiation (a, b-1))
 
number1 = int(input('Введите число: '))
number2 = int(input('Введите степень: '))
print(exponentiation(number1, number2))