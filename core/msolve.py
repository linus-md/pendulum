import logging
import datetime

from sage.all import ideal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm_msolve(qi, pi):
    G = ideal(qi).groebner_basis(algorithm='msolve', proof=False)
    i = 0
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
        
if __name__ == '__main__':
    from systems import chem_fake
    from sage.all import PolynomialRing, QQ
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2', 
                       order='degrevlex')
    qi, pi = chem_fake()
    print(algorithm_msolve(qi, pi))