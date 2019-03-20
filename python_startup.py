import sys
import os
if os.path.exists(os.environ['HOME']+'/AJGAR'):
   sys.path.insert(0,os.environ['HOME']+'/AJGAR/')
if os.path.exists(os.environ['HOME']+'/AJGAR/TurbPlasma'):
   sys.path.insert(0,os.environ['HOME']+'/AJGAR/TurbPlasma/')
if os.path.exists(os.environ['HOME']+'/AJGAR/Py3D'):
   sys.path.insert(0,os.environ['HOME']+'/AJGAR/Py3D/')
sys.path.insert(0,os.environ['HOME']+'/WorkSpace/')
import numpy as np
import scipy as sp
#import pyqtgraph as pg
import matplotlib.pyplot as plt
plt.ion()
from Interfaces.Simulations import p3d
from Interfaces.Simulations import p3do
import TurbPlasma.Analysis.AnalysisFunctions as af
from scipy.ndimage import gaussian_filter as gf
import OLLibs as oll


## Quick fix for imshow to show images in IDL like orientation
def imsh(a,**kwargs): plt.imshow(a.T,origin='low',**kwargs)

###################################################
###################################################
def read_block(input_file, i, nsp, sp , nlines, file_head_count,block_head_count):
   syscomm("head -"+str((sum(nlines)+nsp-1+block_head_count)*(i-1)+file_head_count\
   +(block_head_count+sp-1+sum(nlines[0:sp])))+" "\
   +input_file+" | tail -"+str(nlines[sp-1])+" >/tmp/dist.dat")
   c=np.fromfile("/tmp/dist.dat",dtype=float,count=-1,sep=" ")
   c=np.reshape(c,(nlines[sp-1],4))
   return c
###################################################
###################################################
def calc_dist(a,b,nbins):
   N=len(a)
   out=np.zeros((nbins,nbins),order='F')+1
   ax=np.linspace(a.min(),a.max(),nbins)
   bx=np.linspace(b.min(),b.max(),nbins)
   da=(a.max()-a.min())/nbins; db=(b.max()-b.min())/nbins
   for k in range(0,N):
      i=(a[k]-a.min())/da-0.5; i=int(i)
      j=(b[k]-b.min())/db-0.5; j=int(j)
      out[j,i]=out[j,i]+1
   
   return ax,bx,out
##################################################
##################################################

from TurbPlasma.Utilities.subs import *
