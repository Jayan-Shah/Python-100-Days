height=input("Enter your height in m:")
weight=input("Enter your weight in kg:")
height=float(height) 
weight=float(weight)
BMI=round(weight/(height**2))
print(BMI) # Final answer in whole number 
if BMI < 18.5 :
    print("UnderWeight")
elif BMI < 25 :
    print("Normal Weight")
elif BMI < 30:
    print("Over-Weight")
elif BMI < 35 :
    print("Obese")
else:
    print("Clinically Obese")
