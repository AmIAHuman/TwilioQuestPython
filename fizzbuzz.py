import sys

def check(num):
  print("fizzbuzz" if num % 3 == 0 and num % 5 == 0 else ("fizz" if num % 3 == 0 else ("buzz" if num % 5 == 0 else str(num))))

for index, element in enumerate(sys.argv):
  if index != 0:
    check(int(element))