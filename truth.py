import random


def true_or_false():
    questions = {
        "Alan Shepherd was the first person to play golf on the moon": "true",
        "Lana and Lina(from dress to impress on Roblox)were enemies": "false",
        "Simon Biles is an competes for USA": "true",
    }

    question_list = list(questions.keys())

    streak = 0
    carry_on = True

    while carry_on:
        random.shuffle(question_list)
        for question in question_list:
            player_answer = input("'" + question + "' True or False?  Ans=")
            correct_answer = questions[question]
            if player_answer == correct_answer:
                print("You are correct, next question!!!")
                streak += 1
            else:
                carry_on = False
                break

    print("Sadly you are wrong but your steak is " + str(streak))


if __name__ == '__main__':
    true_or_false()

