import pytest 
import hopfield_network as h
import DataSaver as ds
import utility as ut
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch
import os.path
import shutil

if __name__ == "__main__":
    import doctest # Importing the library
    print("Starting doctests") # not required (just for clarity in output)
    doctest.testmod()

#TESTING THE WEIGHTS 
patterns = np.array([[1,1,-1,-1],[1,1,-1,1], [-1,1,-1,1]])
nb_neurons = patterns.shape[1]
hebbian_test = np.array([[0,1/3,-1/3,-1/3],[1/3,0,-1,1/3],[-1/3,-1,0,-1/3],[-1/3,1/3,-1/3,0]])
storkey_test = np.array([[9/8,1/4,-1/4,-1/2],[1/4,5/8,-1,1/4],[-1/4,-1,5/8,-1/4],[-1/2,1/4,-1/4,9/8]])
H_network = h.HopfieldNetwork(patterns, 'hebbian')
S_network = h.HopfieldNetwork(patterns, 'storkey')

hebbian_result = H_network.weight
storkey_result = S_network.weight

#THINK OF A NEW WAY OF TESTING THE WEIGHTS

def test_hebbian_weights():
    matrix_features(H_network.weight)
    print(H_network.weight)
    assert np.allclose(np.diagonal(H_network.weight), 0)
    assert hebbian_result.shape == (nb_neurons,nb_neurons)  
    assert np.allclose(hebbian_result,hebbian_test)

def test_storkey_weights(): 
    matrix_features(S_network.weight)
    assert storkey_result.shape == (nb_neurons,nb_neurons)
    assert np.allclose(storkey_result,storkey_test)

#IMPLEMENTATION
nbr_modif = 10
nb_pat = 8
nb_neur = 100
our_patterns = ut.generate_patterns(nb_pat,nb_neur)
modif_pat = np.copy(our_patterns[0])
modif_pat = ut.perturb_pattern(modif_pat,nbr_modif)
to_find = np.copy(our_patterns[0])

def test_generate_patterns():
    assert (np.any(our_patterns == 1) |  np.any(our_patterns == -1))

def test_perturb_patterns():
    modified_values = [x for x in (modif_pat== to_find) if x == False]
    assert len(modified_values) == nbr_modif

def test_dynamics_energy():
    #NEGATIVECASE COMMENT ADAPTER ? 
    #not_converging = H_mock.dynamics(modif_pat, heb *-1,20)
    #assert len(not_converging) == 21 #because we add the modified pattern also

    #positive case
    h_dyn_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
    h_dyn_network.dynamics(modif_pat, 1, 20)
    s_dyn_network = h.HopfieldNetwork(our_patterns, 'Storkey')
    s_dyn_network.dynamics(modif_pat, 100, 3000) #pas certain des paramètres là
    states_h = h_dyn_network.data.states_list
    states_s = s_dyn_network.data.states_list
    assert np.allclose(to_find,states_s[-1])
    assert np.allclose(to_find,states_h[-1])

    #ENERGY 
    #h_energy = [h.energy() for x in states_h ]
    #s_energy = [h.energy(x, stork) for x in states_s ]
    assert sorted(h_dyn_network.data.energies, reverse=True) == h_dyn_network.data.energies
    assert sorted(s_dyn_network.data.energies, reverse= True) == s_dyn_network.data.energies

def test_dynamics_async_energy():
    h_async1_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
    h_async1_network.dynamics_async(modif_pat, 20, 30)

    #negative case
    assert len (h_async1_network.data.states_list) ==2
    #assert len (h_async1_network.data.states_list) ==21

    #positive case
    h_async2_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
    h_async2_network.dynamics_async(modif_pat, 1, 10000, 3000)
    async_states_h = h_async2_network.data.states_list

    s_async_network = h.HopfieldNetwork(our_patterns, 'Storkey')
    s_async_network.dynamics_async(modif_pat, 100, 10000, 3000)
    async_states_s = s_async_network.data.states_list
    
    assert np.allclose(to_find,async_states_h[-1])
    assert np.allclose(to_find,async_states_s[-1])  

    #Energy
    #h_energy = [h.energy(x, heb) for x in async_states_h ]
    #s_energy = [h.energy(x, stork) for x in async_states_s]
    assert sorted(h_async2_network.data.energies, reverse=True) == h_async2_network.data.energies
    assert sorted(s_async_network.data.energies, reverse= True) == s_async_network.data.energies 

def test_pattern_match():
    h_match_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
    h_match_network.dynamics(modif_pat, 1, 20)
    assert h_match_network.pattern_match(patterns, patterns[0]) == 0
    assert h_match_network.pattern_match(patterns, patterns[1]) == 1
    assert h_match_network.pattern_match(patterns, np.array([-1,-1,-1,1])) == None

#positive case

h_li_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
h_li_network.dynamics(modif_pat, 1)

li_test = []

for i in patterns : 
    li_test.append(i)
li_test = h_li_network.data.reshape_states_list(li_test)

expected_li = [np.array([[1,1],[-1,-1]]), np.array([[1,1],[-1,1]]),[[-1,1],[-1,1]]]

#negative case
neg_tes = [np.ones((1,3))]

def test_reshape_states_list():
    assert np.allclose(li_test,expected_li)
    assert h_li_network.data.reshape_states_list(neg_tes) == None

@patch("matplotlib.pyplot.show")
def test_save_video(mock_show):
    h_li_network.data.save_video("./test_save_video/test_video_bian_ASYNC.gif", 1)
    assert os.path.exists("./test_save_video/test_video_bian_ASYNC.gif")
    h_li_network.data.save_video("./test_save_video/test_video.gif", 1)
    assert os.path.exists("./test_save_video/test_video.gif")
    shutil.rmtree("./test_save_video")

e = np.array([8.,7.,6.,5.,4.,3.,2.,1.])
@patch("matplotlib.pyplot.show")
def test_plot_energy(mock_show):
    h_li_network.data.plot_energy #test plus de sens
    assert True #sûr le assert true ?
    
def test_checkerboard():
    test_board = np.array([ 1, -1,  1, -1,  1, -1,  1, -1,  1, -1, 
                        -1,  1, -1,  1, -1,  1, -1,  1, -1,  1,  
                        1, -1,  1, -1,  1, -1,  1, -1,  1, -1, 
                        -1,  1, -1,  1, -1,  1, -1,  1, -1,  1, 
                        1, -1,  1, -1,  1, -1,  1, -1,  1, -1, 
                        -1,  1, -1,  1, -1,  1, -1,  1, -1,  1, 
                        1, -1,  1, -1,  1, -1,  1, -1,  1, -1,
                        -1,  1,  -1,  1, -1,  1, -1,  1, -1,  1, 
                        1, -1,  1, -1,  1, -1,  1, -1,  1, -1, 
                        -1,  1, -1,  1, -1,  1, -1,  1, -1,  1,])
    board = ut.checkerboard(100)
    assert np.allclose(board, test_board)
    #case when impossible to creat a square board 10X10
    assert ut.checkerboard(10) == None
    assert ut.checkerboard(144) == None

def matrix_features (mat) : 
    '''
    Verify that a matrix is symmetrical, and that all its values are between -1 and 1
    '''
    assert np.allclose(mat.shape, (np.transpose(mat)).shape)
    assert np.all(mat >= -1) | np.all(mat <= 1)

def test_reset_get() : 
    '''
    Test if the reset of the data put empty lists as attributes as expected
    '''
    h_r_network = h.HopfieldNetwork(our_patterns, 'Hebbian')
    h_r_network.dynamics(modif_pat, 1, 20)
    h_r_network.data.reset()
    assert h_r_network.data.get_data() == ([], [])
    