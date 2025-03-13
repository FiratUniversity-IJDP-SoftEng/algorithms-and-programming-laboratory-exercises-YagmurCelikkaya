# Your Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
numList = [2,5,4,8,7,1,3,9,10,6]
print("original list is:\n" ,numList)

print("reversed list: ")
reversedList = numList[::-1] 
print(reversedList)

print("adding numbers")
addNumList =[12,11,13]
reversedList.extend(addNumList)
print(reversedList)

length = len(reversedList)
print(f"The length of the list is {length}")

print("removing numbers")
reversedList.pop(0)
reversedList.pop(-1)
print(reversedList)

length = len(reversedList)
for i in range(length - 1):  
    shortest = i     
    for j in range(i + 1, length):  
        if reversedList[j] < reversedList[shortest]:
            shortest = j  
    
    reversedList[i], reversedList[shortest] = reversedList[shortest], reversedList[i]
print("Sorted list: \n",reversedList)

newList = []
for num in reversedList:
    if num % 2 == 0:
        newList.append(num)
print("The new list is:\n",newList)


