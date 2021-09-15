import matplotlib.pyplot as plt
import sys

dic = {}
x = []
y = []
wordsHandler  =  open  (sys.argv[1],  encoding='utf-8')
while  True:
    line  =  wordsHandler.readline().rstrip('\n')
    dic[line] = 0
    if not line :
        break
wordsHandler.close()

ansHandler =  open  (sys.argv[2],  encoding='gbk')
while True:
    line = ansHandler.readline()
    s = ''
    flag = 0
    for i in line:
        if flag == 1 and i != '>':
            s+=''.join(i)
        if i == '<':
            flag = 1
        elif i == '>':
            flag = 0
    dic[s] += 1
    if not line:
        break
ansHandler.close()

for key in dic:
    x.append(key)
    y.append(dic[key])
x.pop()
y.pop()

plt.figure(figsize=(10,5))
plt.bar(x,y,color = '#9999ff',width = 0.5)
plt.title('Sensitive word statistics')
plt.xlabel('Sensitive words')
plt.ylabel('pieces')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
