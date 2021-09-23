import numpy as np


class Lattice:
    def __init__(self, basis):
        self.basis = basis
    
    def dimension(self):
        return len(self.basis[0])


def babai(L,w):
    #assume L.basis is written as a matrix of column vectors
    #assume w is given in terms of standard coordinates
    #write w in terms of L.basis()
    w_B = np.linalg.solve(L.basis.transpose(), w)
    print(w_B)
    #round entries of w_B to nearest integer
    w_B = np.rint(w_B)
    print(w_B)
    #return the lattice element represented by w_B
    return B.transpose().dot(w_B)

def hadamard_ratio(B):
    #assume B given as matrix of column basis vectors
    #calculate product of basis vector norms
    V = 1
    for i in range(len(B)):
        V = V*np.linalg.norm(B[i])
    #calculate hadamards ratio
    n = len(B)
    return (np.linalg.det(B) / V)**(1/n)

b1 = np.array([137,312])
b2 = np.array([215,-187])
B = np.array([b1,b2])
L = Lattice(B)
w = np.array([53172,81743])
print(babai(L,w))
print(np.linalg.det(B))
#print(hadamard_ratio(B))

#b1 = np.array([137,312])
#b2 = np.array([215,-187])
#B = np.array([b1,b2])
#L = Lattice(B)
#w = np.array([53172,81743])
#print(babai(L,w))