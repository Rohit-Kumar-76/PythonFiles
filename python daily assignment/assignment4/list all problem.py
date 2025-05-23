#question no 1.

lt=[1,2,3,4]
print(sum(lt))

# question no 2.
#by function calling
def mullist(mylist):
    result=1
    for x in mylist:
        result = result * x
    return result
print(mullist(lt))

# question  no 3.


def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba','1221']))


# question no 4.
# by using loop
a=[1,2,4,5,6,7,7,9,6,3,2,10,11]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)

# by using function
def remove(a):
    fn=[]
    for x in a:
        if x not in fn:
            fn.append(x)
    return fn
a=[1,2,3,4,5,6,7,7,6,9,8,1]
print(remove(a))

# question no 5.

mylist1=[10,20,30,40,50,60,70,80,90,100] #list with some initial data
print(mylist1)
if not mylist1:
    print('Empty list')
else:
    print('List is not Empty\n',mylist1)


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

# question no 7.
list1=["rohit","mehta","has",9000000]
list2=["mony","and",2,"car"]
list1=list1+list2
#list1.append(list2)
print(list1)
