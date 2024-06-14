from sage.all import PolynomialRing, QQ

def kumar_2_2():
    R = PolynomialRing(QQ, 'V, CA, CB, CC, V1, RA, RB, F, Fi, CAi, Keq1, kB', 
                       order='invlex')
    S = PolynomialRing(QQ, 'V, CA, CB, CC', 
                       order='invlex')
    derivatives = [
        R('Fi - F'),
        R('Fi*V1*(CAi - CA) - RA'),
        R('-Fi*V1*CB + RA - RB'),
        R('-Fi*V1*CC + RB'),
    ]
    derivatives += [R('0') for _ in range(8)] # What new derivatives are needed?
    
    constraints = [
        R('V*V1 - 1'),
        R('CA - CB*Keq1'),
        R('RB - kB*CB')
    ]
    return constraints, derivatives, S, R

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, S, R = kumar_2_2()
    result = algorithm_gen(qi, pi, R, R)
    print(result)