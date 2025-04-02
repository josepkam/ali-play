# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import time
import random
from column_add import adding_hero, times_table, question_game
from num2words import num2words


def silly_numbers():
    number = 15420155
    print("The answer is:", num2words(number))


def super_duper_silly_numbers():
    words = "by "
    print("Super duper::", words)


def funny():
    for i in range(7790):
        print(i * 1)
        time.sleep(0.1)


def hello():
    name = input(" Who is your FAV singer? ")
    print(" I like", name)


def would_you_rather():
    print(" Would you rather... ")
    print(" 1) Be a famous youtuber. ")
    print(" 2) Be a famous singer. ")

    answer = input()
    if answer == "1":
        print("Subscribe to @RainbowCloud-k5j!")
    elif answer == "2":
        print("Subscribe to Taylor Swift!")


def great_numbers():
    i1 = random.randint(2, 10)
    if i1 > 5:
        i2 = random.randint(2, 4)
    else:
        i2 = random.randint(2, 10)
    res = i1 * i2

    ans = input(str(i1) + " x " + str(i2) + " = ")
    if ans == str(res):
        print("Yes you're correct!!!!!!!!!!!!!!!!!!!!:) ^-^ :-) ;-) :-0 ^_^ + ^_- -_^")
    else:
        print("-_- :-( ;-( ;-0 -_-%_% correct answer is", res)


def non_sense_words():
    words = {
        "a pill jus": "apple juice",
        "h ot choc o late": "hot chocolate",
        "pi za": "pizza",
        "ex pres ": "express",
        "we dsp ray": "weed spray",
        "pine a pill": "pineapple",
        "wa tur bo tul": "water bottle",
        "pla sta sin fiv": "play station 5",
        "tis oo b ox": "tissue box",
        "con trol ur": "controller",
        "desc con tup ter": "desk computer",
        "an oi ig bru fers": "annoying brothers",
        "Tel i vish on remot": "television remote",
        "tuf pic": "tooth pick",
        "pi ch arm": "pycharm",
        "crist mas pri sent": "christmas present",
        "soc et ch ar jer": "socket charger"
    }

    keys = list(words.keys())
    random.shuffle(keys)

    for key in keys:
        ans = input("'" + key + "' is?  Ans=")
        value = words[key]
        if ans == value:
            print("You're correct")
        else:
            print("Answer: " + value)


if __name__ == '__main__':
    adding_hero()
