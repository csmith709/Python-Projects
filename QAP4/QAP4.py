#OneStopInsuranceCompany
#Witten by CharitySmith
#Written on 17 Nov 2023 - 28 Nov 2023
#git@github.com:csmith709/PythonQAP4.git

#imports
import datetime
import FormatValues as FV
from dateutil import relativedelta
import re

#constants
HST_RATE = .15
PROCESS_FEE_MONTH = 39.99
PROV_LIST = ["NL", "NS", "PE", "NB"]
PAYOPT_LIST = ["F", "M", "D"]
CLAIM_NUM = 1994
LIABILITY_COVERAGE = 130.00
BASIC_PREMIUM = 869.00
ADDCARDISC_RATE = .25
GLASS_COVERAGE = 86.00
LOANER_CAR = 58.00
CUR_DATE = datetime.datetime.now()

#initializing lists
ClaimAmtLst = []
ClaimDateLst = []
ClaimNumLst = []

#functions
#in Program Functions
#Added funtion
while True:

    def NextPayment(CURDATE):
        #calculate payment date as the first of the next month
        CurYear = CURDATE.year
        CurMonth = CURDATE.month
        CurDay = CURDATE.day

        if CurDay >= 25:
            CurMonth += 1

            if CurMonth == 13:
                CurYear += 1
                CurMonth = 1
        PayDate = datetime.datetime(CurYear, CurMonth, 1)
        return PayDate
    PayDate = NextPayment(CUR_DATE)
    break


def PNumS(PhoneStr):
    digits = re.sub(r'\D', '', PhoneStr)

    if len(digits) != 10:
        return "Invalid Phone Number"
    
    PhoneFormat = f'{digits[0:3]}-{digits[3:6]}-{digits[6:]}'
    return PhoneFormat


#while True
#inputs -  Customer first and last names, address, phone number

while True:
    while True:
        CFirstName = input("Enter the customer first name: ").title()
        if CFirstName == "":
            print("Customer first name can not be left blank. Please try again.")
        else:
            break
    while True:
        CLastName = input("Enter the customer last name: ").title()
        if CLastName == "":
            print("Customer last name can not be left blank. Please try again.")
        else:
            break
    while True:
        CStAddress = input("Enter the customer street address: ").title()
        if CStAddress == "":
            print("Customer street address can not be left blank. Please try again.")
        else:
            break
    while True:
        CCity = input("Enter the customer's city of residence: ").title()
        if CCity == "":
            print("Customer's city of residence can not be left blank. Please try again.")
        else:
            break
    while True:
        CProv = input("Enter the customer province of residence (XX): ").upper()
        if CProv == "":
            print("Error - Can not be left blank. Please Try again.")
        elif len(CProv) != 2:
            print("Province must contain 2 numbers only. Please Try again.")
        elif CProv not in PROV_LIST:
            print("Not a valid province. Please Try again.")
        else:
            break
    while True:
        CPostal = input("Enter the customer postal code (X#X#X#): ").upper()
        if CPostal == "":
            print("Customer postal code can not be left blank. Please try again.")
        elif len(CPostal) != 6:
            print("Customer postal code must contain 6 characters. Please try again.")
        elif CPostal [1].isdigit() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")
        elif CPostal [3].isdigit() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")
        elif CPostal [5].isdigit() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")
        elif CPostal [0].isalpha() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")
        elif CPostal [2].isalpha() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")
        elif CPostal [4].isalpha() == False:
            print("Postal code must contain a 'letter, number, letter, number, letter, number' pattern.")   
        else:
            break
    while True:
        CPhoneNum = input("Enter customer phone number (##########): ")
        if CPhoneNum.isdigit() == False:
            print("Phone number must only include numbers. Please try again.")
        elif CPhoneNum == "":
            print("Phone number cannot be left blank. Please try again.")
        elif len(CPhoneNum) != 10:
            print("Phone number must be 10 characters long. Please try again.")
        else:
            formatted_phone = PNumS(CPhoneNum)
            break

    #input - # cars being insured, liability option, glass coverage, loaner car
    while True:
        try:
            NumCars = int(input("Enter the number of cars to insure: "))
        except:
            print("Number of cars must only include numbers. Please try again.")
        
        if NumCars == "":
            print("Number of cars can not be left blank. Please try again.")
        else:
            break
    while True:
        LiabilOpt = input("Would customer like extra liability up to $1,000,000? (Y or N): ").upper()
        if LiabilOpt == "":
            print("Liability option can not be left blank. Please try again.")
        elif LiabilOpt == "Y":
            LiabilCharge = LIABILITY_COVERAGE = 130.00
            break
        elif LiabilOpt != "Y" and LiabilOpt != "N":
            print("Liability option must contain 'Y' or 'N'. Please try again.")
        elif LiabilOpt == "N":
            LiabilCharge = 0
            break
    while True:
        GlassOpt = input("Would customer like glass coverage? (Y or N): ").upper()
        if GlassOpt == "":
            print("Glass coverage option can not be left blank. Please try again.")
        elif GlassOpt == "Y":
            GlassCharge = GLASS_COVERAGE
            break
        elif GlassOpt == "N":
            GlassCharge = 0
            break
        else:
            print("Glass coverage option must contain 'Y' or 'N'. Please try again.")
    
    while True:
        LoanerOpt = input("Would customer like loaner car coverage? (Y or N): ").upper()
        if LoanerOpt == "":
            print("Loaner car option can not be left blank. Please try again.")
        elif LoanerOpt == "Y":
            LoanerCharge = LOANER_CAR
            break
        elif LoanerOpt == "N":
            LoanerCharge = 0
            break
        else:
            print("Loaner car option must contain 'Y' or 'N'. Please try again.")
    
#loop and store in list (like lesson 26) - Claim Number, Date, Amount

    while True:
        ClaimDateStr = input("Enter the date of the claim: (YYYY-MM-DD): (hit ENTER/RETURN to end) ").upper()
        if ClaimDateStr == "":
            break
      
        ClaimAmt = float(input("Enter the total claim amount: "))
        CLAIM_NUM += 1

    #append
        ClaimNumLst.append(CLAIM_NUM)
        ClaimAmtLst.append(ClaimAmt)
        ClaimDateLst.append(ClaimDateStr)

#calculations
    NumAddCar = NumCars - 1
    AddCarCharge = BASIC_PREMIUM * NumAddCar
    AddCarDis = AddCarCharge * ADDCARDISC_RATE
    AddCarTotal = AddCarCharge - AddCarDis

    TotalExCost = LiabilCharge + GlassCharge + LoanerCharge + AddCarTotal
    Total = BASIC_PREMIUM + TotalExCost
    Taxes = Total * HST_RATE
    TotalCost = Total + Taxes

    #input - pay full or month or down pay, if downpay ender amount, enter date, cost of all prev claims. Press ENTER to finish
    
    while True: #had to move to calculations to use TotatCost for D
        PayOption = input("Would customer like to pay in full (F), pay monthly (M) or down pay (D)?: ").upper()
        if PayOption == "":
            print("Payment option can not be left blank. Please try again.")
        elif PayOption not in PAYOPT_LIST:
            print("Must enter 'F', 'M', or 'D'. Please try again.")
        if PayOption == "M":
            MonthlyCost = (TotalCost + PROCESS_FEE_MONTH) / 8
            DPAmt = 0
            break
        if PayOption == "F":
            MonthlyCost = 0
            DPAmt = 0
            break
        if PayOption == "D":
            try:
                DPAmt = float(input("Enter the down payment amount: "))
            except:
                print("Down payment amount must only include numbers. Please try again.")
            if DPAmt == "":
                print("Down payment amount can not be left blank. Please try again.")
            else:
                MonthlyCost = (TotalCost - DPAmt + PROCESS_FEE_MONTH) / 8
                break
        if PayOption is PAYOPT_LIST:  
            break
# display formatting
    CustName = CFirstName + " " + CLastName
    CAddLine = CCity + ", " + CProv + " " + CPostal

    # CPhoneNum = CPhoneNum [0:3] + "-" + CPhoneNum[3:7] + "-" + CPhoneNum[7:]
    

    print(f"")
    print(f"                    One Stop Insurance Company")
    print(f"")
    print(f"----------------------------------------------------------------------")
    print(f"                                                            {FV.FDateS(CUR_DATE):>10s}")
    print(f"Customer Name:       {CustName:<40s}")
    print(f"Customer Address:    {CStAddress:<37s}")
    print(f"                     {CAddLine:<37s}") 
    print(f"Customer Phone #:    {formatted_phone:<12s}")
    print(f"----------------------------------------------------------------------")
    print(f"")
    print(f"Number of cars being insured: {NumCars:<2d}")
    print(f"Number of additional cars beind insured: {NumAddCar:<2d}")
    print(f"")
    print(f"             Basic Premium:                      {FV.FDollar2(BASIC_PREMIUM):>12s}")
    print(f"             Additional Car Cost:                {FV.FDollar2(AddCarCharge):>12s}")
    print(f"             Additional Car Discount:            {FV.FDollar2(AddCarDis):>12s}")
    print(f"             Additional Car Total Cost:          {FV.FDollar2(AddCarTotal):>12s}")
    print(f"             Optional glass coverage:            {FV.FDollar2(GlassCharge):>12s}")
    print(f"             Liability Coverage:                 {FV.FDollar2(LiabilCharge):>12s}")
    print(f"             Loaner Car coverage                 {FV.FDollar2(LoanerCharge):>12s}")
    print(f"                                                 ------------")
    print(f"                                         Total:  {FV.FDollar2(Total):>12s}")
    print(f"                                         Taxes:  {FV.FDollar2(Taxes):>12s}")
    print(f"                                                 ------------")
    print(f"                                    Total Cost:  {FV.FDollar2(TotalCost):>12s}")
    print(f"")
    print(f"----------------------------------------------------------------------")
    print(f"")
    print(f"Payment Options: Full, Monthly, Down payment: ")
    print(f"")
    print(f"           Payment in Full: One Time Payment, no monthly fees")
    print(f"           Down payment amount:                  {FV.FDollar2(DPAmt):>12s}")
    print(f"           Process Fee:                          {FV.FDollar2(PROCESS_FEE_MONTH):>12s}")
    print(f"           Monthly Payment (Fees included):      {FV.FDollar2(MonthlyCost):>12s}")
    print(f"          ----------------------------------------------------")
    print(f"           Next Payment date (If applicable):      {FV.FDateS(PayDate):>10s}")
    print(f"")
    print(f"----------------------------------------------------------------------")
    print(f"")
    print(f"Previous Claims:")
    print(f"")
    print(f"    Claim Number:        Claim Date:           Claim Amount:")
    print(f"    -----------------------------------------------------------")
    for i in range(0, len(ClaimNumLst)):
        print(f"    {ClaimNumLst[i]}                 {ClaimDateLst[i]}            ${ClaimAmtLst[i]}")

    print(f"")
    print(f"----------------------------------------------------------------------")
    print(f"")
    print(f"        Thanks for using One Stop Insurance Company")
    print(f"                    Have a nice day.")
    print(f"")
    end = input ("  To end this program write END. To continue press enter: ").upper()
    if end == "END":
        print(f"        Thanks for using One Stop Insurance Company")
        print(f"")
        break
    if end == "":
        print(f"")
        continue
    else:
        print("Invalid entry, Please try again.")