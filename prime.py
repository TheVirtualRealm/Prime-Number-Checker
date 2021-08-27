def PrimeNumChecker(a):

    if a > 0:

        # I looked up a solution as to why my code repeats itself and was unable to figure it out
        # I was able to figure out why the code was telling me that The number was both prime and not prime on my own
        # I Looked up how to use code to calculate whether or not a number is prime, i also needed to look up what a prime number was lol
        
       
        def rounds(b):
            
            while rounds == 0:
                
                for j in range(2, int(a/2) + 1):
                    if (a % j) == 0:
                        print(a, "is not considered a prime number")
                # break
                    else:
                        print(a, "Is a prime number")
                

                PrimeNumChecker(a)
            

a = int(input("Enter a number you would like me to check: "))
    
b + 1
