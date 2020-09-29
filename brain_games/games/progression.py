from random import randint


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question_and_result():
    """ Provides question for an user and correct answer

        Returns:
            dictionary:
                - question (str): progression with one empty value
                - result (int): the value is missed in the progression

        Example:
            {
                'question': "57, 61, '...', 69, 73, 77, 81, 85, 89, 93",
                'result': 65
            }
    """
    first_value, step = randint(1, 100), randint(1, 10)
    last_value = step * PROGRESSION_LENGTH + first_value
    random_index = randint(1, PROGRESSION_LENGTH - 1)
    progression = get_progression(first_value, last_value, step)
    searching_value = progression[random_index]
    progression[random_index] = '...'
    return (
        str(progression).strip('[]'),
        str(searching_value),
    )


def get_progression(first_value, last_value, step):
    """ Provides progression based on the parameters.

        Parameters:
            first_value (int)
            last_value (int)
            step (int)

        Return:
            progression (list)

        Example:
            [57, 61, 65, 69, 73, 77, 81, 85, 89, 93]
    """
    return list(range(first_value, last_value, step))
