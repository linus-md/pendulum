from sage.all import PolynomialRing, QQ

# See example 1 in 1909.13608

def chem_b2():
    vars = 'x1, x2, x3, x4, x5, x6, x7, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10'
    R = PolynomialRing(QQ, vars, order='degrevlex')
    pi = [R('- k9*x1*x6 + k10*x7'),  
          R('- k5*x2*x3 + k6*x5'),
          R('- k5*x2*x3 + k1*x1 - k3*x3 + k6*x5'),
          R('- 2*k7*x4*x4 + k2*x2 - k4*x4 + 2*k8*x6'),
          R('  k5*x2*x3 - k6*x5'),
          R('  k7*x4*x4 - k9*x1*x6 - k8*x6 + k10*x7'),
          R('  k9*x1*x6 - k10*x7'),
          R('0'), R('0'), R('0'), R('0'), R('0'),
          R('0'), R('0'), R('0'), R('0'), R('0')]

    qi = [R('x1 + x7') , R('x2 + x5')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    qi, pi = chem_b2()
    result = algorithm(qi, pi)
    print(result)