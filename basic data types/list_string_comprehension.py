options = ["any", "are", "by", "day", "apple", "a", "b", "yay"]
valid_string = [
    string 
    for string in options 
    if (len(string)) >= 2 
    if (string[0] == 'a') 
    if (string[-1] == 'y')
    ]

print(valid_string)