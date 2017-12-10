# Scoopie
Heuristiekenproject Protein Pow(d)er

This project uses various alogritms to calculate the optimal folding in a protein. The protein consists of polar (P) and hydrophocic (H)
amino acids, and later in the project also cysteine (C). The amino acids are folded into a 2D array configuration. Two adjecent H amino acids which are not bondend to each other result in a stabilizing 'H-bond'. The amount of 'H-bonds' quantifies how well the stabilization is. A single 'H'-bond contributes with a '-1' for the total score of a protein. The proteins with the best score, so the lowest number, are considered the most stable protein foldings.
Later also the cysteine 'disulfide bonds' with contribute to the protein score, with an amount of '-5'.
At last the proteins are folded in 3 dimensions and the best 3D foldings are estimated.
The various programs output the optimal configurations with stabilization of a given input protein strand.

# Getting Started

Prerequisites

Python v2.7 - https://www.python.org/downloads/
NumPy - https://docs.scipy.org/doc/numpy-1.13.0/user/install.html
Matplotlib v2.1.0 - https://matplotlib.org/users/installing.html#macos
NetworkX v2.0 - https://networkx.github.io/

# Running the tests

In this repository you will find different maps for different methods and algoritms. The name of the map includes which algoritm the files inside of are based on. There are files for defining functions and there are files containing the main functions. Running these main programs will execute the different algoritms to find possible foldings for the different proteins.

# Built With

Matplotlib - a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms
NetworkX - a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks

# Authors

Youssef Bentaher - Initial work
Lucien Koenekoop - Initial work

# Acknowledgments
Yol Tio for inspiration and initial participation in this project
