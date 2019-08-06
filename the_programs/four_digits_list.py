import random
count_of_a = count_of_b = 0


def compare(ans, guslist):
    count_of_a = count_of_b = 0
    for y in range(4):
        if guslist[y] in ans:
            if guslist[y] == ans[y]:
                count_of_a += 1
            else:
                count_of_b += 1
    return count_of_a, count_of_b


print('===================================')


class Number:
    def __init__(self):
        pass
    def random(self):
        ans = random.choice(allthenumlist)
        return ans

guslist = allthenumlist = []
player_give_ab = ""
# 資料庫(一行就能解決的事我寫了10行)

for y in range(123, 9877):
    thenumbers = [int(n) for n in str(y)]
    if len(thenumbers) < 4:
        thenumbers.insert(0, 0)
    if len(thenumbers) != len(set(thenumbers)):
        continue
    allthenumlist.append(thenumbers)
player_give_a = player_give_b = 0
the_history_box = {}

ans = Number()
ans = ans.random()

# 遊戲開始
while count_of_a < 4 and player_give_a < 4:
    gus = input("insert your guess(four numbers):")
    # 處理輸入錯誤
    while True:
        try:
            guslist = [int(x) for x in gus]
            if len(guslist) > 4:
                print('you can only insert four numbers')
                gus = input("insert your guess:")
                continue
            else:
                break
        except:
            print('you insert the wrong thing,try again')
            gus = input("insert your guess:")
            continue
    count_of_a, count_of_b = compare(ans, guslist)
    print("the result is:", count_of_a, "A", count_of_b, "B")
    if count_of_a == 4:
        break
    player_give_a = player_give_b = 0
    notallthenumlist = []
    a = 0
# 電腦產亂數給玩家猜，順便紀錄
    com_gus = random.choice(allthenumlist)
    com_gus_str = map(str, com_gus)
    print("I guess your number is ", com_gus)
    while True:
        try:
            player_give_ab = input("show me the result(?a?b):")
            player_give_a = int(player_give_ab[0])
            player_give_b = int(player_give_ab[2])
            if len(player_give_ab) < 4:
                print("show me the right answer!!")
                continue
            else:
                break
        except:
            print('you insert the wrong thing ,insert it again')
            player_give_ab = input("show me the result(?a?b):")
            a = 1
    the_history_box.update({''.join(com_gus_str): player_give_ab})
# 電腦把不可能的值刪除
    for y in allthenumlist:
        com_count_of_a, com_count_of_b = compare(com_gus, y)
        if com_count_of_a == player_give_a and com_count_of_b == player_give_b:
            notallthenumlist.append(y)
            allthenumlist = notallthenumlist
    # 玩家作弊
    if len(notallthenumlist) == 0:
        print("you cheated!!")
        break
    # 顯示出有神馬可能性
    print(the_history_box, "there are", len(notallthenumlist),
          "possibilities"+'\n'+"==================================================")

# 獲勝條件
if player_give_a == 4:
    print("haha I win loser")
if count_of_a == 4:
    print("it must be a mistake that i lost")
