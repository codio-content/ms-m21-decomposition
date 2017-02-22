
#__________________________________________________________________
#function Figure out how much you can spend
# --	Look up your monthly pay
# --	Figure out all of your current bills
# --	Subtract bills from monthly pay
# --	See what is left and decide on what you can pay per month for car.

def FindSalary():
    hours = 40
    rate = 15
    bills = 2100
    salary = hours * rate * 4  #4 weeks in a month
    afford = salary - bills
    print ("You can afford a car payment of ", round(afford,2))   
#__________________________________________________________________

#__________________________________________________________________
#main part of program
# imagine this is the main steps of the decomposition

# 1 -Figure out how much you can spend
FindSalary()
print ("Go find your car now!")

# OTHER steps that are not practical for programming at this time 
# 2 -Determine what type of vehicle you need/want
# 3 -Research what dealers have those types
# 4 -Go to dealership, test drive cars (could repeat this step – LOOP)
# 5 -Negotiate sale and purchase
#__________________________________________________________________



