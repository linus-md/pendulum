from sage.all import QQ, PolynomialRing, ideal

def partial(f, derivatives, S, R):
    vars = S.gens()
    return sum([derivatives[i] * f.derivative(R(var)) for i, var in enumerate(vars)])

def intersect(J, R, S):
    vars = S.gens()
    J = J.groebner_basis()
    J_S = []
    for f in J:
        if set(f.variables()).issubset(vars):
            J_S.append(f)
    return ideal(R, J_S)

def gen_alg(I, derivatives, S, R):
    i = 0
    J1 = ideal(I)
    print(0, J1.gens())
    J_S = intersect(J1, R, S)
    J2 = J1 + ideal([partial(f, derivatives, S, R) for f in J_S.gens()])
    while J1 != J2:
        i += 1
        J1 = J2
        J_S = intersect(J1, R, S)
        J2 = J1 + ideal([partial(f, derivatives, S, R) for f in J_S.gens()])
        print(0, J1.gens())
    return J1

R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2, dl1, dl2', 
                       order='invlex')

S = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2', 
                       order='invlex')

derivatives = [
    R('u1'),
    R('v1'),
    R('- l1*x1 - l2*(x1 - x2)'),
    R('- l1*y1 - l2*(y1 - y2) - 1'),
    R('u2'),
    R('v2'),
    R('- l2*(x2 - x1)'),
    R('- l2*(y2 - y1) - 1'),
    R('dl1'),
    R('dl2')
    ]

qi = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]

J = gen_alg(qi, derivatives, S, R)
G = J.groebner_basis()
for g in G:
    print(g)