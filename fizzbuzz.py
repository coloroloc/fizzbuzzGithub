numList = list(range(1, 101))

for x in numList:

    if (x%3==0 and x%5==0):
        print("fizzbuzz")

    elif (x%3==0):
        print("fizz")

    elif (x%5==0):
        print("buzz")
        
    else:
        print(x)
