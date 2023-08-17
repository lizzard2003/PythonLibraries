# Random numbers in Python
import random

# Random Numbers
print(random.random())
decider= random.randrange(2)
# we will decide if the coin is going to be flipped on heads or tails
if decider==0:
    print("Heads")
else:
    print("Tails")
print(decider) # this print whether we got a 1 or 2


# if we want to printout a decide we can do 
print("You rolled a " + str(random.randrange(1,7))) # the dice is between 1 and 6 . Since we begin with a strong we have
# to convert the rand into a string too 

#Random Choices
lotteryWinners= ("These are the lucky lottery numbers "+ str( random.sample(range(100),5)))
print(lotteryWinners)

possible_pet=["dog", "cat", "turtle", "zebra", "lion", "goat"]
print(random.choice(possible_pet))

cards =["Jack", "Queen", "Ace", "King"]
random.shuffle(cards)
print(cards)