import random

# @jjeong: Dice roll
def dice_roll():
    """ Rolls a dice."""
    dice_markings = [1, 2, 3, 4, 5, 6]
    roll_dice = input("do you wanna roll the dice? ")
    if roll_dice == "yes":
        print(random.choice(dice_markings))
    else:
        print("oh ok. ")

# @jjeong: Rock paper scissor
def rock_paper_scissors():
    """ Plays a rock paper scissor game. """
    rps = ["rock", "paper", "scissors"]
    wannaplay = input("do you want to play rock paper scissors? ")
    if wannaplay == "yes":
        computerpick = random.choice(rps)
        playerpick = input("what do you choose?")
        if computerpick == "rock":
            if playerpick == "scissors":
                print("and I chose rock, I win. ")
            if playerpick == "rock":
                print("me too, tie. ")
            if playerpick == "paper":
                print("and I chose rock, you win. ")
        if computerpick == "paper":
            if playerpick == "scissors":
                print("and I chose paper, you win. ")
            if playerpick == "rock":
                print("and I chose paper, I win. ")
            if playerpick == "paper":
                print("and I chose paper, tie. ")
        if computerpick == "scissors":
            if playerpick == "scissors":
                print("and I chose scissors, tie. ")
            if playerpick == "rock":
                print("and I chose scissors, you win. ")
            if playerpick == "paper":
                print("and I chose scissors, I win. ")
    else:
        return
