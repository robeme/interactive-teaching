from numpy import *
import pylab as P

x = linspace(pi,3*pi,1000)
k = linspace(1,10,10)
k0 = 5.5
Ak = exp(-(k-k0)**2/5)

# plot wavenumber spectra
for i,ki in enumerate(k):
	P.plot([ki,ki],[0,Ak[i]],'k')
ax = P.gca()
ax.set_frame_on(False)
#ax.axes.get_yaxis().set_visible(False)
ax.tick_params(axis=u'y', which=u'y',length=0)
P.xticks(k)
P.yticks([])
P.xlabel(r'Wellenzahl $k$',fontsize=14)
P.ylabel(r'Amplitudenfunktion $A(k)$',fontsize=14)
P.tick_params(axis='both', which='major', labelsize=14)
P.tight_layout()
P.savefig('wavenumber.pdf')
P.show()



tot = ones(len(x))*0+0j

for i,ki in enumerate(k):
  psi = Ak[i]*exp(1j*ki*x)
  P.plot(x,real(psi),color=[.7,.7,.7])
  tot = tot+psi

P.plot(x,real(tot),'k')
P.axis('off')
P.tight_layout()
P.savefig('wavepackets.pdf')
P.show()
