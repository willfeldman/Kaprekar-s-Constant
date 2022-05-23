start_number = input("Enter any four-digit number using at least two different digits (leading zeros are allowed): ")

current_number = int(start_number)

while current_number != 6174:
  print(" ")
  
  # Sort array of the current_number by decending order of digits for first_number and ascending order for second_number
  second_number_array = [int(x) for x in str(current_number)]
  second_number_array = sorted(second_number_array)
  first_number_array = reversed(second_number_array)
  
  # Convert the new numbers back to an int
  first_number_strings = [str(integer) for integer in first_number_array]
  first_number_string = "".join(first_number_strings)
  first_number = int(first_number_string)
  print(str(first_number))
  
  second_number_strings = [str(integer) for integer in second_number_array]
  second_number_string = "".join(second_number_strings)
  second_number = int(second_number_string)
  print(str("- " + str(second_number)))

  # Subtract and reset current_number
  print("-----")
  current_number = first_number - second_number
  print(str(current_number))
  print(" ")

print("It always leads back to 6174...")