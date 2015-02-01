# Pass in a string to function q; returns an array of ordered characters from string.

def q(l):return[]if not l else q([i for i in l[1:]if i<l[0]])+[l[0]]+q([i for i in l[1:]if i>=l[0]])
