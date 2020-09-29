from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def get_question_and_result():
    operator = choice(OPERATORS)
    value_1, value_2 = randint(0, 10), randint(0, 10)
    return (
         '{} {} {}'.format(value_1, operator, value_2),
         str(calculate(operator, value_1, value_2)),
    )


def calculate(func, value_1, value_2):
    if func == '+':
        return add(value_1, value_2)
    elif func == '-':
        return sub(value_1, value_2)
    elif func == '*':
        return mul(value_1, value_2)
