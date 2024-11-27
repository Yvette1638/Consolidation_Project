import random

#Roll 3 dice
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

#Calculate player's score for turn
def calculate_score(dice):
    if len(set(dice)) == 1:  #If all three dice are the same
        return 0  #Score is 0
    return sum(dice)

#Play single turn for player
def play_turn(player_name):
    print(f"\n{player_name}'s Turn")
    
    # Roll 3 dice
    dice = roll_dice()
    print(f"Rolled: {dice}")
    
    # Check if all dice are the same
    if len(set(dice)) == 1:
        print(f"Tupled out! {player_name} scores 0 points.")
        return 0
    
    #Allow player to re roll unfixed dice
    fixed_dice = [dice[i] for i in range(3) if dice.count(dice[i]) > 1]
    print(f"Fixed dice: {fixed_dice}")
    
    rerolls = 0
    while rerolls < 3:  #Limit to 3 rerolls
        reroll_choice = input(f"Do you want to reroll the remaining dice? (Y/N): ")
        if reroll_choice.lower() == 'n':
            break
        else:
            #Reroll any non-fixed dice
            rerolled_dice = [random.randint(1, 6) if dice[i] not in fixed_dice else dice[i] for i in range(3)]
            dice = rerolled_dice
            print(f"Rolled: {dice}")
            rerolls += 1
    
    #Calculate score and return it
    score = calculate_score(dice)
    print(f"{player_name} scored {score} points this turn.")
    return score

#Main function to start game
def start_game():
    print("Welcome to Tuple Out Dice Game!")
    
    #Scores and high score
    player_scores = {'Player 1': 0, 'Player 2': 0}
    high_score = 0
    rounds = 5  # Set to 5 rounds
    
    # Main game loop
    round_counter = 0
    while round_counter < rounds:
        round_counter += 1
        print(f"\n--- Round {round_counter} ---")
        
        #Player 1's turn
        player_scores['Player 1'] += play_turn('Player 1')
        #Player 2's turn
        player_scores['Player 2'] += play_turn('Player 2')
        
        #Display current scores
        print(f"\nCurrent Scores: Player 1: {player_scores['Player 1']} | Player 2: {player_scores['Player 2']}")
        
        # Check if any player reached 50 points
        if player_scores['Player 1'] >= 50:
            print("\nPlayer 1 wins with 50 points!")
            break
        elif player_scores['Player 2'] >= 50:
            print("\nPlayer 2 wins with 50 points!")
            break
        
    #After game ends update high score
    if player_scores['Player 1'] > high_score:
        high_score = player_scores['Player 1']
    if player_scores['Player 2'] > high_score:
        high_score = player_scores['Player 2']
    
    print(f"\nGame Over! Final Scores: Player 1: {player_scores['Player 1']} | Player 2: {player_scores['Player 2']}")
    print(f"High Score: {high_score}")

if __name__ == "__main__":
    start_game()
