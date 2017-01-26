def get_initials(fullname):
    """given a person's name, return a person's initials(uppercase)"""
    initials = ''
    fullname = fullname.title()

    for char in fullname:
        if char.isupper() == True:
            initials += char
    return initials


def main():
    username = input("What is your full name?")
    answer = get_initials(str(username))
    print("The initials of", username, "are", answer)

if __name__ == '__main__':
    main()