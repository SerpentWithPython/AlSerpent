# -*- coding:gb2312 -*-
__author__ = 'lvkun.lk'

from mmisc import initconf,mtimer

config_file_path="global_setting.ini"

def info():
    print """::Tool set of Mac Lv @Alipay from 2014::
    [USAGE]
    main.py  -h                         #print this help info   [��ӡ������Ϣ]
    main.py  -a  <algorithm>            #runing the algorithm   [����ָ���㷨]

    ==options==
    <algorith>
    """

if __name__ == "__main__":
    info()
    mtimer.showtime()



