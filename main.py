def temp():
    f=float(input("Temperature (degrees F):"))
    s=float(input("Wind speed (MPH):"))
    index=35.74+(0.6215*f)-35.75*(s**0.16)+0.4275*f*(s**0.16)
    print(f"Wind Chill Temperature Index:{index}")
temp()    