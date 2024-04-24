from sage.all import PolynomialRing, QQ

# From Torres et al. (2019) 3.3

def reduced_erk():
    vars = 'x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,' + \
           'k1, k3, kcat, koff, m, l1, l3, lcat, loff, n'
    R = PolynomialRing(QQ, vars, order='degrevlex')
    pi = [
        R('-k1*x1*x2 + n*x6*x8 + lcat*x10'),
        R('-k1*x1*x2 + kcat*x4 + koff*x4'),
        R(' k1*x1*x2 - k3*x3'),
        R(' k3*x3 - kcat*x4 - koff*x4'),
        R(' m*x2*x7 - l1*x5*x8 + kcat*x4'),
        R('-n*x6*x8 + koff*x4'),
        R('-m*x2*x7 + loff*x10'),
        R('-l1*x5*x8 + loff*x10 + lcat*x10'),
        R(' l1*x5*x8 - l3*x9'),
        R('-loff*x10 + l3*x9 - lcat*x10'),
        R('0'), R('0'), R('0'), R('0'), R('0'),
        R('0'), R('0'), R('0'), R('0'), R('0')
    ]

    qi = [
        R('x1 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 - 1'),
        R('x2 + x3 + x4 - 1'),
        R('x8 + x9 + x10 - 1'),
    ]
    return qi, pi

if __name__ == '__main__':
    from core.main import algorithm_0
    qi, pi = reduced_erk()
    result = algorithm_0(qi, pi)
    print(result)