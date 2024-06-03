using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving

# This is a first implementation of a signature based algorithm.
# It just substitutes the signature methods into the naive algorithm.
# Some homogenization is necessary.

# TODO watch out with S=System / S=Subring notation

"""
    Given a sigset return only the polynomial parts of the sigpairs.
"""
function natural(sigset)
    return [sigpair[2] for sigpair in sigset]
end;

"""
    Given a system with an additional variable x_{n+1} for homogenization
    evaluate all polynomials at (x1, x2, ..., xn, 1).
"""
function rehomogenize(system, subring, variables)
    # TODO split this up into removing of x_{n+1} and homogenizing again
    # TODO deal wioth signatures
    systemnew = []
    for polynomial in system
        if parent(polynomial) != subring
            push!(systemnew, polynomial(variables..., 1))
        else
            push!(systemnew, polynomial)
        end
    end
    systemnew = identity.(systemnew) # this is necessary because of the vector type...?
    return AlgebraicSolving._homogenize(systemnew)
end;

"""
    Given a system with `n`` variables and `n` polynomial equations define a
    linear differential operator `patial`.
"""
function partial(polynomial, differentials)
    partial_polynomial = 0
    for (i, differential) in enumerate(differentials)
        partial_polynomial += differential * derivative(polynomial, i)
    end
    return partial_polynomial
end;

"""
    Given an ideal `I = <polynomials>` compute the Groebner basis of the minimal ideal 
    `J` s.t. `J` contains `I` and `J` is closed under `partial``.
"""
function naive_sig_algorithm(polynomials, differrentials, subring, variables)
    system = AlgebraicSolving._homogenize(polynomials)
    g = polynomials # This is should also be homogenious maybe?
    G = sig_groebner_basis(system)
    while true
        g = [partial(gi, differrentials) for gi in g]
        # This does not use signatures
        g = [AlgebraicSolving.normal_form(gi, Ideal(natural(G))) for gi in g]
        if all(g .== 0)
            return G
        else
            append!(system, g)
            system = rehomogenize(system, subring, variables)
            # What happends to the previously computed signatures?
            G = sig_groebner_basis(system)
        end
    end    
    G = dehomogenize(G, subring, variables)
    return G
end;


R, (x1, x2, x3, x4, x5) = polynomial_ring(GF(65521),["x$i" for i in 1:5], ordering=:degrevlex)
differrentials = [
    x3,
    x4, 
    x5*x1,
    x5*x2 - 1,
    0
] 

polynomials = [x1^2 + x2^2 - 1]

G = naive_sig_algorithm(polynomials, differrentials, R, (x1, x2, x3, x4, x5))