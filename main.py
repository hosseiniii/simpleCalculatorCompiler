""" Simple Calculator """

# Constants
OPERATORS = ['=', '+', '-', '/', '*']


def get_inputs(inp):

    index = 0
    begin = index
    state = 0

    while index < len(inp):
        print("State:", state)

        if state == 0:
            if inp[index].isdigit() or inp[index] in ['-', '+']:
                begin = index
                state = 10

            elif inp[index].isalpha() or inp[index] == '_':
                begin = index
                state = 20

            elif inp[index] == '(':
                begin = index
                state = 30

            else:
                index -= 1
                state = 100

        elif state == 10:
            if inp[index].isdigit():
                pass
            elif inp[index] == '=':
                state = 50
            elif inp[index] == '+':
                state = 60
            elif inp[index] == '-':
                state = 70
            elif inp[index] == '*':
                state = 80
            elif inp[index] == '/':
                state = 90

        elif state == 11:
            pass

        elif state == 12:
            pass

        elif state == 13:
            pass

        elif state == 100:
            print("Wrong Input!")
            break

        index += 1


def remove_spaces(inp):

    for i in inp:
        if i == ' ':
            space_location = inp.index(i)
            inp = inp[:space_location] + inp[space_location+1:]

    return inp


# main part
counter = 1

input_string = str(counter) + ": "
user_input = input(input_string)

while user_input != "exit":
    get_inputs(remove_spaces(user_input))

    counter += 1
    input_string = str(counter) + ": "
    user_input = input(input_string)

