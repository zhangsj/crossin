#coding:utf-8
from random import randint
game=r'E:\OPS\test\pylearn\crossin\game.txt'
name=raw_input('请输入你的名字:')
with open(game) as r:
    scores={}
    lines=r.readlines()
    for l in lines:
        s=l.split()
        scores[s[0]]=s[1:]
    score=scores.get(name)
    if score is None:
        score=[0,0,0]
    game_times = int(score[0])
    min_times = int(score[1])
    total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print type(game_times),type(min_times),type(avg_times)
print '%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name,game_times,min_times,avg_times)
num = randint(1,100)
times =0
print 'Guess what i think?'
bingo = False
def check_answer(answer):
    try:
        answer = int(answer)
            if answer <= 0 or answer > 100:
                break
    except Exception:
        answer = raw_input('请输入1-100的数字（输入了字符串或者超出范围）：')


while bingo == False:
    answer=raw_input('请输入1-100的数字:')
    times += 1
    print '第%d次' % times
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'BINGO!'
        bingo = True

if game_times ==0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result += line
                        
#result = '%d %d %d'%(game_times,min_times,total_times)
with open(r'E:\OPS\test\pylearn\crossin\game.txt','w') as outf:
    outf.write(result)
