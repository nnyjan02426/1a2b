import random


class func():
    def __init__(self):
        self.get_ans = True
        self.game_start = False
        self.guesses = 1

    def num_is_unique(self, num):
        lst_1 = [num[i] for i in range(4)]
        lst_2 = []

        for i in range(4):
            if lst_1[i] in lst_2:
                return False
            lst_2.append(lst_1[i])
        return True

    def input_error(self, string):
        try:
            string_int = int(string)
        except ValueError:
            print("[ERROR] Enter a four number digit\n")
            return True

        if len(string) != 4:
            print("[ERROR] Enter a four number digit\n")
            return True

        if not self.num_is_unique(string):
            print("[ERROR] Numbers must not be repeated\n")
            return True
        return False

    def ans_func(self):
        while self.get_ans:
            ans = str(random.randint(100, 9999))

            if len(ans) == 3:
                ans = "0" + ans

            if self.num_is_unique(ans):
                self.game_start = True
                self.get_ans = False
        return ans

    def game(self):
        ans = self.ans_func()
        while self.game_start:
            guess = input(str(self.guesses) + ": ")
            a = 0
            b = 0

            # main
            if not self.input_error(guess):
                for i in range(4):
                    for n in range(4):
                        if guess[i] == ans[n]:
                            if i == n:
                                a += 1
                            else:
                                b += 1

                if a == 4:
                    print("\nCongratulations! You Win!")
                    print("Guesses: " + str(self.guesses) + "\n")
                    self.game_start = False

                else:
                    print("{a}A{b}B\n".format(a=a, b=b))
                    self.guesses += 1

def main():
    Game = func()
    Game.game()

main()