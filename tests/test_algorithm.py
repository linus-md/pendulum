import pytest
from sage.all import PolynomialRing, QQ
from core.main import algorithm, algorithm_0

def test_single_pendulum():
    R = PolynomialRing(QQ, 'x, y, u, v, l', order='degrevlex')
    pi = [R('u'), R('v'), R('l*x'), R('l*y - 1'), R('0')]
    qi = [R('x^2 + y^2 - 1')]
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


def test_simple_double_pendulum():
    R = PolynomialRing(QQ, 'x1, y1, u1, v1, x2, y2, u2, v2', 
                       order='degrevlex')
    pi = [R('u1'),
          R('v1'),
          R('- x1 - (x1 - x2)'),
          R('- y1 - (y1 - y2) - 1'),
          R('u2'),
          R('v2'),
          R('- (x2 - x1)'),
          R('- (y2 - y1) - 1')]
    qi = [R('x1^2 + y1^2 - 1'), R('(x2 - x1)^2 + (y2 - y1)^2 - 1')]
    g = [R('1')]

    assert algorithm(qi, pi) == g
    assert algorithm_0(qi, pi) == g
