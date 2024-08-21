### Differential Gröbner bases

This repository Pontains Python/Sage code to compute full differential ideals that arise in the context of DAE systems. It is supplementary material to my thesis. Specifically Algorithm 2 and a variant of Algorithm 2 are implemented in this package.

### Examples

Executing the following code

```python
from core.main import algorithm
qi, pi = single()
result = algorithm(qi, pi)
print(result)
```

results in the following output

```python
INFO:core.main:Algorithm 1 started
INFO:core.main:Iteration 0 - 2024-08-21 11:44:04.543529
INFO:core.main:Iteration 1 - 0:00:00.018392 - 3
INFO:core.main:Iteration 2 - 0:00:00.003453 - 7
INFO:core.main:Iteration 3 - 0:00:00.002947 - 7
INFO:core.main:Iteration 4 - 0:00:00.002551 - 11
INFO:core.main:Algorithm 1 ended in - 0:00:00.034986
[x*l^2 - x, u*l^2 - u, l^3 + y - 2*l, x^2 - l^2 + 1, x*y - x*l, y^2 + l^2 - 2, x*u, y*u - u*l, u^2 - y + l, y*l - 1, v]
```

### Usage

To use this package without installing it modify the following command and execute it in the terminal. It is necessary to have a working Sage installation.

```bash
export PYTHONPATH="${PYTHONPATH}:/user/path/pendulum"
```
