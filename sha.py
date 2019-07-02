v=int(input())
s=0
t=v
while t>0:
 digit = t%10
 s +=digit ** 3
 t //=10
if v==s:
 print("yes")
else:
 print("no")
