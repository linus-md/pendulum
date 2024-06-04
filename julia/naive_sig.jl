using Pkg
Pkg.activate("/Users/linussommer/signatures")

using AbstractAlgebra: derivative
using AlgebraicSolving
using AlgebraicSolving: _homogenize

# This is a first implementation of a signature based algorithm.
# It just substitutes the signature methods into the naive algorithm.
# Some homogenization is necessary.


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
function dehomogenize(system, subring, variables)
    # TODO deal with signatures
    systemnew = []
    for polynomial in system
        if parent(polynomial) != subring
            push!(systemnew, polynomial(variables..., 1))
        else
            push!(systemnew, polynomial)
        end
    end
    # This narrows the type form Vector{Any} to Vector{fpMPolyRingElem}
    systemnew = identity.(systemnew)
    return systemnew
end

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
    Given an ideal `I = <polynomials>` compute the Groebner basis of the 
    minimal ideal `J` s.t. `J` contains `I` and `J` is closed under `partial`.
"""
function naive_sig_algorithm(polynomials, differrentials, subring, variables)
    system = _homogenize(polynomials)
    g = polynomials # This is should also be homogenious maybe?
    groebnerbasis = sig_groebner_basis(system)
    while true
        g = [partial(gi, differrentials) for gi in g]
        # Without dehomogenizing the result does not correspond to the original algorithm
        nGB = dehomogenize(natural(groebnerbasis), subring, variables)
        # This does not use signatures
        g = [normal_form(gi, Ideal(nGB)) for gi in g]
        if all(g .== 0)
            return groebnerbasis
        else
            append!(system, g) # push vs append?
            system = dehomogenize(system, subring, variables)
            system = _homogenize(system)
            # What happends to the previously computed signatures?
            groebnerbasis = sig_groebner_basis(system)
        end
    end    
    return groebnerbasis
end;


R, (x1, x2, x3, x4, x5) = polynomial_ring(
    GF(65521), ["x$i" for i in 1:5], ordering=:degrevlex)
differrentials = [x3, x4, x5*x1, x5*x2 - 1, R(0)] 
polynomials = [x1^2 + x2^2 - 1]

G = naive_sig_algorithm(polynomials, differrentials, R, (x1, x2, x3, x4, x5))
G = natural(G)
G = dehomogenize(G, R, (x1, x2, x3, x4, x5))
G = groebner_basis(Ideal(G))