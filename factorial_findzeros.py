# num= int(input("Find the number of trailing zeros in the factorial of: \n"))

def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n * factorial (n-1)

# print("The factorial of",num , "is", factorial(num))

def factorialTrailingZeros(n) :
    # fac = factorial(n)
    count = 0
    i=5 
    while (n//i !=0):
        count +=int(n/i)
        i=i*5
    return count

    count = 0
    while(fac%10 == 0) :
        count = count + 1
        fac = fac/10
        return int(count)

# print ("The number of trailing zeros in the factorial of", num , ": ", factorialTrailingZeros(num))
# this gives the number of zeros

if __name__ == '__main__':
    number = int(input("Enter a number: \n"))
   # print("The factorial of", number, "is", factorial(number))
    print("The number of trailing zeros in the factorial of", number,":", factorialTrailingZeros(number))