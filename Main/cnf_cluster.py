from pyeda.inter import *
import sys
import ast
import pla2cnf
import cnf2pla
import subprocess

sys.setrecursionlimit(20000)

#function to split clause list
def split_list(seq, size):
    newlist = []
    splitsize = 1.0/size*len(seq)
    for i in range(size):
        newlist.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newlist

def getClusters(input_CNF_file_name):
    input_CNF_dict = cnf2pla.readCNFFile(input_CNF_file_name)
    clause_list = cnf2pla.getClauses(input_CNF_dict["clauses"])
    num_inputs = cnf2pla.getNumInputs(input_CNF_dict["params"])
    cluster_size = 7
    clause_list_split = [clause_list[x:(x+cluster_size)] for x in range(0, len(clause_list),(cluster_size))]
    print(clause_list_split)
    last_cluster_size = (len(clause_list))%cluster_size
    print(last_cluster_size)
    PLA_terms_list = []
    for current in range(len(clause_list_split)):
        PLA_terms_list.append(cnf2pla.getPLAlist(clause_list_split[current], num_inputs))
    print(PLA_terms_list)
    print(len(PLA_terms_list))
    for current in range(len(PLA_terms_list)-1):
        input_file = input_CNF_file_name.split(".")[0] + "-cluster"+str(current)
        print(input_file)
        cnf2pla.printPLAfile((input_file), PLA_terms_list[current], num_inputs, cluster_size)
    cnf2pla.printPLAfile((input_CNF_file_name.split(".")[0] + "-cluster"+str(len(PLA_terms_list)-1)), PLA_terms_list[-1], num_inputs, last_cluster_size)


if __name__ == '__main__':
    input_CNF_file_name = sys.argv[1]
    getClusters(input_CNF_file_name)
    







































# #Sort the Clauses
# #f_clause_list_str =[]
# # for current in range(len(f_clause_list)):
# #      f_clause_list_str.append(str(f_clause_list[current]))
# # f_clause_list_str.sort()

# #Import CNF file and get clauses in an AST
# with open(sys.argv[1], 'r') as fin:
#     f = parse_cnf(fin.read())
#     #f = ast2expr(parse_cnf(fin.read()))

# #Get CNF Clauses in a list
# l=len(f)
# f_clause_list =[]
# for i in range(1, l):
#     f_clause_list.append(ast2expr(f[i]))

# #Split the clauses into clusters
# num_of_clauses = int(l/50)
# f_clause_list_split = split_list(f_clause_list, (num_of_clauses + 1))
# f_split = []
# for current in range(len(f_clause_list_split)):
#     f_split1 = 1
#     for current2 in range(len(f_clause_list_split[current])):
#         f_split1 = And((f_clause_list_split[current][current2]),f_split1)
#     f_split.append(f_split1)
# print(len(f_split))
# cnf_encode = []
# for current in range(len(f_split)):
#     litmap, nvars, clauses = f_split[current].encode_cnf()
#     cnf_encode.append((DimacsCNF(nvars, clauses)))
# #f_min = str(f_nd)
# print((cnf_encode))
# inputCNF = sys.argv[1]
# for current in range(len(cnf_encode)):
#     CNF_split_files = inputCNF.split(".")[0] + "_out" + str(current) + ".cnf"
#     with open(CNF_split_files, "w" ) as file_out:
#         file_out.write(cnf_encode[current])