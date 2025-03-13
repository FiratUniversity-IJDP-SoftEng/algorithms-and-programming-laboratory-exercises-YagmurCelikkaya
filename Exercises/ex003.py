# Your Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
import datetime
now = datetime.datetime.now()
todaysDate = datetime.date.today()
currentTime = now.strftime("%H:%M:%S")
print("Current date:", todaysDate)
print("Current time:",currentTime)
print(f"Current date and time: {todaysDate} {currentTime}")

