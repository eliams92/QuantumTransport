import kwant
import kwant.continuum
import scipy.sparse.linalg
import scipy.linalg
import numpy as np
import math
import time


import matplotlib as mpl
from matplotlib import pyplot as plt


def qsh_system(a, t=1.0, W=100, r1=80, r2=200): 
    #The function converts the Hamiltoninan written in momentum space to real space with square lattice with lattice constant 'a' with commands at line 32 and line 33. 
    #The parameters C, B, A, M, Dz, D1R, D1I, D2R, D2I become variables at this stage and can be given values when calculations need to be done.
    
    hamiltonian = """
    
       + C * identity(4) - M * kron(sigma_z, sigma_0)
       + B * (k_x**2 + k_y**2) * kron(sigma_z, sigma_0)
       - D * (k_x**2 + k_y**2) * kron(sigma_0, sigma_0)
       + (A + D2R) * k_x * kron(sigma_x, sigma_z)
       - (A + D2R) * k_y * kron(sigma_y, sigma_0)
       + (Dz + D1R) * kron(sigma_y, sigma_y)
       - D2I * k_y * kron(sigma_x, sigma_0)
       - D2I * k_x * kron(sigma_y, sigma_z)
       + D1I * kron(sigma_x, sigma_y)
       
    """
 
    template = kwant.continuum.discretize(hamiltonian, grid=a)
    lat = kwant.lattice.square(a)

    #The shape function defines the geometry of the real-space lattice. Only the spatial coordinates that are between 'r1' and 'r2' are considered (see line 39). 
    def shape(site):
        (x, y) = site.pos
        rsq = x**2 + y**2
        return (r1**2 <= rsq <= r2**2)
        
    #Leads are connected to measure bulk conductances in a Corbino disc. It is an infinitely long rectangular-shaped lead with a width 'W'. 
    #A lead is built from infinity to the scattering region i.e. the Corbino disc.
    def lead_shape(site):
        (x, y) = site.pos
        return (-W/2 < y < W/2)

    syst = kwant.Builder()
    syst.fill(template, shape, (0, r1+a))
    
    #lead and lead1 are leads that are bult from positive and negative infinity to be attached to the Corbino disc 
    lead = kwant.Builder(kwant.TranslationalSymmetry([a, 0]))
    lead.fill(template, lead_shape, (0, 0))
    lead1 = kwant.Builder(kwant.TranslationalSymmetry([-a,0]))
    lead1.fill(template, lead_shape, (0,0))

    syst.attach_lead(lead, lat(0,0)) #lead attaches itself to the inner edge of the Corbino disc
    syst.attach_lead(lead1) #lead attaches to the outer edge of the Corbino disc
    syst=syst.finalized() 
    return syst


def analyze_qsh(a, eg,d1r,d1i,d2r,d2i):

    a2= a*a
    #A dictionary of values for the parameters.
    params = dict(A=0.06*a, B=0.5*a2, D=0, M=eg, C=0, Dz=0.02, D2R=d2r*a, D1R=d1r, D2I=d2i*a, D1I=d1i)
    syst=qsh_system(a=a) 

    

    #data is a list that stores the bulk conductance for each value in the array 'energies'
    data =[]
    energies = np.linspace(-0.20,0.20,320)
    
    for energy in energies:

        # compute the scattering matrix at a given energy
        smatrix = kwant.smatrix(syst, energy, params=params)

        # compute the transmission probability from lead 0 to
        # lead 1
        data.append(smatrix.transmission(1, 0))
        #file.write("%f\n" %energy)

    #saves the generated bulk conductance as a function of energy in energies in the following .dat file
    fname="bulk_cond"+str(params['M'])
    thefile = open(fname + ".dat","w")
    for i in range(len(data)):
        thefile.write(str(energies[i])+"   "+str(data[i])+"\n")


def main():

    aa = 1
    #takes the values from the file as a table (two-dimensional array).
    fl=np.loadtxt('Eg_input.txt')
    #used to loop Eg in shell script to submit jobs in HPC
    gl=np.loadtxt('input.dat', comments='!')
    
    iEg = int(gl)
   
    for i in range(iEg-1,iEg):
        data=analyze_qsh(a=aa, eg=fl[i,0],d1r=fl[i,1],d1i=fl[i,2],d2r=fl[i,3],d2i=fl[i,4])

# Call the main function if the script gets executed (as opposed to imported).
# See <http://docs.python.org/library/__main__.html>.
if __name__ == '__main__':
    main()
