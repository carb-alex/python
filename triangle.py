# -*- coding: utf-8 -*-
#杨辉三角形
def triangle():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
    return 'done'