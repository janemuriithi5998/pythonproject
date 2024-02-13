weight =float(input("Enter your weight:"))
height =float(input("Enter your height in meters:"))

BMI=weight/height
if weight<=18.5:
    print("underweight")
if weight >=19:
    print("normal weight")
if weight >=25-29.9:
    print("overweight")
if BMI>=40:
    print("obesity")

