def alphabet_position(letter):
    '''Returns the alphabet position of a letter'''
    #Convert to lower case for easier handling
    letter = letter.lower()
    #subtracts the ascii value of a to set 'a' to 1
    return ord(letter) - ord('a')  +1


def rotate_character(char, rot):
    #check if character is a letter
    if char.isalpha() == True:
        #run alphabet_position to get a loopable number set
        original_alphabet_position = alphabet_position(char)
        #print('original_alphabet_position', original_alphabet_position)
        #rotate the numeric value of character by the rot value given
        rotated_char = original_alphabet_position + rot
        #print('rotated_char', rotated_char)
        #use modulus to account for rotated values outside of range
        adjustment = rotated_char % 26
        #print('adjustment', adjustment)
        # Use the inverse of the adjustment used in alphabet_position to return the value to ascii value of desired character
        adjustment2 = (adjustment + ord('a') - 1)
        #print('adjustment2', adjustment2)
        #use the cha() built in function to convert to a letter
        adjustment3 = chr(adjustment2)
        #print('adjustment3', adjustment3)
        return_letter = adjustment3
        #The task demanded an uppercase letter, if the given character was an uppercase letter. Runs a check against original character and uppercases it if needed
        if char.isupper() == True:
            return_letter= return_letter.upper()
            return return_letter
        else:
            return return_letter
    #if the character given is not alphabetic, returns character as given value
    else:
        return char
