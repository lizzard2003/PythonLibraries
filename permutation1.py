import itertools

# permutation

election ={ 1:" Barb", 2:" Karen", 3: "Bob"}
for p in itertools.permutations(election):
    print(p)
for p1 in itertools.permutations(election.values()):
    print(p1) # this prints out the values of the dictionary 


# Combinations : Order does not matter - no copies

colorsForPainting =["Puple", "Red", "White", "Pink"]
for c in itertools.combinations(colorsForPainting , 2):
    print (c)