import random
import string

def generate_password(min_length,numbers =True,special_characters =True):
    letters =string.ascii_letters
    digits =string.digits
    special =string.punctuation
    
    characters =letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd=""
    meets_criteria= False
    has_numbers = False
    has_special =False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_numbers = True
        if new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria= has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd


min_length = int(input("Enter min length: "))
has_numbers = input("Do you want numbers: (y/n)?").lower()=="y"
has_special =input("Do you want special characters: (y/n)?").lower()=="y"
pwd =generate_password(min_length,has_numbers,has_special)
print(pwd)