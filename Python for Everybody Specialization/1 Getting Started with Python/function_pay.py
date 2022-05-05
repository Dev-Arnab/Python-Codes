def computepay(h, r):
    p = h * r

    return p

hrs = input("How many hours did you work? ")
hours = float(hrs)
rat = input("What is your rate per hour? ")
rate = float(rat)

if hours > 40:
    extra = 1.5 * (hours - 40) + 40
    pay = computepay(extra, rate)

else:
    pay = computepay(hours, rate)

print("Pay", pay)
