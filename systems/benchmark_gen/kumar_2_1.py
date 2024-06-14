from sage.all import PolynomialRing, QQ

def single():
    R = PolynomialRing(QQ, 'Mv, yA, Ml, xA, T', 
                       order='invlex')
    S = PolynomialRing(QQ, 'Mv, yA, Ml, xA, T, NA, NB, P', 
                       order='invlex')
    pi = [R('')]
    
    qi = [R('')]
    return qi, pi, S, R

if __name__ == '__main__':
    from core.main import algorithm_gen
    qi, pi, S, R = single()
    result = algorithm_gen(qi, pi, S, R)
    print(result)