number = 14

if number % 3 == 0 and number % 7 == 0:
    print("BinGo!")
elif number % 3 == 0:
    print("Bin")
elif number % 7 == 0:
    print("Go")
else:
    print(f"{number} is just a number")