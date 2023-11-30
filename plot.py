import numpy as np
from matplotlib import pyplot as plt


a=np.loadtxt('/home/tania/project1/corbino_200x80/edge_cond.txt')
plt.plot(a[:,175])
plt.xticks(ticks=[0,10,20,30,40,50,60],labels=[0.10,0.28,0.48,0.68,0.88,1.08,1.28],fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('$E_G/E_0$',fontsize=20)
plt.ylabel('$G_{edge}/G_0$', fontsize=20)
plt.tight_layout()
#plt.title("corbino_200x80",fontsize=20)
plt.savefig('step_cond.pdf',format='pdf',dpi=10000)
plt.show()
