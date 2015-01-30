# Print the first 20 numbers in the Fibonacci sequence

f = lambda x:map(lambda o:(map(lambda c:map(lambda l:
o.__setslice__(l[0],l[1],l[2]),([o[2]+3,o[2]+4,[o[0]]],[0,3,[o[1],
reduce(lambda x,o:x+o,o[:2]),o[2]+1]])),range(x)),o)[1],[[1,1,0]+
range(x)])[0][3:]
print f(20)
