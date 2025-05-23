str1="\"astric\""

print(str1)

str2='hsgdsh' \
     'dsjhgdjsds' \
     'hgdshd' \
     'gdshs' \
     'hdsg' \
     'ghdsgdhs' \
     'dhsfhsdhs' \
     ''
str3="""dgshjghsg
ghdsdshd
hdghsdsh
hsgdhs
hdhsd
hgdshd
"""
print("* "*50)
#String slicing
s='CDAC INDIA'
print("last char:",s[-1])
print("last char:",s[len(s)-1])
print("first char:",s[0])
print("first char:",s[-len(s)])

print(s[2])  #third char->A
print(s[ 0 : 3 ] ) #CDA
print(s[ 1 : -2]) #DAC IND
print(s[3::2]) #CIDA
print(s[::3])#CCNA
print(s[:5:3])#CCNA
print(s[::-2])#ADICD



