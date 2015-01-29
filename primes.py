# Print a list of primes < 1000

print filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))
