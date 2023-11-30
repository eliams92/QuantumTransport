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

    def shape(site):
        (x, y) = site.pos
        rsq = x**2 + y**2
        return (r1**2 < rsq < r2**2)

    def lead_shape(site):
        (x, y) = site.pos
        return (-W/2 < y < W/2)

    syst = kwant.Builder()
    syst.fill(template, shape, (0, r1+a))
    
    lead = kwant.Builder(kwant.TranslationalSymmetry([a, 0]))
    lead.fill(template, lead_shape, (0, 0))
    lead1 = kwant.Builder(kwant.TranslationalSymmetry([-a,0]))
    lead1.fill(template, lead_shape, (0,0))

    syst.attach_lead(lead, lat(0,0))
    syst.attach_lead(lead1)
    syst=syst.finalized() 
#    kwant.plot(syst)             #uncomment to see the finite system
    return syst


def analyze_qsh(a, eg,d1r,d1i,d2r,d2i):

    a2= a*a
   
    params = dict(A=0.06*a, B=0.5*a2, D=0, M=eg, C=0, Dz=0.02, D2R=d2r*a, D1R=d1r, D2I=d2i*a, D1I=d1i)
    syst=qsh_system(a=a)

    
    kwant.plotter.bands(syst.leads[0], params=params, momenta=np.linspace(-0.5*np.pi, 0.5*np.pi, 401), show=False)
    plt.xlabel('momentum [1/A]')
    plt.ylabel('energy [eV]')
    plt.xlim(-0.5*np.pi, 0.5*np.pi)
    plt.ylim(-0.3,0.3)
    plt.savefig("energy_dispersion"+str(params['M'])+".pdf", format='pdf', dpi=1000)
    plt.show()



def main():

    aa = 1

    fl=np.loadtxt('Eg_input.txt')

    gl=np.loadtxt('input.dat', comments='!')

    iEg = int(gl)
    
    for i in range(iEg-1,iEg):
        data=analyze_qsh(a=aa, eg=fl[i,0],d1r=fl[i,1],d1i=fl[i,2],d2r=fl[i,3],d2i=fl[i,4])
    
     #Call the main function if the script gets executed (as opposed to imported).
# See <http://docs.python.org/library/__m
