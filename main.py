# main.py
import random


def unique(num):
    num2 = num
    for i in range(4):
        for j in range(4):
            if num[i] == num2[j] and i != j:
                return False
    return True


def input_error(num):
    try:
        num_int = int(num)
    except ValueError:
        print("[ERROR] Please enter a four number digit\n")
        return True

    if len(num) != 4:
        print("[ERROR] Please enter a four number digit\n")
        return True

    if not unique(num):
        print("[ERROR] Numbers must not be repeated\n")
        return True

    return False


def get_a_b(str1, str2):
    a = 0
    b = 0

    if not input_error(str1):
        for i in range(4):
            for n in range(4):
                if str1[i] == str2[n]:
                    if i == n:
                        a += 1
                    else:
                        b += 1
    return a, b


class Game:
    def __init__(self):
        self.get_ans = True
        self.game_start = False
        self.guesses = 1

    def ans_func(self):
        while self.get_ans:
            ans = str(random.randint(100, 9999))

            if len(ans) == 3:
                ans = "0" + ans

            if unique(ans):
                self.game_start = True
                self.get_ans = False
        return ans

    def game(self):
        ans = self.ans_func()
        while self.game_start:
            guess = input("%2d : " % self.guesses)
            
            if guess == "quit":
                print("The answer is: %s" % ans)
                self.game_start = False

            elif not input_error(guess):
                a, b = get_a_b(guess, ans)

                if a == 4:
                    print("\nCongratulations! You Win!")
                    print("Guesses: %d\n" % self.guesses)
                    self.game_start = False

                else:
                    print("{a}A{b}B\n".format(a=a, b=b))
                    self.guesses += 1


game = Game()
game.game()
