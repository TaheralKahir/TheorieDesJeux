import numpy as np

def n_faces(M):
    n = len(M)
    u = 0
    for i in range(n-2):
        if sum(M[i]) < sum(M[i+1]):
            u = sum(M[i+1])
        elif sum(M[i]) > sum(M[i+1]):
            u = sum(M[i])
    return u+1


M = np.array([[0, 1, 1, 1], 
              [1, 0, 1, 1], 
              [1, 1, 0, 1],
              [1, 1, 1, 0]
             ]
            )        
print(n_faces(M))