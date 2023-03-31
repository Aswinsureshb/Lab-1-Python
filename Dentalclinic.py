name = (input("Enter patient name: "))
cleaning = input("Was cleaning performed? (y/n): ")
cavity = input("Was cavity filling performed? (y/n): ")
X_Ray = input("Was X-Ray performed? (y/n): ")

Cleaning_rate = 60
Cavity_rate = 200
X_Ray = 100
Tax_Rate = 0.15
Discount_Threshold_1 = 200
Discount_Threshold_2 = 300
Discount_1 = 0.05
Discount_2 = 0.1

def calculation(cleaning,cavity,xray):
    subtotal = 0
    if cleaning == "y":
        subtotal += Cleaning_rate
    if cavity == "y":
        subtotal += Cavity_rate
    if X_Ray == "y":
        subtotal += X_Ray

    tax = subtotal * Tax_Rate
    total = subtotal + tax

    if total > Discount_Threshold_1:
        total *= (1 - Discount_1)
    elif total > Discount_Threshold_2:
        total *= (1 - Discount_2)

    return total

bill = calculation(cleaning,cavity,X_Ray)

print("Melanie Dental Clinic")
print("Receipt for patient name:", name)
print("Subtotal: ", round(bill / (1 + Tax_Rate), 2))
print("Tax: ", round(bill * Tax_Rate, 2))
print("Total: ", round(bill, 2))