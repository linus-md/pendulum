from sage.all import PolynomialRing, QQ

def parabola():
    # See example 2.5.3 for reference
    R = PolynomialRing(QQ, 'p1, p2, p3, v1, v2, v3, l', order='degrevlex')
    derivatives = [R('v1'), 
          R('v2'), 
          R('v3'), 
          R('2*l*p1'), 
          R('2*l*p2'),
          R('- l - 1'),
          R('0')]
    
    ideal_gens = [R('p1^2 + p2^2 - p3')]
    return ideal_gens, derivatives

if __name__ == '__main__':
    from core.main import algorithm_gb
    ideal_gens, derivatives = parabola()
    result = algorithm_gb(ideal_gens, derivatives)
    print(result)
