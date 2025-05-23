def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

str1=input("Enter a string :")
lenght=len(str1)
if lenght > 2:
     if str1[-3:] == 'ing':
         x=str1.replace('ing','ly')
         print(x)
     else:
         str1 = str1 +'ing'
         print(str1)

else:
    print(str1)
