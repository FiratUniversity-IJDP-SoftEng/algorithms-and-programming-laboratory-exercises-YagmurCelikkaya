#Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
while True:
    convert = input("Which conversion would you like to perform.\nIf you write C it means C to F."
                "\nIf you write F it means F to C: ").upper()

    if convert == "C":
        celsius = (int)(input("What is the temperature for Celsius: "))
        f = (celsius * 9/5) + 32
        print(f"{celsius}° celsius is {f:.2f}° fahrenheit")
        break

    elif convert == "F":
        fahrenheit= (int)(input("What is the temperature for Fahrenheit: "))
        c = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}° fahrenheit is {c:.2f}° celsius")
        break
    else :
        print("Invalid input please try again.\n")
