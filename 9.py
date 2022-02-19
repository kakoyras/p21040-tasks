
arxeio=open("arxeio.txt", "r")  
txt=arxeio.read()   
    
letters=[]
binaries=[]

lenght=len(txt)
for i in range(lenght): 
    j = txt[i]  
    letters.insert(i,j) 
    binary = int(format(ord(letters[i]), '07b'))    

    binary=str(binary)

    if len(binary)==6:
        binary="0"+binary

    binaries.insert(i,binary)
    
    print(binary)
    

print(binaries)


#-------------------------------------------------------------------


m=0
max_1=0
max_0=0

for item in binaries:

    m=m+1
    ak1=1
    ak0=1
    
    for i in range(6):

        if item[i]=="1":
            if item[i+1]=="1":
                ak1=ak1+1

        if item[i]=="0":
            if item[i+1]=="0":
                ak0=ak0+1
            
    if m==1:
        max_1=ak1
        max_0=ak0
    if ak1>max_1:
        max_1=ak1
    if ak0>max_0:
        max_0=ak0


print ("Η Μεγαλύτερη ακολουθεία από 1 ήταν: ")
print (max_1)
print ("Η Μεγαλύτερη ακολουθεία από 0 ήταν: ")
print (max_0)

