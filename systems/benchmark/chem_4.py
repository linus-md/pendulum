from sage.all import PolynomialRing, QQ

def chem_4():
    # See example A.1.1 for reference
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, x5, x6, k1, k2, k3, k4, k5, k6', 
                       order='degrevlex')
    derivatives = [R('- k1*x1 + k4*x3*x5'),    
          R('  k1*x1 - k2*x2 + k5*x4*x5'),
          R('- k3*x3 + k2*x2 - k4*x3*x5'),
          R('  k3*x3 - k5*x4*x5'),
          R('- k4*x3*x5 - k5*x4*x5 + k6*x6'),
          R('  k4*x3*x5 - k6*x6 + k5*x4*x5'),
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0')]

    ideal_gens = [R('x1 + x2 + x3 + x4 - 1'), R('x5 + x6 - 1')]
    return ideal_gens, derivatives

if __name__ == '__main__':
    from core.main import algorithm_gb
    ideal_gens, derivatives = chem_4()
    result = algorithm_gb(ideal_gens, derivatives)
    print(result)
