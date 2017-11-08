from numpy import *
import pylab as P

x = linspace(-pi,pi,1000)
x0 = 0.
b = pi/8.
k0 = 10.

psi = exp(-b*(x-x0)**2)*exp(1j*k0*x)

P.plot(x,real(psi),'b:',label=r'$\mathcal{Re}\left[\Psi(x,0)\right]$')
P.plot(x,imag(psi),'r:',label=r'$\mathcal{Im}\left[\Psi(x,0)\right]$')
P.plot(x,abs(psi),'k',label=r'$|\Psi(x,0)|^2$')
P.axis('off')
P.legend(frameon=False,fontsize=14)
P.tight_layout()
P.savefig('gauss_wavepacket.pdf')

P.show()
