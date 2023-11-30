# codes4doc

Title: INTERPLAY OF QUANTUM SPIN HALL EFFECT AND SPONTANEOUS TIME-REVERSAL SYMMETRY BREAKING IN ELECTRON-HOLE BILAYERS: TRANSPORT STUDY

Delta_s and Delta_p are the s-wave and p-wave exciton pairings. 

The parameters of the Hamiltonian in the codes are the following:

A: Tunneling strength
B: hbar^2/2*m
Dz: Bulk inversion asymmetry
D1R: Real part of Delta_s
D1I: Imaginary part of Delta_s
D2R: Real part of Delta_p
D2I: Imaginary part of Delta_p
E_G: controls the electron and hole densities 

This repository contain the codes used to perform the transport calculations on a Corbino disc using Kwant:
1. Eg_input.txt: Contains the 5 columns in the order, E_G, D1R, D1I, D2R, D2I.
2. plot.py: Plots D1R, D1I, D2R, D2I as a function of E_G.
3. energy_dispersion.py: Calculates the eigenvalues of the Hamiltonian and generates the edge spectrum as a function of k.
4. bulk_conductance.py: Calculates the bulk conductance as a function of energies around the zero energy for a specific E_G.
5. extract.py: Plots the 2D contour plot as function of energies (eV_{dc}) along the y-axis and E_G along the x-axis.
   








