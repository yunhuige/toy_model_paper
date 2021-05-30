import sys ,os
import numpy as np
assign = [[] for i in range(20)] # 20 trajs
for i in range(20):
    print i
    cos = np.load('cos%d_new.npy'%i)
    r = np.load('r%d.npy'%i)
    for j in range(len(r)):
        if r[j] <= 0.2:
            assign[i].append(int(0))
        elif r[j] >= 0.85:
            assign[i].append(int(17))
        else:
            assign[i].append(int(np.argmax(cos[j]))+1)  # +1 since state 0 is assigned to bound state
np.save('Assignment.npy',assign)

