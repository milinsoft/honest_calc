import operator  # https://docs.python.org/3/library/operator.html


# messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


def is_invalid_type(char):
    return str(char).isalpha()


def result_saver(_result, _memory):
    print(msg_4)
    answer_store = input().lower()

    if answer_store == "y":
        _memory = _result
        return _memory

    elif answer_store == "n":
        return _memory
    else:
        return result_saver(_result, _memory)


def continue_calc():
    print(msg_5)
    continue_calculations = input()

    if continue_calculations == "y":
        return main()
    elif continue_calculations == "n":
        exit()
    else:
        return continue_calc()


memory = 0.00  # type(float)


def main():
    global memory

    print(msg_0)
    # read calc
    calc = input()
    # split
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    if any([is_invalid_type(x), is_invalid_type(y)]):
        print(msg_1)
        return main()
    else:
        x, y = float(x), float(y)
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        if oper in ops:
            try:
                result = ops[oper](x, y)
            except ZeroDivisionError:
                print(msg_3)
                return main()
            print(result)

            memory = result_saver(result, memory)
            continue_calc()

        else:
            print(msg_2)
            return main()


if __name__ == '__main__':
    main()


