#hra and da and total salary
s=int(input("tell me your sellary: "))
if s<=2000:
       hra=s/100*(20)
       da=s/100*(10)
       t=float(hra+da+s)
       print("total=", t)
elif s>2000 & s<=5000:
       hra = (s / 100) * (30)
       da = (s / 100) * (20)
       t = hra + da + s
       print("total=", t)

elif s>5000 &  s <= 10000:
       hra = s / 100 * (400)
       da = s / 100 * (30)
       t = float(hra + da + s)
       print("total=", t)
elif s > 10000 :
       hra = s / 100 * (50)
       da = s / 100 * (50)
       t=float(hra+da+s)
       print("total=",t)