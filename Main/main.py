#!/usr/bin/python
from pyeda.inter import *
import sys
import ast
import pla2cnf
import cnf2pla
#import cnf_cluster
import subprocess

sys.setrecursionlimit(20000)
inputCNF = sys.argv[1]
input_CNF_dict = cnf2pla.readCNFFile(inputCNF)
clause_list = cnf2pla.getClauses(input_CNF_dict["clauses"])
num_inputs = cnf2pla.getNumInputs(input_CNF_dict["params"])
cluster_size = 25
clause_list_split = [clause_list[x:(x+cluster_size)] for x in range(0, len(clause_list),(cluster_size))]
#print(clause_list_split)
last_cluster_size = (len(clause_list))%cluster_size
#print(last_cluster_size)
PLA_terms_list = []
for current in range(len(clause_list_split)):
    PLA_terms_list.append(cnf2pla.getPLAlist(clause_list_split[current], num_inputs))
#print(PLA_terms_list)
#print(len(PLA_terms_list))
for current in range(len(PLA_terms_list)-1):
    input_file = inputCNF.split(".")[0] + "-cluster"+str(current)
    #print(input_file)
    cnf2pla.printPLAfile((input_file), PLA_terms_list[current], num_inputs, cluster_size)
cnf2pla.printPLAfile((inputCNF.split(".")[0] + "-cluster"+str(len(PLA_terms_list)-1)), PLA_terms_list[-1], num_inputs, last_cluster_size)


for current in range(len(PLA_terms_list)):
    inputfile = "../Main/"+inputCNF.split(".")[0] + "-cluster"+str(current) + "%_pla.pla"
    #print(inputfile)
    outputfile = inputfile.split("%")[0] + "%_min.pla"
    print(outputfile)
    subprocess.call(("../espresso/./espresso "+inputfile+" > "+outputfile), shell=True)
print("end espresso")
for current in range(len(PLA_terms_list)):
    inputfile = "../Main/"+inputCNF.split(".")[0] + "-cluster"+str(current) + "%_pla.pla"
    PLA_min_files = inputfile.split("%")[0] + "%_min.pla"
    # CNF_min_files = outputfile.split("%")[0] + "%_min_cnf.cnf"
    #print(PLA_min_files)
    pla2cnf.convert_PLA_2_CNF(PLA_min_files)
join_cnf = []
for current in range(len(PLA_terms_list)):
    inputfile = "../Main/"+inputCNF.split(".")[0] + "-cluster"+str(current) + "%_pla.pla"
    PLA_min_files = inputfile.split("%")[0] + "%_min.pla"
    CNF_min_files = PLA_min_files.split("%")[0] + "%min_cnf.cnf"
    #print(CNF_min_files)
    #s="x"+str(current)
    #print(s)
    with open(CNF_min_files) as fin:
        g = ast2expr(parse_cnf(fin.read()))
    join_cnf.append(g)
    #print(join_cnf)
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
f_join1 = 1
for current in range(len(join_cnf)):
    f_join1 = And(f_join1,join_cnf[current])
f_join = []
f_join.append(f_join1)
f_new = f_join[0].to_cnf()
litmap, nvars, clauses = f_new.encode_cnf()
f_nd = DimacsCNF(nvars, clauses)
f_min = str(f_nd)
#print(f_min)
##
inputfile2 = sys.argv[1]
outputfile = inputfile2.split(".")[0] + "_FINAL_out.cnf"
with open(outputfile, "w" ) as file_out:
    file_out.write(f_min)