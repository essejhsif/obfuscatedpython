# Python program that prints its own code

print (lambda s:s.replace(chr(042), chr(047)) %s) ('print (lambda s:s.replace(chr(042), chr(047)) %%s("%s")')
