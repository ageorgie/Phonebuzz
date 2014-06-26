def fizzbuzz(num):
  print "I AM HERE"
  result = []
  for i in range(1, num+1):
    if (i%3==0) and (i%5==0):
      result.append("Fizz Buzz")
    elif(i%3==0):
      result.append("Fizz")
    elif(i%5==0):
      result.append("Buzz")
    else:
      result.append(str(i))
  return ", ".join(result)