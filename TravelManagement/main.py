import re

# Open the file
filename = input("Enter the file name: ")
try:
    file = open(filename, 'r')
except:
    print("File cannot be opened:", filename)
    quit()

# Read the file contents
data = file.read()

# Close the file
file.close()

# Find all numbers using regular expression
numbers = re.findall('[0-9]+', data)

# Convert numbers to integers and compute the sum
total_sum = sum(int(num) for num in numbers)

# Print the sum
print("Sum:", total_sum)
