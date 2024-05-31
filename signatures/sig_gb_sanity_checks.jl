using Pkg
Pkg.activate("/Users/linussommer/signatures")
using AlgebraicSolving

function natural(sigpairs)
    # Return only the polynomial parts of the sigpairs
    return [sigpair[2] for sigpair in sigpairs]
end

function _dehomogenize(eqs, vars)
    # Substitute 1 for the newly introduced variable from _homogenization
    return [eq(vars..., 1) for eq in eqs]
end

R, vars = polynomial_ring(GF(17), ["x$i" for i in 1:6], ordering=:degrevlex)
F = AlgebraicSolving.cyclic(R)
Fhom = AlgebraicSolving._homogenize(F.gens)
G = sig_groebner_basis(Fhom)
G = natural(G)
G = _dehomogenize(G, vars)
G = groebner_basis(Ideal(G)) # sig_gb is not reduced
H = groebner_basis(F)

i = 0
j = 0

for elem in G
    if elem in H
        global i = i + 1
    else
        println("$elem not in H")
    end
end

for elem in H
    if elem in G
        global j = j + 1
    else
        println("$elem not in H")
    end
end

println(i)
println(j)