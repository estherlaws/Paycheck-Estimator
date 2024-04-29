payrate = 16
hoursWorked = float(input("How many hours did you work this pay period? "))
taxRate = 0.16
fidelityContribution = 0.04

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
    hoursOtherPosition = float(input("How many hours did you work as a bartender? "))

    totalEarnings += position * hoursOtherPosition
    taxAmount = totalEarnings * taxRate
    retirementPlan = totalEarnings * fidelityContribution
    netPay = totalEarnings - taxAmount - retirementPlan
    totalHours = hoursWorked + hoursOtherPosition

# Initialize tips variable
tips = 0

# Check if user made any tips
question = input("Did you make any tips on card? (Y/N?) ")
if question == "Y" or question == "y":
    tips = float(input("How much did you make in tips? "))
    totalEarnings += tips
    taxAmount = totalEarnings * taxRate
    retirementPlan = totalEarnings * fidelityContribution
    netPay = totalEarnings - taxAmount - retirementPlan
    totalHours = hoursWorked + hoursOtherPosition

# Decides whether to print total hours in integer form or decimal form 
if totalHours.is_integer():
    print(f"You worked a total of {int(totalHours)} hours")
else:
    print(f"You worked a total of {totalHours} hours")

# Prints paycheck summary
print(f"Your Gross Income Is: ${totalEarnings:.2f}")

# Tips Logic
if tips > 0:
    if tips.is_integer():
        print(f"You made ${int(round(tips, 2))} in tips on card.")
    else:
        print(f"You made {tips:.2f} in tips on card.")
else:
    print("You didn't make any tips on card.")

# Continues paycheck summary
print(f"Your tax contribution is: ${taxAmount:.2f}")
print(f"Your 401k contribution is: ${retirementPlan:.2f}")
print(f"Your Net Pay Is: ${netPay:.2f}")
print("Woo hoo!!! Congrats on surviving another two weeks in hell!")
