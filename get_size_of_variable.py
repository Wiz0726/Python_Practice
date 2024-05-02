import sys

# Define your variable
variable = "Hello, World"

# Get the size of the variable in bytes
variable_size = sys.getsizeof(variable)

# Print the size of the variable
print("Size of the variable:", variable_size, "bytes")