# Your Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
n = (int)(input("Please enter a number: "))

for i in range(n):
    for j in range(n - i - 1):        
        print(" ",end="")
    for j in range(2*i + 1):
        print("*",end="")
    print()

