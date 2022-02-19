from urllib.request import Request, urlopen
import json

k=0 #Βοηθητικοί μετρητές για παρακάτω
m=0
n=0

req=Request("https://drand.cloudflare.com/public/latest", headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0"})
data=urlopen(req).read()

opap=Request("https://api.opap.gr/draws/v3.0/1100/last-result-and-active", headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0"})
kino=urlopen(opap).read()
kino=kino.decode()
kino=json.loads(kino)
kino=kino["last"]
kino=kino["winningNumbers"]
kino=kino["list"]

print(data)                     
middata=str(data)
finaldata=middata[33:97]          
print ("Randomness: ",finaldata)
pairs=[]
ints=[] 
duos=[]

print ("Τα ζεύγη που προκύπτουν: ")
for i in range (32):  
    a=(finaldata[k:k+2])
    pairs.insert (i,a)
    k=k+2
print (pairs)

print ("Μετά την μετατροπή: ")
for i in range (32):
    a=(int(finaldata[m:m+2],16))   
    ints.insert (i,a)
    m=m+2
print(ints)
      
print ("Μετά την πράξη mod 80: ")
for i in range(32):  
    a=((int(finaldata[n:n+2],16))%80)
    duos.insert(i,a)
    n=n+2
print(duos)
      
duos.sort() 
print ("Η λίστα ταξινομιμένη: ")
print (duos)

j=31
for i in range(31):  
    flag="True" 
    while flag=="True":
        if duos[i]==duos[i+1]:
            duos.pop(i+1)
            j=j-1
        elif duos[i]!=duos[i+1]:
            flag="False"
            
print ("Η λίστα χωρίς ίδιους αριθμούς: ")
print (duos)

print ("Οι τελευταίοι αριθμοί που κληρώθηκαν στο κίνο: ")           
print (kino)

for i in range(20):
    for f in range(len(duos)):
        if kino[i]==duos[f]:
            print("Ο αριθμός ", duos[f], " από τoυς τυχαίους αριθμούς κληρώθηκε στο κίνο")
