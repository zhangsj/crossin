#coding:utf-8
from random import randint
# game=r'E:\OPS\test\pylearn\crossin\game.txt'
# name=raw_input('请输入你的名字:')
def re():
    with open(game) as r:
        scores={}
        lines=r.readlines()
        for l in lines:
            s=l.split()
            if len(s)==4:
                scores[s[0]]=s[1:]
                score=scores.get(name)
                game_times = int(score[0])
                min_times = int(score[1])
                total_times = int(score[2])
                avg_times = float(total_times) / game_times
    # print '%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
    return name,game_times,min_times,total_times

def cai():
    global game_times,min_times,total_times
    num = randint(1, 100)
    times=0
    print 'Guess what i think?'
    bingo = False
    while bingo == False:
        times += 1
        answer = input()
        if answer < num:
            print 'too small!'
        if answer > num:
            print 'too big!'
        if answer == num:
            print 'BINGO!'
            bingo=True
            # retrun times
    if game_times ==0 or times < min_times:
        min_times = times
    total_times += times
    game_times += 1
    avg_times=total_times/game_times
    return game_times,min_times,total_times
    print '恭喜你猜中了答案就是%d' % num
    print '你一共用了%d次机会\n你一共完了%d次游戏\n你平均%.2f次猜中答案\n你最好的成绩是%d次！\n' % (total_times,game_times,avg_times,min_times)
# if name is None:
#     score=[str(game_times),str(min_times),str(total_times)]
#     line=' '.join(score)+'\n'
#     print line
#     result += line
#     scores[name]=[str(game_times),str(min_times),str(total_times)]
#
#     for n in scores:
#         if n is None:
#             line=' '.join(score[n])+'\n'
#         else:
#             line=n+' '+' '.join(scores[n])+'\n'
#         result += line
#
# #result = '%d %d %d'%(game_times,min_times,total_times)
#     with open(r'E:\OPS\test\pylearn\crossin\game.txt','w') as outf:
#         outf.write(result)
# coding:utf-8
from random import randint

game = 'game.txt'
name = raw_input('请输入你的名字:')
with open(game) as r:
    scores = {}
    lines = r.readlines()
    for l in lines:
        s = l.split()
        scores[s[0]] = s[1:]
    score = scores.get(name)
    if score is None:
        score = [0, 0, 0]
    game_times = int(score[0])
    min_times = int(score[1])
    total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print type(game_times), type(min_times), type(avg_times)
print '欢迎%s，祝你游戏愉快！\n你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
num = randint(1, 100)
times = 0
print 'Guess what i think?'
bingo = False
while bingo == False:
    while True:
        answer = raw_input('请输入1-100的数字:')
        if answer.isdigit():
            answer=int(answer)
            if  1 <= answer <= 100:
                times += 1
                print times
                if answer < num:
                    print 1
                    print 'too small!'
                if answer > num:
                    print 'too big!'
                if answer == num:
                    print 'BINGO!'
                    bingo = True
        else:
            break

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
scores[name] = [str(game_times), str(min_times), str(total_times)]
print '恭喜你猜中了答案就是%d' % num
print '你一共用了%d次机会\n你一共完了%d次游戏\n你平均%.2f次猜中答案\n你最好的成绩是%d次！\n' % (total_times, game_times, avg_times, min_times)
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line


#
# if not name:
#     print '不记名游戏（不保存记录）'
#     game_times = 0
#     min_times = 0
#     total_times = 0
#     cai()
#
#
# else:
#     name=re()[0]
#     game_times = re()[1]
#     min_times = re()[2]
#     total_times = re()[3]
#     avg_times = total_times / game_times
#     print '%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
#     cai()
#     # result = '%d %d %d'%(game_times,min_times,total_times)
#     with open(r'E:\OPS\test\pylearn\crossin\game.txt', 'w') as outf:
#         outf.write(result)