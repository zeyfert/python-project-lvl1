from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_result():
    value_1, value_2 = randint(1, 100), randint(1, 100)
    return {
        'question': '{} {}'.format(value_1, value_2),
        'result': str(calculate(value_1, value_2))
    }


def calculate(value_1, value_2):
    while value_1 != 0 and value_2 != 0:
        if value_1 > value_2:
            value_1 %= value_2
        else:
            value_2 %= value_1

    return value_1 + value_2
