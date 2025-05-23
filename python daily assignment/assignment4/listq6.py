# question no 6.
# by using function

def con(s):
    new=" "
    for x in s:
        new += x
    return new
s=['R','o','h','i','t']
print(con(s))

# more easy way with join fun()
def conv(s):
    str1=""
    return(str1.join(s))
print(conv(s))
