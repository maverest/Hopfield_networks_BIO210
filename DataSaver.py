import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import os 

class DataSaver:
    """
    Store a sequence of states and their associated energy.
    """
    def __init__(self):
        """
        Initialize a DataSaver object.
    
        Parameter
        ---------
        None
        
        Returns
        --------
        None
        """
        self.states_list = []
        self.energies = []
    
    def reset(self):
        """
        Reset the list of states and the energy.
    
        Parameter
        ---------
        None
        
        Returns
        --------
        None
        """
        self.states_list = []
        self.energies = []      
    
    def store_iter(self, state, weights):
        """
        Add a state to the list of states and add the associated energy to energy list.
    
        Parameter
        ---------
        state: array / pattern 
        weights: matix array / weight matrix
        
        Returns
        --------
        None
        """
        self.states_list.append(state)
        self.energies.append(self.compute_energy(state, weights))

    def compute_energy(self, state, weights):
        """
        Compute the energy associated to a state given a pattern and the weight matrix 
    
        Parameters
        -------
        state: array / state pattern
        weights: 2 dimensional array / weight matrix
    
        Returns
        ----
        energie: float / level of energy 
        """
        p = np.outer(state,state)
        w_p = weights * p
        energie = (-0.5) * w_p.sum()
        return energie

    def get_data(self):
        """
        Return the data stored (list of states and associated list of energies).
    
        Parameter
        ---------
        None
        
        Returns
        --------
        states_list: list / list of states
        energies: list / list of energy associated to the states
        """
        return self.states_list, self.energies
    
   
    def save_video(self, out_path, img_shape):
        """
        Generate a video of the evolution of the system based on its history saved in a list of pattern and saves it in a given path
    
        Parameters 
        ----
        state_list : list of matrix array / state history of the system
        out_path : string / out path
    
        Return
        ----
        None
    
        """
    
        file = out_path.split("/")[1]
        if (os.path.exists(file) == False):
            os.makedirs(file)
        
        d = 'Function used:'
        if 'bian' in out_path.lower() :
            s = 'Hebbian'
        else :
            s = 'Storkey'
        if 'async' in out_path.lower():
            d += ' dynamics_async'
        else:
            d += ' dynamics'

        fig= plt.figure()
        im = fig.add_subplot(1,1,1)
        im.set_title('Pattern convergence (pattern size : {}) \n using the {} learning rule\n{}'.format(len(self.states_list[0])**2, s, d) , pad =15, fontname = 'Helvetica')
        states_as_ims = []
        list_states = self.reshape_states_list(self.states_list)
        for i in range(len(self.states_list)-1) :
            states_as_ims.append([im.imshow(list_states[i],cmap = "gray", animated = True )]) 
        ani = animation.ArtistAnimation(fig, states_as_ims, interval = 1000)

        ani.save(out_path, writer = 'pillow')
    
        plt.show() 


    def plot_energy(self):
        """
        Generate a time vs. energy plot based on the values created by the energy function
    
        Parameter
        ----
        energies : array of floats / energy level associated to states of the network until convergence
        weight : matrix array / hebbian or storkey weight matrix 
    
        Return
        ----
        None
        """
    
        #data for plotting 
        t = np.arange(0, len(self.energies), 1)

        figure, ax = plt.subplots()
        ax.plot(t, self.energies, color='red', marker='2', linestyle='dashed', linewidth=1, markersize=12)
    
        ax.set(xlabel='Time', ylabel='Energy',
        title='Time-energy plot')

        plt.show()
    

    def reshape_states_list(self, states_list):
        """""
        Reshape the stored states vector into sqrt(len(vector)) x  sqrt(len(vector)) matrix stored in a list
    
        Parameters
        ----
        states_list: list of array / state history of the system
    
        Return
        ----
        list of matrix or None if not possible to reshape

        """
        nb_neurons = len(states_list[0])
        try :
            return [x.reshape((int(math.sqrt(nb_neurons)), int(math.sqrt(nb_neurons)))) for x in states_list]
        except: 
            print("vector can not be converted into a square shape")
            return None





