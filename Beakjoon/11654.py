from unicodedata import numeric


string = input()
if string is numeric:
    print(chr(string))
else:
    print(ord(string))