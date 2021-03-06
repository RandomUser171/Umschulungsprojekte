import math
import time
import random


starting_health = 100

player_playing = 0
player_list = ['user', 'computer']
players = {
    player_list[0] : starting_health,
    player_list[1] : starting_health
}

'''It checks the users input'''
def input_checker(*val):
    #print('input_checker')
    users_input = input().lower()
    while True:
        for i in val:
            if i == users_input:
                return users_input
        temp_strng = ''
        for i in val:
            temp_strng += i
            if i != val[-1]:
                temp_strng += ', '
        print('Please type one of the following values: {}'.format(temp_strng))
        users_input = input().lower()


'''Calculates the move'''
def nxt_move(n):
    #print('nxt_move')
    n_damage = 0
    if n == 1:
        n_damage = random.randint(18,25)
    elif n == 2:
        n_damage = random.randint(10,35)
    else:
        n_damage = random.randint(-25,-18)
    return n_damage

'''Identifies the player and selects the move'''
def select_move(n):
    #print('select_move')
    print(n)
    if n == 0:
        print('Please type your attack (1,2,3).')
        return int(input_checker('1','2','3'))
    else:
        if players[player_list[1]] < 30:
            random_choice = random.randint(1,6)
            if random_choice>3:
                random_choice = 3
        else:
            random_choice = random.randint(1,3)
        return random_choice


'''Execute the move'''
def execute_move(dmg, pl):
    #print('execute_move')
    if dmg < 0:
        players[player_list[pl]] += abs(dmg)
        print(player_list[pl], 'healed')
        print('health : {}'.format(players[player_list[pl]]))
    else:
        players[player_list[pl-1]] -= dmg
        print(player_list[pl-1], 'damaged')
        print('health : {}'.format(players[player_list[pl-1]]))



def next_player(nxt_player):
    #print('next_player')
    next_move = select_move(nxt_player)
    damage = nxt_move(next_move)
    execute_move(damage, nxt_player)

    if nxt_player == 0:
        nxt_player = 1
    else:
        nxt_player = 0
    return nxt_player


def main():
    print('Welcome to this turn based fighiting game!')
    print('First roll to check who plays first! (type "roll")')
    input = input_checker('roll')
    player_playing = random.randint(1,len(players))-1
    print('Starting fight!')
    while players[player_list[0]] >0 and players[player_list[1]] >0:
        player_playing = next_player(player_playing)
    print('Fight ended', player_list[player_playing-1],'won')
    time.sleep(0.5)
    print(player_playing)


if __name__=='__main__':main()
