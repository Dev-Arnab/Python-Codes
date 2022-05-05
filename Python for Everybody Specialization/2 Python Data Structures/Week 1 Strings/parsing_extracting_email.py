data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
print(data)

at_position = data.find("@")
print(at_position)

space_position = data.find(" ", at_position) #Here, at_position means to start the searching from after the position of "@"
print(space_position)

host = data[(at_position + 1) : space_position]
print(host)
