one=input()
for i in range(0,len(one)):
   if(one[i].isalpha() and one[i].isdigit()):
    print("No")
else:
  print("Yes")
