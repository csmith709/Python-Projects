#OneStop Insurance Company
#QAP 5
#Written by: Charity Smith
#Written on 30 Nov

#import libraries
import datetime
import FormatValues as FV
Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%d-%b-%y")

#define connstants from file
f = open('OSICDef.dat', 'r')
PolicyNum = int(f.readline())
FirstCarPrem = float(f.readline())
DiscAddCarRate = float(f.readline())
ExCarLiabilityOpt = float(f.readline())
GlassCoverageOpt = float(f.readline())
LoanerCarOpt = float(f.readline())
HSTRate = float(f.readline())
ProcessFeeRate = float(f.readline())
f.close()

#Part 1

#set up headings
# Print main headings and column headings.
print()
print(" ONE STOP INSURANCE COMPANY")
print(f" POLICY LISTING AS OF {TodayDsp}")
print()
print(" POLICY     CUSTOMER          POLICY     INSURANCE       EXTRA      TOTAL")
print(" NUMBER       NAME             DATE       PREMIUM        COSTS     PREMIUM")
print(" ==========================================================================")

# Initialize counters and accumulators for summary / analytics.
PolicyNumCtr = 0
InsPreAcc = 0
ToExAcc = 0
TotPreAcc = 0

# Open the file with the "r" mode for read.
f = open("Policies.dat", "r")

#Assign variables to each item in the list that are required in the report.
for CustRecord in f:      
    # Input - read the first record and split into a list.
    CustLst = CustRecord.split(",")

    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    PolicyNum = CustLst[0].strip()
    CustName = CustLst[3].strip()
    PolicyDate = CustLst[1].strip()
    PolicyDate = datetime.datetime.strptime(PolicyDate, "%Y-%m-%d")
    TotNumCars = int(CustLst[9].strip())
    ExCarLiab = (CustLst[10].strip())
    GlassCov = (CustLst[11].strip())
    LoanerCar = (CustLst[12].strip())
    
   # For an exception report, place an if before the calculations that defines the exception.
    if TotNumCars > 1:
        NumAddCar = TotNumCars - 1
        AddCarCharge = FirstCarPrem * NumAddCar
        AddCarDis = AddCarCharge * DiscAddCarRate
        AddCarTotal = AddCarCharge - AddCarDis
        InsPremium = FirstCarPrem + AddCarTotal
    elif TotNumCars == 1:
        NumAddCar = 0
        AddCarCharge = 0
        AddCarDis = 0
        AddCarTotal = 0
        InsPremium = FirstCarPrem

    if ExCarLiab == "Y":
        ExLiabCharge = ExCarLiabilityOpt
    else:
        ExLiabCharge = 0
        
    if GlassCov == "Y":
        GlassCharge = GlassCoverageOpt
    else:
        GlassCharge = 0
        
    if LoanerCar == "Y":
        LoanerCost = LoanerCarOpt
    else:
        LoanerCost = 0

    TotalExtraCost = ExLiabCharge + GlassCharge + LoanerCost
    TotalPrem = InsPremium + TotalExtraCost

        # Increment and Accumulate the summary / analytics data. 
    PolicyNumCtr += 1
    InsPreAcc += InsPremium
    ToExAcc += TotalExtraCost
    TotPreAcc += TotalPrem

        # Print the detail line.  A detail line is the details of the record you want.
    PolicyDateDsp = datetime.datetime.strftime(PolicyDate, "%Y-%m-%d")


    print(f" {PolicyNum:<4}       {CustName:<14s} {PolicyDateDsp:>12s}   {FV.FDollar2(InsPremium):>9s}   {FV.FDollar2(TotalExtraCost):>9s}   {FV.FDollar2(TotalPrem):>9s}")

#close the file
f.close()
print(f" ==========================================================================")
print(f" Total Policies: {PolicyNumCtr}                      {FV.FDollar2(InsPreAcc):>9s}   {FV.FDollar2(ToExAcc):>9s}  {FV.FDollar2(TotPreAcc):>9s}")
print()
#All Working ^
