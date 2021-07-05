import random


class RpsGame:

    def __init__(self, user_play):
        self.user_play = user_play
        if list_of_options == ['']:
            self.options = ["rock", "paper", "scissors"]
        else:
            self.options = list_of_options
        self.comp_play = random.choice(self.options)

    def win(self):
        global score
        print(f"Well done. The computer chose {self.comp_play} and failed")
        score += 100

    def draw(self):
        global score
        print(f"There is a draw ({self.comp_play})")
        score += 50

    def lose(self):
        print(f"Sorry, but the computer chose {self.comp_play}")

    def play(self):
        if self.user_play not in self.options:
            print("Invalid input")
        elif self.user_play == self.comp_play:
            self.draw()
        else:
            index = self.options.index(self.user_play)
            ordered_list = self.options[index + 1:]
            ordered_list.extend(self.options[:index])
            if ordered_list.index(self.comp_play) < len(ordered_list) / 2:
                self.lose()
            else:
                self.win()


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

score_sheet = open('rating.txt', 'r')
score_list = score_sheet.readlines()
score = 0
for player in score_list:
    if player.startswith(user_name):
        score = int(player.lstrip(f'{user_name} ').rstrip('\n'))

list_of_options = input().split(',')
print("Okay, let's start")

while True:
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        score_sheet.close()
        break
    elif user_choice == "!rating":
        print(f"Your rating: {score}")
    else:
        RpsGame(user_choice).play()
