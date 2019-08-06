import random
import itertools
a = 0


class Game:
    def __init__(self):
        print('''===================================
type "quit" to leave the game''')
        self.p_ct_a = self.computer_a = 0
        self.all_the_maybe_ans = (list(itertools.permutations(range(10), 4)))
        self.the_rest_of_maybe_ans = self.all_the_maybe_ans
        self.player_ans = random.choice(self.all_the_maybe_ans)
        self.the_history_box = {}

    def compare(self, ans, the_gus):
        guslist = [int(x) for x in the_gus]
        count_of_a = count_of_b = 0
        for run_four_times in range(4):
            if guslist[run_four_times] in ans:
                if guslist[run_four_times] == ans[run_four_times]:
                    count_of_a += 1
                else:
                    count_of_b += 1
        return count_of_a, count_of_b

    def player_guess(self):
        while True:
            player_give_guess = input("insert your guess(four numbers):")
            try:
                if player_give_guess == 'quit':
                    return 5
                self.p_ct_a, p_ct_b = self.compare(
                    self.player_ans, player_give_guess)
                print("the result is ", self.p_ct_a, "A", p_ct_b, "B")
                break
            except:
                print('you insert the wrong thing ,insert it again')

    def com_give_gus(self):
        self.comgus = random.choice(self.the_rest_of_maybe_ans)
        print("I guess your number is ", self.comgus)

    def com_solve_player_ans(self):
        only_for_append_list = []
        while True:
            self.player_give_ans = input("show me the result: ")
            try:
                if self.player_give_ans == 'quit':
                    return 5
                self.computer_a = int(self.player_give_ans[0])
                for x in self.the_rest_of_maybe_ans:
                    com_count_of_a, com_count_of_b = self.compare(
                        self.comgus, x)
                    if com_count_of_a == int(self.player_give_ans[0]) and com_count_of_b == int(self.player_give_ans[2]):
                        only_for_append_list.append(x)
                        self.the_rest_of_maybe_ans = only_for_append_list
                print("there are", len(only_for_append_list), "possiblilties")
                break
            except:
                print('you insert the wrong thing ,insert it again')

    def the_whole_history_box(self):
        com_gus_str = map(str, self.comgus)
        self.the_history_box.update(
            {''.join(com_gus_str): self.player_give_ans})
        print(self.the_history_box)

    def repeat(self):
        if self.p_ct_a == 4:
            print("you won the game")
            return 4
        elif self.computer_a == 4:
            print("I won the game haha")
            return 4
        else:
            return 0


while a < 5:
    a = 0
    game = Game()
    while a < 4:
        a = game.player_guess()
        if a == 5:
            break
        game.com_give_gus()
        a = game.com_solve_player_ans()
        game.the_whole_history_box()
        a = game.repeat()
        print('===================================')
    print("another new round!!!!")