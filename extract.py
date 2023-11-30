import numpy as np
from matplotlib import pyplot as plt
import os
import matplotlib.pyplot as mplot
import matplotlib
os.remove("bulk_cond.txt")

e=np.linspace(0.1,1.28,60)

filename="bulk_cond.txt"

for i in e:
    eg_dir="{0:.3f}".format(i)
    eg_file="{0:.2f}".format(i)
    name_dir='Eg_'+eg_dir
    name_file='bulk_cond'+eg_file+'.txt'
    #print(name_dir, name_file)
    a=np.loadtxt('/home/tania/project1/corbino_200x80/bulk/'+ name_dir +'/'+ name_file)
    b=a[:,1]
    bt=b.transpose()
    #np.savetxt(filename,bt)
    with open(filename, 'a') as fileObject:
    # code that computes numpy array
        np.savetxt(fileObject, bt, delimiter = ' ', newline = ' ')
        fileObject.write('\n')



os.remove("edge_cond.txt")

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
    with open(filename, 'a') as fileObject:
    # code that computes numpy array
        np.savetxt(fileObject, bt, delimiter = ' ', newline = ' ')
        fileObject.write('\n')


x=np.linspace(0.1,1.28,60)
y=np.linspace(-0.20,0.20,320)
z2=np.loadtxt('/home/tania/project1/corbino_200x80/edge_cond.txt')
z1=np.loadtxt('/home/tania/project1/corbino_200x80/bulk_cond.txt')


# Contour plotting using contourf
#plt.figure()
#plt.subplot(211)
#cp1 = plt.contourf(x, y, z1.T, cmap=plt.cm.viridis,levels=[0,0.2,0.3,0.4,0.5,0.6,0.7,0.80,0.9,1,1.25,1.5,1.75,2,2.5])
#plt.colorbar(cp1)
#plt.title('Bulk Conductance')
#plt.subplot(212)
#cp2 = plt.contourf(x, y, z2.T, cmap=plt.cm.viridis,levels=[0,0.2,0.3,0.4,0.5,0.6,0.7,0.80,0.9,1,1.25,1.5,1.75,2,2.5])
#plt.colorbar(cp2)
#plt.title('Edge Conductance')
#plt.savefig('conductance.pdf', format='pdf',dpi=10000)
#plt.show()





#plt.figure()
#plt.subplot(211)
#cp1 = plt.contourf(x, y, z1.T, cmap=plt.cm.viridis)
#plt.colorbar(cp1)
#plt.title('Bulk Conductance')
#plt.subplot(212)
#cp2 = plt.contourf(x, y, z2.T, cmap=plt.cm.viridis,levels=[0,2,80])
#plt.colorbar(cp2)
#plt.title('Edge Conductance')
#plt.xticks(fontsize=20)
#plt.savefig('conductance_full.pdf', format='pdf',dpi=1000)
#plt.show()

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
#plt.title("Bulk Conductance",fontsize=20)
plt.savefig('bulk_conductance.png', dpi=1000)
plt.show()

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








