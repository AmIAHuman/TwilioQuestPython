import sys

sum = int(sys.argv[1]) + int(sys.argv[2])
print("You have chosen the path of destitution." if sum <= 0 else ("You have chosen the path of plenty." if sum >= 1 and sum <= 100 else "You have chosen the path of excess."))