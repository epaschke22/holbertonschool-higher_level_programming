#!/usr/bin/python3
def weight_average(my_list=[]):
    tuplist = []
    divlist = []
    for i in my_list:
        tuplist.append(i[0] * i[1])
    for i in my_list:
        divlist.append(i[1])
    return (sum(tuplist) / sum(divlist))
