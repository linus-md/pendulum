from sage.all import PolynomialRing, GF

def double_ll():
    # See example 2.5.2 for reference
    R = PolynomialRing(GF(101), 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2', 
                       order='degrevlex')
    pi = [R('u1'),
        R('v1'),
        R('- l1*x1 - l2*(x1 - x2)'),
        R('- l1*y1 - l2*(y1 - y2) - 1'),
        R('u2'),
        R('v2'),
        R('- l2*(x2 - x1)'),
        R('- l2*(y2 - y1) - 1'),
        R('0'),
        R('0')]

    qi = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm_gb
    qi, pi = double_ll()
    result = algorithm_gb(qi, pi)
    print(result)