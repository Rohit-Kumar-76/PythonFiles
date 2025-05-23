from pylab import *
#matplotlib
#x=[0,1,2,3]
#y=[0,1,2,3]
'''
x=[0,1,2,0]
y=[0,1,0,0]
plot(x, y,label="Triangle")  # basic plotting
legend()
title("Line Graph")  #to set title
show()  #to display the graph
'''

x = [0,0, 2,2,0]
y = [0,1, 1,0,0]
#plot(x, y)  # basic plotting
#show()

#plot(x, y, '.-')  # basic plotting with dot
#show()

#plot(x, y, '.--')  # basic plotting with dashed line
#show()

#plot(x, y, '.:')  # basic plotting with dotted line
#show()

#plot(x, y, '.:g')  # basic plotting with dotted line and
                    # color(r,g,b,k)
#show()
#plot(x,y, '-D')  # diamond shape
#axis('equal')
#show()



x=[1,2,3,4,5,6,7,8,9,10]
y=[10,15,30,36,45,51,60,60,80,95]
'''
stem(x, y)
title("Stem Graph")
show()

pie(x)
show()
bar(x,y,label="score over by over")
legend()
show()

errorbar(x,y)
show()
scatter(x,y)
show()
'''



'''
#sin/cos graph
'''
'''
t = arange(-250, 251)*2*pi/500
#print(t)
x=sin(t)
y=cos(t)
#print(x)
#print(y)
plot(t, x, label="sin")
legend()
show()
plot(t, y, label="cos")
legend()
show()
plot(x, y, label="circle")
legend() #to display label text
axis('equal')
show()
'''


t = arange(50)*2*pi/50
x=sin(t)
subplot(131)
stem(t, x)
subplot(133)
step(t, x)
subplot(132)
stem(t, x)
axis("equal")
show()

