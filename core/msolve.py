import logging
import datetime

from sage.all import ideal, set_verbose
from sage.rings.polynomial.msolve import groebner_basis_degrevlex

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm_1_msolve(qi, pi):
    i = 0
    G = groebner_basis_degrevlex(ideal(qi), proof=False)
    logger.info(f'Iteration {i}: {G} - {datetime.datetime.now()}')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]
        logger.info(f'Monomial order: {qi[0].parent().term_order()}')

        if any(qs != 0 for qs in qi):
            i += 1
            G = ideal(list(set(G + qi)))
            G = groebner_basis_degrevlex(G, proof=False)
            logger.info(f'Iteration {i}: {G} - {datetime.datetime.now()}')
        else:
            return G
        
def algorithm_0_msolve(qi, pi):
    i = 0
    I = ideal(qi)  
    logger.info('Algorithm 0 started')
    logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    logger.info(I)

    while True:
        G = ideal(I).groebner_basis(algorithm='msolve', proof=False)
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi] # use G
        logger.info(f'Monomial order: {qi[0].parent().term_order()}')
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            logger.info(I)
        else:
            return groebner_basis_degrevlex(I, proof=False)

if __name__ == '__main__':
    from systems import double, chem_fake
    set_verbose(2)

    time = datetime.datetime.now()
    qi, pi = double()
    res = algorithm_0_msolve(qi, pi)
    
    print(res)
    print(f"{(datetime.datetime.now() - time).total_seconds()}s")


    # Alg 0:
    # Alg 1:
