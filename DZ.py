x1 = int(input("x1: "))
x2 = int(input("x2: "))
print(x1 // x2, ".", x1 % x2)


guest_list = lower(str(input("Enter guest list: ")))
guest_name = lower(str(input("Enter guest name: ")))

print(bool(guest_name in guest_list))
