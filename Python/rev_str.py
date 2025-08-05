# Function to reverse a string
def reverseString(s):
  	
    # Reverse the string using slicing
    return s[::-1]

inp=input("enter a string: ")
print(reverseString(inp))