#!/usr/bin/python
def readFromFile(name):
    lines_str = []
    inputs_dict = {}
    clause_list = []
    with open(name, "r") as f:
        for line in f.readlines():
            #print (lines[current])
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
            #print (str1)
        inputs_dict['clauses']=clause_list
        f.close()
    return inputs_dict

name = 'data_files/mux.cnf'
inputs = readFromFile(name)
#print(inputs['params'])
for current in range(len(inputs['clauses'])):
    temp = inputs['clauses'][current].split()
    inputs['clauses'][current] = temp
for current in range(len(inputs['clauses'])):
    nums = [int(n) for n in inputs['clauses'][current]]
    inputs['clauses'][current]= nums
param = inputs['params'].split()
num_vars = int(param[2])
num_clause = int(param[3])
print(num_vars)
print(num_clause)
print(inputs['clauses'])
print(abs(-7))
s = "-"
temp_list_total=[]
for current in range(len(inputs['clauses'])):
    temp_list = []
    for index in range(1,(num_vars+1)):
        temp_list.append("-")
    for index in range(len(inputs['clauses'][current])):
        for i in range(1,(num_vars+1)):
            if(abs(inputs['clauses'][current][index])==i):
            #     #print s,
            # else:
                if(inputs['clauses'][current][index]<0):
                    temp_list[i-1]="1"
                    #print 1,
                else:
                    temp_list[i-1]="0"
                    #print 0,
    #print(temp_list)
    temp_list_total.append(temp_list)
outputfile = name.split(".")[0] + "_pla.pla"
with open(outputfile, "w" ) as file_out:
    file_out.write(".i ")
    file_out.write(str(num_vars))
    file_out.write("\n.o 1")
    file_out.write("\n.p ")
    file_out.write(str(num_clause))
    file_out.write("\n")
    #print temp_list_total
    for current in range(len(temp_list_total)):
        for index in range(len(temp_list_total[current])):
            file_out.write(temp_list_total[current][index],)
        file_out.write(" 1 \n")
    file_out.write(".e")