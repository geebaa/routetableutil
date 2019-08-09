#!/usr/bin/env python
file = open('rt_tables', 'r')
rt_table_dict = dict()
for each in file:
    if each[0]=='#' or each[0]=='\n' :
        continue
    print (each)
    each.strip()
    eachsplit=each.split()
    rt_table_dict[eachsplit[1]] = eachsplit[0]


