'''
x = int(5.55)
x+1
x = x+2
y = x*2
x,y = y,x
print(y)
print("-"*20)
print(not (2 + 3 != 5))
print(('car' < 'carpet') and ('dog' > 'dogma'))

r,a,n = 2,10,20
term = a
for i in range(n):
    term = term * r
    if (i > 3):
        break
print (term)

'''
i = 1
while i <= 10:
    if i%2==0:
        continue
    print(i, end=" ")
    i= i+1
