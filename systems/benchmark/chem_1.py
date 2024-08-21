from sage.all import PolynomialRing, QQ

def chem_1():
    # See example 2.5.4 for reference
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, k1, k2, k3, T1, T2', 
                       order='degrevlex')
    derivatives = [R('- k1*x1 + k2*x2*x3'),    
          R('  k1*x1 - k2*x2*x3'),
          R('- k2*x2*x3 + k3*x4'),
          R('  k2*x2*x3 - k3*x4'),
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0')]

    ideal_gens = [R('x1 + x2 - T1'),
          R('x3 + x4 - T2')]
    return ideal_gens, derivatives

if __name__ == '__main__':
    from core.main import algorithm_gb
    ideal_gens, derivatives = chem_1()
    result = algorithm_gb(ideal_gens, derivatives)
    print(result)