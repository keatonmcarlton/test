def decoding():
    guy3 = input("Please enter your password to decode: ")
    print()
    newguy2 = []
    guystring = ''
    guy3.split()
    for i in range(0, len(guy3)):
        newguy2.append((int(guy3[i]) + 7) % 10)
        guystring += str(newguy2[i])
    print('Your password has been decoded and stored!\n')
    return guystring


def encoding():
    guy = input("Please enter your password to encode: ")
    print()
    newguy = []
    guystring = ''
    guy.split()
    for i in range(0, len(guy)):
        newguy.append((int(guy[i]) + 3) % 10)
        guystring += str(newguy[i])
    print('Your password has been encoded and stored!\n')
    return guystring


def main():
    keepgoing = True
    while keepgoing:
        encoded_password = ''
        decoded_password = ''
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        userinput = int(input('Please enter an option: '))

        if userinput == 1:
            print()
            encoded_password = encoding()
        elif userinput == 2:
            print()
            decoded_password = decoding()
        elif userinput == 3:
            keepgoing = False
        else:
            print()
            pass


if __name__ == '__main__':
    main()
