x=input("enetr a Alphabet or digit or spaciel char")
if x[0].isalpha():
    print("\n"+x[0],"is A Alphabet.")
elif x[0].isdigit():
      print("\n"+x[0],"is a digit.")
else :
    print("\n"+x[0],"is a special character.")