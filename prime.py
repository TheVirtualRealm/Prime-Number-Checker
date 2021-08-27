def PrimeNumChecker(a):

    if a > 0:

        for j in range(2, int(a/2) + 1):
            if (a % j) == 0:
                print(a, "is not considered a prime number")
                break

            else:
                print(a, "Is a prime number")

    

a = int(input("Enter a number you would like me to check: "))

PrimeNumChecker(a)
