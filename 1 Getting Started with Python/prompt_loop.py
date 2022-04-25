count = 0
total = 0

while True:
    string_value = input("Enter a number: ")
    if string_value == "done":
        print("ALL DONE")
        break
    try:
        float_value = float(string_value)
    except:
        print("INVALID INPUT")
        continue

    count = count + 1
    total = total + float_value

print(count, total, total/count)
