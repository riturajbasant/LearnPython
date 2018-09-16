def check(a):
    #x = a%2
    if a % 2 == 0:

        return print("you have input even number ")
    
    elif a%4==0:
        print("You have entrered multiple of 4")
        
    else:
        print("You have intered ODD number ")

a = int(input("Please enter number "))
check(a)        
