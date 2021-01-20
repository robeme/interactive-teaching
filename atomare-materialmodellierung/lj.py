import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'size'   : 16}

matplotlib.rc('font', **font)

# lj parameter for neon
 
eps = 0.027
sig = 2.99

r = np.linspace(2,10,1000);
V = 4.0*eps*((sig/r)**12 - (sig/r)**6)
Vatt = -4.0*eps*((sig/r)**6)
Vrep = 4.0*eps*((sig/r)**12)


plt.plot(r,V,'b-',label=r'$4\epsilon((\frac{\sigma}{r})^{12}-(\frac{\sigma}{r})^{6})$')
plt.plot(r,Vatt,'b--',label=r'$-4\epsilon(\frac{\sigma}{r})^{6}$')
plt.plot(r,Vrep,'b:',label=r'$4\epsilon(\frac{\sigma}{r})^{12}$')
plt.ylim([-0.1,0.1])
plt.axvline(sig,ls=':',c='k')
plt.text(sig,max(plt.gca().get_ylim()),'$\sigma$',va='baseline',ha='center')
plt.axhline(-eps,ls=':',c='k')
plt.text(max(plt.gca().get_xlim()),-eps,'$\epsilon$',va='center',ha='left')
plt.legend(frameon=False)
plt.xlabel("r")
plt.ylabel("V(r)")
plt.tight_layout()
plt.savefig("lj.pdf")
plt.show()
