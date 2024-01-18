import numpy as np
import random
import math

def generate_patterns(num_patterns, pattern_size) :
    """
    Generate a given number of patterns composed of -1 and 1 of a given size 
    
    Parameters
    ----
    num_patterns: int / number of neurons
    pattern_size: int / number of pattern
    
    Returns
    ----
    two dimensional array / array of patterns
    """
    patterns = np.random.choice([-1,1], size = (num_patterns,pattern_size))   
    return patterns



def perturb_pattern(pattern, num_perturb):
    """
    Perturb a given number of element(s) on a given pattern
    
    Parameters
    -----
    pattern: array / pattern
    num_perturb: int / number of values to modified
    
    Returns
    ----
    array / the modified pattern
    """
    p = np.copy(pattern)
    c = random.sample([x for x in range(len(pattern)-1)],num_perturb)
    for i in range(num_perturb):
        p[c[i]] = p[c[i]] * -1
    return p
    
    
def checkerboard(case_number) : 
    """ 
    Create a vector array of 1 and -1 of length "case number" that respresents a 10x10 checkboard (1 = white, -1 = black)
    
    Parameters
    ----
    case_number : int / number of values that compose our checkboard !!HAS TO BE A PERFECT SQUARE % 10 == 0 AND MIN VALUE IS 100 (e.g : 100,400,900,1600,2500....)!!
    
    Returns
    ----
    board: vector array / the checkboard
    Or None if the case_number not valid for a square chessboard
    
    """
    size = math.sqrt(case_number)
    a = case_number %10 == 0
    b= size - int(size) == 0
    c = case_number >= 100
    if bool(a*b*c) == 0 :
       print("Argument <case_number> not valid for a square chessboard")
       return None   
    checker_size = int(size/10) #echquier 10X10
    whit,blck = np.ones(checker_size), np.ones(checker_size) *-1
    wb = np.concatenate((whit,blck),axis= None)
    impaire_block = np.tile(wb,checker_size *5)
    paire_block = np.copy(impaire_block) *-1 
    two_by_two = np.concatenate((impaire_block, paire_block),axis = None)
    board = np.tile(two_by_two,5)
    np.reshape(board,(1,case_number))
    return board