# player_name = "Manuel" 
# player_attack = 10
# player_heal = 16
# health = 100

#player = ["Manuel",10,16,100]
from random import randint
game_running = True

game_results = []
# print(player['name'])
# print(monster['health'])

def cal_monster_attack(attack_min,attack_max):
    return randint(attack_min,attack_max)

def game_ends(winner_name):
    print(f'{winner_name }  won the game')

while game_running == True:
    counter = 0
    new_round = True
    player = {'name':"Manuel", 'attack': 13, 'heal':16, 'health':100}

    monster = {'name':'Pogo', 'attack_min':10, 'attack_max':20, 'health':100}

    print("-----" * 12)
    print("Enter Player name: ")
    player['name'] = input()

    print("-----" * 12)
    print(player['name'] + " has " + str(player['health']) + " health ")
    print(monster['name'] + " has " + str(monster['health']) + " health ")

    
    while new_round == True:

        counter = counter+1
        player_won = False

        monster_won = False

        print("Please select an action")
        print("1> Attack")
        print("2> Heal")
        print("3> Exit game")
        print("4> Show Results")

        player_choice = int(input())

        if player_choice == 1:
            #print("Attack")
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack(monster['attack_min'],monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True
        
            print(monster['health'])
            print(player['health'])

        elif player_choice == 2:
            #print("Heal Player")
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - cal_monster_attack(monster['attack_min'],monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True
        
        elif player_choice == 3:
            new_round = False
            game_running = False

        elif player_choice == 4:
            for i in game_results:
                print(i)




        else:
            print("Invalid input")

        if player_won == False and monster_won == False:
            print(player['name'] + " has " + str(player['health']) + " left ")
            print(monster['name'] + " has " + str(monster['health']) + " left ")

        elif player_won:
            game_ends(player['name'])
            round_result = {'name':player['name'],'health':player['health'], 'rounds':counter}
            #print(round_result)
            game_results.append(round_result)
            #print(game_results)
            new_round = False
        
        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name':monster['name'],'health':monster['health'],'rounds':counter}
            #print(round_result)
            game_results.append(round_result)
            #print(game_results)
            new_round = False




