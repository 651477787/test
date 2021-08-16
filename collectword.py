#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 21:05
# @Author  : xiangxiao
# @FileName: collectwords.py
# @Software: PyCharm for conda3
# @Version： V0.1
import sortedcollections

aaalist = []
aaa = "jack dog cat monkey dog cat monkey monkey dog boy boy dog lion"
aaalist = aaa.split(" ")
print(aaalist)

bbblist = []
dic1 = {}
dic2 = {}
for i in range(0, len(aaalist)):
    count = 1
    for j in range(i+1, len(aaalist)):
        if ( aaalist[i] == aaalist[j] ):
            count += 1
    if aaalist[i] not in dic1:
        dic1[aaalist[i]] = count

print(dic1.items())
#print(sorted(dic1.values()))
#print(sorted(dic1.values()))

dic2 = sorted(dic1.items(), key=lambda item:item[1])
print(dic2)
for key, value in dic2:
    #print(f'{key}:{value}')
    if key not in bbblist :
        bbblist.append(key)

bbblist.reverse()
print(bbblist)



dic3 = sorted(dic1.items(), key=lambda item:item[1], reverse=True)
print(dic3)
for key, value in dic3:
    if key not in bbblist :
        bbblist.append(key)
print(bbblist)
