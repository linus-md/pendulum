from sage.all import PolynomialRing, QQ

# See example 1 in 1909.13608

def chem_1():
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, k1, k2, k3, T1, T2', 
                       order='degrevlex')
    pi = [R('- k1*x1 + k2*x2*x3'),    
          R('  k1*x1 - k2*x2*x3'),
          R('- k2*x2*x3 + k3*x4'),
          R('  k2*x2*x3 - k3*x4'),
          R('0'),
          R('0'),
          R('0'),
          R('0'),
          R('0')]

    qi = [R('x1 - x2 - 1'),
          R('x3 - x4 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm
    from sage.all import ideal
    qi, pi = chem_1()
    result = algorithm(qi, pi)
    pc = ideal(result).primary_decomposition()[0].gens()
    print(f"Result: {result}")
    print(f"Primary decomposition: {pc}")
    print("GB is PCD: ",sorted(pc) == sorted(result))

    for p in pi:
      print(p, p in ideal(result))