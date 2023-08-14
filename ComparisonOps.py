# Python Comparison Openerators

# == ----> means equals
# <= ----> means less than or equal to 
# >= ----> means greater than or equal to 
# < ----> means less than
# > ----> means greater than


# less than example
print (10<75) # will return true
print(75<10) # will return false 

if 10 <75:
    print("75 is the bigger number therefore it is True")


# equal to example
kitten = 10
tiger = 75

if kitten< tiger:
    print("The kitten weights less")

# < (less than) example
mouse =1
if mouse < kitten and mouse < tiger:
    print("Then mouse weighs less than the kitten and the tiger")

# Looking for the first mismatch letter 
# A-Z ---> 1-26
# > ----> is greater than
print("Jennifer" > "Jenny") # this return False because after the second "n" Jenny has y 
