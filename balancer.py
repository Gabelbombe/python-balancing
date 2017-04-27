#!/usr/bin/env python

i = iter('(){}[]<>')  # iterative parenthesis
p = dict(zip(i, i))   # create dictionary from i's tuples
c = p.values()

print("\nI:") ; print(list(i))
print("\nP:") ; print(list(p))
print("\nC:") ; print(list(c))

