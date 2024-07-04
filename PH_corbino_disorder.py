# BHZ strip: Energy dispersion, conductance 
# ===============================================================
## Physics background
# ------------------
#  - tight-binding approximation of continuous Hamiltonians
#
# Kwant features highlighted
# --------------------------
#  - kwant.continuum.discretize


import kwant
import kwant.continuum
import scipy.sparse.linalg
import scipy.linalg
import numpy as np
import math
import shutil
import time

# For plotting
import matplotlib as mpl
from matplotlib import pyplot as plt



Mrand = np.random.rand(200,201)


def qsh_system(a, t=1.0, W=100, r1=80, r2=200):
    
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
       - mu(x,y) *  kron(sigma_z, identity(2))
       
    """
 
    template = kwant.continuum.discretize(hamiltonian, grid=a)

    def shape(site):
        (x, y) = site.pos
        rsq = x**2 + y**2
        return (r1**2 < rsq < r2**2)

    def lead_shape(site):
        (x, y) = site.pos
        return (-W/2 < y < W/2 )

    syst = kwant.Builder()
    syst.fill(template, shape, (0, r1+a))
    
    lead = kwant.Builder(kwant.TranslationalSymmetry([-a, 0]))
    lead.fill(template, lead_shape, (0, 0))

    syst.attach_lead(lead)
    syst.attach_lead(lead.reversed())
    syst=syst.finalized() 
    return syst



def all_params(a,eg,d1r,d1i,d2r,d2i):
    a2= a*a
    r1=80
    r2=200
        
    def fdisorder(x,y):
        err = 0
        rsq = x**2 + y **2
        if (r1**2 < rsq < r2**2):
            ii = int(x/a)
            jj = int(y/a)
            err = 1.0-2*Mrand[ii,jj]
        return err
    
    
   
    params = dict(A=0.06*a, B=0.5*a2, D=0, M=eg, C=0, Dz=0.02, D2R=d2r*a, D1R=d1r, D2I=d2i*a, D1I=d1i,mu=fdisorder)
    return params

    
def analyze_qsh(syst,params):
    kwant.plotter.bands(syst.leads[0], params=params,
                        momenta=np.linspace(-np.pi, np.pi, 201), show=False)
    plt.show()
    
    #conductance
    data =[]
    energies = np.linspace(-0.20,0.20,320)

    for energy in energies:

        # compute the scattering matrix at a given energy
        smatrix = kwant.smatrix(syst, energy, params=params)

        # compute the transmission probability from lead 0 to
        # lead 1
        data.append(smatrix.transmission(1, 0))
        #file.write("%f\n" %energy)


    fname="edge_cond"+str(params['M'])
    thefile = open(fname + ".dat","w")
    for i in range(len(data)):
        thefile.write(str(energies[i])+"   "+str(data[i])+"\n")
        
        
def plot_disorder(pardict):
    
    disofunct = pardict.get('mu')
    
    out = [disofunct(xx,yy) for xx in np.linspace(-200,200,401) for yy in np.linspace(-200,200,401)]
    
    out = np.array(out)
    out = out.reshape((401,401))
    plt.imshow(out)
    plt.show()

def main():
    aa = 1
    syst=qsh_system(a=aa)

    fl=np.loadtxt('Eg_input.txt')

    
    #gl=np.loadtxt('input.dat', comments='!')

    #iEg = int(gl)
    
    iEg=40

    ### The three lines below are my (Victor) changes to check that the function
    ### introducing the disorder is working properly.
    ### Once the tests are OK the lines can be comment out    
    params=all_params(a=aa, eg=fl[iEg,0],d1r=fl[iEg,1],d1i=fl[iEg,2],d2r=fl[iEg,3],d2i=fl[iEg,4])
    kwant.plot(syst)
    plot_disorder(params)


    #for i in range(iEg-1,iEg):
    #    params=all_params(a=aa, eg=fl[i,0],d1r=fl[i,1],d1i=fl[i,2],d2r=fl[i,3],d2i=fl[i,4])
    #    analyze_qsh(syst=syst, params=params)
    
    
# Call the main function if the script gets executed (as opposed to imported).
# See <http://docs.python.org/library/__main__.html>.
if __name__ == '__main__':
    main()
