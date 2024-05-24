# Variables
payrate = 16
taxRate = 0.18
fidelityContribution = 0.04

# Server Hours
hoursWorked = float(input("How many hours as a banquet server did you work this pay period? "))

totalEarnings = payrate * hoursWorked
taxAmount = totalEarnings * taxRate
retirementPlan = totalEarnings * fidelityContribution
netPay = totalEarnings - taxAmount - retirementPlan
totalHours = hoursWorked

# Bartending Hours
question = input("Did you bartend? (Y/N?) ")
if question == "Y" or question == "y":
    position = 17.5
    hoursOtherPosition = float(input("How many hours did you work as a bartender? "))

    totalEarnings += position * hoursOtherPosition
    taxAmount = totalEarnings * taxRate
    retirementPlan = totalEarnings * fidelityContribution
    netPay = totalEarnings - taxAmount - retirementPlan
    totalHours = hoursWorked + hoursOtherPosition

# Cashier Hours
question = input("Did you work as a cashier? (Y/N?) ")
if question == "Y" or question == "y":
    position = 12.25
    hoursOtherPosition = float(input("How many hours did you work as a cashier? "))

    totalEarnings += position * hoursOtherPosition
    taxAmount = totalEarnings * taxRate
    retirementPlan = totalEarnings * fidelityContribution
    netPay = totalEarnings - taxAmount - retirementPlan
    totalHours = hoursWorked + hoursOtherPosition

# Initialize tips variable
tips = 0

# Ask if user made any card tips
question = input("Did you make any tips on card? (Y/N?) ")
if question == "Y" or question == "y":
    tips = float(input("How much did you make in tips? "))
    totalEarnings += tips
    taxAmount = totalEarnings * taxRate
    retirementPlan = totalEarnings * fidelityContribution
    netPay = totalEarnings - taxAmount - retirementPlan
    totalHours = hoursWorked + hoursOtherPosition

# Decides whether total hours is to be printed in integer or decimal form
if totalHours.is_integer():
    print(f"You worked a total of {int(totalHours)} hours!")
else:
    print(f"You worked a total of {totalHours} hours!")

# Tips Logic
if tips > 0:
    if tips.is_integer():
        print(f"You made ${int(round(tips, 2))} in tips on card.")
    else:
        print(f"You made {tips:.2f} tips on card.")
else:
    print("You didn't make any tips on card.")

# Continues paycheck summary
print(f"Tax Contribution: ${taxAmount:.2f}")
print(f"401k Contribution: ${retirementPlan:.2f}")

# Decides whether gross income is to be printed in integer or decimal form
if totalEarnings.is_integer():
    print(f"Gross Income: ${int(totalEarnings)}")
else:
    print(f"Gross Income: ${totalEarnings:.2f}")
    
print(f"Net Pay: ${netPay:.2f}")
print("Woo hoo!!! Congrats on surviving another two weeks in hell!")
