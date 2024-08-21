import logging
import datetime

from sage.all import ideal, set_verbose

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def delta(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm(qi, pi):
    i = 0
    logger.info('Algorithm 1 started')
    start_time = datetime.datetime.now()
    last_time = start_time 
    logger.info(f'Iteration {i} - {start_time}')
    G = ideal(qi).groebner_basis()

    while True:
        qi = [delta(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]


        if any(qs != 0 for qs in qi):
            i += 1
            current_time = datetime.datetime.now()
            time_delta = current_time - last_time
            last_time = current_time
            G = ideal(list(set(G + qi))).groebner_basis()
            logger.info(f'Iteration {i} - {time_delta} - {len(G)}')
        else:
            end_time = datetime.datetime.now()
            time_delta = end_time - start_time
            logger.info('Algorithm 1 ended in - {}'.format(time_delta))
            return G

def algorithm_0(qi, pi):
    I = ideal(qi)  
    i = 0
    logger.info('Algorithm 0 started')
    start_time = datetime.datetime.now()
    logger.info(f'Iteration {i} - {start_time}')

    while True:
        qi = [delta(qs, pi) for qs in qi]
        qi = [qs.reduce(I) for qs in qi]
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            current_time = datetime.datetime.now()
            time_delta = current_time - start_time
            
            logger.info(f'Iteration {i} - {time_delta} - {len(I.gens())}')
        else:
            # This gets computed eventhough we compute it for the reduction above...
            end_time = datetime.datetime.now()
            time_delta = end_time - start_time
            logger.info('Algorithm 0 ended at - {}'.format(time_delta))
            return ideal(I).groebner_basis()


def algorithm_exp(qi, pi):
    i = 0
    logger.info('Algorithm Exp started')
    logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    S = qi 
    G = ideal(qi).groebner_basis()

    while True:
        qi = [delta(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]

        if any(qs != 0 for qs in qi):
            i += 1
            logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            S = list(set(S + qi))
            G = ideal(S).groebner_basis()
        else:
            logger.info('Algorithm Exp ended at - {}'.format(datetime.datetime.now()))
            return G

def algorithm_gen(I, derivatives, S, R):
    def partial_gen(f, derivatives, S, R):
        vars = S.gens()
        return sum([derivatives[i] * f.derivative(R(var)) for i, var in enumerate(vars)])

    def intersect(J, R, S):
        vars = S.gens()
        J = J.groebner_basis()
        J_S = []
        for f in J:
            if set(f.variables()).issubset(vars):
                J_S.append(f)
        return ideal(R, J_S)

    def gen_alg(I, derivatives, S, R):
        i = 0
        logger.info('Algorithm Gen started')
        start_time = datetime.datetime.now()
        logger.info(f'Iteration {i} - {start_time}')
        J1 = ideal(I)
        J_S = intersect(J1, R, S)
        J2 = J1 + ideal([partial_gen(f, derivatives, S, R) for f in J_S.gens()])
        while J1 != J2:
            i += 1
            current_time = datetime.datetime.now()
            time_delta = current_time - start_time
            logger.info(f'Iteration {i} - {time_delta}')
            J1 = J2
            J_S = intersect(J1, R, S)
            J2 = J1 + ideal([partial_gen(f, derivatives, S, R) for f in J_S.gens()])
        end_time = datetime.datetime.now()
        time_delta = end_time - start_time
        logger.info('Algorithm Gen ended at - {}'.format(time_delta))
        return J1.groebner_basis()
    
    return gen_alg(I, derivatives, S, R)

if __name__ == '__main__':
    from systems import chem_4_modified, double, single
    from sage.all import PolynomialRing, QQ
    import timeit
    
    n = 1
    qi, pi = single()
    res = algorithm(qi, pi)