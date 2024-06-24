from sage.all import PolynomialRing, QQ

def double_ll():
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2, dl1, dl2', 
                       order='invlex')
    S = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2', 
                       order='invlex')
    pi = [
        R('u1'),
        R('v1'),
        R('- l1*x1 - l2*(x1 - x2)'),
        R('- l1*y1 - l2*(y1 - y2) - 1'),
        R('u2'),
        R('v2'),
        R('- l2*(x2 - x1)'),
        R('- l2*(y2 - y1) - 1'),
        R('dl1'),
        R('dl2')
    ]

    qi = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    return qi, pi, S, R

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, S, R = double_ll()
    result = algorithm_gen(qi, pi, S, R)
    print(result)