text = "X-DSPAM-Confidence:    0.8475"
colon_position = text.find(":")
#last_position = text.find("5")

number = text[(colon_position + 1):]
number_without_space = number.strip()

print(float(number_without_space))
