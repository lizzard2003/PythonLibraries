# boolean we can only have True and False

# example:
isRaining= True
isSunny= False

# Logic Operators -----AND or Or

#AND
#true and true = true
#true and false = false
#false and true = false
#false and false = false

if isRaining and isSunny:
    print("We might see a rainbow ") # this does happen because isSunny is False 
else:
    print("We are having a rainy day")


# OR
#true and true = true
#true and false = true
#false and true = true
#false and false = false
if isRaining or isSunny:
    print("We might have a sunny or rainy day") # this executes because of the or statement 
else:
    print("We have weather")

# NOT
# true ---> false
# false --> true 
if not isRaining:
    print("it must be raining ")

ages = [ 12, 18, 39, 87, 7, 2]
for age in ages: 
    isAdult= age > 17;
    if not isAdult:
        print("Being " + str(age)+ " does not make you an adult")

