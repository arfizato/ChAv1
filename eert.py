#first exmaple 
import sys


base= ["a","c","d","e","g","h","k"]
request = "q"
rules =["k,l,m=i", "i,l,j=q", "c,d,e,l=b","a,b=q", "l,n,o,p=q","c,h=r","r,j,m=s","f,h=b","g=f"]

#second example 
# base= ["h","k"]
# request = "c"
# rules =["a=e","b=d","h=a","e,g=c","e,k=b","d,e,k=c","g,k,f=a"]

minpath=[""]*len(rules)


def getResult(index,request,base):
    global rules 
    rule= rules[index]
    result= rule.split("=")
    result[0] = result[0].split(",") 

    if result[1]!= request: 
        # print("mouch nafsou: ",result[1], request)
        result=""
    elif type(result) is not str:
        for a in range(len(result[0])-1,-1,-1):
            # print("-------->",result[0][a],base)    
            if result[0][a] in base:
                # print("-------->",result[0][a],base)    
                result[0].remove(result[0][a])
    else:
        if result[0] in base:
            result[0]=[]

    return result

def eerThcraes(request,index,path,thisBase,indent):
    global rules    
    result = getResult(index, request,thisBase)

    if result == "":
        print(indent,"~~~Jeni Feregh",request,rules[index])
        return path, True
    elif result[0]==[]:
        print(indent,"<<<<<<<<<<request=",request,"\n",indent,
                "Rule=",rules[index],"\n",indent,
                "path:",path,index,")")
        if index not in path:
            path.append(index)
        return path, False

    else:
        if type(result[0]) is str:
            result[0]=[result[0]]
        
        for newRequest in result[0]:
            print(indent,"########",newRequest,result[0],"\tBase:",thisBase)
            for r in rules:
                print(indent,"-------------\n",indent,"newRequest:",newRequest,"\n",indent,
                        "Rule"+str(rules.index(r))+":",r,"\n",indent,
                        "path:",path
                        )
                path,failed= eerThcraes(newRequest,rules.index(r),path,thisBase,indent+"\t")

                print(indent,"Failed:",failed,"\t","newPath:",path)

                if not failed:
                    if index not in path: 
                        path.append(index)
                    thisBase.append(newRequest)
                    print(indent,"::found",newRequest,"from Rule"+str(rules.index(r))+":",r,"\n",indent,
                    "::Added to path:",path)
                    if newRequest == result[0][-1]:
                        # print("pretty sure we good for now")
                        return path, False
                    break
                # else: 
                #     print(indent,"It's a dead end :((((((((")
                #     return path, True
        
    
    print("\\\\\\\\\\famma mochkel")
    return path, True

OgOutput= sys.stdout
f= open("gol.txt","w")
sys.stdout = f
path= []
for a in rules: 
    print ("----------------------------------------------------------------")
    print("Rule"+str(rules.index(a)) +":",a,"\tRequest:",request,"\tbase:",base,"")

    path, failed= eerThcraes(request, rules.index(a), [],["a","c","d","e","g","h","k"],"\t")

    if not failed and len(path)<len(minpath) : 
        print ("New Minpath:",path,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        minpath=path

print(".\n.\n.\nminpath: ",minpath,"\n\nfile and function name in reverse get it? cause this is backwards chaining 9adechni dhamer ")
sys.stdout= OgOutput
print("\n\nminpath: ",minpath)

