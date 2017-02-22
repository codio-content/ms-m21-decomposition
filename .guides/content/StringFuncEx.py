#examples of string functions

message1 = "Hello World"
print( len(message1))
print()

#tells you where it is found based on letter number
# h is 0, e is 1, l is 2,  etc. 
message2 = "hello world"
print(message2.find("worl"))
print()

#same as above but using another variable
message2 = "hello world"
message3 = message2.find("worl")
print(message3)
print()

#what if it is not in the phrase - it will print a negative 1
message4 = "Hello World"
message5 = message4.find("happy")
print(message5)
print()

#converts to lower case
message6 = "HELLO WORLD"
print(message6.lower())
print()

#converts to upper case
message7 = "Hello World"
print(message7.upper())
print()

#replaces part of the string with another letter or string
message8 = "Hello World"
message9 = message8.replace('l', 'pizza')
print(message9)