__all__ = ["systems"]

from .benchmark.simple_pendulum import simple_pendulum
from .benchmark.double_pendulum import double_pendulum
from .benchmark.double_pendulum_ll import double_pendulum_ll

from .benchmark.chem_1 import chem_1
from .benchmark.chem_4 import chem_4
from .benchmark.chem_4_modified import chem_4_modified

from .benchmark.parabola import parabola

from .benchmark.linear_nn_2 import linear_nn_2

from .hard.double_pendulum_full import double_pendulum_full

from .hard.triple_pendulum import triple_pendulum
from .hard.triple_pendulum_lll import triple_pendulum_lll
from .hard.triple_pendulum_full import triple_pendulum_full