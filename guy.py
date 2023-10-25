
def main():
    print('hello')

    guy = input("give a numerical string: ")
    newguy = []
    guy.split()
    print(guy)
    for i in range(0, len(guy)):
        guy[i] = (int(guy[i]) + 3) % 10
        print(newguy)


if __name__ == '__main__':
    main()
