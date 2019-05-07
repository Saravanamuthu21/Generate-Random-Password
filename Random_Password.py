from string import *
from random import randint

length = input('Enter the length of password u need:')
String = raw_input('Enter your Alphanumeric String:')

if length == '':
    length = 8


for name, value in [('[LETTERS]', ascii_lowercase + ascii_uppercase),('[NUMBERS]', digits)]:
	String = String.replace(name, value)


maxi = len(String) - 1
New_Passwd = ''.join(String[randint(0, maxi)] for i in xrange(length))

print(New_Passwd)
