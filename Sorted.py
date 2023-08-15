# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1 ,12]
sortedGame= sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children =["David", "Franklin", "Adam", "Rebecca"]
print(sorted(children))
print(sorted(["David", "franklin", "Adam", "Rebecca"])) # this would put franklin in the end

# we can put some parameters to fix this
# Key parameters
# this sentence would be returned in alphabetical order 
print(sorted("Popcorn pops with butter to make buttery popcorn".split(), key= str.upper) )
# split wil split it up by the spaces and the upper will change evertything into upper so they can be equal comparisons


# to reverse the list output we can use the reverse method 
print(sorted(children, reverse= True))


leaderBoard={231: "CKL", 123 :"ABC", 456: " DEF"}
print(sorted(leaderBoard, reverse= True )) # this reversed the keys

print(leaderBoard.get(456)) # this will get the number in key position 456 which is DEF

students= [('alice', 'A', 12),('bob', 'C', 15),('mike', 'B', 17)]
print(sorted(students, key= lambda student: student[0])) # this sorts them by name 
print(sorted(students, key= lambda student: student[1])) # this sorts them by grade
print(sorted(students, key= lambda student: student[2])) # sorted by age 

# type() function
