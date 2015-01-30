# Print the first 100 Fibonacci numbers

print map(lambda x,f=lambda x,f:(x<=1) or (f(x-1,f)+f(x-2,f)): f(x,f),range(10))
