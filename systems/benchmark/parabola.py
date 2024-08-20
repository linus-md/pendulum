from sage.all import PolynomialRing, QQ

def parabola():
    R = PolynomialRing(QQ, 'p1, p2, p3, v1, v2, v3, l', order='degrevlex')
    pi = [R('v1'), 
          R('v2'), 
          R('v3'), 
          R('2*l*p1'), 
          R('2*l*p2'),
          R('- l - 1'),
          R('0')]
    
    qi = [R('p1^2 + p2^2 - p3')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm, algorithm_0
    qi, pi = parabola()
    result = algorithm_0(qi, pi)
    print(result)
