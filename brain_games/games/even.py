from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_result():
    value = randint(1, 10)
    return {
        'question': value,
        'result': is_even(value)
    }


def is_even(value):
    return 'yes' if value % 2 == 0 else 'no'
