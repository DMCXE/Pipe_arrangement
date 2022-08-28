import numpy as np
a = np.zeros([1,2])
c = np.append(a,[[2,4]],axis=0)
d = np.array([1,2])

p = np.array([[1,2],[3,4]])
pp = p*np.array([[1,-1],[1,-1]])
p = np.append(p,pp,axis=0)
print(p)
