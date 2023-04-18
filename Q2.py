while(True):
    n = input("Give me a number for 'n':\n")
    n = int(n)
    if n != 0:
        break
sum = 0
def function(n):
    if (n == 0):
        return
    global sum
    x = ((-1)**(n+1)/n)
    sum += x
    function(n-1)

function(n)

print(sum)
