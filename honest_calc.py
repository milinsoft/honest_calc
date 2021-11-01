msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def is_invalid_type(char):
    return char.isalpha()


def is_valid_operator(operator):
    return operator in {"+", "-", "*", "/"}


def main():
    print(msg_0)
    # read calc
    calc = input()
    # split
    x, oper, y = calc.split()

    if any([is_invalid_type(x), is_invalid_type(y)]):
        print(msg_1)
        return main()
    else:
        if is_valid_operator(oper):
            exit()
        else:
            print(msg_2)
            return main()


if __name__ == '__main__':
    main()
