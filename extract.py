import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as mplot
import matplotlib

e=np.linspace(0.1,1.28,60)

filename="bulk_cond.txt"

for i in e:
    #line 12-15 are used to format the variables as named in the path-to-file
    eg_dir="{0:.3f}".format(i)
    eg_file="{0:.2f}".format(i)
    name_dir='Eg_'+eg_dir
    name_file='bulk_cond'+eg_file+'.txt'
    #loads the file that contains bulk-conductance stored for a set of values of energies stored in the file location
    a=np.loadtxt('/home/tania/project1/corbino_200x80/bulk/'+ name_dir +'/'+ name_file)
    #stores the second column of 'a'
    b=a[:,1]
    bt=b.transpose() 
    with open(filename, 'w') as fileObject:
    # code that computes numpy array
        np.savetxt(fileObject, bt, delimiter = ' ', newline = ' ')
        fileObject.write('\n')



filename="edge_cond.txt"

for i in e:
    eg_dir="{0:.3f}".format(i)
    eg_file="{0:.2f}".format(i)
    name_dir='Eg_'+eg_dir
    name_file='edge_cond'+eg_file+'.txt'
    #print(name_dir, name_file)
    a=np.loadtxt('/home/tania/project1/corbino_200x80/edge/'+ name_dir +'/'+ name_file)
    b=a[:,1]
    bt=b.transpose()
    #np.savetxt(filename,bt)
    with open(filename, 'w') as fileObject:
    # code that computes numpy array
        np.savetxt(fileObject, bt, delimiter = ' ', newline = ' ')
        fileObject.write('\n')


x=np.linspace(0.1,1.28,60)
y=np.linspace(-0.20,0.20,320)
z2=np.loadtxt('/home/tania/project1/corbino_200x80/edge_cond.txt')
z1=np.loadtxt('/home/tania/project1/corbino_200x80/bulk_cond.txt')

#plots the bulk conductance in a 2D plot as a function of energies and $E_G$
plt.figure()
cp1 = plt.contourf(x, y, z1.T, cmap=plt.cm.viridis,levels=[-20,0,1,2,10,20,50,80])
cbar=plt.colorbar(cp1)
cbar.ax.set_ylabel('$G_{bulk}/G_0$',fontsize=20)
#plt.ylim(-0.06,0.06)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel('$eV_{dc}/E_0$',fontsize=20)
plt.xlabel('$E_G/E_0$',fontsize=20)
plt.tight_layout()
plt.title("Bulk Conductance",fontsize=20)
plt.savefig('bulk_conductance.png', dpi=1000)
plt.show()

#plots the edge conductance in a 2D plot as a function of energies and $E_G$
plt.figure()
cp2 = plt.contourf(x, y, z2.T, cmap=plt.cm.viridis,levels=[-20,0,1,2,10,20,50,80])
cbar=plt.colorbar(cp2)
cbar.ax.set_ylabel('$G_{edge}/G_0$',fontsize=20)
#plt.ylim(-0.06,0.06)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel('$eV_{dc}/E_0$',fontsize=20)
plt.xlabel('$E_G/E_0$',fontsize=20)
plt.tight_layout()
plt.savefig('edge_conductance.png', dpi=1000)
plt.show()








