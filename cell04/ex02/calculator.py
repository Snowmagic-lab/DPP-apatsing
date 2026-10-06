Num1 = int(input("Give me the first number : ",))
Num2 = int(input("Give me the second number : ",))

def Result(x,y):
    print(str(x) + " + " + str(y) + " = " + str(x + y))
    print(str(x) + " - " + str(y) + " = " + str(x - y))
    print(str(x) + " / " + str(y) + " = " + str(x / y))
    print(str(x) + " * " + str(y) + " = " + str(x * y))

print("Thank you")

Result(Num1,Num2)