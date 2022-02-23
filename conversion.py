
nline = "\n"

vars_lst = []


def findDataType(val):
    val = val.split()
    
    if val[0] in vars_lst:
        res = str(val[2])+" = "+str(val[2])+str(val[3])+str(val[4])+";"
        return res
    else:
        vars_lst.append(val[0])
    if val[2].isdecimal():
        num = val[2]
        res = "int "+str(val[0])+" = "+str(val[2])+";"
        
    else:
        try:
            num = float(val[2])
            res = "float "+str(val[0])+" = "+str(val[2])+";"
        except:
            str_len = 0
            for i in range(2,len(val)):
                num = str(val[i])
                str_len += len(num)
            res = "char "+str(val[0])+"["+str(str_len)+"]"+" = "
            for i in range(2,len(val)):
                res += str(val[i])
            
            res += ";"
    return res

def findDataTypeR(val):
    val = val.split()
    if val[0].isdecimal():
        
        res = "int"
        
    else:
        try:
            
            res = "float"
        except:
            print("Invalid Iterating Variable!")
    return res

def show(val):
    val = val.split()
    res_str = "cout"
    for i in val:
        if i == "show":
            continue
        
        res_str +="<<"
        res_str += i
         
        
    
    res_str += ";"
    return res_str

def ifState(val):
    #if(condition){}
    val = val.split()
    res = "if("+str(val[1])+"){"
    return res

def Block(val):
    return str(val)

def elseState(val):
    return "}else{"

def forL(val):
    val = val.split()
    #First Determine the datatype of Increment
    rt = findDataTypeR(val[2])
    try:
        rtL = findDataTypeR(val[5])
        rtL = findDataTypeR(val[4])
    except:
        rtL = 0

 
    
    #Increment intervel
    if val[3] == "++":
        inc = "++"
    elif val[3] == "+2":
        inc = "="+val[1]+"+2"
    elif val[3] == "+3": 
        inc = "="+val[1]+"+3"
    else:
        print("Else")
        inc = 0
        print("MAX INCREMENT IS 3!")
    
    
    if rtL != 0 and rt == rtL:
        res = "for("+rt+" "+val[1]+"="+val[2]+";"+val[1]+"<="+val[4]+";"+val[1]+str(inc)+"){"
    elif rtL == 0:
        res = "for("+rt+" "+val[1]+"="+ str(0)+";"+val[1]+"<="+val[2]+";"+val[1]+str(inc)+"){"
    else:
        print("Starting and End Value must be of Same type!")
    
    return res

def whileL(val):
    val = val.split()
    res = "while ("+val[1]+"){"
    return res

def cin(val):
    val = val.split()
    res = "cin>>"+str(val[1])+";"
    return res


def functionD(val):
    val = val.split()
    res = val[0] + " " +val[2] +"(){"
    print(res)

