import operator  # https://docs.python.org/3/library/operator.html


class HonestCalculator:
    # messages
    messages = {"msg_0": "Enter an equation",
                "msg_1": "Do you even know what numbers are? Stay focused!",
                "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
                "msg_3": "Yeah... division by zero. Smart move...",
                "msg_4": "Do you want to store the result? (y / n):",
                "msg_5": "Do you want to continue calculations? (y / n):",
                "msg_6": " ... lazy",
                "msg_7": " ... very lazy",
                "msg_8": " ... very, very lazy",
                "msg_9": "You are",
                "msg_10": "Are you sure? It is only one digit! (y / n)",
                "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)",
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
            if not is_one_digit(self.result):
                # print(" ONE DIGIT CHECK SHOWS THAT is_one_digit(self.result):", is_one_digit(self.result))
                HonestCalculator.memory = self.result

            else:
                def obtain_answer(self, msg_index):
                    print(HonestCalculator.messages[f'msg_{msg_index}'])
                    answer = input()
                    if answer == "y":
                        # print("CURRENT MSG_INDEX:", msg_index)
                        if msg_index < 12:
                            msg_index += 1
                            return obtain_answer(self, msg_index)
                        else:
                            HonestCalculator.memory = self.result
                    elif answer == "n":
                        # print("the answer was NO:, current memory status:\n", HonestCalculator.memory)
                        # return HonestCalculator.memory
                        pass
                    else:
                        return obtain_answer(msg_index)
                msg_index = 10
                obtain_answer(self, msg_index)

            # HonestCalculator.memory = self.result
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


def is_one_digit(digit):
    return all([(-10 < digit < 10),  isinstance(digit, float), digit % 1 == 0])  # last statement needed purely for lazy messages


def check(v1, v2, v3):
    msg = ""
    if all([is_one_digit(v1), is_one_digit(v2)]):
        msg = msg + HonestCalculator.messages['msg_6']
    if any([v1 == 1 and v3 == "*", v2 == 1 and v3 == "*"]):
        msg = msg + HonestCalculator.messages['msg_7']
    if any([(v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-")]):
        msg = msg + HonestCalculator.messages['msg_8']
    if msg != "":
        msg = HonestCalculator.messages['msg_9'] + msg
        print(msg)


def main():
    print(HonestCalculator.messages['msg_0'])
    # read calc
    calc = HonestCalculator.from_string(input())

    if calc.x == "M":
        # print("LINE 113 calc.x currently:", HonestCalculator.memory)
        calc.x = HonestCalculator.memory
    if calc.y == "M":
        calc.y = HonestCalculator.memory

    if any([HonestCalculator.is_invalid_type(calc.x), HonestCalculator.is_invalid_type(calc.y)]):
        print(calc.messages['msg_1'])
        return main()
    else:
        calc.x, calc.y = float(calc.x), float(calc.y)
        if calc.oper in calc.ops:

            check(calc.x, calc.y, calc.oper)

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
