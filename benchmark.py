import pytest 
import hopfield_network as h
import numpy as np
import matplotlib.pyplot as plt
import benchmark
from unittest.mock import patch

patterns = h.generate_patterns(50,2500)

def test_speed_storkey(benchmark) :   
    weights = benchmark.pedantic(h.storkey_weights, args =(patterns,),rounds = 5,iterations = 1)
    
def test_speed_hebbian(benchmark) :
    weights = benchmark.pedantic(h.hebbian_weights, args =(patterns,),rounds = 5,iterations = 1)
 
w = h.hebbian_weights(patterns)
p = np.copy(patterns[0])
p1 = np.copy(patterns[0])
p2 = np.copy(patterns[0])
modif = h.perturb_pattern(np.copy(patterns[0]),1000)

def test_speed_update(benchmark) :
    state = benchmark.pedantic(h.update, args = (p,w),rounds = 100, iterations = 1)
 
def test_speed_update_async(benchmark) : 
    tate = benchmark.pedantic(h.update_async, args = (p1,w),rounds = 100, iterations = 1)

def test_speed_energy(benchmark) : 
    energy = state = benchmark.pedantic(h.energy, args = (p2,w),rounds = 100, iterations = 1)

def test_speed_dynamics(benchmark) : 
    state = benchmark.pedantic(h.dynamics, args = (modif, w,20), rounds = 10, iterations = 1)

def test_speed_dynamics_async(benchmark):
    state = benchmark.pedantic(h.dynamics_async, args = (modif, w, 20, 15), rounds = 10, iterations = 1)
""""
#Comented function : 
def test_speed_dynamics_async_rec(benchmark):
    state = benchmark.pedantic(h.dynamics_async_rec, args = (modif, w, 20, 15), rounds = 10, iterations = 1)

def test_speed_dynamics_rec(benchmark) : 
    state = benchmark.pedantic(h.dynamics_rec, args = (modif, w,20), rounds = 10, iterations = 1)
"""
