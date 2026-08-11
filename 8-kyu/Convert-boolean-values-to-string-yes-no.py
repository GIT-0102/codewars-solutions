# Question Convert boolean values to strings 'Yes' or 'No'.

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

#solution 

def bool_to_word(boolean):
    if boolean== True:
        return 'Yes'
    else:
        return 'No'
    
#test cases
print(bool_to_word(True))  # Output: 'Yes'
print(bool_to_word(False))  # Output: 'No'