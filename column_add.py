import random
import PySimpleGUI as sg


def adding_hero():
    i1, i2, expected = add_param()

    content = make_table_content("+", i1, i2)

    window = sg.Window(title="Column add", layout=content, margins=(10, 10), size=(300, 250),
                       text_justification="right", element_justification="center", font=("Lucida Console", 12))

    game_loop(expected, window, add_param, "+")


def add_param():
    i1 = random.randint(0, 50)
    if i1 > 5:
        i2 = random.randint(0, 12)
    else:
        i2 = random.randint(2, 10)
    return i1, i2, i1 + i2


def times_table():
    i1, i2, expected = times_param()

    content = make_table_content("x", i1, i2)
    window = sg.Window(title="Column add", layout=content, margins=(10, 10), size=(300, 250),
                       text_justification="right", element_justification="center", font=("Lucida Console", 12))

    game_loop(expected, window, times_param, "x")


def question_game():
    content = make_questions()
    window = sg.Window(title="Question game", layout=content, margins=(10, 10), size=(300, 250),
                       text_justification="right", element_justification="center", font=("Lucida Console", 12))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-ANS1-":
            window["-MSG-"].update("Sub to Taylor Swift!")

        if event == "-ANS2-":
            window["-MSG-"].update("Sub to @RainbowCloud-k5j!")


def times_param():
    i1 = random.randint(0, 12)
    if i1 > 5:
        i2 = random.randint(0, 12)
    else:
        i2 = random.randint(2, 10)
    return i1, i2, i1 * i2


def make_questions():
    return [
        [sg.Text(" Would you be...")],
        [sg.Button(button_text="A famous singer.", enable_events=True, key="-ANS1-", pad=((0, 0), (20, 0)),
                   font=("Arial", 10))],
        [sg.Button(button_text="A famous youtuber.", enable_events=True, key="-ANS2-", font=("Arial", 10))],
        [sg.Text(key="-MSG-", size=(20, 1), pad=((0, 0), (10, 0)), font=("Arial", 10), justification="center")]
    ]


def make_table_content(op, i1, i2):
    return [
        [sg.Text(fmt(i1), key="-N1-", size=(10, 1), pad=((0, 20), (20, 0)))],
        [sg.Text(op + " " + fmt(i2), key="-N2-", size=(10, 1), pad=((0, 20), (0, 0)))],
        [sg.Text("--------", size=(10, 1), pad=((0, 20), (0, 0)))],
        [sg.In(key="-ANS-", size=(5, 1), pad=((20, 0), (0, 0)), justification="right")],
        [sg.Button(button_text="Check Answer", enable_events=True, key="-CHECK-", pad=((0, 0), (20, 0)),
                   font=("Arial", 10))],
        [sg.Button(button_text="Next Question", enable_events=True, key="-NEXT-", font=("Arial", 10))],
        [sg.Text(key="-MSG-", size=(20, 1), pad=((0, 0), (10, 0)), font=("Arial", 10), justification="center")]
    ]


def game_loop(expected, window, params, op):
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-CHECK-":
            ans = values["-ANS-"]
            window["-MSG-"].update(check(ans.strip(), str(expected)))

        if event == "-NEXT-":
            i1, i2, expected = params()
            window["-N1-"].update(fmt(i1))
            window["-N2-"].update(op + " " + fmt(i2))
            window["-MSG-"].update("")
            window["-ANS-"].update("")


def check(ans, exp):
    if ans == exp:
        return "Yes you're correct!!"
    else:
        return "Correct answer is " + exp


def fmt(nbr):
    if nbr < 10:
        return "  " + str(nbr)
    if nbr < 100:
        return " " + str(nbr)
    else:
        return str(min(nbr, 999))


def rand():
    if random.choice([0, 1, 2]) == 0:
        return random.randint(1, 100)
    else:
        return random.randint(1, 10)

