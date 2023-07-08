from numba import jit
import numpy as np
import time

# x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(x): # Function is compiled and runs in machine code
    n,m=np.shape(x)
    for row in range(n):
        x[row]=np.sort(x[row])
    return x

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
arr=np.array([[3,2,1],[6,5,4],[9,8,7]])
start = time.perf_counter()
print(go_fast(arr))
end = time.perf_counter()
print("Elapsed (with compilation) = {}s".format((end - start)))


for i in range(0, 30):
    # NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
    start = time.perf_counter()
    print(go_fast(arr))
    end = time.perf_counter()
    print(str(i +1) + "º time")
    print("After compilation = {}s".format((end - start)))