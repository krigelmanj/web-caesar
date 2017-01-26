from helpers import alphabet_position, rotate_character

from sys import argv, exit

def encrypt(text, rot):
    return_list = []
    for char in text:
        rotated_character = rotate_character(char, rot)
        return_list.append(rotated_character)
    return_string = ''.join(return_list)
    return return_string

def user_input_is_valid(cl_args):
    if len(cl_args) <= 1:
        return False
    if cl_args[1].isdigit() == True:
        return True
    else:
        return False

def main():
    if user_input_is_valid(argv) == False:
        print('usage: python3 caesar.py n')
        exit()
    # inputstring = str(input('Type a message:'))
    # inputrotate = int(argv[1])
    # print(encrypt(inputstring, inputrotate))

if __name__ == '__main__':
    main()
