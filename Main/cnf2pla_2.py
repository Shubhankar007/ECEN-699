#!/usr/bin/python
#Input: CNF file path
#Output: params from cnf file
import sys
def readCNFParams(name):
    with open(name, "r") as f:
        for line in f:
            li=line.strip()
            if li[0] == "p":
                return li
#Input: CNF file path
#Output: list of clauses from cnf file
def readCNFClauses(name):
    with open(name, "r") as f:
        for line in f:
            li=line.strip()
            if (li[0] in ("c", "C", "p")):
                continue
            else:
                yield li

#Input: inputs_dict["clauses"]
#Output: list of clauses split into integers
def getClauses(clause_list):
    clause_list = (c.split() for c in clause_list)
    return ([int(n) for n in c] for c in clause_list)

#Input: inputs_dict["params"]
#Output: number of inputs in PLA
def getNumInputs(param_list):
    param = param_list.split()
    num_inputs = int(param[2])
    return num_inputs

#Input: inputs_dict["params"]
#Output: number of products in PLA
def getNumProducts(param_list):
    param = param_list.split()
    num_prod = int(param[3])
    return num_prod

#Inputs: 1. list of clauses split into integers
#        2. number of inputs in PLA
#Output: list of products for PLA file    
def getPLAlist(clause_list, num_inputs):
    s = "-"
    for current in clause_list:
        temp_list = []
        for index in range(1,(num_inputs+1)):
            temp_list.append("-")
        for index in range(len(current)):
            for i in range(1,(num_inputs+1)):
                if(abs(current[index])==i):
                    if(current[index]<0):
                        temp_list[i-1]="1"
                    else:
                        temp_list[i-1]="0"
        yield temp_list

#Inputs: 1. input CNF file path
#        2. list of products for PLA file
#        3. number of inputs in PLA
#        4. number of products in PLA
#Output: print PLA file
def printPLAfile(inputFile, PLA_list, num_inputs, num_prod):
    outputfile = inputFile.split(".")[0] + "_pla2.pla"
    with open(outputfile, "w" ) as file_out:
        file_out.write(".i ")
        file_out.write(str(num_inputs))
        file_out.write("\n.o 1")
        file_out.write("\n.p ")
        file_out.write(str(num_prod))
        file_out.write("\n")
        for current in PLA_list:
            for index in range(len(current)):
                file_out.write(current[index],)
            file_out.write(" 1 \n")
        file_out.write(".e")

#Get .pla file from .cnf 
#input: CNF File path
def convert_CNF_2_PLA(name):
    clauses = readCNFClauses(name)
    clause_list = getClauses(clauses)
    print("****************************************************************************************************************")
    params = readCNFParams(name)
    num_vars = getNumInputs(params)
    num_clause = getNumProducts(params)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    PLA_list = getPLAlist(clause_list, num_vars)
    print("#################################################################################################################")
    #print(list(PLA_list))
    printPLAfile(name, PLA_list, num_vars, num_clause)
    print("_________________________________________________________________________________________________________________")

if __name__ == '__main__':
    name = sys.argv[1]
    convert_CNF_2_PLA(name)