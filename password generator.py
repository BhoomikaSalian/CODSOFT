import string
import random
def generate_password(length, complexity):
  'Generates a password of the specified length and complexity.'
                   # Define the character sets to use for generating the password.
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  special_characters = string.punctuation
                   # Determine the character set to use based on the specified complexity.
  if complexity == "low":
    character_set = lowercase_letters + digits
  elif complexity == "medium":
    character_set = lowercase_letters + uppercase_letters + digits
  elif complexity == "high":
    character_set = lowercase_letters + uppercase_letters + digits + special_characters
  else:
    raise ValueError("Invalid complexity level.")
                  # Generate a random password of the specified length.
  password = "".join(random.choice(character_set) for i in range(length))
  return password
                  # Get the length and complexity of the password from the user.
length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity of the password (low, medium, or high): ")
                   # Generate and print the password.
password = generate_password(length, complexity)
print("Your password is:", password)
