number = input("How many lines must be generated? ")
for x in range(0, number):
    if x != number-1 :
        print("*" * (number - int(x) - 1) + " " * x + "*")
    else :
        print("*" * x + "*")