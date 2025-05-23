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