n=int(input("Enter your age here: "))
if n<60 and n>18:
     print("Adult")
else:
     if n>60:
         print("Senior citizen")
     else:
         if n<=13:
            if n>3:
                print("Kid")
            else:
                print("Toddler")
         else:
             print("Teen")