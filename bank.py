# -*- coding:utf-8 -*-

Poc = []    #用来存放进程当前已有的资源数
Src = []    #用来存放各资源总数
Remain_Src = [] #用来存放各资源还剩下多少
Max_Src = []    #用来存放各进程对各资源的最大需求
Need_Src = []   # 存放进程对各资源还欠缺的数量
src_num = int(input('请输入系统资源数：'))
src_name = []   #存放资源名字
ch = 'A'

for a in range(src_num):
    text = '请输入{}总的资源数：'.format(ch)
    temp = int(input(text))
    Src.append(temp)
    Remain_Src.append(temp)
    src_name.append(ch)
    ch = chr(ord(ch) + 1)

poc_num = int(input('请输入系统进程数：'))
for index,b in enumerate(range(poc_num)):
    tmp = []    # 存放进程已拥有各资源的数量
    for one in src_name:
        text = '请输入P{}进程已拥有{}的资源数：'.format(index, one)
        temp = int(input(text))
        tmp.append(temp)
    Poc.append(tmp)

print('\n')
for index, b in enumerate(range(poc_num)):
    tmp2 = []  # 存放进程对各进程的最大需求数
    for one in src_name:
        text = '请输入P{}进程需要{}的最大资源数：'.format(index, one)
        temp = int(input(text))
        tmp2.append(temp)
    Max_Src.append(tmp2)


# 初始分配资源后计算各资源所剩值
def Init_RemainSrc():
    # 存放各资源已用大小
    temp = []
    for one in range(len(src_name)):
        one = 0 #初始为 0
        temp.append(one)

    for index, a in enumerate(Poc):
        for local,value in enumerate(a):
            temp[local] += value

    for index, value in enumerate(Remain_Src):
        Remain_Src[index] = value - temp[index]
        if Remain_Src[index] < 0:
            print('当前所剩资源为：')
            print(Remain_Src)
            print('出现负数，初始资源分配不合理！')
            exit(-1)

# 初始分配后计算剩余资源
Init_RemainSrc()


# 计算各进程还需要各资源数
for index, max_src in enumerate(Max_Src):   # 依次取出每个进程对各资源的最大需求
    had_src = Poc[index]    # 取出对应进程已经分配了的资源数
    temp = []   # 中转，适应自定义的资源大小
    for one in range(len(src_name)):
        one = 0  # 初始为 0
        temp.append(one)

    for i, j in enumerate(max_src):
        temp[i] = j - had_src[i]    # 最大减已拥有资源
    Need_Src.append(temp)


# 计算进程还回资源后的剩余资源
def Update_RemainSrc(index):
    for one in Poc[index]:
        for index,a in enumerate(Remain_Src):
            Remain_Src[index] += a

ok_judge = 0    #记录满足分配需求的进程，如果等于 3 说明当前系统剩余资源能喂饱所有进程，说明存在安全序列
err_judge = 0   #记录不满足分配需求的进程，如果等于 3 说明当前系统剩余资源全部匹配不了，说明不存在安全序列
answer = ''

while 1:
    for index,one in enumerate(Poc):
        if sum(one) == 0:
            continue
        temp = Need_Src[index]  #取出该进程需要的资源数
        isok = 1
        for i,j in enumerate(temp):
            if Remain_Src[i] < j:
                isok = 0
                err_judge += 1
                break
        if isok == 1:
            answer += 'P' + str(index) + ' '
            ok_judge += 1  # 找到一个能满足需要的进程
            Update_RemainSrc(index) # 进程结束后，释放资源对应更新剩余资源

        if ok_judge == len(Poc):
            print('\n当前系统处于安全状态！安全序列为：')
            print(answer)
            exit(0)
        if err_judge == len(Poc):
            print('\n找不到安全序列，当前系统处于不安全状态！')
            exit(0)
