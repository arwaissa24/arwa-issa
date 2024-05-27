def binary_to_decimal(binary_str):


  # Check if the input string only contains 0s and 1s
  if not all(char in '01' for char in binary_str):
    return None

  decimal_value = 0
  power = 0
  for digit in binary_str[::-1]:
    # Convert digit to integer (handles potential '0' or '1' input)
    digit_int = int(digit)
    decimal_value += digit_int * (2 ** power)
    power += 1
  return decimal_value

# Get binary input from the user
while True:
  binary_str = input("Enter a binary number: ")
  decimal_equivalent = binary_to_decimal(binary_str)

  if decimal_equivalent is None:
    print("Invalid binary input. Please enter a string containing only 0s and 1s.")
  else:
    print(f"The decimal equivalent of {binary_str} is {decimal_equivalent}.")
    break
