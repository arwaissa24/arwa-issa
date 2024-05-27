def factorial(n):

  if n < 0:
    return 
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

# Get the number from the user
num = int(input("Enter a non-negative integer: "))

# Calculate the factorial
factorial_result = factorial(num)

# Print the result
if isinstance(factorial_result, str):
  print(factorial_result)
else:
  print(f"The factorial of {num} is {factorial_result}")
