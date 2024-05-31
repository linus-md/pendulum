# TODO watch out with S=System / S=Subring notation

using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving

function natural(G)
    return [sigpair[2] for sigpair in G]
end;

function dehomogenize(S, R, var)
    return G
end

function rehomogenize(S, R, var)
    # TODO split this up
    S_new = []
    for s in S
        if parent(s) != R
            push!(S_new, s(var..., 1))
        else
            push!(S_new, s)
        end
    end
    S_new = identity.(S_new) # this is necessary because of the vector type...?
    return AlgebraicSolving._homogenize(S_new)
end;

function partial(q, ps)
    partial_q = 0
    for (i, pi) in enumerate(ps)
        partial_q =  partial_q + pi * derivative(q, i)
    end
    return partial_q
end;

function naive_sig_algorithm(qs, ps, R, var)
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
            S = rehomogenize(S, R, var)
            G = sig_groebner_basis(S)
        end
    end    
    G = dehomogenize(G, R, var)
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

G = naive_sig_algorithm(qs, ps, R, (x1, x2, x3, x4, x5))