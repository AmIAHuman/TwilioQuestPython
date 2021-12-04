import sys

for index, element in enumerate(sys.argv):
  if index != 0:
    print(str(index) + ". " + element)