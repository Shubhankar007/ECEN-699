#!/usr/bin/python3
from pyeda.inter import *
f = open('quinn.cnf', 'r')
#file_contents = f.read()
lines = f.readlines()
joined_list = ['c']
joined_list_new = []
for current in range(len(lines)):
    #print (lines[current])
    str1=str(lines[current])
    l1=str1.split()
    joined_list = joined_list + l1
f.close()
for current in range(len(joined_list)):
    element = str(joined_list[current])
    if ((element.split()[0] != 'c') & (element.split()[0] != joined_list[2]) & (element.split()[0] != joined_list[5])& (element.split()[0] != 'p')):
        joined_list_new.append(element)
joined_list_new = map(int, joined_list_new)
num_inputs = max(joined_list_new)
#print (joined_list)
#print (joined_list_new)
print (num_inputs)