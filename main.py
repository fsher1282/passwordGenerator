import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '-', ']']

numbers = range(0, 9)

password_char = []


# Randomly select a character from list and append to another list
def rand_selector(nr, lst):
    for i in range(nr):
        rand = random.randint(0, len(lst)-1)
        password_char.append(lst[rand])


# Takes list of characters and scrambles them and return as string
def rand_combo(pw_lst):
    password = ''
    for i in range(len(pw_lst)):
        rand = random.randint(0, len(pw_lst)-1)
        password += str(pw_lst[rand])
        pw_lst.remove(pw_lst[rand])
    return password


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")

    nr_letters = int(input("How many letters would you like in your password? \n"))

    nr_symbols = int(input(f"How many symbols would you like? \n"))

    nr_numbers = int(input(f"How many numbers would you like? \n"))

    rand_selector(nr_symbols, symbols)
    rand_selector(nr_numbers, numbers)
    rand_selector(nr_letters, letters)
    print('Your password is: ' + rand_combo(password_char))
