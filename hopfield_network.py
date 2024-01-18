import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from DataSaver import *


class HopfieldNetwork:
    """
    Define a Hopfield network with its attributes and functionalities.
    """
    def __init__(self, patterns, rule='hebbian'):
        """
        Initialize a Hopfield network with its attributes given in parameter.
    
        Parameter
        ---------
        patterns: matrix array / matrix composed of the patterns
        rule: string / the type of the weight matrix to use
        
        Returns
        --------
        None
        """
        self.patterns = patterns
        self.data = DataSaver()
        if rule == 'hebbian':
            self.weight = self.hebbian_weights(self.patterns)
        else:
            self.weight = self.storkey_weights(self.patterns)
            
    
    def hebbian_weights(self, patterns):
        """
        Implement the Hebbian learning rule to generate the weight matrix of our network

        Parameters
        ------
        patterns: matrix array / matrix composed of our patterns

        Returns
        ------
        two dimensional array / weight matrix

        Doctest
        -------
        >>> HopfieldNetwork(np.array([[1,1,-1,-1],[1,1,-1,1], [-1,1,-1,1]]), "Hebbian").weights
        np.array([[ 0         ,  0.33333333 , -0.33333333 , -0.33333333],
                  [ 0.33333333,  0          , -1          ,  0.33333333],
                  [ 0.33333333, -1          ,  0          , -0.33333333],
                  [-0.33333333,  0.33333333 , -0.33333333 ,  0         ]])
        """
        nb_patern = patterns.shape[0]
        w = (np.dot(np.transpose(patterns), patterns)) /nb_patern
        np.fill_diagonal(w,np.zeros_like(np.diag(w)))
        return w

    def storkey_weights(self, patterns):
        """
        Implement the storkey learning rule to generate the weight matrix of our network 

        Parameters
        ------
        patterns: matrix array / matrix composed of our patterns

        Returns
        ----
        w_mat: two dimensional array / weight matrix


        Doctest
        -------
        >>> HopfieldNetwork(np.array([[1,1,-1,-1],[1,1,-1,1], [-1,1,-1,1]]), "Storkey").weights
        np.array([[  1.125,  0.25 , -0.25 , -0.5  ],
                  [  0.25 ,  0.625, -1    ,  0.25 ],
                  [ -0.25 , -1    ,  0.625, -0.25 ],
                  [ -0.5  ,  0.25 , -0.25 ,  1.125]])
        """
        pattern_size = patterns.shape[1]
        w_mat = np.zeros([pattern_size,pattern_size])
        
        for pattern in patterns:
            #Computing the matrix h needed to compute the weights matrix 
            pattern_matrix = np.transpose(np.broadcast_to(pattern,(pattern_size,pattern_size)))
            h_mat = np.matmul(w_mat - np.diag(np.diag(w_mat)), pattern_matrix - np.diag(np.diag(pattern_matrix)))

            #Implementation of the Storkey learning rule
            to_add = (np.outer(pattern, pattern) - np.transpose(h_mat * pattern) - (h_mat * pattern))
            w_mat += to_add/pattern_size

        return w_mat

    def update(self, state):
        """
        Compute the new sate by receiving a network state pattern and the weight matrix using the updat rule
    
        Parameters
        --------
        state: array / pattern 
        weights: matix array / weight matrix
    
        Returns
        ----
        array / the new state pattern
        """
        new_state = np.dot(self.weight,state)
        new_state = np.where(new_state < 0, -1, 1)
        return new_state


    def update_async(self, state):
        """
        Compute the component of the new state pattern at a random index "i" receiving the sate pattern and the weight matrix by applying the update rule to the previous state pattern and the i-th row of the weight matrix
    
        Parameters
        ------
        state: array /pattern
        weights: matrix array / weights matrix
    
    
        Returns
        ----
        array / the new state pattern
        """
        new_state = np.copy(state)
        i = random.randint(0,new_state.shape[0]-1)
        new_state[i] = np.where(np.dot(self.weight[i], new_state) < 0, -1, 1)
        return new_state

    def dynamics(self, state, saver, max_iter =20):
        """
        Run the dynamical system from the inital state until convergence or until the given max number of iteration is reached.
        Convergence is reached when two consecutives updates return the same state.
    
        Parameters
        ----
        state: array / state pattern
        weights: 2 dimensional array / weight matrix
        max_iter: int / maximum of iteration
    
        Returns
        ----
        list of arrays / state history of the system
            """
        p = np.copy(state)
        i = 0
        while i < max_iter:
            previous_p = np.copy(p)
            p = self.update(p)
            if (i%saver == 0): #Use the skip parameter to save only one every skip states. Utiliser saver comme skip
                self.data.store_iter(p, self.weight)
            if ((p ==previous_p).all()):           
                print("Convergence after: ",i, " itterations" )
                return None
            i += 1
        print("Convergence failed")
        return None

    def dynamics_async(self, state, saver, max_iter=1000, convergence_num_iter =100):
        """
        Run the dynamical system from the inital state until convergence or until the given max number of iteration is reached.
        Convergence is considered to be reached when the state does not change for a given number of iteration.
    
        Parameters
        ----
        state: array / state pattern
        weights: 2 dimensional array / weight matrix
        max_iter: int / maximum of iteration
        convergence_num_iter: int / number of identical iteration to satisfy convergence
        step : int (default value = 1) / we will calculate the energy of each n*step states
    
        Returns
        ----
        states_list: list of arrays / state history of the system
        """
        p = np.copy(state)
        i = 0
        j = 0 
    
        while i < max_iter:
            previous_p = np.copy(p)
            p = self.update_async(p)
            if ((i%saver == 0) or (convergence_num_iter == j)) :  #Use the skip parameter to save only one every skip states
                self.data.store_iter(p, self.weight)
            if ((p == previous_p).all()):
                j += 1
                if j == convergence_num_iter :
                    print("Convergence after: ",i, " itterations" )
                    return None
            else:
                j = 0
            i += 1
        print("Convergence failed")
        return None

    def pattern_match(self, memorized_patterns, pattern):
        """
        Check if a given pattern matches with one of the initially memorized patterns 
    
        Parameters
        -------
        memorized_patterns: matrix array / the list of original patterns
        pattern: array / pattern
    
        Returns
        ----
        none (if nothing matches) | integer (the index/row of the corresponding pattern)
        """
        if pattern in memorized_patterns :
            try :
                return int((np.where((memorized_patterns == (pattern)).all(axis=1))[0])[0])
            except : 
                return None
                
