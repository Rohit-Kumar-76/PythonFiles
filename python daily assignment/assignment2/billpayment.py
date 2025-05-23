
customer=int(input("Enter customer Id"))
if customer==1:
     print("Rohit mehta")
     unit=int(input("enetr unit consumption"))
     if unit<199:
              tu=unit*4.20
              if tu>=800:
                  rs = tu + (tu / 100) * 18

                  print(rs,"Rs")
                  print("minimum bill payment is 200rs")
              else:
                  print(tu,"RS")
     elif unit>=200 and unit <400:
            tu=unit*5.50
            if tu >= 800:
                rs = tu + (tu / 100) * 18

                print(rs,"rs")
                print("minimum bill payment is 200rs")
            else:

                print(tu,"rs")
     elif unit>=400 and unit <600:
           tu=unit*6.80
           if tu >= 800:
                rs = tu + (tu / 100) * 18

                print(rs,"rs")
                print("minimum bill payment is 200rs")
           else:

                print(tu,"rs")

     elif unit>=600 :
            tu=unit*8.0
            if tu >= 800:
               rs = tu + (tu / 100) * 18
               print(rs,"rs")
               print("minimum bill payment is 200rs")
            else:
               print(tu,"rs")
elif customer==2:
     print("Ajit mehta")
     unit=int(input("enetr unit consumption:."))
     if unit<199:
              tu=unit*4.20
              if tu>=800:
                  rs = tu + (tu / 100) * 18
                  print(rs,"rs")
                  print("minimum bill payment is 200rs")
              else:
                  print(tu,"rs")
     elif unit>=200 and unit <400:
            tu=unit*5.50
            if tu >= 800:
                rs = tu +(tu/100)*18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
            else:
                print(tu,"rs")
     elif unit>=400 and unit <600:
           tu=unit*6.80
           if tu >= 800:
                rs = tu + (tu / 100) * 18
                print("BIll=", rs)
                print("minimum bill payment is 200rs")
           else:
                print(tu,"rs")

     elif unit>=600 :
            tu=unit*8.0
            if tu >= 800:
               rs = tu + (tu / 100) * 18
               print(rs,"rs")
               print("minimum bill payment is 200rs")
            else:
               print(tu,"rs")

elif customer==3:
     print("Ankush mehta")
     unit=int(input("Enetr unit consumption:."))
     if unit<199:
              tu=unit*4.20
              if tu>=800:
                  rs = tu + (tu / 100) * 18
                  print(rs,"rs")
                  print("minimum bill payment is 200rs")
              else:
                  print(tu,"rs")
     elif unit>=200 and unit <400:
            tu=unit*5.50
            if tu >= 800:
                rs = tu + (tu / 100) * 18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
            else:
                print(tu,"rs")
     elif unit>=400 and unit <600:
           tu=unit*6.80
           if tu >= 800:
                rs = tu + (tu / 100) * 18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
           else:
                print(tu,"rs")

     elif unit>=600 :
            tu=unit*8.0
            if tu >= 800:
               rs = tu + (tu / 100) * 18
               print(rs,"rs")
               print("minimum bill payment is 200rs")
            else:
               print(tu,"rs")



elif customer==4:
     print("aman mehta")
     unit=int(input("Enetr unit consumption:-"))
     if unit<199:
              tu=unit*4.20
              if tu>=800:
                  rs = tu + (tu / 100) * 18
                  print(rs,"rs")
                  print("minimum bill payment is 200rs")
              else:
                  print(tu,"rs")
     elif unit>=200 and unit <400:
            tu=unit*5.50
            if tu >= 800:
                rs = tu +(tu/100)*18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
            else:
                print(tu,"rs")
     elif unit>=400 and unit <600:
           tu=unit*6.80
           if tu >= 800:
                rs = tu + (tu / 100) * 18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
           else:
                print(tu,"rs")

     elif unit>=600 :
            tu=unit*8.0
            if tu >= 800:
               rs = tu + (tu / 100) * 18
               print(rs,"rs")
               print("minimum bill payment is 200rs")
            else:
               print(tu,"rs")

elif customer==5:
     print("sameer mehta")
     unit=int(input("Enetr unit consumption:-"))
     if unit<199:
              tu=unit*4.20
              if tu>=800:
                  rs = tu + (tu / 100) * 18
                  print(rs,"rs")
                  print("minimum bill payment is 200rs")
              else:
                  print(tu,"rs")
     elif unit>=200 and unit <400:
            tu=unit*5.50
            if tu >= 800:
                rs = tu + (tu / 100) * 18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
            else:
                print(tu,"rs")
     elif unit>=400 and unit <600:
           tu=unit*6.80
           if tu >= 800:
                rs = tu + (tu / 100) * 18
                print(rs,"rs")
                print("minimum bill payment is 200rs")
           else:
                print(tu,"rs")

     elif unit>=600 :
            tu=unit*8.0
            if tu >= 800:
               rs = tu + (tu / 100) * 18
               print(rs,"rs")
               print("minimum bill payment is 200rs")
            else:
               print(tu,"rs")


else :
    print("this not valid")


