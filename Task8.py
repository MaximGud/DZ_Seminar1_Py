# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки (рядов): "))
m = int(input("Введите размер шоколадки (колонок): "))
k = int(input("Введите количнество отламываемых долек: "))

if k%m ==0 or k%n == 0: print("Yes")
else: print("No")