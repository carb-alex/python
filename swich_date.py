# -*- coding: utf-8 -*-
# requirement: python 3.6+
# usage: pls put the script in the folder "downloadTrades_inp.csv"

import os
import time
import datetime

#folder1 = "DownloadOrderInfo"
#folder2 = "DownloadTrades"
format_file = "downloadTrades_inp.csv"

def get_date(offset=0):
    """
    today = 20200609
    param: offset
    0:  return '20200609'
    -1: return '20200608'
    1:  return '20200610'
    """
    day = datetime.datetime.today()
    day = day + datetime.timedelta(days=offset)
    return day.strftime('%Y%m%d')

def _replace_date_in_file(daystr, filename):
    replace_row = 6
    lines = None

    with open(filename, 'r') as rf:
        lines = rf.readlines()

    cur_row = 0
    with open(filename, 'w') as wf:
        for line in lines:
            if cur_row < replace_row:
                wf.writelines(line)
            else:
                line = line.split(',')
                line[0] = daystr
                line[1] = daystr
                line = ','.join(line)
                wf.writelines(line)
            cur_row = cur_row + 1
            
def replace_date():
    daystr = get_date(-1)
    file = os.path.join('.',format_file)
    _replace_date_in_file(daystr, file)

if __name__ == "__main__":
    replace_date()
