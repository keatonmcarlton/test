def decode(encoded):
    decoded = ''
    for char in encoded:
        if int(char) - 3 >= 0:
            decoded += str(int(char) - 3)
        else: #needs to loop back to the top of 0-9 order if it cant be subtracted
            decoded += str(int(char) + 7)
    print(f'The encoded password is {encoded}, and the original password is {decoded}.')
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
    encoded_password = '' #these need to be here or they will be reset every time
    decoded_password = '' #these need to be here or they will be reset every time
    while keepgoing:
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
            decode(encoded_password)
        elif userinput == 3:
            keepgoing = False
        else:
            print()
            pass


if __name__ == '__main__':
    main()
