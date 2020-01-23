word = input('insert word:')
word_ls=[x for x in word]
gus_ls=[ '-' for x in word]
count=0
ls=[]
for x in range(len(gus_ls)):
    ls.append("0")
while True:
    gus = input('insert guess:')
    if gus=='123':
        break
    if len(gus)==1:
        if gus in word_ls:
            while gus in word_ls:
                gus_ls[word_ls.index(gus)]=gus
                word_ls[word_ls.index(gus)]="0"
        else:
            print("wrong guess!!!!!")
    else:
        print("one letter at a time!!!!!")
    count+=1
    for x in gus_ls:
        print(x,end='')
    print('  counts:',count)
    if ls == word_ls:
        break
print('congrats!!')