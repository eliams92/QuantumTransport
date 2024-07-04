import numpy as np
import matplotlib.pyplot as plt
import math
#loads Eg_input as a 2D array
b=np.loadtxt('Eg_input.txt') 

#plots coloumn 0 (x-axis) versus coloumn 1-4 (y-axis) in lines 8-11 
plt.plot(b[:,0],b[:,1],label='$Re(\Delta_1)$') 
plt.plot(b[:,0],b[:,2],label='$Im(\Delta_1)$')  
plt.plot(b[:,0],b[:,3],label='$Re(\Delta_2)$')  
plt.plot(b[:,0],b[:,4],label='$Im(\Delta_2)$')

#legends and labels for the plot
plt.legend(prop={'size': 20})
plt.xlabel('$E_G/E_0$',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#saving the generated figure
plt.savefig('TR_brokenphase.pdf',format='pdf',dpi=10000) #dpi decides the quality of the figure generated (pixel count)
plt.show() #shows the figure generated after running
