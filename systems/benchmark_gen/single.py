from sage.all import PolynomialRing, QQ

def single():
    R = PolynomialRing(QQ, 'x, y, u, v, l, dl', order='invlex')
    S = PolynomialRing(QQ, 'x, y, u, v, l', order='invlex')
    pi = [R('u'), 
          R('v'), 
          R('l*x'), 
          R('l*y - 1'), 
          R('dl')]
    
    qi = [R('x^2 + y^2 - 1')]
    return qi, pi, S, R

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, S, R = single()
    result = algorithm_gen(qi, pi, S, R)
    print(result)