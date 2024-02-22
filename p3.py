w=float(input("Enter weight here "))
h=float(input("Enter height in m here "))
r=w/(h*h)
if r<=18.4:
    print("Underweight")
elif r>=18.5 and r<=24.9:
    print("Normal")
elif r>=25 and r<=29.9:
    print("Overweight")
elif r>=30:
    print ("Obese")
