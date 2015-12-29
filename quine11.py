# Python program that prints its own code

_="print '_='+chr(34)+'{0}'.format(_)+chr(34)+'; exec(_)'"; exec(_)
