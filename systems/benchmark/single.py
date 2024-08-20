from sage.all import PolynomialRing, QQ

def single():
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    pi = [R('u'), 
          R('v'), 
          R('l*x'), 
          R('l*y - 1'), 
          R('0')]
    
    qi = [R('x^2 + y^2 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm, algorithm_0
    qi, pi = single()
    result = algorithm_0(qi, pi)
    print(result)