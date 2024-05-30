using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving


function partial(q, ps)
    partial_q = 0
    for (i, pi) in enumerate(ps)
        partial_q =  partial_q + pi * derivative(q, i)
    end
    return partial_q
end;

function naive_algorithm(qs, ps)
    S = qs
    g = qs
    G = sig_groebner_basis(Ideal(S))
    while true
        g = [partial(gi, ps) for gi in g]
        g = [AlgebraicSolving.normal_form(gi, Ideal(G)) for gi in g]
        if all(g .== 0)
            return G
        else
            append!(S, g)
            G = sig_groebner_basis(Ideal(S))
        end
    end    
end;

R, (x1, x2, x3, x4, x5) = polynomial_ring(GF(17), ["x$i" for i in 1:5])
F = [x3, x4, x1, x2-1, 0*x1]
F_hom = AlgebraicSolving._homogenize(F)
sol = sig_groebner_basis(F_hom)