n=int(input())
if(n%400==0):
    print ("leap")
elif(n%100==0):
    print("not leap")
elif(n%4==0):
    print ("leap")
else:
    print("not leap")
