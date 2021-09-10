#读写文件
desktop_path = "D:\\pythonProject\\"  # 新创建的txt文件的存放路径
full_path = desktop_path + 'ans.txt'  # 也可以创建一个.doc的word文档
file = open(full_path, 'w')


fileHandler  =  open  ("words.txt",  encoding='utf-8')#在python中默认的编码方式是 “ gbk ”，而Windows中的文件默认的编码方式是 “ utf-8 ”
while  True:
    # Get next line from file
    line  =  fileHandler.readline()
    # If line is empty then end of file reached
    file.write(line)
    if  not  line  :
        break;
    print(line.strip())
    # Close Close
fileHandler.close()
