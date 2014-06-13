#coding=utf-8
#测试可用的google ip
import os
import urllib2
import re
import random   


workpath = os.getcwd()
#pattern = re.compile(r'(?<=href=").*(?=" target)') #预处理readme.md中的ip,结果保存在globalip.txt中
datafile = workpath + '/globalip.txt'
data = open(datafile).read().split('\n')

def google(ip):
    door = []
    for i in ip:
        if i != '':
            try:
                f = urllib2.urlopen(i,timeout = 0.3) #设置timeout,避免程序过长时间执行
                if f.getcode() == 200:
                    door.append(i)
            except IOError:
                pass
    return door

if __name__ == '__main__':
    luck = 0
    while(luck != 1):
        lucky = random.sample(data , 30)
        google_gate = google(lucky)
        if len(google_gate) != 0:
            luck = 1
            for g in google_gate:
                print(g)
    



