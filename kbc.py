import random
from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    if question["answer"] == answer:
        return True
    return False


def lifeLine(ques):
    # TODO: optimize this mess
    count = 2
    temp = 1
    while count:
        if ques["answer"] != temp:
            choice = "option" + str(temp)
            ques[choice] = ""
            count -= 1
            temp = int(temp)
        temp += 1

    return ques


def kbc():
    print("Welcome to the KBC game!!")

    reward = 0
    incorrect = False
    question = 0
    has_used_lifeLine = False
    for i in range(len(QUESTIONS)):
        print(f'Price Won: {reward}')
        print(f'\tQuestion 1: {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations
        if ans == "quit":
            break
        elif ans == "lifeline":
            if not has_used_lifeLine and (i != 14):
                has_used_lifeLine = True
                question = lifeLine(QUESTIONS[i])
                print(f'\tQuestion {i}: {question["name"]}')
                print(f'\t\tOptions:')
                print(f'\t\t\tOption 1: {question["option1"]}')
                print(f'\t\t\tOption 2: {question["option2"]}')
                print(f'\t\t\tOption 3: {question["option3"]}')
                print(f'\t\t\tOption 4: {question["option4"]}')
                ans = input('Your choice ( 1-4 ) : ')
            else:
                print("You can't use lifeline at this stage!!")
                ans = input('Your choice ( 1-4 ) : ')

        if isAnswerCorrect(QUESTIONS[i], int(ans)):
            # print the total money won.
            reward = reward + QUESTIONS[i]["money"]
            print(f'Total Money won: {reward}')
            # See if the user has crossed a level, print that if yes
            if i == 5:
                print(f'you are now at level 1 and your min-reward is -/10000')
            elif i == 10:
                print(f'you are now at level 2 and your min-reward is -/320000')
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            incorrect = True
            print('\nIncorrect !')
            x = QUESTIONS[i]["answer"]
            correct_ans = QUESTIONS[i][f'option{x}']
            print(f'The Correct answer is: {correct_ans}')
            break

    # print the total money won in the end.
    if incorrect:
        if i < 6:
            print('You have won -/0')
        elif 6 <= i < 10:
            print("You have won -/10000")
        elif i > 10:
            print("You have won -/320000")
    else:
        print(f'You have won -/{reward}')


kbc()
