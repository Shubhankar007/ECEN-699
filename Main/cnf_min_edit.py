#!/usr/bin/python
from pyeda.inter import *
import sys
import ast
sys.setrecursionlimit(25000)
#function to split clause list
def split_list(seq, size):
    newlist = []
    splitsize = 1.0/size*len(seq)
    for i in range(size):
        newlist.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newlist


f_clause_list_str =[]

#Sort the Clauses
# for current in range(len(f_clause_list)):
#      f_clause_list_str.append(str(f_clause_list[current]))
# f_clause_list_str.sort()

#Import CNF file and get clauses in an AST
with open(sys.argv[1], 'r') as fin:
    f = parse_cnf(fin.read())
    #f = ast2expr(parse_cnf(fin.read()))

#Get CNF Clauses in a list
l=len(f)
f_clause_list =[]
for i in range(1, l):
    f_clause_list.append(ast2expr(f[i]))

#Split the clauses into clusters
num_of_clauses = int(l/30)
f_clause_list_split = split_list(f_clause_list, (num_of_clauses + 1))
f_split = []
for current in range(len(f_clause_list_split)):
    f_split1 = 1
    for current2 in range(len(f_clause_list_split[current])):
        f_split1 = And((f_clause_list_split[current][current2]),f_split1)
    f_split.append(f_split1)
    
#APPLY DE MORGAN
#Get NOT(F)
f_bar_split = []
f_bar_2 = []
for current in range(len(f_split)):
    f_bar_2.append(((~f_split[current])).to_nnf())
    f_bar_split.append(f_bar_2[current].to_dnf())
#print(f_bar)

############################## BOTTLENECK #############################################
#Run Espresso on split NOT(F)
f_bar_min_split = []
f_bar_min_split_2 = None
for current in range(len(f_bar_split)):
    f_bar_min_split_2 = espresso_exprs(f_bar_split[current])
    f_bar_min_split.append(expr(f_bar_min_split_2[0]))
#print(f_bar_min_split)

#Combine NOT(F)
c = 0
for current in range(len(f_bar_min_split)):
    c = Or((f_bar_min_split[current]),c)
#f_split.append(f_split1)
f_bar_min = expr(c)
#print(f_bar_min)

#APPLY DE MORGAN
#Get Minimized F
f_n = (~f_bar_min).to_nnf()
f_new = f_n.to_cnf()
litmap, nvars, clauses = f_new.encode_cnf()
f_nd = DimacsCNF(nvars, clauses)
f_min = str(f_nd)
#print(f_min)

#Generate Output file
inputfile = sys.argv[1]
outputfile = inputfile.split(".")[0] + "_out.cnf"
with open(outputfile, "w" ) as file_out:
    file_out.write(f_min)