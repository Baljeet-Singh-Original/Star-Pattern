n = int(input("Enter number turns you want to print Star pattern >>> "))
f = 1 
i = 1
k = 0
while i <= 2 * n - 1:
    if (i < n - k):
        print(" ", end = "")
    else:
        if (f):
            print("*", end = "")
        else:
            print(" ", end = "")
        f = 1 - f
    if (i == n + k):
        k += 1
        print()
        if (i == 2 * n - 1):
            break
        i = 0
        f = 1
    i += 1
    
    
    