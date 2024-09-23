#OneStop Insurance Company
#QAP 5
#Written by: Charity Smith
#Written on 30 Nov

#import libraries
import datetime
import FormatValues as FV
Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%d-%b-%y")


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

#set up headings
# Print main headings and column headings.
print()
print(" ONE STOP INSURANCE COMPANY")
print(f" POLICY LISTING AS OF {TodayDsp}")
print()
print(" POLICY     CUSTOMER       TOTAL         HST       TOTAL       DOWN         MONTHLY")
print(" NUMBER       NAME        PREMIUM                  COST       PAYMENT       PAYMENT")
print(" ==================================================================================")

# Initialize counters and accumulators for summary / analytics.
PolicyNumCtr = 0
HSTAcc = 0
TotAcc = 0
DwnPayAcc = 0
MonthAcc = 0
TotPremAcc = 0


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
    PayType = CustLst[13].strip()
    DownPayment = float(CustLst[14].strip())
    
   # For an exception report, place an if before the calculations that defines the exception.
      # For an exception report, place an if before the calculations that defines the exception.
    if PayType == "Monthly" or PayType == "Down Pay":
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
        TotPrem = InsPremium + TotalExtraCost

        if PayType == "Down Pay":
            HSTCost = TotPrem*HSTRate
            TotalCost = TotPrem + HSTCost
            MonthlyCost = ((TotalCost + ProcessFeeRate) - DownPayment) / 12
        if PayType == "Monthly":
            HSTCost = TotPrem*HSTRate
            TotalCost = TotPrem + HSTCost
            MonthlyCost = (TotalCost + ProcessFeeRate) / 12

            # Increment and Accumulate the summary / analytics data. 
        PolicyNumCtr += 1
        HSTAcc += HSTCost
        TotAcc += TotalCost
        DwnPayAcc += DownPayment
        MonthAcc += MonthlyCost
        TotPremAcc += TotPrem
        
        
            # Print the detail line.  A detail line is the details of the record you want.
        print(f" {PolicyNum:<4s}      {CustName:<14s} {FV.FDollar2(TotPrem):>9s}  {FV.FDollar2(HSTCost):>9s}   {FV.FDollar2(TotalCost):>9s}  {FV.FDollar2(DownPayment):>9s}    {FV.FDollar2(MonthlyCost):>9s}")
        

    #close the file
f.close()
print(f" ==================================================================================")
print(f" Total Policies: {PolicyNumCtr:>3}      {FV.FDollar2(TotPremAcc):>9s}  {FV.FDollar2(HSTAcc):>9s}   {FV.FDollar2(TotAcc):>9s}  {FV.FDollar2(DwnPayAcc):>9s}    {FV.FDollar2(MonthAcc):>9s}")
print()
