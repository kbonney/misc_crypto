def isSS(M):
    n = len(M)
    x = 1
    for i in range(n-1):
        x = x*(M[i+1] >= 2*M[i])
    return x

def findSSsoln(M,S):
    n = len(M)
    x = [None]*n
    for i in range(n):
        if M[n-1-i] <= S:
            x[n-1-i]=1
            S = S - M[n-1-i]
        else:
            x[n-1-i]=0
    return x


def testSSsoln():
    M = (3,11,24,50,115)
    S = 142
    if isSS(M):
        print(findSSsoln(M,S))
    else:
        print("Make sure M is a super-increasing sequence")

def __main__():
    testSSsoln()

__main__()