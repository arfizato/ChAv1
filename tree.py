from http.client import REQUEST_URI_TOO_LONG
import sys

from numpy import require

#first example 
# base= ["h","k"]
# request = "c"
# rules =["a=e","b=d","h=a","e,g=c","e,k=b","d,e,k=c","g,k,f=a"]
#second example 
base= ["a","c","d","e","g","h","k"]
request = "q"
rules =["k,l,m=i", "i,l,j=q", "c,d,e=b","a,b=q", "l,n,o,p=q","c,h=r","r,j,m=s","f,h=b","g=f"]

minpath=[""]*len(rules)
path=[]

def getResult(base,index):
    global rules 
    rule= rules[index]
    result= rule.split("=")

    required = result[0].split(",") 
    print("result: ",result,"\trequired: ",required)
    result=result[1]
    for a in required:
        if a not in base:
            return ""

    return result

def treeSearch(thisbase,index,path,indentation):
    global rules
    global request
    global minpath
    result=getResult(thisbase,index)
    if result in thisbase :
        print("turned ",result," to blank because it already exists in ", thisbase)
        result =""

    # recursion stop
    if result == request: 
        path.append(index)
        thisbase.append(result)
        print("found it ", path)
        return path, False
        
        # appel recusif
    elif result != request:
        if result =="":    
            print(indentation,"not doable")    
            return path, True 
            
        thisbase.append(result)
        path.append(index)            
        if len(path) == len(minpath)-1 :
            print(indentation+"there's already a better path")
            return path, True

        for a in rules:
            
            path,failed = treeSearch(thisbase[:],rules.index(a),path,indentation+"\t")
            print(indentation,thisbase,"rule["+str(rules.index(a))+"]: ",a,path)

            if len(minpath) > len(path) and not failed:
                print("new path selected:\n", path, " length(path)=",len(path),
                "\n",minpath," length(minpath)= ",len(minpath))

                minpath= path
                return path, True



    return ["na3rch 3lik ya bro"], True

f= open("log.txt","w")
originalStdout = sys.stdout
sys.stdout= f
for pending in rules: 
    print("\n-------------------------------------------------------------------------------------------------\nbase: ",base,"\nrule: ",pending,"\nminpath: ",minpath)

    path, failed =treeSearch(base[:],rules.index(pending) ,[],"\t")    # ["a","c","d","e","g","h","k"] if testing using other example  
    if not failed: 
        if len(path)<len(minpath):
            minpath=path
        print(path)

print("\n\nminpath= ",minpath)
sys.stdout = originalStdout
print("\n\nminpath= ",minpath)
