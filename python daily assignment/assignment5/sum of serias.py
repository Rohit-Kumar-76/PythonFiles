

# normal approach using loop
n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))


#By using function

def sums(num):
    res = 0
    fact = 1

    for i in range(1, num + 1):
        fact *= i
        res = res + (i / fact)

    return res


n = int(input("Enter the number of terms: "))

print("Sum: ", sums(n))