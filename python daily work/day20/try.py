
'''
snacks = set(['burger', 'fries', 'pizza' , 'fries', 'toast', 'peanuts', 'fries', 'pizza'])
print(
'Burger' in snacks
)

s1 = set(['burger', 'fries', 'pizza' , 'fries', 'toast', 'peanuts', 'fries', 'pizza'])
s2 = set(['burger', 'fries', 'burger', 'fries', 'omlette'])

print(s1-s2)
snacks = set(['burger', 'fries', 'pizza' , 'fries', 'toast', 'peanuts', 'fries', 'pizza'])
print(len(snacks))



M = 10
def area(x):
    M = 2
    return M*x*x
def update_M(v):
    global M
    M = v
print (area(7))
update_M(5)
print (area(10))


FACTOR = 10
def f(r):
  return FACTOR * r
def update_FACTOR():
  FACTOR = 16
x =f(5)
update_FACTOR()
y = f(5)
print (x, y)


M = 10
def double(M):

    return M+M
print (double(7), double(M))


#x = cube(sqr(3) - sqr(2))

n = 13
while (n > 1):
    n = n // 2
print(n)

'''
n = 13
sum = 0
while (n > 1):
 n = n//2
 sum = sum + n
print(sum)

