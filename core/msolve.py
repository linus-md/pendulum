import logging
import datetime

from sage.all import ideal, set_verbose

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm_1_msolve(qi, pi):
    i = 0
    G = ideal(qi).groebner_basis(algorithm='msolve', proof=False)
    logger.info(f'Iteration {i}: {G} - {datetime.datetime.now()}')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]

        if any(qs != 0 for qs in qi):
            i += 1
            G = ideal(list(set(G + qi)))
            G = G.groebner_basis(algorithm='msolve', proof=False)
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
        #G = ideal(I).groebner_basis(algorithm='msolve', proof=False)
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(I) for qs in qi] # use G
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            logger.info(I)
        else:
            return I.groebner_basis(algorithm='msolve', proof=False)

if __name__ == '__main__':
    from systems import chem_fake
    set_verbose(2)

    time = datetime.datetime.now()
    qi, pi = chem_fake()
    res = algorithm_1_msolve(qi, pi)
    
    print(res)
    print(f"{(datetime.datetime.now() - time).total_seconds()}s")


    # Alg 0:
    # Alg 1:
