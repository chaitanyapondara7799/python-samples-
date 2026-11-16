def pattern_generator(n):
    for i in range(n):
        for i in range(i+1):
            print("*", end="")
        print()


a=int(input("Enter the number of rows: "))
pattern_generator(a)


#  prime number function
def is_prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

m=int(input("Enter a number to check if it is prime: "))
print(f"{m} is prime: {is_prime(m)}")