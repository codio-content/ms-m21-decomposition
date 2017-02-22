Lets look at the program to the left. It is an example of a program with a function that figures out a salary. 

This is a VERY simplistic example.  The hours, rate, and bills are all assigned variables.  A better program would ask for amounts and then calculate.  You have to also understand this example does not translate well to a program. Hence all of the comments and not all code. 

Let look at the syntax of the function - 
 - you must define the function
  --`def FindSalary()`:   This defines it (def) and gives it a name you will use in the man program (FindSalary).  The parentheses past the name are for passing in values.  We will look at that later. 
 - indent all of the steps needed for that function
- the function is written at the top of the program so that the program knows the definition of FindSalary before it is used in the main program. 
- to use it in the main program you just use the name with parentheses (FindSalary())
- Note: `round(afford,2)` is using the round function to take the variable afford and round it to 2 decimal places.  You do not see the function defined at the top because round is a python built in function.  There are some functions already written for you to use.  Print is actually a function as well. 


{Run}(python3 .guides/content/FuncEx1.py )
