def fizzBuzz():
    num = int(input("Enter the number to fizzbuzz: "))
    for i in range(1, num + 1):
        if not(i%3 == 0) and not(i%5 == 0):
            print(i)
        else:
            if (i%3 == 0):
                print("fizz", end = '')
            if (i%5 == 0):
                print("buzz", end = '')
            print()    

fizzBuzz()
