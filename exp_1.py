from core.main import algorithm
from systems.benchmark.double_ll import double_ll

qi, pi = double_ll()
result = algorithm(qi, pi, method='singular:std')
print(result)