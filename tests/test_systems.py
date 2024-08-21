import pytest
import systems

def test_single_pendulum():
    ideal_gens, derivatives = systems.single()
    assert len(ideal_gens) == 1
    assert len(derivatives) == 1*2 + 1*2 + 1

def test_double_pendulum():
    ideal_gens, derivatives = systems.double()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 2*2 + 2*2

def test_double_ll_pendulum():
    ideal_gens, derivatives = systems.double_ll()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 2*2 + 2*2 + 2

def test_full_double_pendulum_g():
    ideal_gens, derivatives = systems.double_full_g()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 2*2 + 2*2 + 3

def test_simple_triple_pendulum():
    ideal_gens, derivatives = systems.triple_simple()
    assert len(ideal_gens) == 3
    assert len(derivatives) == 3*2 + 3*2

def test_full_triple_pendulum():
    ideal_gens, derivatives = systems.triple_full()
    assert len(ideal_gens) == 3
    assert len(derivatives) == 3*2 + 3*2 + 3

def test_full_triple_pendulum_g():
    ideal_gens, derivatives = systems.triple_full_g()
    assert len(ideal_gens) == 3
    assert len(derivatives) == 3*2 + 3*2 + 4

def test_chem_1():
    ideal_gens, derivatives = systems.chem_1()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 4 + 3 + 2

def test_chem_4():
    ideal_gens, derivatives = systems.chem_4()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 6 + 6

def test_chem_4_modified():
    ideal_gens, derivatives = systems.chem_4_modified()
    assert len(ideal_gens) == 2
    assert len(derivatives) == 6 + 6
