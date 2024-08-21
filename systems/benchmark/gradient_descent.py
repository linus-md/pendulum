from sage.all import PolynomialRing, QQ, matrix, vector, ideal

def gradient_descent():
    # See example 2.5.7 for reference
    R = PolynomialRing(
        QQ, [f'a{i}{j} ' for i in range(1, 3) for j in range(1, 3)] \
        + [f'b{i}{j} ' for i in range(1, 3) for j in range(1, 3)] \
        + ['x1', 'x2', 'y1', 'y2'],
        order='degrevlex')

    A = matrix([[R('a11'), R('a12')], [R('a21'), R('a22')]])
    B = matrix([[R('b11'), R('b12')], [R('b21'), R('b22')]])
    x = vector([R('x1'), R('x2')])
    y = vector([R('y1'), R('y2')])

    f = (A*B*x - y)
    GF = vector(f.list())
    loss = GF.dot_product(GF)/2

    derivatives = [loss.derivative(var) for var in R.gens()][:-4]
    derivatives += [R('0'), R('0'), R('0'), R('0')]
    constraints = (A.transpose()*A - B*B.transpose()).list()

    return derivatives, constraints

if __name__ == '__main__':
    from core.main import algorithm_gb
    derivatives, ideal_gens = gradient_descent()
    result = algorithm_gb(ideal_gens, derivatives)
    print(ideal(ideal_gens) == ideal(result))
