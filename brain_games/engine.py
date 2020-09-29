from prompt import string


def play(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION, '\n')
    name = string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    answers_count = 0
    while answers_count < 3:
        question, result = game.get_question_and_result()
        print(question)
        user_answer = string('Your answer: ')
        if result != user_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(user_answer, result))
            print("Let's try again, {}".format(name))
            return
        else:
            print('Correct!')
            answers_count += 1
    else:
        print('Congratulations, {}'.format(name))
