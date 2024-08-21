from sage.all import PolynomialRing, QQ

def double_full_g():
    # See example 2.5.2 for reference
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2, g', 
                       order='degrevlex')
    derivatives = [R('u1'),
          R('v1'),
          R('- l1*x1 - l2*(x1 - x2)'),
          R('- l1*y1 - l2*(y1 - y2) - g'),
          R('u2'),
          R('v2'),
          R('- l2*(x2 - x1)'),
          R('- l2*(y2 - y1) - g'),
          R('0'),
          R('0'),
          R('0')]

    ideal_gens = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    return ideal_gens, derivatives

if __name__ == '__main__':
    from core.main import _algorithm_gb
    ideal_gens, derivatives = double_full_g()
    result = _algorithm_gb(ideal_gens, derivatives)
    print(result)