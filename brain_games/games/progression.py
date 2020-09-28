from random import randint


DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def get_question_and_result():
    progression, index = get_progression_and_index()
    result = progression[index]
    progression[index] = '...'
    return {
        'question': str.join(' ', progression),
        'result': result,
    }


def get_progression_and_index():
    first_value, step, index = randint(1, 100), randint(1, 10), randint(0, LENGTH_PROGRESSION)
    last_value = step * LENGTH_PROGRESSION + first_value
    return [str(i) for i in range(first_value, last_value, step)], index
