
'''
while number != 0:
        count = count + 1
        sum = sum + number % 10
        number = number // 10
if sum-rem==rem:
    print("Handsome Number ")
else:
    print("Not a Handsome number")

'''

def handsome(number):
    sum=0
    rem=number%10
    while number != 0:
        sum = sum + number % 10
        number = number // 10
    if sum - rem == rem:
        print("Handsome Number ")
    else:
        print("Not a Handsome number")

handsome(1124)
handsome(123)
handsome(2345)