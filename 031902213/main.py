  "诋": "讠氐",
  "谴": "讠遣",
  "限": "阝艮",
  "帕": "巾白",
  "伊": "亻尹",
  "掖": "扌夜",
  "列": "歹刂",
  "呃": "口厄",
  "颁": "分页",
  "纽": "纟丑",
  "瑚": "王胡",
  "键": "钅建",
  "捆": "扌困",
  "绑": "纟邦",
  "剽": "票刂",
  "蹦": "崩",
  "猖": "犭昌",
  "獗": "犭厥",
  "栋": "木东",
  "悚": "忄束",
  "幌": "巾晃",
  "赔": "贝咅",
  "吁": "口于",
  "锐": "钅兑",
  "哟": "口约",
  "剔": "易刂",
  "朽": "木丂",
  "吖": "口丫",
  "儆": "亻敬",
  "锈": "钅秀",
  "附": "阝付",
  "滔": "氵舀",
  "婊": "女表",
  "坊": "土方",
  "彰": "章彡",
  "懈": "忄解",
  "湛": "氵甚",
  "粥": "弓米弓",
  "妨": "女方",
  "胁": "月办",
  "腿": "月退",
  "邓": "又阝",
  "嗖": "口叟",
  "璐": "王路",
  "喵": "口苗",
  "槛": "木监",
  "朝": "龺月",
  "韩": "龺韦"
}

#开始时间
time1 = time.time()
#特殊符号集合
SpecialCode=['`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\','\'',';',',',
             '.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"',
             '<','>','?','…','·','*','【','】','？','《','》','：','“','，','。','、','/',' ','￥','！']
#创建空字典，将‘错误文本：正确文本’以键值对的形式存于该字典中
dict = {}
#检测出的敏感词总数，初始化为0
total = 0

class DfaFilter(object):
    def __init__(self):
        super(DfaFilter, self).__init__()
        #创建一个空敏感字字典
        self.Sensitive_dict={}
        #定义结束标志
        self.delimit = '\x00'

    #将敏感词导入并进行预处理
    def GetSensitiveWords(self, path):
        #打开敏感词文本，因为python的默认编码方式是gbk，而windows是utf-8，所以这里要用utf-8，否则打不开
        WordsHandler = open (path, encoding='utf-8')
        while True:
            #按行读取敏感词并去除读取字符串尾的换行符
            keywords = WordsHandler.readline().rstrip('\n')
            #针对拆分偏旁建树
            ppform = ''
            for i in keywords:
                #过滤字母
                if i not in zimubiao:
                    if i in chazi:
                      #将敏感字在拆分偏旁字典中查询拆分后的部分
                        ppform += ''.join(chazi[i])
            #将其形成键值对放入字典
            dict[ppform] = keywords
            #将其送入敏感词树建立函数
            self.AddSensitiveWords(ppform)
            #这里创建一个空列表，用来装一个字的拼音及其首字母
            pylist=[]
            #将一个敏感词的每一个敏感字都转成拼音及其首字母的形式
            for i in keywords:
                pyform = ""
                Firstcode = ""
                for index, value in enumerate(pypinyin.pinyin(i, style=pypinyin.NORMAL)):
                    #用join函数将转化成的拼音变成字符串
                    pyform += "".join(value)
                    #首字母
                    Firstcode += "".join(value[0][0])
                    pylist.append([pyform, Firstcode])
            self.DiGui(pylist, 0, len(keywords), '', keywords)
            #读入的关键词为空，则break
            if not keywords:
                break
        WordsHandler.close()

    #递归函数，将每个字的拼音或首字母与其他字的拼音和首字母进行排列组合，比如傻子:shaz or shazi
    def DiGui(self, pylist, i, length, chars, keywords):
        if i == length:
            #错误文本：正确文本
            dict[chars] = keywords
            #将排列组合后的敏感词字母送入敏感词生成树函数
            self.AddSensitiveWords(chars)
            return
        #将chars与下一个字的拼音合并
        self.DiGui(pylist, i+1, length, chars + pylist[i][0], keywords)
        #将chars与下一个字的首字母合并
        self.DiGui(pylist, i+1, length, chars + pylist[i][1], keywords)
        return


    def AddSensitiveWords(self, stword):
        if not stword:
            return
        #定义一个字典tree
        tree = self.Sensitive_dict
        for i in range(len(stword)):
            #如果这个字母已经在字典中，则字典跳转到该字母的下一个结点
            if stword[i] in tree:
                tree = tree[stword[i]]
            #如果不在就创建一个新结点
            else:
                for j in range(i, len(stword)):
                    #新结点首先为空
                    tree[stword[j]] = {}
                    #得到新树和新结点
                    last_tree = tree
                    last_char = stword[j]
                    #跳转到新结点的位置
                    tree = tree[stword[j]]
                #全部导入之后，打上结束键值对
                last_tree[last_char] = {self.delimit: 0}
                break
            if i == len(stword) - 1:
                tree[self.delimit] = 0


    def FilterSensitiveWords(self, message, linepos, ret):
        #起始位置
        start = 0
        #一行的敏感词总数
        part_total = 0
        while start < len(message):
            tree = self.Sensitive_dict
            #将文本进行切片后检测，比如start不断++，直到检测到敏感词头，则过滤后，start到达敏感词尾，然后继续切片检测
            message_chars = message[start:]
            #正常状态下，放入敏感词字母
            normal_ret = ''
            #分支状态下，放入敏感词字母，为了回退的时候，加入的字母也能同时回退，直接设置两个空字符串
            mirror_image_ret = ''
            #正常步数
            normal_step = 0
            #回退步数
            mirror_image_step = 0
            stop = 0
            #已经检测到敏感词标志
            Code_flag = 0
            #进入分支状态标志
            Branch_flag = 0
            for char in message_chars:
                #创建一个空字符串，用来存待检测字的拼音
                pychar=''
                for index,value in enumerate(pypinyin.pinyin(char,style=pypinyin.NORMAL)):
                    pychar+=''.join(value).lower()
                #front为敏感词头在原文本中的位置
                front = start
                #Code_flag状态为1，表明正在检测一个敏感词，此时如果待检测的字为特殊符号，则步数+1，进入下一次循环
                if Code_flag == 1 and pychar[0] in SpecialCode:
                    #检测的位置不能超过待检测文本长度
                    if (start+normal_step+1) < len(message):
                        #该记号表明前面遇到了分支,镜像步数用于回退
                        if Branch_flag == 1:
                            normal_step += 1
                            mirror_image_step += 1
                            continue
                        #若未遇到分支，则正常步数+1
                        else:
                            normal_step += 1
                            continue

                #遍历字符串中的每个字母
                for i in pychar:
                    #如果这个字母在敏感词树中
                    if i in tree:
                        #对于正常状态下，且值不含结束键的字母存入normal_ret
                        if Branch_flag == 0 and self.delimit not in tree[i]:
                            normal_ret += ''.join(i)
                        #对于值只有结束键的字母
                        elif self.delimit in tree[i] and len(tree[i]) == 1:
                            #分支状态
                            if Branch_flag == 1:
                                mirror_image_ret += ''.join(i)
                            #正常状态
                            else:
                                normal_ret += ''.join(i)
                        #分支状态下或者值不仅仅包含结束键
                        else:
                            #区分此时的字母在原文本中是为单字母还是一个字的拼音的一个字母
                            #如果是一个字的拼音的一个字母，比如falungong中的前一个g
                            if len(pychar) != 1:
                                mirror_image_ret += ''.join(i)
                            #如果是单字母，比如falg中的g
                            else:
                                normal_ret += ''.join(i)
                        Code_flag = 1
                        #结束键不在这个字母的字典中
                        if self.delimit not in tree[i]:
                            #跳转到i结点
                            tree = tree[i]
                        #结束键在这个字母的字典中，但子树的字典键值对不止一个，表明此时遇到了分支，进入分支状态
                        elif self.delimit in tree[i] and len(tree[i]) != 1:
                            Branch_flag = 1
                            #跳转到i结点
                            tree = tree[i]
                        #这个字母的字典里只有结束键,表示找到了敏感词尾
                        else:
                            #找到敏感词尾的位置
                            start += normal_step
                            back = start
                            part_total += 1
                            #找到错误文本对应的正确文本
                            true = dict[normal_ret+mirror_image_ret]
                            # 将结果写入ret列表中
                            ret.append('Line'+str(linepos)+':'+'<'+true+'>'+message[front:back+1])
                            #停止遍历
                            stop = 1
                            break
                    #如果这个字母不在敏感词树中
                    else:
                        #如果为分支状态
                        if Branch_flag == 1:
                            if normal_ret in dict:
                                start += normal_step
                                #步数回退
                                start -= mirror_image_step
                                back = start
                                part_total += 1
                                true = dict[normal_ret]
                                ret.append('line' + str(linepos) + ':' + '<' + true + '>' + message[front:back+1])
                                #重置分支状态
                                Branch_flag = 0
                                #停止遍历
                                stop = 1
                                break
                            else:
                                start += normal_step
                                start -= mirror_image_step
                                stop = 1
                                break
                        else:
                            #停止遍历
                            stop = 1
                            break
                if stop == 1:
                    break
                #分支状态下，镜像步数和正常步数要同步，用于回退
                if Branch_flag == 1:
                    normal_step += 1
                    mirror_image_step += 1
                else:
                    normal_step += 1
            start += 1
        #返回敏感词数量
        return part_total,ret

    #针对拆分偏旁进行过滤
    def SplitSideFilter(self,message,linepos,ret):
        start = 0
        part_total = 0
        message = message.lower()
        while start < len(message):
            tree = self.Sensitive_dict
            step = 0
            Ret = ''
            front = start
            message_chars = message[start:]
            for char in message_chars:
                #因为拆分偏旁一定是汉字，所以排除字母
                if char in tree and char not in zimubiao:
                    Ret += ''.join(char)
                    step += 1
                    if self.delimit not in tree[char]:
                        tree = tree[char]
                    else:
                        start += step - 1
                        back = start
                        part_total += 1
                        true = dict[Ret]
                        ret.append('Line' + str(linepos) + ':' + '<' + true + '>' + message[front:back + 1])
                else:
                    break
            start += 1
        return part_total,ret

if __name__ == "__main__":
    #实例化对象
    x = DfaFilter()
    x.GetSensitiveWords(sys.argv[1])
    #在python中默认的编码方式是 “ gbk ”，而Windows中的文件默认的编码方式是 “ utf-8 ”
    OrgHandler = open(sys.argv[2], encoding='utf-8')
    linepos = 1
    empty_flag = 0
    # 一个空列表，用来暂时储存过滤结果
    ret = []
    while True:
        # 获取文件的每行内容
        line = OrgHandler.readline().rstrip('\n')
        #整个文本的敏感词总数
        result,ret=x.FilterSensitiveWords(line, linepos, ret)
        total += result
        result,ret= x.SplitSideFilter(line, linepos, ret)
        total +=result
        #行数++
        linepos += 1
        if not line:
            flag1+=1
        if line:
            flag1 = 0
        #当空行数量大于3时才跳出
        if flag1 > 3:
            break
    OrgHandler.close()
    #将列表里的结果按顺序打印在输出文本中
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
    print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024) )
