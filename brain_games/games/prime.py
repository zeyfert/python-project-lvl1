from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_result():
    value = randint(1, 3571)
    result = 'yes' if is_prime(value) else 'no'
    return (value, result)


def is_prime(value):
    """ Checks if the value is prime or not

        Parameters:
            value (int): the value for check

        Returns:
            result (bool): True if prime else False

    """
    divider = 3
    if value < 2 or value % 2 == 0:
        return False
    divider = 3
    while divider <= value // 2:
        if value % divider == 0:
            return False
        divider += 1
    return True
