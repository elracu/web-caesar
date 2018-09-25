# Create alphabet index as a dictionary
alphabet_index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4,
'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 
'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
'x':23, 'y':24, 'z':25}

def alphabet_position(letter):
    # Turn the input into lowercase
    letter = letter.lower()
    # Use get method to get the value associated with the letter
    return (alphabet_index.get(letter)) 

def rotate_character(char, rot):
    # Define values that will be used
    rotated_number = 0
    new_character = ''

    # Check if character is alphabetic
    if char.isalpha():
        cycle_by_number = alphabet_position(char) + rot
        # If it is, calculate the rotated_number based on the provided char and rot
        if cycle_by_number < 26:
            rotated_number = cycle_by_number
        else:
            rotated_number = rotated_number + (cycle_by_number % 26)
        # Once rotated_number is determined reference alphabet_index to get corresponding key
        # and assign to new_character
        for (k,v) in alphabet_index.items():
            if v == rotated_number:
                new_character = k
            # Check if char provided is capitalized. If it is, capitalize new character     
            if char.isupper():
                new_character = new_character.upper()

        return new_character
    else:
        return char