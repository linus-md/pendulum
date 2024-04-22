from sage.all import PolynomialRing, QQ

def kepler_full():
    R = PolynomialRing(QQ, 'x, y, u, v, R, a1, a2, a3, a4, a5, a6', 
                        order='degrevlex')
    pi = [R('u'),
          R('v'),
          R('x*R^3'),
          R('y*R^3'),
          R('-(x*u + y*v)*R^3'), 
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0')]

    qi = [R('R^2*(x^2 + y^2) - 1'), 
          R('a1*x^2 + a2*y*x + a3*y^2 + a4*x + a5*y + a6')]

    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    qi, pi = kepler_full()
    result = algorithm(qi, pi)
    print(result)
