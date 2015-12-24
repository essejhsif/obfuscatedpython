# Python program that prints its own code

s = r"print 's = r\"' + s + '\"' + '\nexec(s)'"
exec(s)
