from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_result():
    progression, index = get_progression_and_index()
    result = progression[index]
    progression[index] = '...'
    return {
        'question': str.join(' ', progression),
        'result': result,
    }


def get_progression_and_index():
    first_value, step, index = randint(1, 100), randint(1, 10), randint(0, 9)
    last_value = step * 10 + first_value
    return [str(i) for i in range(first_value, last_value, step)], index
