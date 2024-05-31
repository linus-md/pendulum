using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving

# This is a Julia implementation of the naive algorithm.
# See also the Maple and Python/Sage implementation.
# This adds to the Gröbner basis and not the Ideal.

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
    G = groebner_basis(Ideal(S))
    while true
        g = [partial(gi, ps) for gi in g]
        g = [AlgebraicSolving.normal_form(gi, Ideal(G)) for gi in g]
        if all(g .== 0)
            return G
        else
            append!(S, g)
            G = groebner_basis(Ideal(S))
        end
    end    
end;

R, (x, y, u, v, l) = polynomial_ring(GF(65521),["x","y","u","v","l"], ordering=:degrevlex)
ps = [
    u,
    v, 
    l*x,
    l*y - 1,
    0
] 

q = [x^2 + y^2 - 1]
G = naive_algorithm(q, ps)
println(G)
println(length(G) == 11) # small sanity check