#Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

n = input("Введите трехзначное число: ")
n = int(n)
c = n % 10
n = n // 10
b = n % 10
a = n // 10
print("Сумма цифр числа:", a + b + c)


