import pytest
from sage.all import PolynomialRing, QQ
from core.main import algorithm, algorithm_0, algorithm_exp, algorithm_gen
from systems.benchmark.single import single
from systems.benchmark.double import double
from systems.benchmark.chem_1 import chem_1

def test_single_pendulum():
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    qi, pi = single()

    g = [R('x*l^2 - x'), 
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
    
    assert algorithm(qi, pi) == g
    assert algorithm_0(qi, pi) == g
    assert algorithm_exp(qi, pi) == g


def test_simple_double_pendulum():
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2', 
                       order='degrevlex')
    qi, pi = double()
    g = [R('1')]

    assert algorithm(qi, pi) == g
    assert algorithm_0(qi, pi) == g
    assert algorithm_exp(qi, pi) == g

def test_chem_1():
    R = PolynomialRing(QQ, 'x1, x2, x3, x4, k1, k2, k3, T1, T2', 
                       order='degrevlex')
    qi, pi = chem_1()

    assert algorithm(qi, pi) == qi
    assert algorithm_0(qi, pi) == qi
    assert algorithm_exp(qi, pi) == qi

def test_general_simple():
    R = PolynomialRing(QQ, 'x, y, u, v, l, dl', order='invlex')
    S = PolynomialRing(QQ, 'x, y, u, v, l', order='invlex')
    derivatives = [R('u'), R('v'), R('l*x'), R('l*y - 1'), R('dl')]
    q = R('x^2 + y^2 - 1')
    J = algorithm_gen(q, derivatives, S, R)

    G = [R('dl - 3*v'), R('l + v^2 + u^2 - y'), R('y*v + x*u'), 
         R('x^2*v - v - x*y*u'), R('x^2 + y^2 - 1')]
    
    assert J.groebner_basis() == G

