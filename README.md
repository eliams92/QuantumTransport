# Transport Properties

Title: INTERPLAY OF QUANTUM SPIN HALL EFFECT AND SPONTANEOUS TIME-REVERSAL SYMMETRY BREAKING IN ELECTRON-HOLE BILAYERS: TRANSPORT STUDY

Collaborators: Dr. Timo Hyart and Dr. V.F. Becerra

Description: The electron-hole bilayer such as InAs/GaSb is a band-inverted system that also supports quantum spin Hall phase as a function of well width and electron-hole densities. However, in experiments, for long samples, this material has shown linearly increasing longitudinal resistance with device length, mean free path of which, is found to be temperature independent for a wide range of temperature of $20$mK to $4.2$K. An appearance of spontaneously broken time-reversal symmetry phase could allow elastic backscattering processes which may explain the magnitude and temperature independence of the mean free path. As this material is also a candidate for supporting correlated phases of excitons, it has been shown that there is a spontaneous time-reversal symmetry broken phase that appears between trivial and QSH phases in the topological phase diagram as a function of increasing electron-hole densities. The breaking of TRS due to the presence of excitons, leads to an unconventional topological transition where the bulk-gap closing is absent. In the paper below, we present a transport study on a Corbino disc which proposes that this TRS broken phase could be observed in an experiment through measuring bulk and edge conductances as a function of electron-hole densities. As the electron-hole densities are increased, the bulk-conductance remains zero while the edge conductance smoothly takes a quantized value around the Fermi energy, demonstrating the occurrence of a topological transition without bulk-gap closing. 


Here, we use the Kwant package in Python to calculate bulk and edge conductance on a Corbino disc. Kwant is an efficient quantum transport package designed for topological insulators, superconductors etc. A more detailed version is available at : https://kwant-project.org/ . 

This repository contain the codes used to perform the transport calculations on a Corbino disc using Kwant:
1. Eg_input.txt: Contains the 5 columns in the order, E_G, Re{Delta_s}, Im{Delta_s}, Re{Delta_2}, Im{Delta_2}. Each row has a unique entry E_G. 
2. TRSbreaking.py: Plots Re{Delta_s}, Im{Delta_s}, Re{Delta_2}, Im{Delta_2} as a function of E_G.
3. energy_dispersion.py: Calculates the eigenvalues of the Hamiltonian and generates the edge spectrum as a function of k.
4. bulk_conductance.py: Calculates the bulk conductance as a function of energies around the zero energy for a specific E_G.
5. edge_conductance.py: Calculates the edge conductance as a function of energies around the zero energy for a specific E_G.
6. extract.py: Plots the 2D contour plot as function of energies (eV_{dc}) along the y-axis and E_G along the x-axis.
7. disorder.py: Introduces a random disorder (or noise) to each spatial point in Corbino disc. Useful in studying the role of disorder on transport effect.

Delta_s and Delta_p are the s-wave and p-wave exciton pairings that arise from the Coulomb interactions in Type-II quantum well. They are self-consistently obtained. More details at : https://journals.aps.org/prb/abstract/10.1103/PhysRevB.106.235420

The parameters of the Hamiltonian in the codes are the following:

A: Tunneling strength
B: hbar^2/2*m
Dz: Bulk inversion asymmetry
D1R: Real part of Delta_s
D1I: Imaginary part of Delta_s
D2R: Real part of Delta_p
D2I: Imaginary part of Delta_p
E_G: controls the electron and hole densities and is tuned to obtain the topological phase diagram. 


DISCLAIMER: The original code from Kwant has been modified to implement the above model. 




   








