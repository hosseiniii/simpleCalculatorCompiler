"""
 Simple Calculator

    Seyyed Sadegh Hosseini
    9621160009

"""

tokens = []
variable_name = ""
number = ""


class Type:
    ID = 1
    EQUAL = 2
    NUMBER = 3
    REAL = 4
    LPAR = 5
    RPAR = 6
    PLUS = 7
    MINUS = 8
    MUL = 9
    DIVIDE = 10


def get_inputs(inp):

    index = 0
    state = 0

    while index < len(inp):
        global variable_name
        global number

        print("State:", state)

        if state == 0:
            if inp[index].isalpha() or inp[index] == '_':
                state = 10

            elif inp[index].isdigit():
                state = 20

            elif inp[index] == '(':
                state = 30

            elif inp[index] == ')':
                state = 40

        elif state == 10:
            if inp[index].isalpha():
                state = 10
                variable_name += inp[index]
                index += 1

            elif inp[index].isdigit():
                state = 10
                variable_name += inp[index]
                index += 1

            elif inp[index] == '_':
                state = 10
                variable_name += inp[index]
                index += 1

            else:
                tokens.append([Type.ID, variable_name])
                state = 0
                variable_name = ""

        elif state == 20:
            if inp[index].isdigit():
                state = 20
                number += inp[index]
                index += 1

            elif inp[index] == '.':
                state = 21
                number += inp[index]
                index += 1

            else:
                tokens.append([Type.NUMBER, number])
                state = 0
                number = ""

        elif state == 21:
            if inp[index].isdigit():
                state = 22
                number += inp[index]
                index += 1

            else:
                tokens.append([Type.REAL, number])
                state = 0
                number = ""

        elif state == 12:
            pass

        elif state == 13:
            pass


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

