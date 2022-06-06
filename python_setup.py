# print("Hello from inside a file!")


def hello():
    print('Greeting Otto')


# hello()


def pack(sandwhich, snack, drink):
    lunch = [f'{sandwhich},{snack},{drink}']

    print(lunch)


# pack('Sandwhich', 'Chips', 'Coke')


my_lunch = ['sandwich', 'chips', 'apple']
no_lunch = []


def lunch(array):

    i = 0
    while i < len(array):

        if i == 0:
            print(f'First I eat {array[i]}')
            i += 1
        elif i <= len(array):
            print(f'Next I eat {array[i]}')
            i += 1
    print('My lunchbox is now empty')


# lunch(my_lunch)
