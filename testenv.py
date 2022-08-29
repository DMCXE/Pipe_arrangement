from PipeArrange import Pip_arrangement
import numpy as np
import time

s1 = 3.2
s2 = s1 * np.sqrt(3) / 2
s3 = 2 * s1
e = 0.1
r = 1.1
N = 1000

'''
s1 = 32 * 1e-3
s2 = s1 * np.sqrt(3) / 2
s3 = 2 * s1
e = 32 * 1e-3
r = 11  * 1e-3
N = 3220
'''
st = time.time()
pipe = Pip_arrangement(s1, s2, s3, e, r, N, 'Tri')
pipe.arrangement()
pos = pipe.Pippos
print(pipe.R,pipe.PipeNum)
stt = time.time()
print(stt-st)
pipe.visualize(pos, r)
