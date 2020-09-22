from prompt import string


def start_game(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION, '\n')
    name = string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    correct_answers = 0
    while correct_answers < 3:
        question, result = game.get_question_and_result().values()
        print(question)
        user_answer = string('Your answer: ')
        if result != user_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(user_answer, result))
            print("Let's try again, {}".format(name))
            break
        else:
            print('Correct!')
            correct_answers += 1
    if correct_answers == 3:
        print('Congratulations, {}'.format(name))
