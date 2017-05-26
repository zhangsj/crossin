
from random import randint

game = 'game.txt'
name = raw_input('请输入你的名字:')
while True:
    with open(game) as r:
        scores = {}
        lines = r.readlines()
        for l in lines:
            s = l.split()
            scores[s[0]] = s[1:]
        score = scores.get(name)
        if score is None:
            score = [0, 0, 0]
            print '欢迎%s首次来玩！'% name
        else:
            game_times = int(score[0])
            min_times = int(score[1])
            total_times = int(score[2])
            avg_times = float(total_times) / game_times
            print '欢迎%s，祝你游戏愉快！\n你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
    num = randint(1, 100)
    times = 1
    print '你猜是几?'
    bingo = False
    while bingo == False:
        while True:
            print '第%d次' % times
            answer = raw_input('请输入1-100的数字:')
            if answer.isdigit():
                answer=int(answer)
                if  1 <= answer <= 100:
                    print answer
                    times += 1
                    # print times
                    if answer < num:
                        print '%d 太小了!\n' % answer
                    if answer > num:
                        print '%d 太大了!\n' % answer
                    if answer == num:
                        print '猜中了！！答案就是%d \n' % answer
                        bingo = True
                        break
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
    with open(r'game.txt', 'w') as outf:
        outf.write(result)
    g=raw_input('输入“go”再玩一次，否则退出游戏')
    if g=='go':
        print "新游戏"
        continue
    else:
        break