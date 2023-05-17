# Metronome Training
# Made by Hagop Ketchedjian
# Version 1.0
# November 2021

import random
from playsound import playsound


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def start():
    print(color.BOLD + color.UNDERLINE + color.RED + "Welcome to Metronome Training!\n" + color.END)
    print(color.BOLD + color.BLUE + "Directions: You will be given a random tempo between 30 BPM and 240 BPM.\nOnce the audio is played you will have a chance to enter in your guess.\nYou will be asked to keep trying until you correctly guess the tempo and then a new tempo will be given.\n" + color.END)
    print("Type 'start' to begin.")
    start = input()
    if (start == "start"):
        print()
        hardRandomBPM()
    else:
        print("\nYou spelled 'start' wrong... Please try again")
        start = input()
        if (start == "start"):
            print()
            hardRandomBPM()
        else:
            print(color.PURPLE + "\nYou spelled 'start' wrong 2 times in a row..." + color.END)
            print("Either you are really bad at spelling or you are joking around.")
            print("This is my lesson on how to spell 'start'.")
            print("S - T - A - R - T.")
            print(color.YELLOW + "Good now rerun the program :)" + color.END)


def hardRandomBPM():
    BPM = random.randint(30, 240)
    print(BPM)
    metronomeTrackFinder(BPM)
    guessing(BPM)


def metronomeTrackFinder(BPM):
    file = 'Metronome/%d.mp3' % (BPM)
    playsound(file)


def guessing(BPM):
    guess = input("Enter your guess: ")
    for i in range(1, 100):
        if (int(guess) != int(BPM)):
            guess = input("You are incorrect. Guess again: ")
        if (int(guess) == int(BPM)):
            print(color.GREEN + "Good job! You are correct!\n" + color.END)
            print("Next tempo...")
            hardRandomBPM()

start()