#FormattingIFStatements
#St. John's Marina $ Yacht Club Yearly Membership Recipt
#Written by: Charity Smith
#Written: Sept 26/2023 - Sept 28th/2023

#enter constants
EVEN_SITE_RATE = 80.00
ODD_SITE_RATE = 120.00
ADD_MEM_RATE = 5.00
SITE_CLEAN_RATE= 50.00
VID_SURV_RATE = 35.00
TAX_RATE = .15
MONTH_DUE_ST_RATE = 75.00
MONTH_DUE_EX_RATE = 150.00
PROCESS_FEE = 59.99
YEAR = 12
CANCEL_FEE_RATE =.6

#enter inputs
SiteNumber = int(input("Enter the site number (1-100): "))
MemName = input("Enter the member name: ")
StreetAddress = input("Enter the street address: ")
City = input("Enter the city name: ")
Province = input("Enter the province: ").upper()
Postal = input("Enter the postal code (X#X #X#): ").upper()
PhoneNum = input("Enter the phone number: ")
CellNum = input("Enter the cell phone number: ")
MemType = input("Enter the membership type - (S) for Standard or (E) for Executive: ").upper()
NumAddFamily = int(input("Enter the number of additional friends or family members: "))
WeekClean = input("Do you want optional weekly site cleaning? (Y or N): ").upper()
VideoSurv = input("Do you want optional video survalence? (Y or N): ").upper()
CancelNotice = input("Is a cancellation notice given? (Y or N): ").upper()
Date = input("Enter date (####-##-##): ")

#do calculations
#even and odd site charges
if SiteNumber % 2 == 0:
    SiteCost = EVEN_SITE_RATE
else:
    SiteCost = ODD_SITE_RATE
#additional members and total site charges
AddMemCost = ADD_MEM_RATE*NumAddFamily
TotSiteCharges = SiteCost+AddMemCost
#optional charges, and total
if WeekClean == "Y":
    WeekCleanCost = SITE_CLEAN_RATE
else:
    WeekCleanCost = 0

if WeekClean == "Y":
    WeekCleanDsp = "YES"
else:
    WeekCleanDsp = "NO"

if VideoSurv == "Y":
    VidSurvCost = VID_SURV_RATE
else:
    VidSurvCost = 0

if VideoSurv == "Y":
    VidSurDsp = "YES"
else:
    VidSurDsp = "NO"

TotOptionalCost = WeekCleanCost+VidSurvCost
#Subtotal and taxes
Subtotal =TotSiteCharges+TotOptionalCost
Taxes = Subtotal*TAX_RATE
TotalMonthlyCharge =Subtotal+Taxes
#monthly dues
if MemType == "S":
    MonthDues = MONTH_DUE_ST_RATE
else:
    MonthDues = MONTH_DUE_EX_RATE
if MemType == "S":
    MemDisp = "STANDARD"
else:
    MemDisp = "EXECUTIVE"
TotMonthlyFees = TotalMonthlyCharge+MonthDues
#yearly fees, processing fees
TotYearlyFees = TotMonthlyFees*YEAR
MonthlyPayment = (TotYearlyFees+PROCESS_FEE)/12
#cancelation fee
if CancelNotice == "N":
    CancelFee = (YEAR*SiteCost)*CANCEL_FEE_RATE
else:
    CancelFee = 0

#Display -  calculated values
print(f"      St. John’s Marina & Yacht Club")
print(f"         Yearly Member Receipt")
print(f"--------------------------------------------")

print(f"Client Name and Address:")
print(f"")
print(f"{MemName:<24s}")
print(f"{StreetAddress:<24s}")
print(f"{City:<15s}, {Province:<2s} {Postal:<6s}")
print(f"Phone: {PhoneNum:<10s} (H)")
print(f"       {CellNum:<10s} (C)")
print(f"")
print(f"Site #: {SiteNumber:>3d} Member type: {MemDisp:<9s}")
print(f"")
print(f"Alternate members:                       {NumAddFamily:>2d}")
print(f"Weekly site cleaning:                   {WeekCleanDsp:>3s}")
print(f"Video surveillance:                     {VidSurDsp:>3s}")
print(f"")
TotSiteChDsp = "${:,.2f}".format(TotSiteCharges)
print(f"Site charges:                      {TotSiteChDsp:>6s}")
TotOptCoDsp = "${:,.2f}".format(TotOptionalCost)
print(f"Extra charges:                       {TotOptCoDsp:>5s}")
print(f"                               -------------")

SubtotDsp = "{:,.2f}".format(Subtotal)
print(f"Subtotal:                            {SubtotDsp:>6s}")
TaxDsp = "${:,.2f}".format(Taxes)
print(f"Sales tax (HST):                     {TaxDsp:>5s}")
print(f"                              --------------")

TotMonChaDsp = "${:,.2f}".format(TotalMonthlyCharge)
print(f"Total monthly charges:              {TotMonChaDsp:>6s}")
MonDueDsp = "${:,.2f}".format(MonthDues)
print(f"Monthly dues:                       {MonDueDsp:>5s}")
print(f"                               -------------")

TotMonFeeDsp = "${:,.2f}".format(TotMonthlyFees)
print(f"Total monthly fees:                 {TotMonFeeDsp:>6s}")
TotYeaFeeDsp = "${:,.2f}".format(TotYearlyFees)
print(f"Total yearly fees:                {TotYeaFeeDsp:>6s}")
print(f"")

MonPayDsp = "${:,.2f}".format(MonthlyPayment)
print(f"Monthly payment:                    {MonPayDsp:>6s}")

print(f"Issued: {Date}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print(f"")

CancFeeDsp = "${:,.2f}".format(CancelFee)
print(f"Cancellation fee:                   {CancFeeDsp:>6s}")