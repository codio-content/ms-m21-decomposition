__author__ = 'shoeppner'

#age will be sent from challenge
age = int(sys.argv[1])

#function
def DriveStatus():
  age=14
  if age ==16:
      print ('you can get your license')
  elif age < 16:
      print ('you are too young to get your license')
  else:
      print ('you already have your license')
      
#main program     
DriveStatus()