# n=int(input("Enter number of rows: "))
# r=0
# for i in range(1, n+1):
#     for e in range(1, (n-i)+1):
#         print(end="  ")
#     while r!=(2*i-1):
#         print("* ", end="")
#         r+=1
#     r=0
#     print()
n=int(input("Enter no. of students:"))
n1=int(input("Enter no. of subjects:"))
n2=int(input("Enter no. of marks per subject:"))
for i in range(n):
    t=0
    n3=input("Enter name of the student: ")
    for j in range(n1):
        m=int(input("Enter marks in this subject:"))
        t+=m
    print(n3,"has scored",t,"out of",n1*n2)
