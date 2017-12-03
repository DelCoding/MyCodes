# -*- coding:utf-8 -*-

file = open('hello.txt', 'r', encoding='UTF-8')
strs = file.read()
count = len(strs)
print("该文件字符串长度为：" + str(count))

carry = 0   # 存放进位
sum = 0     # 存放结果
dou_list = []   # 存放每对字符串的16进制
for a in range(0, count, 2):    # 下边从0开始每隔2个长度取出字符串,(He),(ll)...
    dec = ord(strs[a])
    one = hex(dec)[-2:]   #将第一个字符转化为16进制
    # 如果count是奇数的话，第二个字符就为 00
    if a + 1 == count:
        second = '00'
    else:
        dec1 = ord(strs[a + 1])
        second = hex(dec1)[-2:]      #将第二个字符转化为16进制
    double = '0x' + one + second    # 两位结合成：0x4865添加到列表中
    dou_list.append(double)

for i in range(len(dou_list)):
    num1 = int(dou_list[i], 16)     #将第一个操作数从16进制转化成10进制
    sum += num1
    if sum > 65535:    # FFFF 的十进制为 65535，大于这个数说明有进位
        sum -= 65536   # 把进位去掉，仅保留后四位，如 123F1 转换成 23F1
        carry += 1      # 记录进位

sum += carry    # 最后将结果跟进位相加， 有进位的话还是要舍去后再相加
if sum > 65535:
    sum -= 65536
    sum += 1

print("此文件的16位校验和为：" + hex(sum))






