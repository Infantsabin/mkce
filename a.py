a=int(input())
for y in range(0,a):
    num=input()
    count=0
    for t in range(0,len(num)):
        count=count+int(num[t])
    print (count)
