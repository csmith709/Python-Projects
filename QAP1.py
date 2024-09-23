# Edsel Rental Company sevice info and charges
# Written: Sept 12, 2023
# Written by:Charity Smith

# Define Constants
CostPerDay = 55.00
MilaegePerKm = 0.24
InsurancePerDay = 14.00
HST = 0.15

#Inputs - Customer name, customer phone number, number of days rented (int), odometer start number (int), odometer end number (int)
CustName = input("Enter customer name: ")
PhoneNum = input("Enter customer phone number: ")
DaysRented = int(input("Enter the number of days rented: "))
OdometerStart = int(input("Enter the starting Odometer 5 digit number: "))
OdometerEnd = int(input("Enter the ending Odometer 5 digit number: "))

# Calculations - Total Km (use Odometer numbers), determine the rental cost, dtermine the mileage cost, determine the insurance cost, calculate a 10% discount off rental cost nad 25% off mileage, calculate the total rental cost, calculate the HST, calculate the rental cost, total invoice (rental cost + HST)
TotalKm = OdometerEnd - OdometerStart
RentalCost = DaysRented*CostPerDay
MileageCost = TotalKm*MilaegePerKm
InsuranceCost = DaysRented*InsurancePerDay
Dis10 = RentalCost*0.1
Dis25 = MileageCost*.25
TotalDis = Dis10 + Dis25
TotalRental = RentalCost + MileageCost + InsuranceCost - TotalDis
Taxes = TotalRental*HST
FinalInvoice = TotalRental+HST

#Display all input values and all calculated values (discounts as 1 value)
print("Customer name: ",CustName)
print("Customer phone number: ",PhoneNum)
print("Number of days rented: ",DaysRented)
print("Odometer starting 5 digits: ",OdometerStart)
print("Odometer ending 5 digits: ",OdometerEnd)
print("Total number of Km traveled: ",TotalKm)
print("Rental cost per day: ",RentalCost)
print("Total Mileage cost: ",MileageCost)
print("Total insurance cost: ",InsuranceCost)
print("Total discounts: ",TotalDis)
print("Total rental cost: ",TotalRental)
print("Total taxes: ",Taxes)
print("Final Invoice: ",FinalInvoice)