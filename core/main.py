import logging
import datetime

from sage.rings.ideal import Ideal as ideal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def differential_groebner_basis(ideal_gen, derivatives, algorithm='ideal'):
    """
    This function computes the minimal ideal generated by the polynomials
    ``ideal_gen`` that is stable under ``delta(ideal_gen, derivatives)``.
    The user can decide which algorithm to use. The default algorithm is
    the one described in the thesis. The other algorithm is an adapted version.

    INPUT:

    ``ideal_gen`` : list of polynomials
        List of polynomials that represent the initial ideal.
    ``derivatives`` : list of polynomials
        List of polynomials that represent the linear differential operator.
    ``algorithm`` : str
        The algorithm to use. Either 'ideal' or 'gb'.

    OUTPUT:

    Groebner basis of the minimal ideal generated by the polynomials
    ``ideal_gen`` that is stable under ``delta(ideal_gen, derivatives)``.
    """
    if algorithm == 'ideal':
        return _algorithm_ideal(ideal_gen, derivatives)
    elif algorithm == 'gb':
        return _algorithm_gb(ideal_gen, derivatives)
    else:
        raise ValueError('Invalid algorithm')


def delta(ideal_gen, derivatives):
    """
    This function computes the linear differential operator given by
    polynomials ``derivatives`` and an applies it to the polynomial
    ``polynomial``.

    INPUT:

    ``derivatives`` : list of polynomials
        List of polynomials that represent the linear differential operator.
    ``ideal_gen`` : polynomial

    OUTPUT:

    polynomial
    """
    vars = ideal_gen.parent().gens()
    return sum([derivatives[i] * ideal_gen.derivative(var) for i, var in enumerate(vars)])


def _algorithm_ideal(ideal_gens, derivatives):
    """
    This function computes the minimal ideal generated by the polynomials
    ``ideal_gens`` that is stable under ``delta(ideal_gens, derivatives)``.
    This function is an implementation of Algorithm 2 in the thesis.

    INPUT:

    ``ideal_gens`` : list of polynomials
        List of polynomials that represent the initial ideal.
    ``derivatives`` : list of polynomials
        List of polynomials that represent the linear differential operator.

    OUTPUT:

    Groebner basis of the minimal ideal generated by the polynomials
    ``derivatives`` that is stable under ``delta(ideal_gens, derivatives)``.
    """
    I = ideal(ideal_gens)
    i = 0
    logger.info('Algorithm 2 started')
    start_time = datetime.datetime.now()
    last_time = start_time
    logger.info(f'Iteration {i} - {start_time}')

    while True:
        ideal_gens = [delta(gen, derivatives) for gen in ideal_gens]
        ideal_gens = [gen.reduce(I) for gen in ideal_gens]

        if any(gen != 0 for gen in ideal_gens):
            i += 1
            I = I + ideal(ideal_gens)
            current_time = datetime.datetime.now()
            time_delta = current_time - last_time
            last_time = current_time
            logger.info(f'Iteration {i} - {time_delta} - {len(I.gens())}')
        else:
            # This gets computed eventhough we compute it above...
            end_time = datetime.datetime.now()
            time_delta = end_time - start_time
            logger.info('Algorithm 0 ended at - {}'.format(time_delta))
            return ideal(I).groebner_basis()


def _algorithm_gb(ideal_gens, derivatives):
    """
    This function computes the minimal ideal generated by the polynomials
    ``derivatives`` that is stable under ``delta(ideal_gen, derivatives)``.
    This function is an implementation of an adapted version of Algorithm 2
    in the thesis. Instead of adding new generators to the ideal,
    they are added to the new Gröbner basis.

    INPUT:

    ``ideal_gens`` : list of polynomials
        List of polynomials that represent the initial ideal.
    ``derivatives`` : list of polynomials
        List of polynomials that represent the linear differential operator.

    OUTPUT:

    Groebner basis of the minimal ideal generated by the polynomials
    ``ideal_gens`` that is stable under ``delta(ideal_gens, derivatives)``.
    """
    i = 0
    logger.info('Algorithm 2.1 started')
    start_time = datetime.datetime.now()
    last_time = start_time
    logger.info(f'Iteration {i} - {start_time}')
    G = ideal(ideal_gens).groebner_basis()

    while True:
        ideal_gens = [delta(gen, derivatives) for gen in ideal_gens]
        ideal_gens = [gen.reduce(G) for gen in ideal_gens]

        if any(gen != 0 for gen in ideal_gens):
            i += 1
            current_time = datetime.datetime.now()
            time_delta = current_time - last_time
            last_time = current_time
            G = ideal(list(set(G + ideal_gens))).groebner_basis()
            logger.info(f'Iteration {i} - {time_delta} - {len(G)}')
        else:
            end_time = datetime.datetime.now()
            time_delta = end_time - start_time
            logger.info('Algorithm 1 ended in - {}'.format(time_delta))
            return G
