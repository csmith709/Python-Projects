#Honest  Harry Used Car Lot
#Written by Charity Smith
#Started on October 11, 2023
#Finished on October .., 2023

#imports
import datetime
CurDate = datetime.datetime.now() #grabs current system date

#define constants (CAPITALIZE)
HST_RATE = 0.15
LICENCE_FEE_UNDER5K = 75.00
LICENCE_FEE_OVER5K = 165.00
TRANSFER_RATE_UNDER20K = .01
TRANSFER_RATE_OVER20K = .016
FINANCE_FEE_RATE = 39.99

#gather inputs
while True:
    while True:
        CustFName = input("Enter customer first name: (End to quit): ").title()
        if CustFName == "":
            print("Customer first name can not be left blank. Please try again.")
        else:
            break
    if CustFName.upper() == "END":
        print("Thank you for using our services, have a nice day")
        break
    while True:
        CustLName = input("Enter customer last name: ").title()
        if CustLName == "":
            print("Customer last name can not be left blank. Please try again")
        else:
            break
    while True:
        PhoneNum = input("Enter customer phone number (##########): ")
        if PhoneNum.isdigit() == False:
            print("Phone number must only include numbers. Please try again.")
        elif PhoneNum == "":
            print("Phone number can not be left blank. Please try again.")
        elif len(PhoneNum) != 10:
            print("Phone number must be 10 characters long. Please try again.")
        else:
            break
    while True:
        PlateNum = input("Enter the licence plate number (XXX###): ").upper()
        if PlateNum == "":
            print("Plate number can not be left blank. Please try again.")
        elif len(PlateNum) != 6:
            print("Plate number must contain 6 characters. Please try again.")
        elif PlateNum [0:3].isalpha() == False:
            print("First three characters must be alphabetical.")
        elif PlateNum [3:].isdigit() == False:
            print("Last three characters must me numbers.")   
        else:
            break
    while True:
        CarMake = input("Enter the make of the car (ie: Toyota): ").title()
        if CarMake == "":
            print("Car make can not be left empty. Please try again.")
        else:
            break
    while True:
        CarModel = input("Enter the model of the car (ie: Corolla): ").title()
        if CarModel == "":
            print("Car model can not be left empty. Please try again.")
        else:
            break
    while True:
        CarYear = input("Enter the year the car was made (####): ")
        if CarYear.isdigit() == False:
            print("Year must only include numbers. Please try again.")
        elif CarYear == "":
            print("Car year can not be left blank. Please try again.")
        elif len(CarYear) != 4:
            print("Must enter a valid year using four numbers. Please try again.")
        else:
            break
    while True:
        try:
            SalePrice = float(input("Enter the selling cost of the car: "))
        except:
            print("The selling price must contain a vaild number. Please try again.")
        else:
            if SalePrice == "":
                print("Car selling price can not be left blank. Please try again.")
            elif SalePrice > 50000.00:
                print("Car selling price can not exceed 50,000.00. Please try again.")
            else:
                break
    while True:
        try:
            TradePrice = float(input("Enter the trade value of the car: "))
        except:
            print("The trade in value must contain a vaild number. Please try again.")
        else:
            if TradePrice == "":
                print("Trade in price can not be left blank. Please try again.")
            elif TradePrice > SalePrice:
                print("Trade in price can not exceed can price.Please try again.")
            else:
                break
            #non-verified inputs
    SaleName = input("Enter the sales person's name: ").title()
    StreetAddress = input("Enter street address: ")
    City = input("Enter city name: ").title()
    Province = input("Enter province (XX): ").upper()
    Postal = input("Enter postal code (X#X #X#): ").upper()

#calculations (price after trade, licence fee, transfer fee, HST, subtotal, total sales price)

    AfterTradePrice = SalePrice - TradePrice

    if SalePrice <= 5000.00:
        LicenceCharge = LICENCE_FEE_UNDER5K
    else:
        LicenceCharge = LICENCE_FEE_OVER5K

    if SalePrice < 20000.00:
        TransferFee = SalePrice*TRANSFER_RATE_UNDER20K
    else:
        TransferFee = (SalePrice*TRANSFER_RATE_UNDER20K) + (SalePrice*TRANSFER_RATE_OVER20K)

    Subtotal = AfterTradePrice + TransferFee + LicenceCharge
    Taxes = Subtotal*HST_RATE
    TotalSalePrice = Subtotal + Taxes

#Display formating
    CustName = CustFName[0] + ". " + CustLName
    ReciptID = CustFName[0] + CustLName[0] + "-" + PlateNum[3:] + "-" + PhoneNum[6:]
    PhoneNum = PhoneNum[0:3] + "-" + PhoneNum[3:7] + "-" + PhoneNum[7:] #12 characters
    AddressDsp = City + ", " + Province + " " + Postal


# first payment is 30days after purchase date
    CurDatePlus30 = CurDate + datetime.timedelta(days = 30)

#formating dates
    CurDateDsp = (CurDate.strftime("%b %d, %Y"))
    CurDateDsp2 = (CurDate.strftime("%d-%b-%y"))
    CurDate30Dsp = (CurDatePlus30.strftime("%d-%b-%y"))


#display 78 accross
    print(f"")
    print(f"Honest Harry Car Sales                       Invoice Date:  {CurDateDsp:>10s}")
    print(f"Used Car Sale and Recipt                    Recipt No:       {ReciptID:>9s}")
    print(f"")#blank
    SalePriceDsp = "${:,.2f}".format(SalePrice)
    print(f"                                       Sale Price:            {SalePriceDsp:>10s}")
    TradePriceDsp = "${:,.2f}".format(TradePrice)
    print(f"Sold To:                               Trade Allowance:       {TradePriceDsp:>10s}")
    print(f"                                       ----------------------------------")
    AftTraPriDsp = "${:,.2f}".format(AfterTradePrice)
    print(f"       {CustName:<27s}     Price After Trade:     {AftTraPriDsp:>10s}")
    LicenceChDsp = "${:,.2f}".format(LicenceCharge)
    print(f"       {StreetAddress:<29s}   Licence Fee:           {LicenceChDsp:>10s}")
    TransFeeDsp = "${:,.2f}".format(TransferFee)
    print(f"       {AddressDsp:<27s}     Transfer Fee:          {TransFeeDsp:>10s}")
    print(f"       {PhoneNum:>12s}                    ----------------------------------")
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    print(f"                                       Subtotal:              {SubtotalDsp:>10s}")
    TaxDsp = "${:,.2f}".format(Taxes)
    print(f"Car Details:                           HST:                   {TaxDsp:>10s}")
    print(f"                                       ----------------------------------")
    TotalSalePriceDsp = "${:,.2f}".format(TotalSalePrice)
    print(f"       {CarYear:>4s} {CarMake:>13s} {CarModel:>10s}   Total Sales Price:     {TotalSalePriceDsp:>10s}")
    print(f"")#blank
    print(f"-------------------------------------------------------------------------")
    print(f"")#blank
    print(f"                               Financing     Total         Monthly")
    print(f"       # Years    # Payments      Fee        Price         Payment")
    print(f"     ----------------------------------------------------------------")
#Payment scedule calculations
    for Years in range(1,5):
        FinanceFee = FINANCE_FEE_RATE*Years
        FinaFeeDsp = "${:,.2f}".format(FinanceFee)
        TotalPrice = FinanceFee + TotalSalePrice
        TotalPriceDsp = "${:,.2f}".format(TotalPrice)
        NumMonthlyPayment = Years*12
        MonthlyPayment = TotalPrice/NumMonthlyPayment
        MonPayDsp = "${:,.2f}".format(MonthlyPayment)
        print(f"         {Years:>1d}         {NumMonthlyPayment:>2d}        {FinaFeeDsp:>10s}    {TotalPriceDsp:>10s}   {MonPayDsp:>10s}")
    print(f"     ----------------------------------------------------------------")
    print(f"       Invoice Date: {CurDateDsp2:>7s}        First Payment Date: {CurDate30Dsp:>7s}")
    print(f"       Sales Persons Name: {SaleName:<30s}")
    print(f"")#blank
    print(f"-------------------------------------------------------------------------")
    print(f"")