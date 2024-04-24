import logging
import datetime

from sage.all import ideal, set_verbose

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
set_verbose(2)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm(qi, pi, method='std'):
    i = 0
    logger.info('Algorithm 1 started')
    logger.info(f'Iteration {i}')
    logger.info(f'{datetime.datetime.now()}')
    G = ideal(qi).groebner_basis(method)
    logger.info(G)
    logger.info('')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]

        if any(qs != 0 for qs in qi):
            i += 1
            logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            G = ideal(list(set(G + qi))).groebner_basis()
            logger.info(G)
        else:
            return G

def algorithm_0(qi, pi):
    I = ideal(qi)  
    i = 0
    logger.info('Algorithm 0 started')
    logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    logger.info(I)
    logger.info('')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(I) for qs in qi]
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            logger.info(f'')
            logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            logger.info(I)
        else:
            return ideal(I).groebner_basis()
