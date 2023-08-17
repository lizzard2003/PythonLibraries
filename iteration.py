#itertool
import itertools

#infinite counting
for x in itertools.count(50,5): # the 5 will count by 5
    print(x)
    if x==65:
        break; # this will print out 50-65

#infinity cycle
x=0;
for c in itertools.cycle("Racecar"):
    print(c)
    x= x+1
    if x>20:
        break