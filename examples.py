

# my_set = {12, 55, 33, 40, 55, 33, 20, 12}

# print(my_set)


# new_set = {2, 3, 5}


# new_set.add(8)


# print(new_set)

# another_tuples = (4, 8, 5, 9)


# print(another_tuples)


# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# for day in days:
#     print(day)


# x = 10
# add_list = [10, 6, 12, 4, 5]

# for element in add_list:
#     x += element
#     print(x)

#     i = 1
#     while i < 10:
#         i += 5
#         print(i)


# favorite_movie = "Top Gun"

# if favorite_movie == 'Top Gun':
#     print("that's a great movie")
# else:
#     print("that's not a good movie")


# movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

# for movie in movie_list:
#     if movie == "blueberries":
#         print("item is fruit and not a movie")
#     elif movie == "Toyota":
#         print('item is a car and not a movie')
#     else:
#         print(movie)


# a = 5
# b = 5
# c = 12

# addition = a + b
# print(addition)

# subtraction = b - c
# print(subtraction)


# if a == b:
#     print("this was equal")


# Number 1
def arb_args(*args):
    for element in args:
        print(element)


arb_args('Hello', 'How', 'Are', 'You', 'Doing?')


# Number 2
def numbers(first_func, second_func):

    def add(first_func):
        first = first_func + 10
        print(first)
    add(first_func)

    def subtract(second_func):
        second = second_func - 5
        print(second)
    subtract(second_func)


numbers(20, 5)


# Number 3
def lunch_lady(name, preference):
    if (preference == ''):
        print(name, 'mystery meat')
    else:
        print(name, preference)


lunch_lady('Otto', '')


# Number 4
def sum_n_product(num1, num2, product):
    sum = num1 + num2
    return product, sum


print(sum_n_product(3, 7, 'Onions'))

# Number 5


def alias_arb_args(*args):
    arb_args(*args)


print('Hello', "there!")

# Number 6


#
def name_args(**kwargs):
    for element in kwargs.values():
        print(f"{element}: {kwargs[element]}")


name_args(a='a', b='b')


def all_true(array):
    for element in array:
        print(bool(element))


someArray = ['', 5, 'Hello']

# all_true(someArray)


def one_true(array):
    for element in array:
        element


def my_func(array):
    x = any(array)
    return print(x)


my_func(someArray)
