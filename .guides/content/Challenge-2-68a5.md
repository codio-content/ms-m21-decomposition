You are going to finish the program that asks the user to guess a number and then compares it to the random number.  If the guess is wrong the user must guess again.  You will also keep count of how many guesses it takes for the user to get it right. 

Here is the steps you will need.  They are also further commented in the program.
 - get a random number from 1-10
 - ask for intial guess
 - increase the guess count
 - while loop compares guess and number
    - asks for another guess
    - adds one to the guess count
- prints out the number and now many guesses it took

This will open a terminal window so you can input your guess
{Run | terminal}(python3 .guides/content/RandTest.py)

*Since this does not grade itself please advise your teacher when completed and they can review your final program.*

|||guidance
# Solution
To view your students work see [Viewing Student Code](https://codio.com/docs/teacher/assess/studentcode/)

```python
import random

#just giving the variables a starting value
countofguesses = 0
guess = 0

#for the random number we get one from 0-9 but 
#we want it from 1-10 so we just add 1 
number = random.randrange(10) + 1

#ask for initial guess
guess = int(input('What is your guess from 1 -10?'))

#first guess so increment count of guesses
countofguesses = 1

#while the guess is not equal to the number you will ask them to guess again 
#and add one more to the count of guesses
while guess != number:
   print ("not correct, guess again")
   guess = int(input('What is your guess from 1 -10?')) 
   countofguesses = countofguesses + 1
    
#Once they have guessed the number print out the number of guesses    
print ('CORRECT It took you %d guesses' % countofguesses)
print ('The number was', number)
```
|||
   