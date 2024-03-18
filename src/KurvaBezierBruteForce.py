from point import Point
import matplotlib.pyplot as plt
import numpy as np
import time

def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def rumusbezier(p0:Point, p1:Point, p2:Point, t) :
    return [(1-t)*(1-t)*p0.getAbsis() + 2*(1-t)*t*p1.getAbsis() + t*t*p2.getAbsis(), (1-t)*(1-t)*p0.getOrdinat() + 2*(1-t)*t*p1.getOrdinat() + t*t*p2.getOrdinat()]

def bezierBF(p0,p1,p2,iterasi) :
    t = 2**iterasi
    arraybezier = []
    for i in range(0,t+1) :
        b = rumusbezier(p0,p1,p2,(i/t))
        arraybezier.append(Point(b[0],b[1]))
    return arraybezier

def plotAnimation(ip, n):
    x_input_points = np.array([x.getAbsis() for x in ip])
    y_input_points = np.array([y.getOrdinat() for y in ip])
    for i in range(n):
        res = []
        res = bezierBF(ip[0],ip[1],ip[2], i+1)
        res = np.concatenate(([ip[0]], res, [ip[-1]]))
        x_res = [x.getAbsis() for x in res]
        y_res = [y.getOrdinat() for y in res]
        x_input_points = [x.getAbsis() for x in ip]
        y_input_points = [y.getOrdinat() for y in ip]
        plt.clf()
        plt.plot(x_input_points, y_input_points, marker="p", c="r")
        plt.plot(x_res, y_res, marker="o", label=f"Iterasi ke-{i+1}")
        plt.title("Bezier Curve with Divide n' Conquer")
        plt.legend()
        plt.pause(1.25)

def mainbf() :
    #Inputs
    n = int(input("Masukkan jumlah iterasi : "))
    while(n<=0):
        print("Input salah!, Masukkan ulang input >:(")
        n = int(input("Masukkan jumlah iterasi : "))
    p0 = Insert_Point("p0")
    p1 = Insert_Point("p1")
    p2 = Insert_Point("p2")
    ip=[p0,p1,p2]

    #Displaying, with a bit animation
    plotAnimation(ip, n)
    plt.show()

if __name__ == "__main__" :
    mainbf()