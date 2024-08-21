from sage.all import PolynomialRing, QQ

def triple_full():
      # See example 2.5.2 for reference
      vars = 'x1, y1, u1, v1, x2, y2, u2, v2, x3, y3, u3, v3, l1, l2, l3'
      R = PolynomialRing(QQ, vars, order='degrevlex')

      pi = [R('u1'), 
            R('v1'), 
            R('- l1*x1 - l2*(x1 - x2)'), 
            R('- l1*y1 - l2*(y1 - y2) - 1'), 
            R('u2'), 
            R('v2'), 
            R('- l2*(x2 - x1) - l3*(x2 - x3)'), 
            R('- l2*(y2 - y1) - l3*(y2 - y3) - 1'), 
            R('u3'), 
            R('v3'), 
            R('- l3*(x3 - x2)'), 
            R('- l3*(y3 - y2) - 1'),
            R('0'),
            R('0'),
            R('0')]

      qi = [R('x1^2 + y1^2 - 1'), 
            R('(x2 - x1)^2 + (y2 - y1)^2 - 1'), 
            R('(x3 - x2)^2 + (y3 - y2)^2 - 1')]
      
      return qi, pi

if __name__ == '__main__':
    from core.main import algorithm_gb
    qi, pi = triple_full()
    result = algorithm_gb(qi, pi)
    print(result)
