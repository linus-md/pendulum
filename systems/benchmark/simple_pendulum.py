from sage.rings.rational_field import QQ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing


def simple_pendulum():
    # See example 2.5.1 for reference
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    derivatives = [
        R('u'),
        R('v'),
        R('l*x'),
        R('l*y - 1'),
        R('0')]

    ideal_gens = [R('x^2 + y^2 - 1')]
    return ideal_gens, derivatives


if __name__ == '__main__':
    from core.main import _algorithm_gb
    ideal_gens, derivatives = simple_pendulum()
    result = _algorithm_gb(ideal_gens, derivatives)
    print(result)
