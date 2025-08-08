purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount > 1000:
    tax = purchase_amount * 0.05
    print("Tax rate: 5%")
else:
    tax = purchase_amount * 0.02
    print("Tax rate: 2%")

total = purchase_amount + tax

print("Purchase amount:", purchase_amount)
print("Tax amount:", tax)
print("Total amount:", total)