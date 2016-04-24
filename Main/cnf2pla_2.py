#!/usr/bin/python3
# from pyeda.inter import *
# f = open('mux.cnf', 'r')
# #file_contents = f.read()
# lines = f.readlines()
# for current in range(len(lines)):
#     print (lines[current])
#     str1=str(lines[current])
#     print (str1)
#     y=parse_cnf(str1)
#     print (y)
# #print (lines)
# f.close()
from pyeda.inter import *
import os
from pyeda.boolalg.table import TruthTable, PC_ZERO, PC_ONE, PC_DC


# ReadTheDocs doesn't build C extensions
# See http://docs.readthedocs.org/en/latest/faq.html for details



with open("quinn.cnf") as fin:
    f1 = ast2expr(parse_cnf(fin.read()))
#print(f)
#f.satisfy_one()
f_bar = (~f1).to_nnf()
exprs = f_bar.to_dnf()

support = frozenset.union(*[f.support for f in exprs])
inputs = sorted(support)

# Gather all cubes in the cover of input functions
fscover = set()
for f in exprs:
    fscover.update(f.cover)

ninputs = len(inputs)
noutputs = len(exprs)

cover = set()
for fscube in fscover:
    invec = list()
    for v in inputs:
        if ~v in fscube:
            invec.append(1)
        elif v in fscube:
            invec.append(2)
        else:
            invec.append(3)
    outvec = list()
    for f in exprs:
        for fcube in f.cover:
            if fcube <= fscube:
                outvec.append(1)
                break
        else:
            outvec.append(0)

    cover.add((tuple(invec), tuple(outvec)))

print(cover)
#f_bar_min = espresso_exprs(f_bar_2)
#f_n = ast2expr(f_bar_min)
#print(f_bar_min)
# f_n2 = (~expr(f_bar_min)).to_nnf()
# f_new = f_n2.to_cnf()
# f_new.satisfy_one()
#f.satisfy_one()