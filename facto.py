def factorial(a):
     x = 1
     while(a>=1):
          x = x*a
          a = a-1

     
     return x

a = int(input("Enter Number "))

print(factorial(a))
