def fizzbuzz(numList):
    
    for x in numList:

        fb =""
        
        if (x%3!=0 and x%5!=0):
            fb = str(x)

        if (x%3==0):
            fb ="fizz"

        if (x%5==0):
            fb += "buzz"            

        print(fb)


numRange = list(range(1, 101))

fizzbuzz(numRange)
