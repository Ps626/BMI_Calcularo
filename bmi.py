print("Welcome to the BMI Calculator.")
height = float(input("Please enter your hight in meter."))
Weight = float(input("Please enter your weight in Kilogram."))

BMI =round(Weight/height**2)
if BMI < 18.5:
   print(f'your BMI is {BMI}, you are underweight.')
elif BMI < 25:
   print(f'your BMI is {BMI}, you weight is normal.')
else:
    print("work Hard till you get fit.")
    
