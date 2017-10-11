def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared) <--%d because is comming from def (function)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.
square(10)


--------------------------
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

-------------------------------

def one_good_turn(n):
  return n + 1
    
def deserves_another(m):
  return one_good_turn(m) + 2  <0 use the result of the frist funciton to apply in the second
  
  ---------------------------
  def cube(number):
  return number * number * number

def by_three(number):
  
  if number % 3 == 0: <-- if the number is devided by 3 
    return cube(number)
  
  else:
    return False
  
  -----------------
  def distance_from_zero(p):
  if type(p) == int or type(p) == float:
    return abs(p)
  else:
    return "Nope"
