# Range --> range instance that holds all nums counting by one bwtween first outpus and last
# List --> list number from the input tuple

numberedContestants = range(30) # 0-29 will be printed 

print(list(numberedContestants)) # will list out all the numbers in the numberedConstestant List 

for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")


luckyWinner= range(7,30, 5) # we are counting from 7(start), 30(ending), 5(counting by 5)
print(list(luckyWinner)) # we are printing it on a list 
# we got [7,12, 17,22, 27] as output 


# Min and Max
playerOneScore = 10
playerTwoScore = 4
print(min(playerOneScore, playerTwoScore)) # returns 4 
print(max(playerOneScore, playerTwoScore)) # returns 10


print(min(0, 5, -19, 9))


# Rounding

# round()
myGPA= 3.6
print(round(myGPA))

amountOfSalt= 1.4
print(round(amountOfSalt))

# ABS(Absolute value)
distanceAway= -13
print(abs(distanceAway))

# pow()
chanceOfTails = 0.5
inARowTails = 3
print(pow( chanceOfTails, inARowTails))