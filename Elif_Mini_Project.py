#!/usr/bin/env python3


from glob import glob
import random
import os


squirtle = 0
bulbasaur = 0
charmander = 0
missingo = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def eval(input):
    global squirtle
    global bulbasaur
    global charmander
    global missingo

    pokeArr = ["1", "2", "3", "4", "5", "6"]

    c1 = pokeArr.pop(random.randint(0, len(pokeArr)-1))
    c2 = pokeArr.pop(random.randint(0, len(pokeArr)-1))
    c3 = pokeArr.pop(random.randint(0, len(pokeArr)-1))
    c4 = pokeArr.pop(random.randint(0, len(pokeArr)-1))
    c5 = pokeArr.pop(random.randint(0, len(pokeArr)-1))
    c6 = pokeArr[0]

    if(input in [c1, c2]):
        squirtle += 1
    elif(input in [c3, c4]):
        bulbasaur += 1
    elif(input in [c5, c6]):
        charmander += 1
    else:
        missingo += 1


def question_1():
    print("Where do you live?")
    print("1. Pallet Town    2. Viridian City    3. Pewter City\n4. Cerulean City    5. Vermillion City    6. Lavender Town")
    userInput = input("Select a number between 1 and 6: ")
    if(int(userInput) in range(1, 6)):
        eval(userInput)
    else:
        question_1()
    clear()
    question_2()


def question_2():
    print("Pick a badge: ")
    print("1. Boulder Badge    2. Cascade Badge    3. Thunder Badge    4. Rainbow Badge    5. Soul Badge    6. Volcano Badge")
    userInput = input("Select a number between 1 and 6: ")
    eval(userInput)
    clear()
    question_3()


def question_3():
    print("Final question: What is your favorite game?")
    print("1. Pokemon Red    2. Pokemon Blue    3. Pokemon Yellow    4. Pokemon Ruby    5. Pokemon X   6. Pokemon Diamond")
    userInput = input("Select a number between 1 and 6: ")
    eval(userInput)
    clear()
    scenario_1()


def scenario_1():
    global charmander
    global squirtle
    global bulbasaur
    global missingo

    choices = ["Fight", "Item", "Pokemon", "Run"]

    print("You get into a battle with a overleveled pokemon and your hp is low, what do you do?")
    print("(F)ight (I)tem (P)okemon (R)un")

    userInput = ""

    while(userInput not in choices):
        userInput = input("Enter your choice: ").strip().capitalize()

    if userInput == "Fight":
        charmander += 1
    elif userInput == "Item":
        bulbasaur += 1
    elif userInput == "Pokemon":
        squirtle += 1
    else:
        missingo += 1

    final()


def final():
    global charmander
    global squirtle
    global bulbasaur
    global missingo

    if missingo > 2:
        print("you are a missingo")
    elif(charmander > squirtle and charmander > bulbasaur):
        print("You are a charmander")
    elif(squirtle > charmander and squirtle > bulbasaur):
        print("You are a squirtle")
    else:
        print("You are a bulbasaur")


question_1()
