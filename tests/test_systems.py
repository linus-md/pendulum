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

def test_chem_1():
    qi, pi = systems.chem_1()
    assert len(qi) == 2
    assert len(pi) == 4 + 3 + 2

def test_chem_4():
    qi, pi = systems.chem_4()
    assert len(qi) == 2
    assert len(pi) == 6 + 6

def test_chem_4_modified():
    qi, pi = systems.chem_4_modified()
    assert len(qi) == 2
    assert len(pi) == 6 + 6
