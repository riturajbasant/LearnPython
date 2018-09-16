

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Enter number"))

new_num = []

for i in a:
    if i <= num:
        new_num.append(i)

print(new_num)        
