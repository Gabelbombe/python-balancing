#!/usr/bin/env python

i = iter('(){}[]<>')  # iterative parenthesis
p = dict(zip(i, i))   # create dictionary from i's tuples
