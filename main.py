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

        if state == 0:
            if inp[index].isalpha() or inp[index] == '_':
                state = 10

            elif inp[index].isdigit():
                state = 20

            elif inp[index] == '(':
                state = 30

            elif inp[index] == ')':
                state = 40

            elif inp[index] == '=':
                state = 50

            elif inp[index] == '*':
                state = 60

            elif inp[index] == '/':
                state = 70

            elif inp[index] == '+':
                state = 80

            elif inp[index] == '-':
                state = 90

            elif inp[index] == '#':
                state = 100

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
                state = 21
                number += inp[index]
                index += 1

            else:
                tokens.append([Type.REAL, number])
                state = 0
                number = ""

        elif state == 30:
            tokens.append([Type.LPAR, ""])
            state = 0
            index += 1

        elif state == 40:
            tokens.append([Type.RPAR, ""])
            state = 0
            index += 1

        elif state == 50:
            tokens.append([Type.EQUAL, ""])
            state = 0
            index += 1

        elif state == 60:
            tokens.append([Type.MUL, ""])
            state = 0
            index += 1

        elif state == 70:
            tokens.append([Type.DIVIDE, ""])
            state = 0
            index += 1

        elif state == 80:
            tokens.append([Type.PLUS, ""])
            state = 0
            index += 1

        elif state == 90:
            tokens.append([Type.MINUS, ""])
            state = 0
            index += 1

        elif state == 100:
            for t in tokens:
                typ = t[0]
                type_str = ""
                if typ == 1:
                    type_str = "ID"
                elif typ == 2:
                    type_str = "EQUAL"
                elif typ == 3:
                    type_str = "NUMBER"
                elif typ == 4:
                    type_str = "REAL"
                elif typ == 5:
                    type_str = "LPAR"
                elif typ == 6:
                    type_str = "RPAR"
                elif typ == 7:
                    type_str = "PLUS"
                elif typ == 8:
                    type_str = "MINUS"
                elif typ == 9:
                    type_str = "MUL"
                elif typ == 10:
                    type_str = "DIVIDE"

                print("(" + str(type_str), ", ", str(t[1])+ ")", end=" ")
            index = len(inp)
            print()


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

