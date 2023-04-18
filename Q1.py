#Question 1
x = input("Give me a number for 'x'")
n = input("Give me a number for 'n'")

x = int(x)
n = int(n)


lambdaFunc = lambda x: 1 if x<2 else x*lambdaFunc(x-1)

list =[]

for i in range(1,x+1):
    list.append((n**i)/lambdaFunc(i))


list.insert(0,1)

total = sum(list)

print(total)



