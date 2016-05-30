import numpy as np
three = np.array([[1,1,1],[-1,-1,1],[1,1,1],[-1,-1,1],[1,1,1]])
five = np.array([[1,1,1],[1,-1,-1],[1,1,1],[-1,-1,1],[1,1,1]])
seven = np.array([[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1],[1,-1,-1]])
print ( three,"\n\n",five,"\n\n",seven)



three_vctr = np.array([[1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1]])
five_vctr = np.array([[1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1]])
seven_vctr = np.array([[1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1]])

X = [three_vctr,five_vctr,seven_vctr]
Y = X

dict = {} 
dict1 = {} 
#def weights():
W = np.zeros((15,15)) #добавить обнуление старшей диагонали
for V in X:
    Xt = V.transpose()
    W += Xt*V
    
print("\n\n",W)
    
def net0(W):
    
    n=0
    k=14
    NNet1  = 0
    for j in range (1,k+1):
        NNet1 += (W[j][k])*Y[j]
        NNet = NNet1
        dict.update({str(n)+str(k): NNet})
        Fnet
        dict1.update({str(n)+str(k): F})
        Out = Out.append(F)

def net(n):
    k=14
    NNet1,NNet2=0
    for j in range (1,k+1):
       # for i in range (0,3):
        NNet1 += (W[j][k])*Y[j]
    for j in range (1,k+1):
        #for i in range (0,3):
        NNet2 += (W[j][k])*(dict.get(str(n)+str(k))) # Х предыдущей эпохи
        NNet = NNet1+NNet2
    dict.update({str(n)+str(k): NNet})

    
#print (W)

def Fnet (n):
    
    if NNet > 0:
        F = 1
    elif NNet == 0:
        F = dict1.get(str(n)+str(k))
    else:
        F = -1
    
    dict1.update({str(n)+str(k): F})
    Out = Out.append(F)
    print (Out)
    
        


Y = np.array(input())

for n in range (0,16):
    net0(W)
    net(n)
    Fnet(n)



