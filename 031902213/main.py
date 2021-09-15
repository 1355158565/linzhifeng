import time
import pypinyin
import sys
import psutil
import os

time1 = time.time() #开始时间
regEx=['`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\','\'',';',',',
       '.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"',
       '<','>','?','…','·','*','【','】','？','《','》','：','“','，','。','、','/',' ','￥','！'] #特殊符号集合
dict = {}
total = 0
ret = []

class dfafilter(object):
    def __init__(self):
        super(dfafilter, self).__init__()
        self.keywords_chain={}
        self.delimit = '\x00'

    def getsensitivewords(self,path):
        wordsHandler = open(path, encoding='utf-8')
        while True:
            keyword = wordsHandler.readline().rstrip('\n')
            list1 = []
            for i in keyword:
                s1 = ""
                s2 = ""
                for index, value in enumerate(pypinyin.pinyin(i, style=pypinyin.NORMAL)):
                    s1 += "".join(value)
                    s2 += "".join(value[0][0])
                    list1.append([s1,s2])
            self.digui(list1,0,len(keyword),'',keyword)
            if not keyword:
                break

    def digui(self,list1,i,length,char,keyword):
        if i == length:
            dict[char] = keyword
            self.addsensitivewords(char)
            return
        self.digui(list1,i+1, length, char+list1[i][0], keyword)
        self.digui(list1,i+1, length, char+list1[i][1], keyword)
        return

    def addsensitivewords(self, stword):
        if not stword:
            return
        tree = self.keywords_chain
        for i in range(len(stword)):
            if stword[i] in tree:
                tree = tree[stword[i]]
            else:
                for j in range(i, len(stword)):
                    tree[stword[j]] = {}
                    last_level, last_char = tree, stword[j]
                    tree = tree[stword[j]]
                last_level[last_char] = {self.delimit: 0}
                break
            if i == len(stword) - 1:
                tree[self.delimit] = 0

    def filtersensitivewords(self, message, linepos):
        start = 0
        resttotal = 0
        while start < len(message):
            tree = self.keywords_chain
            message_chars = message[start:]
            step = 0
            step1 = 0
            ret1 = ''
            ret2 = ''
            stop = 0
            flag = 0
            flag1 = 0
            for char in message_chars: #遍历剩余未遍历的字符串
                ss=''
                for index,value in enumerate(pypinyin.pinyin(char,style=pypinyin.NORMAL)):  #将某字变成拼音并且转为小写字符串形式
                    ss+=''.join(value)
                    ss=ss.lower()
                front = start  #front为敏感词头在原文本中的位置
                if flag == 1 and ss[0] in regEx:
                    if (start+step+1) < len(message):
                        if flag1 == 1:
                            step += 1
                            step1 += 1
                            continue
                        else:
                            step += 1
                            continue
                for i in ss:   #遍历一个字符串中的每个字母
                    if i in tree:   #如果这个字母在敏感词树中
                        if flag1 == 0:
                            ret1 += ''.join(i)  #将其放入空字符串中
                        else:
                            ret2 += ''.join(i)
                        flag = 1
                        if self.delimit not in tree[i]: #结束符不在这个字母的子树中
                            tree = tree[i]  #跳入子树
                        elif self.delimit in tree[i] and len(tree[i]) != 1: #如果结束符在这个字母的子树，但子树的字典键值对不止一个
                            flag1 = 1  #标记
                            tree = tree[i] #跳入子树
                        else:  #这个字母的子树字典里只有结束符
                            start += step  #找到敏感词尾的位置
                            back = start
                            resttotal += 1 #统计数+1
                            true = dict[ret1+ret2] #找到错误文本对应的正确文本
                            ret.append('line'+str(linepos)+':'+'<'+true+'>'+message[front:back+1]) #将结果写入ret空列表中
                            stop = 1 #停止这一次遍历
                    else:  #如果这个字母不在敏感词树中
                        if flag1 == 1: #标记为1
                            start += step #
                            start -= step1
                            back = start
                            resttotal += 1
                            true = dict[ret1]
                            ret.append('line' + str(linepos) + ':' + '<' + true + '>' + message[front:back])
                            flag1 = 0
                            stop = 1
                        else:
                            stop = 1
                            break
                if stop == 1:
                    break
                step += 1
            start += 1
        return resttotal

if __name__ == "__main__":
    x = dfafilter()  # 实例化对象
    x.getsensitivewords(sys.argv[1])
    fileHandler = open(sys.argv[2], encoding='utf-8')  # 在python中默认的编码方式是 “ gbk ”，而Windows中的文件默认的编码方式是 “ utf-8 ”
    linepos = 1
    flag1 = 0
    while True:
        # 获取文件的每行内容
        line = fileHandler.readline().rstrip('\n')
        result=x.filtersensitivewords(line, linepos)
        total += result
        linepos += 1
        if not line:
            flag1+=1
        if line:
            flag1 = 0
        if flag1 > 3:
            break
    fileHandler.close()
    ret.append(str(total))
    file = open(sys.argv[3], 'w')
    y=len(ret)-1
    file.write('total:')
    file.write(str(ret[y]))
    file.write('\n')
    for i in range(len(ret)-1):
        file.write(str(ret[i]))
        file.write('\n')
    time2 = time.time()
    print('总共耗时:' + str(time2 - time1) + 's')
    print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
