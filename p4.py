flag=False
num=int(input())
if num==1:
     print(flag)
elif num>1:
     a=1
     while a < num-1:
        a+=1
        if num%a==0:
            
            flag=True
if flag==True:
    print("Not a prime number")
else:
    print("Prime number")
    
        
     