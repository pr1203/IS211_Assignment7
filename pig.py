import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

    def roll_die(self):
        roll = random.randint(1, 6)
        print(f"{self.name} rolled a {roll}")
        if roll == 1:
            print(f"{self.name} scored 0 points this turn")
            self.turn_score = 0
            return False
        else:
            self.turn_score += roll
            print(f"{self.name} has a turn score of {self.turn_score}")
            return True

    def hold(self):
        self.score += self.turn_score
        print(f"{self.name} scored {self.turn_score} points this turn")
        print(f"{self.name} now has a total score of {self.score}")
        self.turn_score = 0

    def reset(self):
        self.score = 0
        self.turn_score = 0

def get_players():
    player1_name = input("Enter name of player 1: ")
    player2_name = input("Enter name of player 2: ")
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    return player1, player2

def play_game():
    random.seed(0)
    player1, player2 = get_players()
    current_player = player1
    while True:
        print(f"{current_player.name}'s turn")
        decision = input("Enter 'r' to roll or 'h' to hold: ")
        if decision == 'r':
            if not current_player.roll_die():
                current_player = player2 if current_player == player1 else player1
        elif decision == 'h':
            current_player.hold()
            if current_player.score >= 100:
                print(f"{current_player.name} wins!")
                break
            current_player = player2 if current_player == player1 else player1
        else:
            print("Invalid input. Enter 'r' to roll or 'h' to hold")

if __name__ == '__main__':
    play_game()
