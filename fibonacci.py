import math

def fibonacci(n):
  if n == 0:
    last = 0
  elif n == 1:
    last = 1
  else:
    GR = 1.618034
    firstNum = GR ** n
    secNum = (1 - GR)
    thirdNum = secNum ** n
    numerator1 = firstNum - thirdNum
    demo1 = math.sqrt(5)
    last = numerator1 / demo1
  return last
