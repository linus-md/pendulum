from sage.all import PolynomialRing, QQ

# See example 4 in 1909.13608

def chem_fake():
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, x5, x6, k1, k2, k3, k4, k5, k6', 
                       order='degrevlex')
    
    pi = [
        R('- k1*x1 + k4*x3*x5'), 
        R(' k1*x1 - k2*x2 + k5*x4*x5'),
        R('- k3*x3 + k2*x2 + k4*x3*x5'),
        R(' k3*x3 - k5*x4*x5'),
        R('- k4*x3*x5 - k5*x4*x5 + k6*x6'),
        R(' k4*x3*x5 - k6*x6 + k5*x4*x5'),
        R('0'),
        R('0'),
        R('0'),
        R('0'),
        R('0'),
        R('0')
    ]

    qi = [R('x1 + x2 + x3 + x4 - 1'), R('x5 + x6 - 1')]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm_0
    import time
    
    qi, pi = chem_fake()
    start_time = time.time()
    result = algorithm_0(qi, pi)
    end_time = time.time()

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    print(result)

    # Execution: 414.9023480415344 seconds