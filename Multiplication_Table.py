import random

print("Multiplication Table\n")

while True:
    user = input("Enter a number: ")

    if not user.isdigit():
        print("numbers only")
    else:
        user = int(user)
        for i in range(1, 2):
            for j in range(1, 11):
                print(f"{user} x {j} = {user * j}")
            print()
            continue
