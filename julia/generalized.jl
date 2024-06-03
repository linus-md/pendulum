using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving

# It is nt clear if this algorithm is correct!!!

function partial(q, ps, R, S)
    partial_q = 0
    # need check if dl in pi somehow
    for (i, pi) in enumerate(ps)
        partial_q =  partial_q + pi * derivative(q, i)
    end
    return partial_q
end;

function generalized_algorithm(qs, ps, R, S)
    S = qs
    g = qs
    G = groebner_basis(Ideal(S))
    while true
        g = [partial(gi, ps, R, S) for gi in g]
        g = [AlgebraicSolving.normal_form(gi, Ideal(G)) for gi in g]
        if all(g .== 0)
            return G
        else
            append!(S, g)
            G = groebner_basis(Ideal(S))
        end
    end    
end;

R, (x, y, u, v, l, dl) = polynomial_ring(GF(65521),["x","y","u","v","l","dl"], 
                                         ordering=:degrevlex)
ps = [
    u,
    v, 
    l*x,
    l*y - 1,
    dl,
    0
] 
q = [x^2 + y^2 - 1]

#S, (x, y, u, v, l) = polynomial_ring(GF(65521),["x","y","u","v","l"],
#                                     ordering=:degrevlex)

res = generalized_algorithm(q, ps, R, R) # RR !