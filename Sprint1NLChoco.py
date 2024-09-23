# Program to process travel claims for NL Chocolate Company Salespeople
# Completed by Group 6 - SD10 - Charity Smith, William Young, Ed Spurrell
# Completed for: Maurice Baubin
# Completed on October 25 2023

#imports

import datetime

#Constants

RENT_KM_RATE = 0.17
SALES_CAR_DAY_RATE = 65.00
PER_DIEM_DAY_RATE = 85.00
BONUS_DAY_RATE = 100
BONUS_KM_RATE = .04
EXEC_BONUS_RATE = 45
DEC_BONUS_RATE  = 50.00
HST_RATE = 0.15 

#Inputs

while True:

    while True:
        EmpNum = input("Please enter your five digit employee number (enter all zeros to quit): ")

        if EmpNum == "":
            print("Employee Number cannot be empty, please re-enter.")
        elif len(EmpNum) != 5:
            print("Employee Number must be 5 digits, please re-enter.")
        else:
            break
        
    if EmpNum == "00000":
        break

    while True:
        EmpFirstName = input("Please enter your first name: ").title()

        if EmpFirstName == "":
            print("First name cannot be empty, please re-enter.")
        else:
            break

    while True:
        EmpLastName = input("Please enter your last name: ").title()

        if EmpLastName == "":
            print("Last name cannot be empty, please re-enter.")
        else:
            break
    
    TripLoc = input("Please enter the location of your trip: ")

    while True:
        try:
            TripStartDate = input("Please enter the date your trip began(YYYY-MM-DD): ")
            TripStartDate = datetime.datetime.strptime(TripStartDate, "%Y-%m-%d")
        except:
            print("Incorrect format for the start date, please re-enter as YYYY-MM-DD.")
        else:
            if TripStartDate == "":
                print("Trip start date cannot be empty, please re-enter.")
            else:
                break


    while True: 
        try:
            TripEndDate = input("Please enter the date your trip ended (YYYY-MM-DD): ")
            TripEndDate = datetime.datetime.strptime(TripEndDate, "%Y-%m-%d")
            NumDays = (TripEndDate - TripStartDate).days
        except:
            print("Incorrect format for the end date, please re-enter as YYYY-MM-DD.")
        else:
            if NumDays > 7:
                print("You have exceeded the max number of days, pleae re-enter.")
            elif TripEndDate == "":
                print("Trip end date cannot be empty, please re-enter.")
            else:    
                break
    
    allowed_trip_type = set("OR")
    while True:
        CarType = input("Please enter an O if you used your own vehicle, or R if you rented one: ").upper()
    
        if CarType == "":
            print ("Transportation type must be entered, please re-enter.")
        elif set(CarType).issubset(allowed_trip_type) == False:
            print("An incorrect option was selected, please enter  an O or R.")
        else:
            break

    while True:        
        TotKm = float(input("Please enter the total kilometers traveled: "))
        if TotKm > 2000:
            print ("You have exceeded the maximum amount of kilometers for a single trip, please re-enter.")
        elif TotKm == "":
            print ("If you used your personal vehicle, the amount of kilometers traveled must be entered, please re-enter.")
        else:
            break
    
    allowed_claim_type = set("ES")
    while True:
        ClaimType = input("Please enter an E if this is an Executive claim, or an S if this is a Standard Claim: ").upper()

        if ClaimType == "":
            print("A claim type must be entered, please re-enter an E or S.")
        elif set(ClaimType).issubset(allowed_claim_type) == False:
            print("An incorrect option was seleted, please enter an E or S.")
        else:
            break

    #Calculations

    NumDays = (TripEndDate-TripStartDate).days
    
    #Bonus Calculations

    if NumDays > 3:
        BonusDayAdd = BONUS_DAY_RATE
    else:
        BonusDayAdd = 0
    
    if TotKm >1000 and CarType == "O":
        BonusKmAdd = TotKm*BONUS_KM_RATE
    else:
        BonusKmAdd = 0
    
    if ClaimType == "E":
        BonusExecAdd = EXEC_BONUS_RATE
        ClaimType = "Executive"
    else:
        BonusExecAdd = 0
        ClaimType = "Standard"

    if TripStartDate.month == 12 and TripStartDate.day in range (15,23):
        BonusDecAdd = DEC_BONUS_RATE*NumDays
    else:
        BonusDecAdd = 0
    
    BonusAmt = BonusDayAdd + BonusKmAdd + BonusExecAdd + BonusDecAdd

    #Per Diem Calculations
    PerDiemAmt = NumDays*PER_DIEM_DAY_RATE

    #Milage Calculations
    if CarType == "O":
        MilageAmt = TotKm*RENT_KM_RATE
        CarType = "Personal Vehicle"
    else:
        MilageAmt = 0
        CarType = "Rented Vehicle"
    
    #Total Claim Calculations
    ClaimAmt = PerDiemAmt + MilageAmt+BonusAmt
    HST = ClaimAmt * HST_RATE
    TotClaim = ClaimAmt + HST


    #Display
    print()
    print(f"           NL Chocolate Company      ")
    print(f"        Employee Travel Claim Form          ")
    print(f"__________________________________________")
    print()
    print(f" Claim Details: ")
    print()
    EmpName = EmpFirstName + " " + EmpLastName
    print(f" Employee Name:    {EmpName:<24s}")
    print(f" Employee Number:  {EmpNum:<5s}")   
    print(f" Trip Location:    {TripLoc:<24s}")
    print()
    TripStartDsp = TripStartDate.strftime("%Y-%m-%d")
    print(f" Trip Start Date:  {TripStartDsp:<10s}")
    TripEndDsp = TripEndDate.strftime("%Y-%m-%d")
    print(f" Trip End Date:    {TripEndDsp:<10s}")
    print(f" Number of Days:   {NumDays:<2d}")
    print() 
    print(f" Vehicle Type:     {CarType:>5s}")
    TotKmDsp = "{:,.0f}".format(TotKm)
    print(f" Total Km Driven:  {TotKmDsp:>4s}")
    print(f" Claim Type:       {ClaimType:>9s}")
    print(f"__________________________________________")
    print()
    print(f"Reimbursment Breakdown: ")
    print()
    PerDiemDsp = "${:,.2f}".format(PerDiemAmt)
    print(f" Per Diem:                        {PerDiemDsp:8>s}")
    BonusAmtDsp = "${:,.2f}".format(BonusAmt)
    print(f" Bonus:                           {BonusAmtDsp:8>s}")
    MilageAmtDsp = "${:,.2f}".format(MilageAmt)
    print(f" Milage:                            {MilageAmtDsp:8>s}")
    print(f"                                ---------")
    ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
    print(f" Claim Total:                     {ClaimAmtDsp:8>s}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f" Tax (HST):                        {HSTDsp:8>s}")
    print(f"                                ---------")
    TotClaimDsp = "${:,.2f}".format(TotClaim)
    print(f" Total Claim Reimbursement:       {TotClaimDsp:8>s}")
    print()
    print(f"-------------------------------------------------------------------------")
    print(f"Please return this completed form, with all invoices, to the main office. ")
    print(f"-------------------------------------------------------------------------")
    print()