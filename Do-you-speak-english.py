# Codewars question: Do you speak English?

# Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".
# The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
# Upper or lower case letter does not matter -- "eNglisH" is also correct.
# Return value as boolean values, true for the string to contains "English", false for it does not.

#Solution

def sp_eng(sentence): 
    x=sentence.lower()
    if 'english' in x:
        return True
    else:
        return False
    
#Local test cases
    
print(sp_eng("english"))           # True
print(sp_eng("egnlish"))           # False
print(sp_eng("engliish"))          # False
print(sp_eng("1234egn lis;h"))     # False
print(sp_eng("1234english ;k"))    # True
print(sp_eng("English"))           # True
print(sp_eng("eNgliSh"))           # True
print(sp_eng("1234#$%%eNglish ;k9"))  # True
print(sp_eng("EGNlihs"))           # False
print(sp_eng("1234englihs**"))     # False
print(sp_eng(""))                  # False