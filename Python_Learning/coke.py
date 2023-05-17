amount_due = 50
while amount_due > 0:
    print("Amount Due: ", amount_due)
    amount_inserted = int(input("Insert Coin: "))
    if amount_inserted in [25, 10, 5]:
        amount_due = amount_due - amount_inserted
    
print("Change Owed: ", -amount_due)
