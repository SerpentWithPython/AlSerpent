# -*- coding:gb2312 -*-
__author__ = 'lvkun.lk'

import time, datetime


def showtime():
    #��ӡ��ǰʱ�䣬time��datetime������֮һ�� datetime���Եõ������뼶����ʱ��
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #print datetime.datetime.now()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))