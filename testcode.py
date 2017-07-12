# print 'it'
# Fibonacci Series:
# the sum of two elements defines the next
import math
Primes = set([2])
Value = 3
Number = 600851475143
while Value < math.sqrt(Number):
    Prime = True
    for k in Primes:
        if Value % k == 0:
            Prime = False
            Value += 2
    if Prime:
        Primes.add(Value)
        if Number % Value == 0:
            print Value
            Number = Number / Value
print Number

# mylist = ["Zadv","topics","Zin", "CS", "ZWCATY","2017"]
# print [item if not item.startswith("Z") else item[1:] for item in mylist]

mydictionary = {} # Blank
testdictionary = {'key': 'value', 7:[7,7,7,7]} # Prepopulated

mydictionary[0] = 'zero' # Creating a new key with a value
mydictionary["Keegan"] = (1,1) # Creating a new key with a value

# for thing in mydictionary.iterkeys()

import time
print time.time()
time.sleep(3)
print time.time