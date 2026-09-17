import time 
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4
dt = 0.01
steps  = 100
seed = 0 


start = time.perf_counter()
result = simulate_loop(N0, lam, dt, steps, seed)
py_time = time.perf_counter() - start

start = time.perf_counter()
result = simulate(N0, lam, dt, steps, seed)
numpy_time = time.perf_counter() - start

diff = py_time / numpy_time

print("NumPy test: ", numpy_time)
print("Py test: ", py_time)

print("Difference: ", diff)