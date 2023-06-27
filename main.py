import random
import os

map = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
clear = lambda: os.system('cls')

player_choices = []

def display_board():
    for row in map:
        print(f"{row[0]}|{row[1]}|{row[2]}")
        if row == map[0] or row == map[1]:
            print("--------")

def player_turn(player_choices):
    player_pos = input("Where would you like to place your 'x'?\n Type your x and y position as one number. EX. (2,3) = 23: ")
    while map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] != " ":
        player_pos = input("That space is already full/not valid. Please try again.\n Type your x and y position as one number. EX. (2,3) = 23: ")
    map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] = "x"
    player_choices.append([player_pos[1], player_pos[0]])

def second_player():
    player_pos = input("Where would you like to place your 'o'?\n Type your x and y position as one number. EX. (2,3) = 23: ")

    while map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] != " ":
        player_pos = input("That space is already full/not valid. Please try again.\n Type your x and y position as one number. EX. (2,3) = 23: ")

    map[int(player_pos[1]) - 1][int(player_pos[0]) - 1] = "o"

def transpose_map(map): #Creating a transposed list. So all the columns are together instead of all the rows in the list. For winner checking.
    return [
        [map[0][0], map[1][0], map[2][0]],
        [map[0][1], map[1][1], map[2][1]],
        [map[0][2], map[1][2], map[2][2]],
    ]

def horizontal_check(map): #Checking to see if each value in each row is either an 'x' or an 'o'.
    for row in map:
        if all(each == "x" for each in row):
            return "x"
        
        elif all(each == "o" for each in row):
            return "o"
    return None

def diag_check(map): # Checking to see if everything in a diagonal is the same. Returning that value if so.
    if (map[0][0]==map[1][1]==map[2][2]) and map[0][0] != " ":
        return map[0][0]
    if (map[2][0]==map[1][1]==map[0][2]) and map[2][0] != " ":
        return map[2][0]
    return None

def win_checker(map): # using the 3 functions to check if anyone won every rotation.
    return (horizontal_check(map) or horizontal_check(transpose_map(map)) or diag_check(map))

game = True

while game:
    player_turn(player_choices)
    second_player()
    clear()
    display_board()

    if win_checker(map) != None:
        game = False
        clear()
        display_board()
        print(f"Looks like {win_checker(map)} won!")
