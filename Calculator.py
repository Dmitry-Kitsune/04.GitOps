class Calculator:
#empty constructor
 def __init__(self):
   pass
#add method - given two numbers, return the addition
 def add(self, x, y):
  return x + y
#multiply method - given two numbers, return the  
#multiplication of the two
 def multiply(self, x, y):
  return x * y
#subtract method - given two numbers, return the value
#of first value minus the second
 def subtract(self, x, y):
  return x - y
#divide method - given two numbers, return the value
#of first value divided by the second
 def divide(self, x, y):
 if y != 0:
  return x / y