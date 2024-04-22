import logging
from sage.all import ideal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def algorithm(qi, pi):
    def diff_op(qi, pi):
        vars = qi.parent().gens()
        return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

    #set_verbose(2)
    G = ideal(qi).groebner_basis()
    i = 0

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]

        if any(qs != 0 for qs in qi):
            G = ideal(list(set(G + qi))).groebner_basis()
            logger.info(f'Iteration {i}: {G}')
            i += 1
        else:
            return G
