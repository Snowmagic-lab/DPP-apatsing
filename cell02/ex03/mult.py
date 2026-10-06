
Num1 = int(input("Enter the first number:",))
Num2 = int(input("Enter the second number",))

Num = Num1 * Num2

Text = str(Num1) + " X " + str(Num2) + " = "

if Num == 0:
    print(Text, Num)
    print("The result is both positive and negative")
elif Num > 0:
    print(Text, Num)
    print("The result is positive")
else:
    print(Text, Num)
    print("The result is negative")


