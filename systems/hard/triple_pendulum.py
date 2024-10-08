from sage.rings.rational_field import QQ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing


def triple_pendulum():
    # See example 2.5.2 for reference
    R = PolynomialRing(
                QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, x3, y3, u3, v3',
                order='degrevlex')

    derivatives = [
        R('u1'),
        R('v1'),
        R('- x1 - 1*(x1 - x2)'),
        R('- y1 - 1*(y1 - y2) - 1'),
        R('u2'),
        R('v2'),
        R('- (x2 - x1) - (x2 - x3)'),
        R('- (y2 - y1) - (y2 - y3) - 1'),
        R('u3'),
        R('v3'),
        R('- (x3 - x2)'),
        R('- (y3 - y2) - 1')]

    ideal_gens = [
        R('x1^2 + y1^2 - 1'),
        R('(x2 - x1)^2 + (y2 - y1)^2 - 1'),
        R('(x3 - x2)^2 + (y3 - y2)^2 - 1')]

    return ideal_gens, derivatives


if __name__ == '__main__':
    from core.main import _algorithm_gb
    ideal_gens, derivatives = triple_pendulum()
    result = _algorithm_gb(ideal_gens, derivatives)
    print(result)
