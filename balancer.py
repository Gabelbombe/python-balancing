#!/usr/bin/env python

i = iter('(){}[]<>')        # iterative parenthesis
p = dict(zip(i, i))         # create dictionary from i's tuples
c = p.values()              # create values (aka, opp neighbor)


def balancer(input):
    s = []                  # as stack
    for c in input:         # iterate through our input
        d = p.get(c, None)  # get parenthesis' val (opp neighbor)
        if d:
            s.append(d)     # append paren to lookup
        elif c in c:
            if not s or c != s.pop():
                return False
    return not bool(s)


# Output:
# >>> balancer('[()<>]')
# True
# >>> balancer('[<(>)]')
# False

# Issues:
# names c and input are shadowed from outer scopes =/