# Hopfield networks :brain:  <img src="https://user-images.githubusercontent.com/114407059/207599921-4d0a3d50-5b0e-413d-9f16-911dd014c310.gif" width ="200" align ="right" >


### Part of the BIO-210 Course

**Team 13**

A Hopfield network is a form of recurrent artificial neural network that can be viewed as a computational model for associative memory. It was proposed by John Hopfield in 1982. The model consist in a process that shows how a network can store the entity it wants to _remember_ using weighted connections between neurons, those weights either deriving from the Hebbian or the Storkey learning rule.


## Requirements :snake:

- Python >= 3.9 

- numpy

- matplotlib

- pytest

- pytest-benchmark

You can find our environment file **projectEnv.yml** and create a conda environment using the commands:

<pre><code> conda env create -f Hopfield_project.yml </code></pre>

And then you can activate the environment using:

<pre><code> conda activate envHopfieldProject </code></pre>

in a terminal.

## Tests :clipboard:

We use [pytest](ttps://docs.pytest.org/en/6.2.x/contents.html)

### Pytests

We created unit-tests for the **hopfield.py** in **test_HP.py** to run the tests use the command:

<pre><code> pytest test_HP.py </code></pre>

in the terminal.

### Coverage
To run the tests and get a comprehensive coverage report, use the command  

<pre><code> coverage run -m pytest 

 coverage report</code></pre>

in the terminal or run the **test.sh** script. 



## Expected results of convergence :chess_pawn:
In order to visualise the convergence of the system, we represented our patterns under the appearance of a checkboard. Here is a _.gif_ of the consecutives states of the aforementionned system until convergence.

For this system convergence we used the santard synchronous update with the Hebbian learning rule :

<p align="center">
 <img src="https://user-images.githubusercontent.com/55958594/205643505-7b17809d-5257-48fc-99c4-8de0d1dd5c77.gif" width = "50%" >
</p>


## Results by releases :chart_with_upwards_trend:

The project was organised in weekly releases including the implementation of new functinnalities and/or code refactoring.

### Release 1

We implemented the basics of the project : the algorithm of the Hebbian learning rule to compute the weight matrix as well as the standard update function.

### Release 2

We refactored our code into function, standardizing our API and adding a few functions. We also implemented the storkey learning rule, a second way to compute the weight matrix along with the asynchronous update.

### Release 3

We worked on visualisation of the convergence, producing checkerboards to have a tangible model and we implemented and ploted the corresponding energy function of the system, helping monitoring its behaviour.

<p align="center">
<image width = "75%" src="https://user-images.githubusercontent.com/55958594/205655315-1c223aa8-f0de-4d75-9673-01dc0713c5ac.gif">
<p>

<p align="center">
<img width="75%" alt="image" src="https://user-images.githubusercontent.com/55958594/205652045-59201eb1-6b96-4abb-9e2a-035b435aeeea.png">
<p>


### Release 4
We focused on testing using doctests and pytest along with coverage reports.

### Release 5
We addressed the code review from the week prior and organised the conda environnement.

### Release 6
We optimised the performance aspect of the code using Cprofile to identify the bottlenecks and benchmark for quantify the progress. The improvements were mainly performed using the numpy library.

### Release 7
We refactored the whole code in a object oriented version. The object oriented version is added in an additional file but it contains not the experiment part.

### Release 8
We proceeded to experimentations on our project. We tested the capacity, the robusteness and the image reconstruction. The results are detailed in the [summary.md](https://github.com/EPFL-BIO-210/BIO-210-22-team-13/blob/sanspoo/summary.md) file.

#### Contributors :bust_in_silhouette:
[jciardo](https://github.com/jciardo), [frossardr](https://github.com/frossardr), [maverest](https://github.com/maverest)

