import numpy as np
three = [[1,1,1],[-1,-1,1],[1,1,1],[-1,-1,1],[1,1,1]]
five = [[1,1,1],[1,-1,-1],[1,1,1],[-1,-1,1],[1,1,1]]
seven = [[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1],[1,-1,-1]]

three_vctr = np.array([[1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1]])
five_vctr = np.array([[1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1]])
seven_vctr = np.array([[1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1]])

X = [three_vctr,five_vctr,seven_vctr]
Y = X
 
dict = {} 
dict1 = {} 
def weights():
    W = np.zeros((15,15))
    for V in X:
        Xt = V.transpose()
        W += Xt*V

def net0():
    n=0
    k=15
    NNet1  = 0
    for j in range (1,k):
        for i in range (0,3):
            NNet1 += (W[j][k])*Y[i][j]
            NNet = NNet1
            dict.update({str(n)+str(k): NNet})
            Fnet
            dict1.update({str(n)+str(k): F})


def net(n):
    k=15
    NNet1,NNet2=0
    for j in range (1,k):
        for i in range (0,3):
            NNet1 += (W[j][k])*Y[i][j]
    for j in range (1,k+1):
        for i in range (0,3):
            NNet2 += (W[j][k])*(dict.get(str(n)+str(k))) # Х предыдущей эпохи
            NNet = NNet1+NNet2
    dict.update({str(n)+str(k): NNet})
    
#print (W)

def Fnet (n):
    
    if NNet > 0:
        return F == 1
    elif NNet == 0:
        return F == dict1.get(str(n)+str(k))
    else:
        return F == -1
    dict1.update({str(n)+str(k): F})

for n in range (0,16):
    weights
    X = np.array(input())
    
    net0
    net
    Fnet


