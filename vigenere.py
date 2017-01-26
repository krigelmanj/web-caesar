from helpers import alphabet_position, rotate_character

def encrypt(string, rotword):
    return_list = []
    return_string = []
    rotchar = 0
    for char in string:
        if char.isalpha() == True:
            rotamt = 0
            rotamt = alphabet_position(rotword[rotchar]) - 1
            newchar =rotate_character(char, rotamt)
            return_list.append(newchar)
            rotchar = (rotchar + 1) % len(rotword)
        else:
            return_list.append(char)
    return_string = ''.join(return_list)
    return return_string

def main():
    inputstring = str(input('Type a message:'))
    inputrotateword = str(input('Rotate by:'))
    #print(encrypt(inputstring, inputrotateword))

if __name__ == '__main__':
    main()
