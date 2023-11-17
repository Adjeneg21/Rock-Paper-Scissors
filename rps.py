
import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AlwaysRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            return random.choice(moves)
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_index = 0

    def move(self):
        move = moves[self.move_index]
        self.move_index = (self.move_index + 1) % 3
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move: ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move. Please enter rock, paper, or scissors.")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif (
            (move1 == 'rock' and move2 == 'scissors') or
            (move1 == 'scissors' and move2 == 'paper') or
            (move1 == 'paper' and move2 == 'rock')
        ):
            self.p1_score += 1
            print("Player 1 wins!")
        else:
            self.p2_score += 1
            print("player 2 wins!")

        print(f"Score - Player 1: {self.p1_score}  Player 2: {self.p2_score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print("Welcome to Rock-Paper-Scissors. "
              "\nBest out of 5 Rounds! \nGame start!")
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Player 1 score:{self.p1_score}Player 2 score: {self.p2_score}")


def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == 'yes':
            return True
        elif again == 'no':
            print("Thanks for playing")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == '__main__':
    while True:
        player_choice = input("Choose opponent: "
                              "\n1 for AlwaysRock"
                              "\n2 for Random"
                              "\n3 for Reflect"
                              "\n4 for Cycle: ")
        if player_choice == '1':
            opponent = AlwaysRockPlayer()
        elif player_choice == '2':
            opponent = RandomPlayer()
        elif player_choice == '3':
            opponent = ReflectPlayer()
        elif player_choice == '4':
            opponent = CyclePlayer()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        game = Game(HumanPlayer(), opponent)
        game.play_game(5)

        if not play_again():
            break
