import random

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

player_choices = []

def display_board():
    for row in map:
        print(f"{row[0]}|{row[1]}|{row[2]}")
        if row == row1 or row == row2:
            print("--------")

def player_turn(player_choices):
    player_pos = input("Where would you like to place your 'x'?\n Type your x and y position as one number. EX. (2,3) = 23: ")
    map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] = "x"
    player_choices.append([player_pos[1], player_pos[0]])

def second_player():
    player_pos = input("Where would you like to place your 'o'?\n Type your x and y position as one number. EX. (2,3) = 23: ")
    
    while map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] != " ":
        player_pos = input("Where would you like to place your 'o'?\n Type your x and y position as one number. EX. (2,3) = 23: ")

    map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] = "o"

game = True

while game:
    player_turn(player_choices)
    second_player()
    display_board()
