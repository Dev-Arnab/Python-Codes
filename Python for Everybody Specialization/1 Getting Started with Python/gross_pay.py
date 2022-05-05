hours = input("How many hours you worked?")
rate = input("What is your rate per hour?")

if int(hours) <= 40:
    pay = float(hours) * float(rate)

else:
    extra = (float(hours) - 40) * 1.5
    total = 40 + extra
    pay = total * float(rate)

print(pay)
