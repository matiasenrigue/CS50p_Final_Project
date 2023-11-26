import sys
from tabulate import tabulate
from termcolor import colored


def get_valid_player_name():
    while True:
        try:
            name = input("Enter player's name: ").title()
            name_validator(name)
        except ValueError as e:
            print(e)
        else:
            return name




def name_validator(name):
    if len(name) > 22:
            raise ValueError("Name too long. Please enter a name with maximum 22 characters.")
    elif any(char.isdigit() for char in name):
        raise ValueError("Name cannot contain numbers. Please enter a valid name.")
    else:
        return True


player1 = get_valid_player_name()
player2 = get_valid_player_name()



def point_scored(punto):
    """
    This functions returns a tupple (0, 1) or (1,0) depending on who scored the point
    If user enters "1" player 1 scored so the tupple would be (1,0)
    If user enters "2" player 2 scored so the tupple would be (2.0)
    Any other input will not be accepted
    """
    global player1, player2
    score_1 = 0 #local variable
    score_2 = 0
    punto = punto.replace('"', '')
    punto = punto.strip()
    if punto == "1":
        score_1 += 1
    elif punto == "2":
        score_2 += 1
    
    elif punto == "d":
        print("Are you sure to exit?")
        while True:
                user = input('write "yes" or "no": ').replace('"', '')
                user = user.lower().strip()
                if user == "no":
                    break
                elif user == "yes":
                    sys.exit()
                else:
                    continue
            
    else:
        raise(ValueError)
    return (score_1, score_2)



def point_converter(scoreboard, tiebreak):
    """
    This function takes a list scoreboard and converts it into tennis format
    For example [2,1] becomes [30,15]
    --> The loop will iterate to the list [1,2] and convert both elemnts to tennis
    """
    tennis_score = []

    if tiebreak == 0:

        if (scoreboard[0] <= 3 and scoreboard[1] < 3) or (scoreboard[0] < 3 and scoreboard[1] <= 3): #not deuce / advantage (game playing) until 40-40
            score_map = {0: 0, 1: 15, 2: 30, 3:40}
            for score in scoreboard:
                tennis_score.append(score_map[score])
        
        elif scoreboard[0] == 4 and scoreboard[1] < 3: #player 1 wins
            tennis_score = ["Game 🏅", 0]
        elif scoreboard[1] == 4 and scoreboard[0] < 3: #player 2 wins
            tennis_score = [0, "Game 🏅"]

        else:  #after 40-40
            if scoreboard[0] == scoreboard[1]: #deuce
                tennis_score = ["40❕", "40❕"]
            elif scoreboard[0] == (scoreboard[1] + 1): #advantaje player 1
                tennis_score = ["Adv❗", 40]
            elif scoreboard[1] == (scoreboard[0] + 1): #advantaje player 2
                tennis_score = [40, "Adv❗"]
            elif scoreboard[0] > (scoreboard[1] + 1): #player 1 wins
                tennis_score = ["Game 🏅", 0]
            elif scoreboard[1] > (scoreboard[0] + 1): #player 2 wins
                tennis_score = [0, "Game 🏅"]
    
    elif tiebreak == 1:
        tennis_score = [scoreboard[0], scoreboard[1]]

    return tennis_score



def print_score(score, tiebreak):
    """
    This function improves the printing of the
    """
    if tiebreak == 0:
        dummy = 0
    elif tiebreak == 1:
        dummy = 1

    headers = [player1, player2]
    tennis_score = point_converter(score, dummy)   # Convert score to tennis format
    return (tabulate([tennis_score], headers=headers, 
                    tablefmt="grid", colalign=("center", "center")))



    

def game_counter():
    """
    This functions adds the tupples resulting from the function points scores
    So reciving something like (0,1) (0,1) (1,0)
    It would add to (1,2) as the points result in this game

    This functions also stoops the game when:
    - one player reaches 4 points and has 2 point difference with his rival
    - both players reached 3 points or more (40 in tennis) but one has  a 2 point difference

    The input will only be passed to the function if its a valid one: "1", "2", or "d"
    """
    score_1 = 0 #local variable
    score_2 = 0

    while True:
        try:
            user = input(f'"1" if {player1} won the point,      or "2" if {player2} won the point,      or "d" to exit: ')
            punto = point_scored(user)
        except ValueError:
            #print(f"Please insert a valid input to know if {player1} or if {player2} won the point")
            continue
        else:     
            score_1 += int(punto[0]) #count points for first player
            score_2 += int(punto[1]) #count points for second player
            score = [score_1,score_2]
            print(print_score(score, 0)) #conerts to tennis format

        if score_1 == 4 and score_2 < 3: #player 1 wins without deuce
            return "player1"
        if score_2 == 4 and score_1 < 3: #player 2 wins without deuce
            return "player2"
        
        if score_1 >= 3 and score_2 >= 3: #game reached deuce: 40-40 or more
            if score_1 > (score_2 + 1):
                return "player1"
            elif score_2 > (score_1 + 1):
                return "player2"



def tie_breakcounter():
    """
    This functions adds the tupples resulting from the function points scores
    So reciving something like (0,1) (0,1) (1,0)
    It would add to (1,2) as the points result in this game

    This functions also stoops the tiebreak when:
    - one player reaches 7 points and has 2 point difference with his rival
    - both players reached 6 points or more but one has  a 2 point difference

    The input will only be passed to the function if its a valid one: "1", "2", or "d"
    """
    score_1 = 0 #local variable
    score_2 = 0

    while True:
        try:
            user = input(f'write "1" if {player1} won the point, or "2" if {player2} did: ')
            punto = point_scored(user)
        except ValueError:
            continue
        else:
            score_1 += int(punto[0]) #count points for first player
            score_2 += int(punto[1]) #count points for second player
            score = [score_1,score_2]
            print(print_score(score, 1))

        if score_1 == 7 and score_2 < 6: #player 1 wins without going to 8
            return "player1"
        if score_2 == 7 and score_1 < 6: #player 2 wins without goiing to 8
            return "player2"
        
        if score_1 >= 6 and score_2 >= 6: #tie-break reached 6-6, now we need 2 point difference
            if score_1 > (score_2 + 1):
                return "player1"
            elif score_2 > (score_1 + 1):
                return "player2"




def set_counter(sets_player1, sets_player2):
    games_player1 = 0
    games_player2 = 0

    while True:
        game_result = game_counter()
        if game_result == "player1":
                games_player1 += 1
        elif game_result == "player2":
            games_player2 += 1
        
        
        table_data = [
            ["Player", "Sets", "Games"],
            [player1, sets_player1, games_player1], 
            [player2, sets_player2, games_player2]
        ]

        tabla_result = tabulate(table_data, headers="firstrow", tablefmt="grid", stralign="center")
        concatenada = ("🎾"*10) + "\n\n ➤ Game Score:\n" + tabla_result + "\n\n" + ("🎾"*10) 
        tabla_result = colored(concatenada, "green", attrs=["bold"])
        frase_result = "\n\n" + tabla_result + "\n\n"


        if not (games_player1 >= 5 and games_player2 >= 5): #until result reaches 5-5, win is on 6
            print(frase_result)

            if games_player1 >= 6 and (games_player1 - games_player2) >= 2: #player 1 wins set
                #print(f"{player1} wins the set")
                return "player1"
            elif games_player2 >= 6 and (games_player2 - games_player1) >= 2: #player 2 wins set
                #print(f"{player2} wins the set")
                return "player2"
        
        if games_player1 >= 5 and games_player2 >= 5: #if 5-5 now is either to 7 or tiebreak

            if games_player1 == 5 or games_player2 == 5:
                print(frase_result)
                if games_player1 >= 7 and (games_player1 - games_player2) >= 2: #player 1 wins set
                    #print(f"{player1} wins the set")
                    return "player1"
                elif games_player2 >= 7 and (games_player2 - games_player1) >= 2: #player 2 wins set
                    #print(f"{player2} wins the set")
                    return "player2"
                
            elif games_player1 == 6 and games_player2 == 6: #tiebreak
                print(frase_result)
                print(colored("\n", "white", "on_yellow"), end="")
                print(colored("\n\n         Tie-Break is staring         \n", "yellow", "on_red", attrs=["bold"]), end="")
                print(colored("\n", "white", "on_yellow"), end="\n\n\n\n")                 
                tiebreak_result = tie_breakcounter()
                if tiebreak_result == "player1": # player 1 wins the tiebreak and set
                    #print(f"{player1} wins the tiebreak and set")
                    return "player1"
                elif tiebreak_result == "player2": # player 2 wins the tiebreak and set
                    #print(f"{player2} wins the tiebreak and set")
                    return "player2"


def match_counter():
    sets_player1 = 0
    sets_player2 = 0
    while True:
        print(colored("\n", "white", "on_cyan"), end="")
        print(colored("\n\n         New set is staring         \n", "cyan", "on_white", attrs=["bold"]), end="")
        print(colored("\n", "white", "on_cyan"), end="\n\n")
        set_result = set_counter(sets_player1,sets_player2)
        if set_result == "player1":
            sets_player1 += 1
            winner = player1
        elif set_result == "player2":
            sets_player2 += 1
            winner = player2
        
        print(colored("\n", "white", "on_cyan"), end="")
        frase_set1 = f"\n\n         {winner} wins the set"
        frase_set2 = f"         Sets Score: {player1} {sets_player1} - {sets_player2} {player2}\n"
        print(colored(frase_set1 + "\n" + frase_set2, "cyan", "on_white", attrs=["bold"]), end="")
        #print(colored("\n", "white", "on_cyan"), end="")

        if sets_player1 == 2:
            return "player 1"
        elif sets_player2 == 2:
            return "player 2"
       


def main():
    #Start of the Match
    print(colored("\n", "white", "on_cyan"), end="")
    uno = "\n\n         Welcome to this Tenis match\n"
    dos = f"         {player1} will pay against {player2}\n"
    tres = f"\n         Controls:"
    cuatro = f"\n         - 1: if {player1} won the point:"
    cinco = f"\n         - 2: if {player2} won the point:"
    seis = f"\n         - d: to exit the game:"
    tot = uno + dos
    print(colored(tot, "cyan", "on_white", attrs=["bold"]), end="")

    #Match is played
    victory = match_counter()

    #End of the Match
    if victory == "player 1":
        winner = player1
    elif victory == "player 2":
        winner = player2
    
    print(colored("\n", "white", "on_cyan"), end="")
    frase_match = f"\n\n         {winner} wins the Match\n"
    print(colored(frase_match, "cyan", "on_white", attrs=["bold"]), end="")
    print(colored("\n", "white", "on_cyan"))
    print("\n\n")


if __name__ == "__main__":
    main()
