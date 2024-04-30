import logging
import datetime

from sage.all import ideal, set_verbose

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#set_verbose(2)

def diff_op(qi, pi):
    vars = qi.parent().gens()
    return sum([pi[i] * qi.derivative(var) for i, var in enumerate(vars)])

def algorithm(qi, pi):
    i = 0
   #logger.info('Algorithm 1 started')
   #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    G = ideal(qi).groebner_basis()
    ##logger.info(G)
   #logger.info('')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]
       #logger.info(f'Monomial order: {qi[0].parent().term_order()}')

        if any(qs != 0 for qs in qi):
            i += 1
           #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            G = ideal(list(set(G + qi))).groebner_basis()
            #print(G)
            ##logger.info(G)
        else:
            return G

def algorithm_0(qi, pi):
    I = ideal(qi)  
    i = 0
    #logger.info('Algorithm 0 started')
    #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    #logger.info(I)
    #logger.info('')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(I) for qs in qi]
    
        if any(qs != 0 for qs in qi):
            i += 1
            I = I + ideal(qi)
            # print the number of gens
            #logger.info(f'Number of generators: {len(I.gens())}')

            #logger.info(f'')
            #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            #logger.info(f'Monomial order: {qi[0].parent().term_order()}')
            #print(I.groebner_basis())
            ##logger.info(I)
        else:
            # This gets computed eventhough we compute it for the reduction above...
            return ideal(I).groebner_basis()


def algorithm_exp(qi, pi):
    i = 0
    #logger.info('Algorithm 1 started')
    #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
    S = qi 
    G = ideal(qi).groebner_basis()
    ##logger.info(G)
    #logger.info('')

    while True:
        qi = [diff_op(qs, pi) for qs in qi]
        qi = [qs.reduce(G) for qs in qi]
        #logger.info(f'Monomial order: {qi[0].parent().term_order()}')

        if any(qs != 0 for qs in qi):
            i += 1
            #logger.info(f'Iteration {i} - {datetime.datetime.now()}')
            S = list(set(S + qi))
            G = ideal(S).groebner_basis()
            # print(G)
            ##logger.info(G)
        else:
            return G

if __name__ == '__main__':
    from systems import chem_fake, double, single
    from sage.all import PolynomialRing, QQ
    import timeit
    
    n = 1
    qi, pi = chem_fake()
    execution_time = timeit.timeit(lambda: algorithm_exp(qi, pi), number=n)
    print(execution_time/n)