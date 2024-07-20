first = int(input("Ввведите первое целое число "))
second = int(input("Ввведите второе целое число "))
third = int(input("Ввведите третье целое число "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif not first == second == third:
    print(0)