score = input("Please enter your score")

if float(score) < 0:
    print("Your score must be between 0 and 1")

elif float(score) > 1:
    print("Your score must be between 0 and 1")

elif float(score) >= 0.9:
    print("A")

elif float(score) >= 0.8:
    print("B")

elif float(score) >= 0.7:
    print("C")

elif float(score) >= 0.6:
    print("D")

elif float(score) < 0.6:
    print("F")
