from sage.all import PolynomialRing, QQ

def kepler_simple():
    R = PolynomialRing(QQ, 'x, y, u, v, R', order='degrevlex')
    pi = [R('u'),            
          R('v'),
          R('x*R^3'),
          R('y*R^3'),
          R('-(x*u + y*v)*R^3')]

    qi = [R('R^2*(x^2 + y^2) - 1')]

    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    qi, pi = kepler_simple()
    result = algorithm(qi, pi)
    print(result)