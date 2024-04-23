from sage.all import PolynomialRing, QQ

def double_simple():
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2',
                       order='degrevlex')
    pi = [R('u1'),
        R('v1'),
        R('- x1 - (x1 - x2)'),
        R('- y1 - (y1 - y2) - 1'),
        R('u2'),
        R('v2'),
        R('- (x2 - x1)'),
        R('- (y2 - y1) - 1')]

    qi = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    qi, pi = double_simple()
    result = algorithm(qi, pi)
    print(result)
