import pytest

import sage.all
from sage.rings.rational_field import QQ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from core.main import _algorithm_gb, _algorithm_ideal, differential_groebner_basis
from systems.benchmark.single import single
from systems.benchmark.double import double
from systems.benchmark.chem_1 import chem_1

def test_single_pendulum():
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    ideal_gens, derivatives = single()

    result = [
         R('x*l^2 - x'), 
         R('u*l^2 - u'), 
         R('l^3 + y - 2*l'), 
         R('x^2 - l^2 + 1'), 
         R('x*y - x*l'), 
         R('y^2 + l^2 - 2'), 
         R('x*u'), 
         R('y*u - u*l'),
         R('u^2 - y + l'), 
         R('y*l - 1'), 
         R('v')]
    
    assert _algorithm_gb(ideal_gens, derivatives) == result
    assert _algorithm_ideal(ideal_gens, derivatives) == result
    assert differential_groebner_basis(ideal_gens, derivatives, 'gb') == result
    assert differential_groebner_basis(ideal_gens, derivatives, 'ideal') == result


def test_simple_double_pendulum():
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2', 
                       order='degrevlex')
    ideal_gens, derivatives = double()
    result = [R('1')]

    assert _algorithm_gb(ideal_gens, derivatives) == result
    assert _algorithm_ideal(ideal_gens, derivatives) == result
    assert differential_groebner_basis(ideal_gens, derivatives, 'gb') == result
    assert differential_groebner_basis(ideal_gens, derivatives, 'ideal') == result

def test_chem_1():
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, k1, k2, k3, T1, T2', 
                       order='degrevlex')
    ideal_gens, derivatives = chem_1()

    assert _algorithm_gb(ideal_gens, derivatives) == ideal_gens
    assert _algorithm_ideal(ideal_gens, derivatives) == ideal_gens
    assert differential_groebner_basis(ideal_gens, derivatives, 'gb') == ideal_gens
    assert differential_groebner_basis(ideal_gens, derivatives, 'ideal') == ideal_gens
