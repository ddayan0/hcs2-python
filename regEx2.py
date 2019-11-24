def line():
    print('----------------------------------------------------------------')
import re as regex

def regExChecker(string, pattern):
    if (pattern.search(string)):
        print("Found!")
    else:
        print('None')

#1. RBRHS user name
pattern = regex.compile('^([a-z]*)(\d{2})$')
regExChecker('ddayan21', pattern)
line()
# 2. Passwords with at least
# 	- 1 lowercase
# 	- 1 capital
# 	- 1 number
# 	- 1 special character
# 	- between 8-15 characters long
#pattern = regex.compile('([a-z]{+1}[A-Z]{+1}\d{+1}(?=.*[@#$%^&+=])){8,15}') #F A I L E D!
pattern = regex.compile('((?=(.*[0-9]))(?=.*[A-Za-z0-9])(?=.*[@#$%^&+=!]))^.{8,15}$')
regExChecker('Passw0rd!', pattern)
line()
print('email')
pattern = regex.compile('^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
regExChecker('cwatson22@rbrhs.org', pattern)


print('url')
pattern = regex.compile('(www\.)?[a-zA-Z0-9@:%._\+~#=]{2,20}\.[com]')
regExChecker('www.google.com', pattern)

