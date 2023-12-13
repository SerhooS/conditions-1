# 1. Користувач вводить три цифри з клавіатури. Необхідно знайти суму чисел, добуток чисел.
# Результат обчислень вивести на екран.

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

result1 = (n1+n2+n3)
result2 = (n1*n2*n3)
print(f"Sum of numbers: {result1} \nProduct of numbers: {result2}")

# 2. Напишіть програму, яка обчислює площу ромба. Користувач із клавіатури вводить довжину двох його діагоналей.
# Площа ромба дорівнює половині добутку його діагоналей: S = (AC · BD)/2.

n1 = int(input("Enter diagonal length AC: "))
n2 = int(input("Enter diagonal length BD: "))

Result = (n1*n2)/2
print(f"Area: {Result}")

# 3. Користувач вводить з клавіатури число, що складається із чотирьох цифр. Потрібно знайти добуток цифр.
# Наприклад, якщо з клавіатури введено 1324 тоді результат буде - 1*3*2*4 = 24.

number = int(input("Enter 4-r digit number: "))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10

result = n1 * n2 * n3 * n4
print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
print(f"Result: {result}")