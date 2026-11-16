def pattern_generator(n):
    for i in range(n):
        for i in range(i+1):
            print("*", end="")
        print()


a=int(input("Enter the number of rows: "))
pattern_generator(a)


