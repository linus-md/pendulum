from sage.all import PolynomialRing, QQ

def akzo_nobel():
    R = PolynomialRing(QQ, 'FLB, FLBT', order='invlex')
    S = PolynomialRing(QQ, '', order='invlex')

    r = [
        R('k1 * FLB^4 * CO2^(1/2))'),
        R('k2 * FLBT * ZHU'),
        R('k2/K * FLB * ZLA'),
        R('k3 * FLB * ZHU'),
        R('k4 * FLBZHU * CO2^(1/2)'),
    ]

    Fin = R('3.3/737 - CO2')
    Ks = R('115.83')

    # nCO2 = CO2^(1/2) ?

    derivatives = [
          -2*r[0] + r[1] - r[2] -   r[3],
        -1/2*r[0] +                 r[3] - 1/2*r[4] + Fin,
             r[0] - r[1] + r[2],
                   -r[1] + r[2] - 2*r[3],
                    r[1] - r[2]
    ]
    
    constraints = [
        Ks*R('x1*x4') - R('x6')
    ]
    return qi, pi, S, R

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, S, R = akzo_nobel()
    #result = algorithm_gen(qi, pi, S, R)
    #print(result)
    print(akzo_nobel)