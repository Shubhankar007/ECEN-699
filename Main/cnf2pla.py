#!/usr/bin/python
#Input: CNF file path
#Output: dictionary of params and clauses from cnf file
def readCNFFile(name):
    lines_str = []
    inputs_dict = {}
    clause_list = []
    with open(name, "r") as f:
        for line in f.readlines():
            lines_str.append(str(line))
        for current in range(len(lines_str)):
            li=lines_str[current].strip()
            if li.startswith("c"):
                pass
            elif li.startswith("C"):
                pass
            elif li.startswith("p"):
                inputs_dict['params'] = li
            else:
                clause_list.append(li)
        inputs_dict['clauses']=clause_list
        f.close()
    return inputs_dict

#Input: inputs_dict["clauses"]
#Output: list of clauses split into integers
def getClauses(clause_list):
    for current in range(len(clause_list)):
        temp = clause_list[current].split()
        clause_list[current] = temp
    for current in range(len(clause_list)):
        nums = [int(n) for n in clause_list[current]]
        clause_list[current]= nums
    return clause_list

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
    temp_list_total=[]
    for current in range(len(clause_list)):
        temp_list = []
        for index in range(1,(num_inputs+1)):
            temp_list.append("-")
        for index in range(len(clause_list[current])):
            for i in range(1,(num_inputs+1)):
                if(abs(clause_list[current][index])==i):
                    if(clause_list[current][index]<0):
                        temp_list[i-1]="1"
                    else:
                        temp_list[i-1]="0"
        temp_list_total.append(temp_list)
    return temp_list_total 

#Inputs: 1. input CNF file path
#        2. list of products for PLA file
#        3. number of inputs in PLA
#        4. number of products in PLA
#Output: print PLA file
def printPLAfile(inputFile, PLA_list, num_inputs, num_prod):
    outputfile = inputFile.split(".")[0] + "_pla.pla"
    with open(outputfile, "w" ) as file_out:
        file_out.write(".i ")
        file_out.write(str(num_inputs))
        file_out.write("\n.o 1")
        file_out.write("\n.p ")
        file_out.write(str(num_prod))
        file_out.write("\n")
        for current in range(len(PLA_list)):
            for index in range(len(PLA_list[current])):
                file_out.write(PLA_list[current][index],)
            file_out.write(" 1 \n")
        file_out.write(".e")

#Get .pla file from .cnf 
#input: CNF File path
def convert_CNF_2_PLA(name):
    inputs = readCNFFile(name)
    clause_list = getClauses(inputs['clauses'])
    num_vars = getNumInputs(inputs['params'])
    num_clause = getNumProducts(inputs['params'])
    PLA_list = getPLAlist(clause_list, num_vars)
    printPLAfile(name, PLA_list, num_vars, num_clause)

if __name__ == '__main__':
    name = 'data_files/mux.cnf'
    convert_CNF_2_PLA(name)