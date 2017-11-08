from numpy import *
import pylab as P
import matplotlib 
from sympy.physics.hydrogen import R_nl
from sympy.abc import x
from sympy.utilities.lambdify import lambdify


matplotlib.rc('xtick', labelsize=14) 
matplotlib.rc('ytick', labelsize=14) 


fig = P.figure()

def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none')  # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])

#n=1,l=0
r = linspace(0,10,100)
lam_R_nl = lambdify(x, R_nl(1,0,x))
ax = fig.add_subplot(6, 1, 1)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False,label=r'$a_0^2|R_{nl}(r)|^2$')
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False,label=r'$R_{nl}(r)$')
ax.plot([1,1],[min(r**2*abs(lam_R_nl(r))**2),max(r**2*abs(lam_R_nl(r))**2)],'k--')
ax.set_ylim([0,1.])
P.legend(frameon=False,fontsize=14,loc='best',ncol=2)
adjust_spines(ax, ['left'])

#n=2,l=0
r = linspace(0,15,100)
lam_R_nl = lambdify(x, R_nl(2,0,x))
ax = fig.add_subplot(6, 1, 2)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False)
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False)
ax.set_ylim([-.2,.2])
ax.set_yticks([-0.2,0.2])
adjust_spines(ax, ['left'])

#n=2,l=1
r = linspace(0,15,100)
lam_R_nl = lambdify(x, R_nl(2,1,x))
ax = fig.add_subplot(6, 1, 3)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False)
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False)
ax.set_ylim([0,.2])
ax.plot([4,4],[min(r**2*abs(lam_R_nl(r))**2),max(r**2*abs(lam_R_nl(r))**2)],'k--')
adjust_spines(ax, ['left'])

#n=3,l=0
r = linspace(0,25,100)
lam_R_nl = lambdify(x, R_nl(3,0,x))
ax = fig.add_subplot(6, 1, 4)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False)
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False)
ax.set_ylim([0,.2])
adjust_spines(ax, ['left'])

#n=3,l=1
r = linspace(0,25,100)
lam_R_nl = lambdify(x, R_nl(3,1,x))
ax = fig.add_subplot(6, 1, 5)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False)
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False)
ax.set_ylim([0,.2])
adjust_spines(ax, ['left'])

#n=3,l=2
r = linspace(0,25,100)
lam_R_nl = lambdify(x, R_nl(3,2,x))
ax = fig.add_subplot(6, 1, 6)
ax.plot(r,r**2*abs(lam_R_nl(r))**2,'k',clip_on=False)
ax.fill(r,r**2*abs(lam_R_nl(r))**2,color=[.7,.7,.7])
ax.plot(r,lam_R_nl(r),'k:',clip_on=False)
ax.set_ylim([0,.2])
#ax.axvline(9,color='k',linestyle='--')
ax.plot([9,9],[min(r**2*abs(lam_R_nl(r))**2),max(r**2*abs(lam_R_nl(r))**2)],'k--')
ax.set_xlabel(r'$r/a_0$',fontsize=14)
adjust_spines(ax, ['left', 'bottom'])

P.tight_layout()
P.savefig('radial_wavefunctions.pdf')
P.show()
