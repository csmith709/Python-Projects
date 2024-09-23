# Name of Program: XYZ Company Equipment Maintenance Schedule
# Description of Program: This program creates a maintenance schedule and evaluation formula for major pieces of equipment

# Date Written: 2023-10-30
# Author: William Young

##########################::::::::::    CONSTANTS    :::::::::::####################################

USEFUL_LIFE_MONTHS = 180
BASIC_CLEANING_DAYS = 10
TUBE_AND_FLUID_CHECK_DAYS = 21
MAJOR_INSPECTION_DAYS = 180

PURCHASE_DATE_FORMAT = r'^\d{2}-\d{2}-\d{4}$'

##########################::::::::::   USER INPUTS   :::::::::::####################################

while True: # REPEAT PROGRAM LOOP

    import datetime
    from datetime import datetime
    import re

    while True:
 
        EquipmentCost = input("Enter the cost of equipment: ");
 
        if EquipmentCost == "":
            print("Equipment cost cannot be blank. Please re-enter")
        else:
            break

    while True:
 
        PurchaseDate = input("Enter the purchase date of equipment (MM-DD-YYYY): ")
        if re.match(PURCHASE_DATE_FORMAT, PurchaseDate):
            break
        else:
            print("Purchase Date must be entered as (MM-DD-YYYY). Please re-enter")

##########################::::::::::   CALCULATIONS  :::::::::::####################################

   # PurchaseDate = datetime.strftime("%b-%d-%Y").upper()
    PurchaseDate_TIMEOBJECT = datetime.strptime(PurchaseDate, "%m-%d-%Y")
    PurchaseDate_TIMEOBJECTDSP = PurchaseDate_TIMEOBJECT.strftime("%m-%d-%Y").upper()

    EquipmentCost = float(EquipmentCost)
    SalvageValue = EquipmentCost * 0.1
    AmortizationValue = (EquipmentCost - SalvageValue) / USEFUL_LIFE_MONTHS

    import datetime

    BasicCleaning = PurchaseDate_TIMEOBJECT + datetime.timedelta(days = BASIC_CLEANING_DAYS)

    TubeAndFluidCheck = PurchaseDate_TIMEOBJECT + datetime.timedelta(days = TUBE_AND_FLUID_CHECK_DAYS)

    MajorInspection = PurchaseDate_TIMEOBJECT + datetime.timedelta(days = MAJOR_INSPECTION_DAYS)

##########################::::::::::  DISPLAY FORMAT :::::::::::####################################

    EquipmentCostDSP = "${:,.2f}".format(EquipmentCost)
    AmortizationValueDSP = "${:,.2f}".format(AmortizationValue)
    SalvageValueDSP = "${:,.2f}".format(SalvageValue)

    BasicCleaningDSP = BasicCleaning.strftime("%m-%d-%Y").upper()
    TubeAndFluidCheckDSP = TubeAndFluidCheck.strftime("%m-%d-%Y").upper()
    MajorInspectionDSP = MajorInspection.strftime("%m-%d-%Y").upper()

##########################::::::::::      OUTPUT     :::::::::::####################################

    print("-------------------------------------------------")
    print(f"  XYZ Company                           ")
    print(f"  Equipment Maintenance Schedule       ")
    print("                                   ")
    print("                                   ")
    print(f"  Equipment Details:                            ")
    print(f"       -------------------------------------")
    print(f"       Equipment Cost:    {EquipmentCostDSP:>18s}")
    print(f"       Purchase Date:     {PurchaseDate_TIMEOBJECTDSP:>18s}")
    print(f"       -------------------------------------")
    print(f"                                       ")
    print("                                   ")
    print(f"  Schedule of Maintenance:                            ")
    print(f"       -------------------------------------")
    print(f"       Basic Cleaning - {BasicCleaningDSP:>20s} ")
    print(f"       Tube and Fluid Check - {TubeAndFluidCheckDSP:>14s}")
    print(f"       Major Inspection - {MajorInspectionDSP:>18s}")
    print(f"       -------------------------------------")
    print("                                   ")
    print("                                   ")
    print(f"  Equipment Evaluation:  ")
    print(f"       -------------------------------------")
    print(f"       Salvage Value:              {SalvageValueDSP:>9s}")
    print(f"       Monthly Amortization:       {AmortizationValueDSP:>9s}")
    print(f"       -------------------------------------")
    print("                                   ")
    print(f"        *Monthly Amortization is based off")
    print(f"           of a useful life of 15 years*")
    print("                                                                             ")
    print("-------------------------------------------------")

##########################::::::::::  REPEAT PROMPT  :::::::::::####################################

    Continue = input("Do you want to process another maintenance schedule? (Y/N): ").upper()
    if Continue == "N":
        break
