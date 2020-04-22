# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:16:39 2020

@author: Thomas Gallenberger
Some sections have been commented out to prevent unnecessary rewriting of files or because they reference an external file.
"""

#import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Defines the functions as they are defined in the paper regarding the isodynamic stellarator
def Radfunc(N, R_o, E_R, a_R, phi):
    return R_o*E_R*np.cos(N*phi+a_R*np.sin(N*phi))+R_o

def Zfunc(N, R_o, E_Z, a_Z, phi):
    return R_o*E_Z*np.sin(N*phi+a_Z*np.sin(N*phi))


fig = plt.figure()
ax = fig.gca(projection='3d')
phi_dom = np.linspace(-1 * np.pi, 1 * np.pi, 2500)

#plots the first helical coil
rH1 = Radfunc(4, 1.15, .5, .6, phi_dom)
zH1 = Zfunc(4, 1.15, .6, .6, phi_dom)
xH1 = rH1 * np.sin(phi_dom)
yH1 = rH1 * np.cos(phi_dom)
ax.plot(xH1, yH1, zH1, label='Helical Coil #1')

#plots the second helical coil
rH2 = Radfunc(4, 1.25, 0, 0, phi_dom)
zH2 = Zfunc(4, 1.25, .4, .4, phi_dom)
xH2 = rH2 * np.sin(phi_dom)
yH2 = rH2 * np.cos(phi_dom)
ax.plot(xH2, yH2, zH2, label='Helical Coil #2')

#plots the first and second poloidal coil
rP12=1.8
xP12=rP12*np.cos(phi_dom)
yP12=rP12*np.sin(phi_dom)
zP12=[-.8,.8]
for j in [0,1]:
    ax.plot(xP12,yP12, zP12[j], label='Poloidal Coil #' + str(j+1))
            
#plots the third and fourth poloidal coil
rP34=.5
xP34=rP34*np.cos(phi_dom)
yP34=rP34*np.sin(phi_dom)
zP34=[-.6,.6]
for j in [0,1]:
    ax.plot(xP34,yP34, zP34[j], label='Poloidal Coil #' + str(j+3))
            
#Creates the legend for the plot
ax.legend()
ax.set_xlabel('X axis [m]')
ax.set_ylabel('Y axis [m]')
ax.set_zlabel('Z axis [m]')

#Loads and plots the results from flf
'''
results=np.loadtxt('results_iso5.out',skiprows=1, max_rows=96)
z2=[]
x2=[]
y2=[]
for w in range (60):
    x2.append(results[w,0]*np.cos(results[w,2]))
    y2.append(results[w,0]*np.sin(results[w,2]))
    z2.append(results[w,1])
ax.plot(x2,y2,z2)
ax.scatter([.9],[0],[0])
'''
#plt.close() #remove line to see plot



#Creates coil files to be loaded in solidworks
'''
HelicalCurveNames=['isoH1.sldcrv','isoH2.sldcrv']

xHComp=[xH1,xH2]
yHComp=[yH1,yH2,yP12,yP12,yP34,yP34]
zHComp=[zH1,zH2,zP12,zP12,zP34,zP34]

for i in range(2):
    f=open(str(HelicalCurveNames[i]), "w")
    for j in range(2499):
        f.write(str(xHComp[i][j]) + '\t'+ str(zHComp[i][j])+ '\t' + str(yHComp[i][j]) + '\n')
    f.close

xPComp=[xP12,xP12,xP34,xP34]
yPComp=[yP12,yP12,yP34,yP34]
zPComp=[zP12[0],zP12[1],zP34[0],zP34[1]]
PoloidalCurveNames=['isoP1.sldcrv','isoP2.sldcrv','isoP3.sldcrv','isoP4.sldcrv']

for i in range(4):
    f=open(str(PoloidalCurveNames[i]), "w")
    for j in range(2499):
        f.write(str(xPComp[i][j]) + '\t'+ str(zPComp[i])+ '\t' + str(yPComp[i][j]) + '\n')
    f.close
'''

#Creates a coil file to be converted to an Mgrid file
f=open("coils.iso_wmain","w")
f.write('periods 1\nbegin filament\nmirror NUL\n')
for i in range(2499):
     f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xH1[i], yH1[i], zH1[i]))
f.write('\t'+str(xH1[2499])+ '\t'+ str(yH1[2499])+'\t'+ str(zH1[2499]) + '\t0\t1 MainCoil1\n')
for i in range(2499):  
   f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xH2[i], yH2[i], zH2[i]))
f.write('\t'+str(xH2[2499])+ '\t'+ str(yH2[2499])+'\t'+ str(zH2[2499]) + '\t0\t2 MainCoil2\n')
for i in range(2499):  
   f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xP12[i], yP12[i], zP12[0]))
f.write('\t'+str(xP12[2499])+ '\t'+ str(yP12[2499])+'\t'+ str(zP12[0]) + '\t0\t3 AuxCoil1\n')
for i in range(2499):  
   f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xP12[i], yP12[i], zP12[1]))
f.write('\t'+str(xP12[2499])+ '\t'+ str(yP12[2499])+'\t'+ str(zP12[1]) + '\t0\t4 AuxCoil2\n')
for i in range(2499):  
   f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xP34[i], yP12[i], zP34[0]))
f.write('\t'+str(xP12[2499])+ '\t'+ str(yP34[2499])+'\t'+ str(zP34[0]) + '\t0\t5 AuxCoil3\n')
for i in range(2499):  
   f.write('\t{0}\t{1}\t{2}\t-1\n'.format(xP34[i], yP12[i], zP34[1]))
f.write('\t'+str(xP12[2499])+ '\t'+ str(yP34[2499])+'\t'+ str(zP34[1]) + '\t0\t6 AuxCoil4\n')
f.close()

