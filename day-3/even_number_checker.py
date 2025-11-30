# Little program to check if the number is even or uneven.
number_to_check = int(input("Give me a number please!\n"))
print(f"Checking:{number_to_check}")

if number_to_check %2 == 0:
    print("The number is even.")
else:
    print("The number is uneven.")
