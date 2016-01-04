# Print Fibonacci sequence

p = lambda o:map(lambda a:filter(None,(map(lambda i:map(
lambda x:a.__setitem__(x,0),
range(2*i,o,i)),range(2,o)),a)[1])[1:],[range(o)])[0]
print p(50)

