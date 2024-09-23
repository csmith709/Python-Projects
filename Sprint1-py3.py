#Written by Charity Smith
#Started on 22 Oct
#Finished 23 Oct
#Group 6

#Cool Stuff with Strings and Dates
#Fizz Blizz Employee data

#imports
import datetime
CurDate = datetime.datetime.now()
import random
from datetime import date
Today = date.today()
Today = (Today.strftime("%Y-%m-%d"))

#constants
RETIREMENT = 65

#variables
Counter = random.randint(100, 999)

#inputs
#first & last name, phone #, date, start date, birthdate
FirstName = input("Enter the employee first name: ").title()
LastName = input("Enter the employee last name: ").title()
PhoneNum = input("Enter the employee phone number (###-###-####): ")
EmpStartDatestr = input("Enter the employee start date (YYYY-MM-DD): ")
EmpBirthdaystr = input("Enter the employee birth date (YYYY-MM-DD): ")
EmpStartDate = datetime.datetime.strptime(EmpStartDatestr, "%Y-%m-%d")
EmpBirthday = datetime.datetime.strptime(EmpBirthdaystr, "%Y-%m-%d")

#"calculations" and formatting
#Use inputs to create ID, Username, Password. Determine length of employment , retirement day, years til retirement, how long until birthday.

#Use inputs to create ID, Username, Password
EmpID = EmpStartDatestr[0:4] + FirstName[0] + LastName.upper()[-1] + "-" + EmpBirthdaystr[2:4] + str(Counter)

UserName = FirstName[0] + LastName + str(Counter)

Password = str(Counter) + EmpBirthdaystr[4:] + EmpStartDatestr[2:4] + "-" + LastName[0:1] + FirstName.upper()[-2]


#breaking down dates for calculations
CurDateDsp = (CurDate.strftime("%Y-%m-%d"))
CurYear = CurDate.year
CurMonth = CurDate.month
CurDay = CurDate.day
BirthYear = EmpBirthday.year
BirthMonth = EmpBirthday.month
BirthDay = EmpBirthday.day

#how long with company
CompanyTime = CurDate-EmpStartDate
CompanyTimeDsp = str(CompanyTime)[0:5] + "days"


#how long til birthday
NextBirthday = date(CurYear,BirthMonth,BirthDay)
if NextBirthday < CurDate.date():
    NextBirthday = date(CurYear+1, BirthMonth, BirthDay)
DaysTil = NextBirthday - CurDate.date()
DaysTilDsp = (str(DaysTil)[0:3] + " days")


#retirement date & time left
RetireDate = BirthYear + 65
print(RetireDate)
RetireTime = RetireDate - CurYear
print(RetireTime)

#print inputs and "calculations"
print(f"")
print(f"        FizzBlizz Employee Records")
print(f"------------------------------------------")
print(f"")
print(f"First Name:               {FirstName:<18s}")
print(f"Last Name:                {LastName:<12s}")
print(f"Phone Number:             {PhoneNum:<12s}")
print(f"")
print(f"Employee Start Date:      {str(EmpStartDate)[0:10]}")
print(f"Employee birthday:        {str(EmpBirthday)[0:10]}")
print(f"Current Date:             {CurDateDsp}")
print(f"")
print(f"------------------------------------------")
print(f"")
print(f"Employee ID:              {EmpID}")
print(f"Employee Username:        {UserName}")
print(f"Employee Passowrd:        {Password}")
print(f"")
print(f"------------------------------------------")
print(f"")
print(f"Time With Company:        {CompanyTimeDsp}")
print(f"Time Until Birthday:      {DaysTilDsp}")
print(f"Retirement Date:          {RetireDate}")
print(f"Years Until Retirement:   {RetireTime}")
print(f"")
