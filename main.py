import numpy as np
import hopfield_network as h
import utility as u
from timeit import default_timer as timer


#---------MAIN------------------------------------------------------------------------------------------------------        
pat = u.generate_patterns(49,2500)
board = u.checkerboard(2500)
pat = np.insert(pat,len(pat), board, axis = 0)
print(pat.shape)
modif = u.perturb_pattern(board, 1000)

#STORKEY
#-------
storkey_network = h.HopfieldNetwork(pat, 'storkey')
#dynamics
storkey_network.dynamics(modif, 1, 20)
storkey_network.data.plot_energy()
storkey_network.data.save_video('./videos/video_Storkey.gif', 1)
#dynamics_async
storkey_network.data.reset()
storkey_network.dynamics_async(modif, 1000, 35000, 10000)
storkey_network.data.plot_energy()
storkey_network.data.save_video('./videos/video_Storkey_ASYNC.gif', 1)

#HEBBIAN
#-------
hebbian_network = h.HopfieldNetwork(pat, 'hebbian')
#dynamics
hebbian_network.dynamics(modif, 1, 20)
hebbian_network.data.plot_energy()
hebbian_network.data.save_video('./videos/video_Hebbian.gif', 1)
#dynamics_async
hebbian_network.data.reset()
hebbian_network.dynamics_async(modif, 1000, 35000, 10000)
hebbian_network.data.plot_energy()
hebbian_network.data.save_video('./videos/video_Hebbian_ASYNC.gif', 1)




"""""
#--------------CPROFILE---------------------------------------

def main() :
    patterns = h.generate_patterns(50,2500)
    modif = np.copy(patterns[0])
    converge = np.copy(patterns[0])
    modif = h.perturb_pattern(modif, 1000)
    wh = h.hebbian_weights(patterns)
    ws = h.storkey_weights(patterns)
    h.dynamics(modif,wh,20)
    h.dynamics(modif,ws,20)
    h.dynamics_async(modif,wh,30000,10000)
    h.dynamics_async(modif,ws,30000,10000)


def main2():
    patterns = h.generate_patterns(50,2500)
    ws = h.storkey_weights(patterns)

start = timer()
main2()
end = timer()
duration = end - start # duration in seconds
print(duration)
"""






