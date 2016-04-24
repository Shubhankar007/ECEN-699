#!/usr/bin/python
from pyeda.inter import *
with open("quinn.cnf") as fin:
    f = ast2expr(parse_cnf(fin.read()))
#print(f)
#f.satisfy_one()
#APPLY DE MORGAN
#Get NOT(F)
f_bar = (~f).to_nnf()
f_bar_2 = f_bar.to_dnf()
#Run Espresso on NOT(F)
f_bar_min = espresso_exprs(f_bar_2)
f_bar_min_2 = expr(f_bar_min[0])
#APPLY DE MORGAN
#Get Minimized F
f_n = (~f_bar_min_2).to_nnf()
f_new = f_n.to_cnf()
litmap, nvars, clauses = f_new.encode_cnf()
f_nd = DimacsCNF(nvars, clauses)
print(f_nd)