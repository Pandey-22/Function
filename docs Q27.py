def speed():
    spd=int(input("enter the number"))
    if spd<=70:
        print("OK")
    elif spd>=80 and spd<=100:
        print("Very fast")
    else:
        print("License suspended")
speed()