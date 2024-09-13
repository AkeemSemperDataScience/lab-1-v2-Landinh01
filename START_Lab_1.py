def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb * 1024 * 1024 * 1024
    return num_bytes



def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    if not isinstance(name, str) or name == "":
        return None
    
    length= len(name)
    if length % 2 == 0:
        is_odd = False
    else:
        is_odd = True

    return is_odd



def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    # Check if the index exists in the string
    if input_number < len(input_string):
        # Return the character at the given index
        character_at = input_string[input_number]
    else:
        # If the index is out of range, return -1
        character_at = -1
    return character_at


def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []

    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Check if the word is a number
                if word.isdigit():
                    # Add the number to the list (convert to integer)
                    list_of_nums.append(int(word))

    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    from collections import Counter
    # Count the frequency of each number in the list
    count = Counter(list_numbers)
    
    # Find the mode, which is the number with the highest frequency
    mode_of_list = count.most_common(1)[0][0]

    return mode_of_list


def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    
    # Define the values of each type of coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    total = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.