from main import largest_number


def main():
    datum = [
        '73 737',
        '737 73',
        '12323 34 2',
        '1000 999 990 900 90 9',
        '9 7 79 759 5',
        '5 12 4 3 5 0 43 4 4 41 48 490',
        '2 7 79 70 7 71',
        '6 69 77 76 78 2 7 79 70 7 71',
        '79 71 0 77 770 9 73 40 70 7 7 76',
        '4 484 4 4 8 8 84'
        '2 4 5 2 10',
        '1 783 2',
        '0 1 5 9',
    ]

    for data in datum:
        print(largest_number(data, sep=' '))


if __name__ == '__main__':
    main()
