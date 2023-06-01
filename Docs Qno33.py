def body(weight,height):
    height2=height/100
    bmi=weight/height2**2
    if bmi<=30:
        return "Obese"
    elif bmi<=18.5:
        return "Underweight"
    elif bmi<=25.0:
        return "Normal"
    elif bmi>30.0:
        return "Overweight"           
a=int(input("enter your weight:"))
b=int(input("enter your height in cm:"))
print(body(a,b))