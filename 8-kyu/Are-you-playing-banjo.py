# Question: Are you playing banjo?

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.


#Solution 

def are_you_playing_banjo(name):
    # using index value to take 1st letter 
    if(name[0]=='R' or name[0]=='r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#Local test cases

print(are_you_playing_banjo("martin"))  #martin does not play banjo
print(are_you_playing_banjo("Rikke"))   #Rikke plays banjo
print(are_you_playing_banjo("bravo"))   #bravo does not play banjo
print(are_you_playing_banjo("rolf"))    #rolf plays banjo