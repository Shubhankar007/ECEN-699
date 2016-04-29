import subprocess
print("start")
inputfile = "../Main/xor_5.pla"
outputfile = inputfile.split("_")[0] + "_out.pla"
subprocess.call(("../espresso/./espresso "+inputfile+" > "+outputfile), shell=True)
print("end")