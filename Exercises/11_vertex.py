# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 09:23:33 2022

@author: quill
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

cv_path = 'C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\wingdisc_data\\wingdisc\\wd-large\\cv.txt'
    
vp_path = 'C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\wingdisc_data\\wingdisc\\wd-large\\vp.txt'

#determine x,y-postions of the vertices of all cells
def get_list(cv_path,vp_path):
    
    #transfer the data from the file into a list
    with open(cv_path) as fyle:
        cv = fyle.readlines()    
        
    with open(vp_path) as fyle:
        vp = fyle.readlines()
        
    #convert cv from str to list of list of integers
    for i,el in enumerate(cv):
        cv[i] = el.rstrip("\n").split(" ")
        
        ints = []
        for j,el in enumerate(cv[i]):
            if len(el) != 0:
                ints.append(int(el))
        cv[i] = ints
            
    return cv,vp

def cell_positions(vp):
    #get the x,y-positions of the vertices of all cells
    x = []
    y = []
    
    for i in vp:
        l = i.split(" ")
        ints = []
        for j,el in enumerate(l):
            if len(el) != 0:
                ints.append(float(el.rstrip("\n")))
        x.append(ints[0])
        y.append(ints[1])
    return x,y

cv,vp = get_list(cv_path, vp_path)

x,y = cell_positions(vp)
#print(x[cv[0][3]],y[cv[0][3]])

#calculate cell areas
def area(cv,x,y,round=6):
    x = np.array(x)
    y = np.array(y)
    #calculate cell areas
    areas = []
    
    def compute(x,y):
        A = 0
        for i in range(0,len(x)):   
            A += ((x[i]*y[i-1]) - (x[i-1]*y[i]))    # compute area of cell  
        return(A/2)
        
    for i in cv:
        #create two lists containing the vertices coordinates for 1 cell
        xs = x[i]
        ys = y[i]
        areas.append(np.around(compute(xs,ys),round))
        
    return(areas)
A = area(cv,x,y)

#calculate positions of cell centroid and distance of centroid to wingdisc center
def centroid(cv,x,y,A,round=2):
    x = np.array(x)
    y = np.array(y)
    #calculates cell centroids
    def compute(x,y,A):
        Cx = 0
        Cy = 0
        for i in range(0,len(x)):   
            Cx += (x[i]+x[i-1])*((x[i]*y[i-1]) - (x[i-1]*y[i]))    # compute centroid x
            Cy += (y[i]+y[i-1])*((x[i]*y[i-1]) - (x[i-1]*y[i]))    # compute centroid y
        Cx = Cx/(6*A)
        Cy = Cy/(6*A)
        return(Cx,Cy)
    
    cx = []
    cy = []
    for i,a in zip(cv,A):
        #create two lists containing the vertices coordinates for 1 cell
        xs = x[i]
        ys = y[i]
        c_x,c_y = np.around(compute(xs,ys,a),round)
        cx.append(c_x)
        cy.append(c_y)
    return(np.array(cx),np.array(cy))

c1,c2 = centroid(cv,x,y,A)
#print(c1[1],c2[1])    

def distance_center(cx,cy,round = 5, arr=False):
    #calculate the distance of the cell centroids to the disc center
    ds = []
    for i,j in zip(cx,cy):
        d = np.sqrt(i**2+j**2)
        ds.append(np.round(d,round))
    if arr:
        return(np.array(ds))
    else:
        return(ds)
Dist = distance_center(c1, c2)  

#plot cell area against distance from wingdisc center and add a linear fit
def plotting(Dist,A):
    #plot areas including the linear fit
    
    m, h = np.polyfit(Dist,A,1)
    print(np.round(m,3),h)
    ylin = [m*i+h for i in Dist] 
    plt.plot(Dist,A,".k")
    plt.plot(Dist,ylin,label=f"y={np.round(m,4)}x+{np.round(h,4)}")
    plt.title("Cell area against distance from wingdisc center")
    plt.xlabel(r"Cell Area $\mu m^2$")
    plt.ylabel(r"Dist to wingdisc center $\mu m$")
    plt.legend()
    plt.show()
#plotting(Dist,A)

#do statistical test (t-test)
#Test whether cells up to half the maximum wing disc 
#radius have areas that are significantly different from 
#those of the cells further away from the center.

def statistical_test(Dist,A):
    
    half_max = max(Dist)/2
    close = []
    far = []
    for i, el in enumerate(Dist):
        if el > half_max:
            close.append(A[i])
        if el < half_max:
            far.append(A[i])
            
    t,p = st.ttest_ind(close,far)
    return(t,p)
#print(statistical_test(Dist, A))


    
#function to draw the wing disc
def draw_disc(cpx, cpy, area, size):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    #input arguments: 
    ## cpx, cpy: x,y/positions of the vertices of all cells 
	# format: list (1 element per cell) of sublists (1 number per vertex, eg 3 numbers for a triangle). 
    ## area: cell area
	# format: 1-dimensional numpy array (1 number per cell)
    ## size: 'large' for the large disc and 'small' for the small disc
    
    #convert the bloody string format to int 
    # cpy_int = []
    # for i in cpy:
    #     cpy_int.append(i.split(" "))
    # cpy = []
    # for i in cpy_int:
    #     for j in i:
    #         if len(j) != 0:
    #             s = j.rsplit("\n")
    #             cpy.append(eval(s[0]))
    # cpy_int = []
    # for i in range(0,len(cpy)-1,2):
    #     el = [cpy[i],cpy[i+1]]
    #     cpy_int.append(el)
    # cpy = cpy_int
    
    polygs = []
    for i in range(len(cpx)):
        polyg = []
        for j in range(len(cpx[i])):
            polyg.append([cpx[i][j], cpy[i][j]])
        
        polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors = np.array(colors)
    # color value for all the mitotic cells (area>14) is set to 14
    colors[colors > 14] = 14
    patches.set_array(np.array(colors))  # for colors

    fig = plt.figure()
    panel = fig.add_subplot(1, 1, 1)
    panel.add_collection(patches)
    color_bar = fig.colorbar(patches)
    color_bar.set_label('Cell area (um2)', rotation=270, labelpad=15)
    panel.set_xlim(-120, 110)
    panel.set_ylim(-85, 85)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')


x = np.array(x)
y = np.array(y)

cpx = []
cpy = []
for i in cv:
    #create two lists containing the vertices coordinates for 1 cell
    cpx.append(x[i])
    cpy.append(y[i])
    
#draw_disc(cpx, cpy, A, 'large')
#do this for a small and a large disc
cv_path = 'C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\wingdisc_data\\wingdisc\\wd-small\\cv.txt'   
vp_path = 'C:\\Users\\quill\\Documents\\UZH-1\\Programming in biology\\Data\\wingdisc_data\\wingdisc\\wd-small\\vp.txt'
def analyze_disc(cv_path,vp_path):

    #call the functions above
    cv,vp = get_list(cv_path, vp_path)
    x,y = cell_positions(vp)
    A = area(cv,x,y)
    c1,c2 = centroid(cv,x,y,A)
    Dist = distance_center(c1, c2) 
    t,p = statistical_test(Dist, A)
    x = np.array(x)
    y = np.array(y)

    cpx = []
    cpy = []
    for i in cv:
        #create two lists containing the vertices coordinates for 1 cell
        cpx.append(x[i])
        cpy.append(y[i])
        
    draw_disc(cpx, cpy, A, 'small')
    plotting(Dist,A)
    print(f"""tstat: {t}  p-val: {p}""")
          
analyze_disc(cv_path, vp_path) 
    
    