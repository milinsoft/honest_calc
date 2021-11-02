import operator  # https://docs.python.org/3/library/operator.html


class HonestCalculator:
    # messages
    messages = {"msg_0": "Enter an equation",
                "msg_1": "Do you even know what numbers are? Stay focused!",
                "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
                "msg_3": "Yeah... division by zero. Smart move...",
                "msg_4": "Do you want to store the result? (y / n):",
                "msg_5": "Do you want to continue calculations? (y / n):"
                }

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
        x, oper, y = data.split()
        return cls(x, oper, y)

    def result_saver(self):
        print(self.messages['msg_4'])
        answer_store = input().lower()
        if answer_store == "y":
            HonestCalculator.memory = self.result
            return HonestCalculator.memory
        elif answer_store == "n":
            return HonestCalculator.memory
        else:
            return self.result_saver()

    def continue_calc(self):
        print(self.messages['msg_5'])
        continue_calculations = input()

        if continue_calculations == "y":
            return main()
        elif continue_calculations == "n":
            exit()
        else:
            return self.continue_calc()


def main():
    print(HonestCalculator.messages['msg_0'])
    # read calc
    calc = HonestCalculator.from_string(input())

    if calc.x == "M":
        calc.x = HonestCalculator.memory
    if calc.y == "M":
        calc.y = HonestCalculator.memory

    if any([HonestCalculator.is_invalid_type(calc.x), HonestCalculator.is_invalid_type(calc.y)]):
        print(calc.messages['msg_1'])
        return main()
    else:
        calc.x, calc.y = float(calc.x), float(calc.y)
        if calc.oper in calc.ops:
            try:
                calc.result = calc.ops[calc.oper](calc.x, calc.y)
            except ZeroDivisionError:
                print(calc.messages['msg_3'])
                return main()
            print(calc.result)

            calc.result_saver()
            calc.continue_calc()
        else:
            print(calc.messages['msg_2'])
            return main()


if __name__ == '__main__':
    main()
