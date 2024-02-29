a=list(map(int,input().split(' ')))
b=int(input("Enter no. of items: "))
c=0
odd=[]
eve=[]
while c<b:
    if a[c]%2==0:
        eve.append(a[c])
    else:
        odd.append(a[c])
    c+=1
print(odd)
print(eve)


    

