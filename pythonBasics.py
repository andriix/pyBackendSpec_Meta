print("Hello. Input bill_total:")
bill_total = float(input())

discount1 = 10
discount2 = 20

if 100 < bill_total <= 200:
    print("greater than 100!")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("greater than 200!")
else:
    print("less than 100")

print("total is " + str(bill_total))