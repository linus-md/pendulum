using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving

function natural(G)
    return [sigpair[2] for sigpair in G]
end;

function partial(q, ps)
    partial_q = 0
    for (i, pi) in enumerate(ps)
        partial_q =  partial_q + pi * derivative(q, i)
    end
    return partial_q
end;

function naive_sig_algorithm(qs, ps)
    S = AlgebraicSolving._homogenize(qs)
    g = qs
    G = sig_groebner_basis(S)
    while true
        g = [partial(gi, ps) for gi in g]
        g = [AlgebraicSolving.normal_form(gi, Ideal(natural(G))) for gi in g]
        if all(g .== 0)
            return G
        else
            append!(S, g)
            println(S)
            # This introduces problems with to many variables
            S = AlgebraicSolving._homogenize(S)
            G = sig_groebner_basis(S)
        end
    end    
    return G
end;


R, (x1, x2, x3, x4, x5) = polynomial_ring(GF(65521),["x$i" for i in 1:5], ordering=:degrevlex)
ps = [
    x3,
    x4, 
    x5*x1,
    x5*x2 - 1,
    0
] 

qs = [x1^2 + x2^2 - 1]

res = naive_sig_algorithm(qs, ps)