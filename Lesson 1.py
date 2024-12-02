Name = "starla"
age = 5

description = f"{name} likes wand toys and is {age}"
print(description)
description = name + " likes wand toys and is " + str(age)
print(description)

# indexting - every charecter in a string has a location starting at 0
# starting at 0 from the beggining or -1 from the end

# 0 1 2 3 4 5
# S t a r l a
# -6 -5 -4 -3 -2 -1 

first_letter - name[0] # always use 0 if you do not know the length

print(first_letter) # test of it

first_letter = name[-6]
print(first_letter)
