#coding:gbk
from random import randint

name = raw_input('请输入你的名字:')
while True:
    with open('game.txt','a+') as r:
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
            # print u'欢迎\t'
            print '\n欢迎%s首次来玩！' % name
        else:
            game_times = int(score[0])
            min_times = int(score[1])
            total_times = int(score[2])
            avg_times = float(total_times) / game_times
            print '\n欢迎%s祝你游戏愉快\n你已经玩了%d次,最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
    num = randint(1, 100)
    times = 1
    print '\n你猜是几',num
    bingo = False
    while bingo == False:
        while True:
            print '第 %d 次' % times
            answer = raw_input('请输入1-100的数字:')
            if answer.isdigit():
                answer=int(answer)
                if  1 <= answer <= 100:
                    print answer

                    # print times
                    if answer < num:
                        print '%d 太小了!\n' % answer
                    if answer > num:
                        print '%d 太大了!\n' % answer
                    if answer == num:
                        print '\n猜中了！！答案就是%d' % answer
                        bingo = True
                        break
                    times += 1
            else:
                break
    total_times += times
    game_times += 1
    if game_times == 1:
        min_times = times
        avg_times = times
    else:
        avg_times=float(total_times)/game_times
    if  times < min_times:
        min_times = times
    scores[name] = [str(game_times), str(min_times), str(total_times)]
    # print '恭 喜 你 猜 中 了 答 案 就 是',num
    print '\n你一共猜了%d次\n你一共完了%d次游戏\n你平均%.2f次猜中答案\n你最好的成绩是%d次！\n' % (total_times, game_times, avg_times, min_times)
    result = ''
    for n in scores:
        line = n + ' ' + ' '.join(scores[n]) + '\n'
        result += line
    with open(r'game.txt', 'w') as outf:
        outf.write(result)
    g=raw_input('输入“go”再玩一次，否则退出游戏   ')
    if g=='go':
        print '\n新游戏'
        continue
    else:
        break
    False
