from sage.all import PolynomialRing, QQ

def parabola():
    R = PolynomialRing(QQ, 'p1, p2, p3, v1, v2, v3, l, dl', order='invlex')
    S = PolynomialRing(QQ, 'p1, p2, p3, v1, v2, v3, l', order='invlex')
    pi = [R('v1'), 
          R('v2'), 
          R('v3'), 
          R('2*l*p1'), 
          R('2*l*p2'),
          R('- l - 1'),
          R('dl')]
    
    qi = [R('p1^2 + p2^2 - p3')]
    return qi, pi, R, S

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, R, S = parabola()
    result = algorithm_gen(qi, pi, S, R)
    print(result)
