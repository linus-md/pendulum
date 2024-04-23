import logging
import datetime

from sage.all import ideal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm(qi, pi):
    G = ideal(qi).groebner_basis()
    i = 0
    logger.info(f'Iteration {i}: {G} - {datetime.datetime.now()}')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]

        if any(qs != 0 for qs in qi):
            i += 1
            G = ideal(list(set(G + qi))).groebner_basis()
            logger.info(f'Iteration {i}: {G} - {datetime.datetime.now()}')
        else:
            return G

def algorithm_0(qi, pi):
    I = ideal(qi)  
    i = 0
    logger.info('Using algorithm 0')
    logger.info(f'Iteration {i}: {I} - {datetime.datetime.now()}')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(I) for qs in qi]
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            logger.info(f'Iteration {i}: {I} - {datetime.datetime.now()}')
        else:
            return ideal(I).groebner_basis()
