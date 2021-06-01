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
    index = 0
    total = 15
    has_used_lifeline = False

    while index < 15:
        if not has_used_lifeline:
            print("You also have a 50-50 lifeline. Type 'lifeline' to use the lifeline.")
        print(f'Price Won: {reward}')
        print(f'\tQuestion 1: {QUESTIONS[index]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[index]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[index]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[index]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[index]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations
        if ans == "quit":
            break

        if ans == "lifeline":
            if not has_used_lifeline and (index != 14):
                has_used_lifeline = True
                question = lifeLine(QUESTIONS[index])
                print(f'\tQuestion {index}: {question["name"]}')
                print(f'\t\tOptions:')
                print(f'\t\t\tOption 1: {question["option1"]}')
                print(f'\t\t\tOption 2: {question["option2"]}')
                print(f'\t\t\tOption 3: {question["option3"]}')
                print(f'\t\t\tOption 4: {question["option4"]}')

            elif has_used_lifeline:
                print("You have already used your lifeline!!!!")

            else:
                print("You can't use lifeline at this stage!!")
            ans = input('Your choice ( 1-4 ) : ')

        try:
            int(ans)
        except :
            print("Invalid Input!!")
            continue
        if int(ans) not in range(1, 5):
            print("Invalid Input!!")
            continue

        if isAnswerCorrect(QUESTIONS[index], int(ans)):
            # print the total money won.
            reward = reward + QUESTIONS[index]["money"]
            print(f'Total Money won: {reward}')
            # See if the user has crossed a level, print that if yes
            if index == 5:
                print(f'you are now at level 1 and your min-reward is -/10000')
            elif index == 10:
                print(f'you are now at level 2 and your min-reward is -/320000')
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            incorrect = True
            print('\nIncorrect !')
            x = QUESTIONS[index]["answer"]
            correct_ans = QUESTIONS[index][f'option{x}']
            print(f'The Correct answer is: {correct_ans}')
            break
        index += 1

    # print the total money won in the end.
    if incorrect:
        if index < 6:
            print('You have won -/0')
        elif 6 <= i < 10:
            print("You have won -/10000")
        elif index > 10:
            print("You have won -/320000")
    else:
        print(f'You have won -/{reward}')




kbc()
