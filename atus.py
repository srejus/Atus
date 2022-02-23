#!/usr/bin/python3

#Open a file and read its name then its content
#Create a file.cpp with name from the opened file
#Add header and main method
#Read the contents from the opend file and start writing it to the cpp file

import os
import sys
import time

from conversion import *

#starting time
start = time.time()


print(">>>>>>>>>>ATUS<<<<<<<<<<")


fname = sys.argv[1]

method_lst = []

# fname = "test"
try:
    file1 = open(fname+'.atus')

    # lst = []

    cts = file1.read()
    lst = cts.split("\n")


    #BLOCK

    start = 0


    block = 0


    #Cpp File Creation and Writing

    cFname = open('.'+fname+'.cpp',"w")
    cFname.write("#include<iostream>"+"\n")
    cFname.write("using namespace std;"+"\n")


    for i in lst:

        
        line_lst = i.split()
        
        if len(line_lst) == 0:
            line_lst = [1,0,3]
        elif len(line_lst) == 1:
            line_lst.append(0)
        
        if "{" in line_lst and start == 0:
            cFname.write(i+" \n")
            method_lst.append(line_lst[1])
            block = 1
            continue
        
        if line_lst[0] == "return":
            i = i+";"
            cFname.write(i+" \n")
            continue
        
        if i in method_lst:
            i = i+";"
            cFname.write(i+" \n")
            continue


        
        
        if i == "start":
            cFname.write("int main(){"+"\n")
            start = 1
            continue
        if line_lst[1] == "=":
            i = findDataType(i)

        elif line_lst[0] == "show":
            i = show(i)
        
        elif line_lst[0] == "if":
            i = ifState(i)
            block = 1
        
        elif line_lst[0] == "for":
            i = forL(i)
            block = 1
        
        elif line_lst[0] == "while":
            i = whileL(i)
            block = 1

        elif line_lst[0] == "break":
            i = "break;"
        
        elif line_lst[0] == "continue":
            i = "continue;"

        elif line_lst[0] == "enter":
            i = cin(i)
        
        elif line_lst[1] == "function":
            i = functionD(i)
            
        
        elif line_lst[0] == "else":
            i = elseState(i)
            block = 1
        
        elif line_lst[0] == "}":
            block = 0
            i = "}"
            
        
        
        elif line_lst[0] == "#":
            continue

        if block == 1:
            i = Block(i)
        
        if ";" not in i:
            i = i+";"
        
        cFname.write(i+" \n")


    cFname.write('return 0; \n }')

    cFname.close()

    #Run the CPP File

    
    

    x = 0
    try:
        sec_arg = sys.argv[2]
        x = 2
    except:
        x = 1

    
    if x == 1:
        os.system(f"g++ .{fname}.cpp -o .{fname}")
        print("\n PROGRAM COMPILED SUCCESSFULLY")
    elif x == 2:
        os.system(f"g++ .{fname}.cpp -o {fname}")
        os.system(f"./{fname}")

        print("\n PROGRAM EXECUTION SUCCESSFULLY COMPLETED")

    else:
        pass

    os.remove(f".{fname}.cpp")
    

except:
    print(f"No File named {fname} Found!")

# end time
end = time.time()

print("Execution completed in- ", end-start)


