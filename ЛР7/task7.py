# Ask the user to input a string
user_input = input("Enter a string: ")

# Convert the string to lowercase for easier counting
user_input = user_input.lower()

# Initialize counters for vowels and consonants
vowels_count = 0
consonants_count = 0

# Define sets of vowels and consonants
vowels_set = set("aeiou")
consonants_set = set("bcdfghjklmnpqrstvwxyz")

# Count the number of vowels and consonants in the string
for char in user_input:
    if char in vowels_set:
        vowels_count += 1
    elif char in consonants_set:
        consonants_count += 1

# Print the results
print("Number of vowels:", vowels_count)
print("Number of consonants:", consonants_count)
