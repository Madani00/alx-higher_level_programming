#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    summ = 0
    fre = 0
    for i in my_list:
        summ += (i[0] * i[1])
        fre += (i[1])
    return summ / fre
