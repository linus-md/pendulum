from sage.all import PolynomialRing, QQ

def double():
    # See example 2.5.2 for reference
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2',
                       order='degrevlex')
    derivatives = [R('u1'),
        R('v1'),
        R('- x1 - (x1 - x2)'),
        R('- y1 - (y1 - y2) - 1'),
        R('u2'),
        R('v2'),
        R('- (x2 - x1)'),
        R('- (y2 - y1) - 1')]

    ideal_gens = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    return ideal_gens, derivatives

if __name__ == '__main__':
    from core.main import algorithm_gb
    ideal_gens, derivatives = double()
    result = algorithm_gb(ideal_gens, derivatives)
    print(result)
