import operator

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

def is_invalid_type(char):
    return char.isalpha()


def calculate_result(arg1, sign, arg2):
    ...


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
        x, y = float(x), float(y)
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        if oper in ops:
            try:
                result = ops[oper](x, y)
                print(result)
            except ZeroDivisionError:
                print(msg_3)
                return main()
        else:
            print(msg_2)
            return main()


if __name__ == '__main__':
    main()
