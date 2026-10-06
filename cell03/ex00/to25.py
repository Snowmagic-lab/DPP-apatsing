n = int(input())
max = 25

if n < 25:
    k = n
    while k < 26:
        print("Inside the loop, my variable is " + str(k))
        k = k + 1
else:
    print("error")