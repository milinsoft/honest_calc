import operator  # https://docs.python.org/3/library/operator.html


class HonestCalculator:
    # messages
    messages = ("Enter an equation",
                "Do you even know what numbers are? Stay focused!",
                "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
                "Yeah... division by zero. Smart move...",
                "Do you want to store the result? (y / n):",
                "Do you want to continue calculations? (y / n):",
                " ... lazy",
                " ... very lazy",
                " ... very, very lazy",
                "You are",
                "Are you sure? It is only one digit! (y / n)",
                "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "Last chance! Do you really want to embarrass yourself? (y / n)",
                )  # converted from dict to tuple to reduce memory consumption from 232 to 40 bytes

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    memory = 0.00

    def __init__(self, x, oper, y):
        self.x = x
        self.oper = oper
        self.y = y
        self.result = 0.00

    @staticmethod
    def is_invalid_type(char):
        return str(char).isalpha()

    @classmethod
    def from_string(cls, data):
        try:
            x, oper, y = data.split()
        except ValueError:
            print("An equation must be delimited with a space, like: 1 + 2")
            return main()
        return cls(x, oper, y)

    def result_saver(self):
        print(self.messages[4])
        answer_store = input().lower()
        if answer_store == "y":
            if not is_one_digit(self.result):
                HonestCalculator.memory = self.result
            else:
                def obtain_answer(msg_index):
                    print(HonestCalculator.messages[msg_index])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            return obtain_answer(msg_index)
                        else:
                            HonestCalculator.memory = self.result
                    elif answer == "n":
                        pass
                    else:
                        return obtain_answer(msg_index)

                obtain_answer(msg_index=10)

        elif answer_store == "n":
            return HonestCalculator.memory
        else:
            return self.result_saver()

    def continue_calc(self):
        print(self.messages[5])
        continue_calculations = input()

        if continue_calculations == "y":
            return main()
        elif continue_calculations == "n":
            exit()
        else:
            return self.continue_calc()


def is_one_digit(digit) -> bool:
    return all([(-10 < digit < 10),  isinstance(digit, float), digit % 1 == 0])  # last statement needed purely for lazy messages


def check(v1, v2, v3):
    msg = ""
    if all([is_one_digit(v1), is_one_digit(v2)]):
        msg = msg + HonestCalculator.messages[6]
    if all([v3 == "*", any([v2 == 1, v1 == 1])]):
        msg = msg + HonestCalculator.messages[7]
    if any([(v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-")]):
        msg = msg + HonestCalculator.messages[8]
    if msg != "":
        msg = HonestCalculator.messages[9] + msg
        print(msg)


def main():
    print(HonestCalculator.messages[0])
    # read calc
    calc = HonestCalculator.from_string(input())

    if calc.x == "M":
        calc.x = HonestCalculator.memory
    if calc.y == "M":
        calc.y = HonestCalculator.memory

    if any([HonestCalculator.is_invalid_type(calc.x), HonestCalculator.is_invalid_type(calc.y)]):
        print(calc.messages[1])
        return main()
    else:
        calc.x, calc.y = float(calc.x), float(calc.y)
        if calc.oper in calc.ops:

            check(calc.x, calc.y, calc.oper)

            try:
                calc.result = calc.ops[calc.oper](calc.x, calc.y)
            except ZeroDivisionError:
                print(calc.messages[3])
                return main()

            print(calc.result)

            calc.result_saver()

            calc.continue_calc()
        else:
            print(calc.messages[2])
            return main()


if __name__ == '__main__':
    main()
