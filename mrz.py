class token:
    def __init__(self, kt, v):
        self.keytype = str(kt)
        self.value = v


###########
buf = []
RE = []


def main():
    index = 0
    j = 0
    state = 0
    start = 0
    temp = []
    # token re
    # buf = input("Your equation:\t")
    buf = "a=  1+2\n"
    while (buf[index] != '\n'):
        if (state == 0):
            if ((buf[index] >= 'a' and buf[index] <= 'z') or (buf[index] >= 'A' and buf[index] <= 'Z')):
                state = 20
                temp.append(buf[index])
                index = index + 1
            elif (buf[index] >= '0' and buf[index] <= '9'):
                state = 10
                temp.append(buf[index])
                index = index + 1
            elif (buf[index] == '*' or buf[index] == '+' or buf[index] == '-' or buf[index] == '/' or buf[
                index] == '(' or buf[index] == ')' or buf[index] == '='):
                state = 30
            else:
                index = index + 1

        elif (state == 20):
            i = 1
            while ((buf[index] >= 'a' and buf[index] <= 'z') or (buf[index] >= 'A' and buf[index] <= 'Z') or (
                    buf[index] >= '0' and buf[index] <= '9') or buf[index] == '_'):
                temp.append(buf[index])
                # i=i+1
                index = index + 1
            state = 0
            RE.append(token("ID", temp))

        elif (state == 10):
            i = 1
            while (buf[index] >= '0' and buf[index] <= '9'):
                temp.append(buf[index])
                # i=i+1
                index = index + 1
            if (buf[index] == '.'):
                while (buf[index] >= '0' and buf[index] <= '9'):
                    temp.append(buf[index])
                    # i=i+1
                    index = index + 1
                RE.append(token("DOUBLE", temp))
                state = 0
            else:
                RE.append(token("INT", temp))
                state = 0

        elif (state == 30):
            if (buf[index] == '+'):
                RE.append(token("PLUS", " "))
            if (buf[index] == '-'):
                RE.append(token("MINUS", " "))
            if (buf[index] == '*'):
                RE.append(token("MULTIPLY", " "))
            if (buf[index] == '/'):
                RE.append(token("DIVIDE", " "))
            if (buf[index] == '('):
                RE.append(token("LPAR", " "))
            if (buf[index] == ')'):
                RE.append(token("RPAR", " "))
            if (buf[index] == '='):
                RE.append(token("APPOINT", " "))
            index = index + 1
            state = 0

    print(RE)

    for r in RE:
        print(r.value)


main()
