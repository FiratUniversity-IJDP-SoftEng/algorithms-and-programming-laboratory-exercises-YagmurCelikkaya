# Your Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
firstNum = int(input("Please enter the first number: "))
secondNum = int(input("Please enter the second number: "))
while True:
    operation = input("Please enter which operation would you like to use for these numbers "
                  " \n(addition - subtraction - multiplication or division) : ").lower()
    if operation == "addition": 
        result = firstNum + secondNum 
        print(f"The result of addition is {result}")
        
    elif operation == "subtraction":  
        result = firstNum -  secondNum      
        print(f"The result of subtraction is {result}")
        
    elif operation == "multiplication":
        result = firstNum * secondNum
        print(f"The result of multiplication is {result}")
        
    elif operation == "division":
        if secondNum == 0:
            print("The result is undefined.")
        else:
            result = firstNum / secondNum
            print(f"The result of division is {result:.2f}")
            
    else: 
        print("invalid input. Please try again\n")
        continue
    
    newOperation = input("Would you like to perform another calculation [yes/ no] : ").lower()
    if newOperation != "yes":
        print("Exitting program.")
        break
