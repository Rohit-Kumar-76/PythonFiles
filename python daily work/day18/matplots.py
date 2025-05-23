from pylab import *
'''
x =[0,1,2]
y =[0,1,2]
plot(x,y,label="line graph ")
title("line graph")
show()
'''
'''
x=[0,0,2,2,0,2,3,2.5,2.5,3,3.5,3.5,3,4,4,4,5,5,5,5.5,7,6,6]
y=[0,4,4,2,2,0,0,1,2.5,3.5,2.5,1,0,0,4,2,2,4,0,0,0,0,4]
plot(x,y,'.:r')
#plot(x,y,'.-') # ploting with a dot
#plot(x,y,'.--')# ploting with dash line
#legend()
title("line graph")
#title("Stem Graph")
show()
'''
#print("-------------")
x=[0,0,2,2,0,2,3,2.5,2.5,3,3.5,3.5,3,4,4,4,5,5,5,5.5,7,6,6]
y=[0,4,4,2,2,0,0,1,2.5,3.5,2.5,1,0,0,4,2,2,4,0,0,0,0,4]
'''
#plot(x,y,'.:r')
stem(x,y)
#plot(x,y,'.-') # ploting with a dot
#plot(x,y,'.--')# ploting with dash line
#legend()
#title("line graph")
title("Stem Graph")
show()

pie(x)
show()
bar(x,y,label="score ")
show()
'''
'''
errorbar(x,y)
show()
scatter(x,y)
show()
'''
'''
t =arange(-250,251)*2*pi/500
x=sin(t)
y=cos(t)
#print(x)
#print(y)

plot(t,x,label="sin")
plot(t,y,label="cos")
plot(x,y,label="circle")
legend()
axis('equal')
show()
'''

t = arange(50)*2*pi/50
x=sin(t)
subplot(131)# first value no of row,second value no of coloum ,third value positions
stem(t,x)
subplot(133)
step(t,x)
subplot(132)
stem(t,x)
axis("equal")
show()