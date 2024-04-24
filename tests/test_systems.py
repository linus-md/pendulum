import pytest
import systems

def test_single_pendulum():
    qi, pi = systems.single()
    assert len(qi) == 1
    assert len(pi) == 1*2 + 1*2 + 1

def test_double_pendulum():
    qi, pi = systems.double()
    assert len(qi) == 2
    assert len(pi) == 2*2 + 2*2

def test_double_ll_pendulum():
    qi, pi = systems.double_ll()
    assert len(qi) == 2
    assert len(pi) == 2*2 + 2*2 + 2

def test_full_double_pendulum_g():
    qi, pi = systems.double_full_g()
    assert len(qi) == 2
    assert len(pi) == 2*2 + 2*2 + 3

def test_simple_triple_pendulum():
    qi, pi = systems.triple_simple()
    assert len(qi) == 3
    assert len(pi) == 3*2 + 3*2

def test_full_triple_pendulum():
    qi, pi = systems.triple_full()
    assert len(qi) == 3
    assert len(pi) == 3*2 + 3*2 + 3

def test_full_triple_pendulum_g():
    qi, pi = systems.triple_full_g()
    assert len(qi) == 3
    assert len(pi) == 3*2 + 3*2 + 4

def test_simple_kepler():
    qi, pi = systems.kepler_simple()
    assert len(qi) == 1
    assert len(pi) == 5

def test_half_kepler():
    qi, pi = systems.kepler_half()
    assert len(qi) == 2
    assert len(pi) == 10

def test_full_kepler():
    qi, pi = systems.kepler_full()
    assert len(qi) == 2
    assert len(pi) == 11

def test_chem_1():
    qi, pi = systems.chem_1()
    assert len(qi) == 1
    assert len(pi) == 4 + 3

def test_chem_4():
    qi, pi = systems.chem_4()
    assert len(qi) == 2
    assert len(pi) == 6 + 6

def test_chem_b2():
    qi, pi = systems.chem_b2()
    assert len(qi) == 2
    assert len(pi) == 7 + 10

def test_chem_erk_reduced():
    qi, pi = systems.reduced_erk()
    assert len(qi) == 3
    assert len(pi) == 10 + 4 + 1 + 3 +1