import os,random

while True:
        jpg=input("enter name of jpg file: \n")
        if not jpg.endswith(".jpg"):
            jpg+=".jpg"
        if os.path.exists(jpg):
            break
amnt=int(input("how much corruption do you want, represented as an integer \n"))
 
def corrupt(amount):
    global jpg
    with open(jpg,"rb") as f:
        data=f.read()
        
    
    for i in range(amount):
        array=bytearray(data)
        index=random.randint(1,len(array))
        array[index:index]=b"a"*random.randint(1,amount*10)
        #del array[index:index+amount]
        data=array
    if not jpg.startswith("fucked up "):
        jpg="fucked up "+jpg    
    with open((jpg),"wb") as f:
        #print(data)
        f.write(data)
    amnt=int(input("how much corruption do you want, represented as an integer \n"))
    corrupt(amnt)
corrupt(amnt)