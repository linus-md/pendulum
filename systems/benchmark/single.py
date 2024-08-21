from sage.all import PolynomialRing, QQ

def single():
    # See example 2.5.1 for reference
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    pi = [R('u'), 
          R('v'), 
          R('l*x'), 
          R('l*y - 1'), 
          R('0')]
    
    qi = [R('x^2 + y^2 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    qi, pi = single()
    result = algorithm(qi, pi)
    print(result)