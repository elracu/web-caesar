# Import functions alphabet_position and rotate_character from the
# helpers.py file
from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    # Define values that will be used
    return_value = ''
    # Cycle through the characters in the phrase provided and
    # by using the alphabet_position and the rotate_character
    # functions generate the encrypted message
    for character in text:
        rotated_character = rotate_character(character,rot)
        return_value = return_value + rotated_character    

    return return_value


def main():

    # Asking for messgae and rotate by number
    phrase = input ( "Type a message:" )
    rotate_by = input ("Rotate by: ")
    # Turn rotate_by into an integer
    rotate_by_number = int(rotate_by)
    # printing the result of invoking the encrypt function
    print(encrypt(phrase, rotate_by_number))

    # Test print for each of the individual functions below

        # print (encrypt('a', 13))
    
        # print (rotate_character('B', 3))

        # letter_given = input ( "Input a letter" )
        # print (alphabet_position(letter_given))

if __name__ == '__main__':
    main()
