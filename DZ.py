#Task 1
x1 = int(input("Введите первое число: "))
x2 = int(input("Введите второе число: "))
print("Целочисленный результат:", x1 // x2, "Остаток:", x1 % x2)
#Task 2
guest_list = str(input("Enter guest list: "))
guest_list=guest_list.lower()
guest_list=guest_list.translate({ord(','): None})
guest_list=guest_list.translate({ord('.'): None})
guest_name = str(input("Enter guest name: "))
guest_name=guest_name.lower()
if bool(guest_name in guest_list) == True:
    print("You can pass!")
else:
    print("You can't pass!")
