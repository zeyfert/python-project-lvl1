from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_result():
    """ Method provides a random value
        And result of check "Is it even?"
        The answer may be "yes" or "no"

        Returns:
            dictionary with value and answer
    """
    value = randint(1, 10)
    result = 'yes' if is_even(value) else 'no'
    return (value, result)


def is_even(value):
    """ Method checks if a value is even or not

        Parameters:
            value (int): the value which should be ckecked
        Returns:
            result of check (bool): it may be true or false
    """
    return value % 2 == 0
