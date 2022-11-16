import os

from psutil import *
from time import *

temp = []

for i in disk_partitions():  # 初始化列表
    temp.append(i[1])

while True:
    temp1 = str(temp)  # 将列表保存副本
    temp.clear()  # 清空列表

    for i in disk_partitions():  # 获取新列表
        temp.append(i[1])

    if len(temp) > len(temp1.split(',')):  # 比较是否有新设备接入
        more = [x for x in temp if x not in temp1]  # 求取并储存新加入设备的盘符
        print('有新的设备插入:' + str(more))
        for m in more:  # 遍历所有新接入的设备并寻找AUTORUN文件
            for a in os.listdir(m):
                if os.path.splitext(a)[0].upper() == 'AUTORUN':
                    os.startfile(m + a)  # 使用默认程序打开文件

    sleep(1)
