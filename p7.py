# a=list(map(int,input().split(' ')))
# b=int(input("Enter no. of items: "))
# c=0
# odd=[]
# eve=[]
# while c<b:
#     if a[c]%2==0:
#         eve.append(a[c])
#     else:
#         odd.append(a[c])
#     c+=1
# print(odd)
# print(eve)


flag = False
n=int(input())
if n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

    if flag:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")
    

