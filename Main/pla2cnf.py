#!/usr/bin/python
#Input: PLA file path
#Output: dictionary of params and minterms from pla file
###
def readPLAfile(name):
    lines_str = []
    inputs_dict = {}
    clause_list = []
    with open(name, "r") as f:
        for line in f.readlines():
            lines_str.append(str(line))
        for current in range(len(lines_str)):
            li=lines_str[current].strip()
            if li.startswith(".i"):
                inputs_dict['vars'] = li
            elif li.startswith(".o"):
                pass
            elif li.startswith(".e"):
                pass
            elif li.startswith(".p"):
                inputs_dict['clause_num'] = li
            else:
                clause_list.append(li)
        inputs_dict['clauses']=clause_list
        f.close()
    return inputs_dict
###
def getProducts(clause_list):
    temp_list = []
    for current in range(len(clause_list)):
        temp = clause_list[current].split()
        clause_list[current] = temp
        temp_list.append(clause_list[current][0])
    return temp_list

#Inputs: list of products
#Output: list of clauses for CNF file    
def getCNFlist(product_list):
    clause_list = []
    for current in range(len(product_list)):
        temp_list = []
        for c in range(len(product_list[current])):
            if (product_list[current][c]=="1"):
                s=str(-(c+1))+" "
                temp_list.append(s)
            if (product_list[current][c]=="0"):
                s=str(c+1)+" "
                temp_list.append(s)
        clause_list.append(temp_list)
    return clause_list

#Input: inputs_dict["clause_num"]
#Output: number of variables in CNF
def getNumVars(param_list):
    param = param_list.split()
    num_vars = int(param[1])
    return num_vars

#Input: inputs_dict["vars"]
#Output: number of clauses in CNF
def getNumClauses(param_list):
    param = param_list.split()
    num_clause = int(param[1])
    return num_clause

#Inputs: 1. input PLA file path
#        2. list of clauses for CNF file
#        3. number of variables in CNF
#        4. number of clauses in CNF
#Output: print CNF file
def printCNFfile(inputFile, CNF_list, num_vars, num_clause):
    outputfile = inputFile.split(".")[0] + "_cnf.cnf"
    with open(outputfile, "w" ) as file_out:
        file_out.write("p cnf ")
        file_out.write(str(num_vars)+" ")
        file_out.write(str(num_clause))
        file_out.write("\n")
        for current in range(len(CNF_list)):
            for index in range(len(CNF_list[current])):
                file_out.write(CNF_list[current][index],)
            file_out.write("0\n")
#Get .cnf file from .pla 
#input: PLA File path
def convert_PLA_2_CNF(name):
    inputs=readPLAfile(name)
    product_list = getProducts(inputs['clauses'])
    clause_list = getCNFlist(product_list)
    num_clause = getNumClauses(inputs['clause_num'])
    num_vars = getNumClauses(inputs['vars'])
    printCNFfile(name, clause_list, num_vars, num_clause)

if __name__ == '__main__':
    name = 'data_files/quinn_pla2.pla'
    convert_PLA_2_CNF(name)