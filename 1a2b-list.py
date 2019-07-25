import random
d = dict.fromkeys(range(10))
ans = random.sample(list(d), 4)
print(d)
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


while count_of_a < 4:
    gus = input("insert:")
    guslist = [int(x) for x in gus]
    count_of_a, count_of_b = compare(ans, guslist)
    print(count_of_a, "A", count_of_b, "B")
