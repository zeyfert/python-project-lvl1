from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_result():
    value = randint(1, 3571)
    return {
        'question': value,
        'result': is_prime(value)
    }


def is_prime(value):
    divider = 2
    while value % divider != 0:
        divider += 1
    return 'yes' if value == divider else 'no'
