You are going to get some choice in how to do this program.  The only requirements are that you use the following string methods.
   - `len()`
   - `find()`
   - `lower()`
   - `upper()`
   - `replace()`
   
 It is suggested that you use your name or a favorite phrase.  Then have your program print out the length, etc.  Obviously to show the upper and lower your name, word, or phrase cannot all be in one case.

{Run}(python3 .guides/content/StringTest.py )

*Since this does not grade itself please advise your teacher when completed and they can review your final program.*

|||guidance
# Solution

There are so many variations that it is not possible to give an exact solution.  You can use the example String program StringFuncEx.py from earlier in the unit technically as a solution (and copied here)

To view your students work see [Viewing Student Code](https://codio.com/docs/teacher/assess/studentcode/)
```python
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
```

It is important sometimes to give MS students the freedom to play with code and do something of their choice. 
|||
